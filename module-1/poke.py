import requests
import time

url = input("Enter a URL: ")

starttime = time.time()
response = requests.get(url)
endtime = time.time()

timetaken = endtime - starttime
nbytes = len(response.content)

rate = (nbytes / timetaken / 1e6)

print(f"{nbytes} bytes read from {url}")
print(f"Time elapsed: {round(timetaken, 2)} seconds")
print(f"Inferred Rate: {round(rate, 5)} megabytes per second")