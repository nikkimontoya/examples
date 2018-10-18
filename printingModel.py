from data_structures.queue import Queue
from printer import Printer
from task import Task

import random


def simulation(num_seconds, ppm):
    printer = Printer(ppm)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if not printer.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.waitTime(current_second))
            printer.start_next(next_task)

        printer.tick()
        
    average_wait = sum(waiting_times) / len(waiting_times)
    #print("Average Wait %6.2f secs %3d tasks remaining."%(average_wait,print_queue.size()))
    return average_wait


def new_print_task():
    return random.randrange(1, 181) == 180    


number_of_attempts = 10
ten_ppm_time = 0
five_ppm_time = 0

for i in range(number_of_attempts):
    ten_ppm_time += simulation(3600, 10)
    five_ppm_time += simulation(3600, 5)

print("Average waiting time for 10 ppm = ", str(ten_ppm_time / number_of_attempts))
print("Average waiting time for 5 ppm = ", str(five_ppm_time / number_of_attempts))