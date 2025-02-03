# multithreading with thread pool executor 

from concurrent.futures import ThreadPoolExecutor
import time 

def print_number(number):
    time.sleep(2)
    return f'number: {number}'


numbers=[1,2,3,4,5,6,7,8,9,10]
t=time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_number,numbers)
f=time.time()-t
for result in results:
    print(result)

print(f'total_time: {f}')

