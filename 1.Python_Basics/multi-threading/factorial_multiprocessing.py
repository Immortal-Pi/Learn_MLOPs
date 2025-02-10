''' 
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario Factorial calculation 
using multiprocessing we will distribute the workload across multiple CPU 
cores, imroving performance 
'''

import time 
import multiprocessing 
import math
import sys 

sys.set_int_max_str_digits(100000)

# function to compute factorial of a given number

def compute_factorial(number):
    print(f'Computing factorial of number {number}')
    result=math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result 

if __name__=='__main__':
    numbers=[5000,6000,700,9000]
    start=time.time()
    ## create a pool of worler processes 
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)
    end=time.time()

    print(f'Result: {results}')
    print(f'Time taken: {end-start} seconds')