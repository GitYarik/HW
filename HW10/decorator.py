# Напишите декоратор, который будет считать время исполнения функции (используя
# библиотеку time)


import time


def time_function(func):
    def wrapped():
        start_time = time.time()
        time.sleep(1)
        func()
        time.sleep(1)
        finish_time = time.time()
        print(f"{finish_time - start_time} время выполннения программы")

    return wrapped


@time_function
def time_sleep():
    time.sleep(2)


time_sleep()
