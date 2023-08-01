import random
from datetime import datetime, timedelta

def random_ip():
    return f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,255)}.{random.randint(1,254)}"

def random_http_request_type():
    return ["POST", "GET"][random.randint(0,1)]

def random_directory()
    

def generate_logs(num_lines:int):
    logs = []
    timestamp = datetime(2022, 6, 10, 15, 33, 30)

    for i in range(num_lines):
        timestamp += timedelta(minutes=random.randint(0,2), seconds=random.randint(0,59))
        logs.append(
            f"{random_ip()} - - [{timestamp}] \"{random_http_request_type()}\""
        )