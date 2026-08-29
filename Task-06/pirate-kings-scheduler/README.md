## Pirate King's Scheduler

The Pirate Kinds's Scheduler is a CLI scheduling simulator built in Golang. It models the incomming pirate crew as the process competitons for the CPU resources and the the simulation is done in three fundamenta CPU scheduling ways :

1. First Come , First serve ( FIFO )
2. Shortest job first ( SJF )
3. Round Robin ( RR ) 

The simulator provides real-time ASCII Gant charts of which crew ( process ) runs when , shows each process's individual state and also calculate the `Average Turnaround Time ( ATAT )` and `Average Waiting Time (AWT) `.

### Mathematical Formulas :

1. `Turnaround Time` : It is the total time a process spends in the system - from the exact moment it arrives to the moment till the whole process in completely finished .

Formula :

		Turnaound Time = Completion time - Arrival time 


