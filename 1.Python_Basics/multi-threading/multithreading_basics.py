import threading
import time 

def print_numbers():
    for i in range(26):
        time.sleep(1)
        print(f'numbers: {i}')

def print_letters():
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        time.sleep(1)
        print(f"letter: {letter}")

def print_numbers_with_args(range_number:int):
    for i in range(range_number):
        time.sleep(1)
        print(f'number: {i}')


def print_letter_with_args(string_given):
    for i in string_given:
        time.sleep(1)
        print(f'letter: {i}')

##create 2 thread 
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter_with_args,args=("abcdefghijklmnopqrstuvwxyz",))


t=time.time()
# print_numbers()
# print_letters()
# start the thread 
t1.start()
t2.start()

# wait for threads to complete 
t1.join()
t2.join()
finished=time.time()-t 
print(f'time taken for execution: {finished}')
