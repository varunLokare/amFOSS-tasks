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



