''' 
Real-world examples: Multithreading for I/O-bound Tasks 
Scenario: Web scrapping 
network requests to fetch web pages. These tasks are I/O-bound
'''

url_list=[
    'https://en.wikipedia.org/wiki/Elon_Musk',
    'https://en.wikipedia.org/wiki/Sundar_Pichai',
    'https://en.wikipedia.org/wiki/Jeff_Bezos'
]


import threading
import requests 
from bs4 import BeautifulSoup


def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]

for url in url_list:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All web pages fetched')