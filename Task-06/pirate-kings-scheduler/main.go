package main

import "fmt"

type Process struct {
	pid            string
	arrivalTime    int
	burstTime      int
	remainingTime  int
	completionTime int
	waitingTime    int
	turnaroundTime int
	completed      bool
}

func sortByArrivalTime(processes []Process) {
	for i := 0; i < len(processes)-1; i++ {
		for j := i + 1; j < len(processes); j++ {

			if processes[j].arrivalTime < processes[i].arrivalTime {
				temp := processes[i]
				processes[i] = processes[j]
				processes[j] = temp
			}
		}
	}
}

func fcfs(processes []Process) {

	currentTime := 0
	totalWaitingTime := 0
	totalTurnaroundTime := 0

	fmt.Println("\n--- FCFS Scheduling ---")
	fmt.Println("\nGantt Chart:")

	for i := 0; i < len(processes); i++ {

		if currentTime < processes[i].arrivalTime {
			currentTime = processes[i].arrivalTime
		}

		fmt.Printf("| %s ", processes[i].pid)

		// Run the process completely
		currentTime += processes[i].burstTime

		processes[i].completionTime = currentTime

		processes[i].turnaroundTime =
			processes[i].completionTime - processes[i].arrivalTime

		processes[i].waitingTime =
			processes[i].turnaroundTime - processes[i].burstTime

		totalWaitingTime += processes[i].waitingTime
		totalTurnaroundTime += processes[i].turnaroundTime
	}

	fmt.Println("|")

	displayResults(processes, totalWaitingTime, totalTurnaroundTime)
}

func sjf(processes []Process) {

	currentTime := 0
	completed := 0

	totalWaitingTime := 0
	totalTurnaroundTime := 0

	fmt.Println("\n--- SJF (Non-Preemptive) ---")
	fmt.Println("\nG Chart:")

	for completed < len(processes) {

		shortestIndex := -1
		for i := 0; i < len(processes); i++ {

			if processes[i].arrivalTime <= currentTime &&
				!processes[i].completed {

				if shortestIndex == -1 ||
					processes[i].burstTime < processes[shortestIndex].burstTime {

					shortestIndex = i
				}
			}
		}
		if shortestIndex == -1 {
			currentTime++
			continue
		}

		fmt.Printf("| %s ", processes[shortestIndex].pid)
		currentTime += processes[shortestIndex].burstTime

		processes[shortestIndex].completionTime = currentTime

		processes[shortestIndex].turnaroundTime =
			processes[shortestIndex].completionTime -
				processes[shortestIndex].arrivalTime

		processes[shortestIndex].waitingTime =
			processes[shortestIndex].turnaroundTime -
				processes[shortestIndex].burstTime

		processes[shortestIndex].completed = true

		totalWaitingTime += processes[shortestIndex].waitingTime
		totalTurnaroundTime += processes[shortestIndex].turnaroundTime

		completed++
	}

	fmt.Println("|")

	displayResults(processes, totalWaitingTime, totalTurnaroundTime)
}

func roundRobin(processes []Process, timeQuantum int) {

	currentTime := 0
	completed := 0

	totalWaitingTime := 0
	totalTurnaroundTime := 0

	queue := []int{}

	added := make([]bool, len(processes))

	fmt.Println("\n--- Round Robin Scheduling ---")
	fmt.Println("\nGantt Chart:")

	for completed < len(processes) {

		for i := 0; i < len(processes); i++ {

			if processes[i].arrivalTime <= currentTime &&
				!added[i] {

				queue = append(queue, i)
				added[i] = true
			}
		}

		if len(queue) == 0 {
			currentTime++
			continue
		}

		index := queue[0]

		queue = queue[1:]

		fmt.Printf("| %s ", processes[index].pid)
		runTime := timeQuantum

		if processes[index].remainingTime < timeQuantum {
			runTime = processes[index].remainingTime
		}
		
		currentTime += runTime

		processes[index].remainingTime -= runTime
		for i := 0; i < len(processes); i++ {

			if processes[i].arrivalTime <= currentTime &&
				!added[i] {

				queue = append(queue, i)
				added[i] = true
			}
		}

		if processes[index].remainingTime == 0 {

			processes[index].completionTime = currentTime

			processes[index].turnaroundTime =
				processes[index].completionTime -
					processes[index].arrivalTime

			processes[index].waitingTime =
				processes[index].turnaroundTime -
					processes[index].burstTime

			totalWaitingTime += processes[index].waitingTime
			totalTurnaroundTime += processes[index].turnaroundTime

			completed++

		} else {
			queue = append(queue, index)
		}
	}

	fmt.Println("|")

	displayResults(processes, totalWaitingTime, totalTurnaroundTime)
}

func displayResults(processes []Process, totalWaitingTime int, totalTurnaroundTime int) {

	fmt.Println("\nProcess Results:")
	fmt.Println("PID\tAT\tBT\tCT\tTAT\tWT")

	for i := 0; i < len(processes); i++ {

		fmt.Printf("%s\t%d\t%d\t%d\t%d\t%d\n",
			processes[i].pid,
			processes[i].arrivalTime,
			processes[i].burstTime,
			processes[i].completionTime,
			processes[i].turnaroundTime,
			processes[i].waitingTime,
		)
	}

	averageWaitingTime :=
		float64(totalWaitingTime) / float64(len(processes))

	averageTurnaroundTime :=
		float64(totalTurnaroundTime) / float64(len(processes))

	fmt.Printf("\nAverage Waiting Time: %.2f\n",
		averageWaitingTime)

	fmt.Printf("Average Turnaround Time: %.2f\n",
		averageTurnaroundTime)
}

func main() {

	var n int

	fmt.Println("-----PIRATE KING'S SCHEDULER -----")

	fmt.Print("\nEnter number of processes: ")
	fmt.Scan(&n)

	processes := make([]Process, n)

	for i := 0; i < n; i++ {

		fmt.Printf("\nProcess %d\n", i+1)

		fmt.Print("Enter Process ID: ")
		fmt.Scan(&processes[i].pid)

		fmt.Print("Enter Arrival Time: ")
		fmt.Scan(&processes[i].arrivalTime)

		fmt.Print("Enter Burst Time: ")
		fmt.Scan(&processes[i].burstTime)

		processes[i].remainingTime = processes[i].burstTime
	}

	fmt.Println("\n--- Process Details ---")

	for i := 0; i < n; i++ {

		fmt.Println("Process ID:", processes[i].pid)
		fmt.Println("Arrival Time:", processes[i].arrivalTime)
		fmt.Println("Burst Time:", processes[i].burstTime)
		fmt.Println()
	}

	sortByArrivalTime(processes)
	var choice int

	fmt.Println("Choose Scheduling Algorithm:")
	fmt.Println("1. FCFS")
	fmt.Println("2. SJF (Non-Preemptive)")
	fmt.Println("3. Round Robin")
	fmt.Print("\nEnter your choice: ")
	fmt.Scan(&choice)

	switch choice {
	case 1:
		fcfs(processes)
	case 2:
		sjf(processes)
	case 3:
		var timeQuantum int
		fmt.Print("Enter Time Quantum: ")
		fmt.Scan(&timeQuantum)
		roundRobin(processes, timeQuantum)
	default:
		fmt.Println("Invalid choice!")
	}
}