import queue
import time
import threading
import random

REQUEST_TYPES = ["Hello", "Waqas"]
PROCESSING_TIMES = {"Hello": 2, "Waqas": 4}

def process_request(request_type):
    print(f"Processing {request_type} request...")
    time.sleep(PROCESSING_TIMES[request_type])
    print(f"{request_type} request processed.")

def web_server(queue):
    while True:
        if not queue.empty():
            request_type = queue.get()
            process_request(request_type)

def simulate_requests(queue, num_requests):
    for _ in range(num_requests):
        request_type = random.choice(REQUEST_TYPES)
        queue.put(request_type)
        time.sleep(1)

request_queue = queue.Queue()

web_server_thread = threading.Thread(target=web_server, args=(request_queue,), daemon=True)
web_server_thread.start()

num_requests = 4
simulate_requests(request_queue, num_requests)

web_server_thread.join()
