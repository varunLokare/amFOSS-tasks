# Task 05: Grand Line Guardian

For this task we had to build a terminal-based system monitoering sysetem similar to monitoring systems like `htop` and `bt0p++`.

This task mainly focuses on to understand the system files and to monitor the processes currently running on the linux system and then display all the needed information onto the terminal in real time .

Ive built this project using pythong language . Insted of using the library `psuil`( a library of python that help us to fetch the process files direcly without any manually fetcing of the files by the user) , i have directly got the process information from the Linux `/proc` virtual file system Which helped me understand how linux provides information about the running processed through the kernel .

## The application displays :

```text
.Process ID (PID)
.Process Name
.Memory Usage
.CPU Usage
.Total number of active processes
.Total CPU usage
.Total memory usage
.Current time
```
All the above application are continuously updated at the terminal in the real time.

## Technologies Used:
```text
.Python 3
.Linux
./proc virtual filesystem
.Rich pythong liberary
.Python standard library modules:
	.os
	.sys
	.select
	.datetime
Note : The psutil library was not used for this task.
```
## How actually does the program gets the process information :

So basically the Linux `/proc` filesystem stores the information about the running processess insider `/proc` and then linux provies that information for us to work on . We were required to fetch the PID's ( Process id's ) from the `/proc` files and then display all the necessary application that to be displayed for the task.

The task contents are to be displayed real time so we js need to run the program in the loop in a interval of time less then 1s ( as given by the task instructor) so it allows us to run the program or display the content in real time.


## Requirements :

The task only has one external denepdency `rich=15.0.0` and the other modules used in the task such as `0s`,`sys`,`select` and `datetime` are the part of python's standard libarary 

Note : psutil is not being used for this task. 

## Concepts Learned :

While grinding through this task ive learned several new topics and concepts like :


### 1. Linux "/proc" file system:

The linux `/proc` is a virtual file provided by linux to give the information about processes and system information .

### 2. Process IDs:

I found out that every process that runs in our system has a PID ( process id ) which is useful to access the information under `/proc`.

### 3.Process statistics :

Ive learned how Linux stores the information related to  CPU and memory of each individual procoesses.

### 4. CPU Timin and clock ticking :

Got to know that CPU usage can be calculated by comparting CPU time between two different points insted of js reading a fixed CPU percentage .

### 5. Terminal application :

Learnt how terminal application can continuoulsy update its output without printing a new output every time the application is refreshed .

### 6. Linux management: 
Got to understand how linx keeps track of the running processes and provice their information through the kernel interfact .

## Resources used:
1.AMFOSS Praveshan Task 05 description
2.Linux /proc filesystem documentation
3.Rich Python documentation.
4.Operating Systems: Three Easy Pieces

 

 
