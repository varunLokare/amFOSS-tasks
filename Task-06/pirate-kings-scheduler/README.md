# Pirate King's Scheduler

The Pirate Kinds's Scheduler is a CLI scheduling simulator built in Golang. It models the incomming pirate crew as the process competitons for the CPU resources and the the simulation is done in three fundamenta CPU scheduling ways :

1. First Come , First serve ( FCFS )
2. Shortest job first ( SJF )
3. Round Robin ( RR ) 

The simulator provides real-time ASCII Gant charts of which crew ( process ) runs when , shows each process's individual state and also calculate the `Average Turnaround Time ( ATAT )` and `Average Waiting Time (AWT) `.

## Mathematical Formulas :

1. `Turnaround Time` : It is the total time a process spends in the system - from the exact moment it arrives to the moment till the whole process in completely finished .

Formula :

		Turnaound Time = Completion time - Arrival time 


2. `Waiting time`: It is the total time spent by an process doing notting waiting for its turn to come to use the CPU.

Formula :
		Waiting Time = Turnaroundtime - Bust time 

Bust time is the ammount of time a process needes to actually run on the CPU and to finisht its task ( basically "work time" for the process ).

3. Averages :
	
	Averatge Waiting Time = Sum of all waiting times / N

	Averate Turnaround Time = Sum of all the turnaround times / N

## Algorithm Implimentation :

### 1. First come , First Serve ( FCFS ):

 FCFA is a non-preemitive schedulling system . Whoever arrices first gets seved first . Once the process gets the access to the CPU , it doesnt stop until it completly finished the process ( bust time ).


Implimentation of logic in the code :

1.  All the processes are sorted in the ascending order of `arrivalTime`
2.  Before excecuting the next process i, checks if the CPU clock ( currentTime ) is behind the process's arrival ( arrivalTime ) . If `currentTime < arrivalTime` , the CPU was sitting idle and was doing ntg so js forward the arrivalTime to currentTime I.E.. `currentTime = arrivalTime`.
3.  Add the full `bustTime` directly to the current time.
4.  compute the following :

     	-> Completion time ( CT ) = current time 

     	-> Turnaround time ( TAT )= CT - AT

     	-> Waiting time (WT) = TAT - BT
    
6. Repeat immediately for the process i + 1.

### 2. Shortest Job First (SJF — Non-Preemptive):
SJF lookat at all the jobs that have already arrived and are currely waitiing, amongst  all the processed one with the shortest burst time is picked .

Implimentation of logic in the code :

1. Loop runs continiously while `completed < len(processes)`
2. At the current tick ( `currentTime` ), inspect every process in the list :

 		-> `arrivalTime <= currentTime` AND `!complete`.
 
 		-> Find the process with the minimum burstTime.

3. If no process satisfy the condition then increment the clock by 1 tick and check again.
4. Execute Selected Job:
 -> Run the chosen process for its full burstTime: currentTime += burstTime.
 -> Mark completed = true and increment the completed counter.

5.  Calculate Metrics:
		-> CT = current time 
     -	-> TAT = CT - AT
     	-> WT = TAT - BT

### 3. Round Robin (RR — Preemptive):
Robbin round allocates every process a fixed time slive ( `Time Quantum `, Q ). if the job is not done in the given time then the CPU pausese it and moves it back to the waiting queue and proceeds with the next process.

Implimentation of logic in the code :

1. Add all the arrived processed to a FIFO queue.
2. pop the first process from the queue and execute the process up to the time quantum .
3. Now update the `currentTime` and then reduce the process's remainingTime.
4. Push newly arrived processes back to the queue before re-queuing the current one .
5. If the `remainingTime == 0`, mark it complete and then calculate the stats, or else push it back to the queue.

### Topics Learnt :
1. Queue usage in Robin Round :Learned how to handle the tricky timing when a process finishes its time slice right as a new one arrives.
2. Handling CPU Idle Time : If the CPU finishes early and the next task hasn't arrived yet, advancing the clock forward prevents the program from freezing and keeps time calculations accurate.
3. Go structures and slices :By bundling each process's details inside a struct slice (processes []Process), you can modify all its stats directly in one place.

### Resources Used :
    -> Operating System Concepts

    -> The Go Programming Language
	
    -> GeeksforGeeks OS Scheduling Tutorials


