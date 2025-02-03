# multithreading with ProcessPoolExecutor 

from concurrent.futures import ProcessPoolExecutor
import time 

def square_numbers(number):
    time.sleep(2)
    return f'number: {number*number}'


numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13]

if __name__=='__main__':
    with ProcessPoolExecutor(max_workers=3) as executer:
        # results=executer.map(square_numbers,numbers)
        results=[executer.submit(square_numbers,i) for i in numbers]
    
    for result in results:
        print(result)