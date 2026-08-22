import os
import time
import sys
import select
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.live import Live

console = Console()

clock_ticks = os.sysconf(os.sysconf_names["SC_CLK_TCK"])
previous_ticks = {}


def get_process_name(pid):
    try:
        with open(f"/proc/{pid}/comm", "r") as file:
            return file.read().strip()
    except (FileNotFoundError, PermissionError):
        return None


def get_memory_usage(pid):
    try:
        with open(f"/proc/{pid}/status", "r") as file:
            for line in file:
                if line.startswith("VmRSS:"):
                    memory_kb = int(line.split()[1])
                    return memory_kb / 1024
    except (FileNotFoundError, PermissionError):
        return 0.0

    return 0.0


def get_cpu_time(pid):
    try:
        with open(f"/proc/{pid}/stat", "r") as file:
            values = file.read().split()

            utime = int(values[13])
            stime = int(values[14])

            return utime + stime

    except (FileNotFoundError, PermissionError):
        return 0


def create_table(process_list):
    current_time = datetime.now().strftime("%H:%M:%S")

    # Added totals calculation
    total_memory_mb = sum(process[2] for process in process_list)
    total_cpu_percent = sum(process[3] for process in process_list)

    table = Table(
        title=(
            f"[bold]Grand Line Guardian[/bold]\n"
            f"Time: {current_time} | Active Processes: {len(process_list)}\n"
            f"Total CPU: {total_cpu_percent:.1f}% | Total Memory: {total_memory_mb:.2f} MB"
        ),
        caption="Type 'q' and press Enter to quit." # Added hint
    )

    table.add_column("PID", justify="right", style="cyan")
    table.add_column("Process Name", style="green")
    table.add_column("Memory (MB)", justify="right", style="yellow")
    table.add_column("CPU %", justify="right", style="red")

    ROWS = console.size.height - 9

    for process in process_list[:ROWS]:
        table.add_row(
            str(process[0]),
            process[1],
            f"{process[2]:.2f}",
            f"{process[3]:.1f}"
        )

    return table


with Live(console=console, refresh_per_second=2, screen=True) as live:

    while True:

        process_list = []

        for pid in os.listdir("/proc"):

            if not pid.isdigit():
                continue

            process_name = get_process_name(pid)

            if process_name is None:
                continue

            memory_mb = get_memory_usage(pid)

            current_ticks = get_cpu_time(pid)

            previous = previous_ticks.get(int(pid))

            if previous is None:
                cpu_percent = 0.0
            else:
                delta_ticks = current_ticks - previous
                cpu_percent = (delta_ticks / clock_ticks) * 100

            previous_ticks[int(pid)] = current_ticks

            process_list.append(
                (
                    int(pid),
                    process_name,
                    memory_mb,
                    cpu_percent
                )
            )

        process_list.sort(
            key=lambda process: process[3],
            reverse=True
        )

        live.update(create_table(process_list))

        # Replaced time.sleep(1) with a 1-second pause that listens for 'q'
        if select.select([sys.stdin], [], [], 1)[0]:
            user_input = sys.stdin.readline().strip().lower()
            if user_input == 'q':
                break