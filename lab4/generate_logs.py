"""
    This script generates logs that mimic an Apache Web server for use in python_lab4. The reference for this
    can be found here: https://www.researchgate.net/figure/Web-Logs-from-Apache-Web-Server_fig5_267775041
"""

import random
from datetime import datetime, timedelta

def random_ip():
    return f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,255)}.{random.randint(1,254)}"

def random_http_request_type():
    return ["POST", "GET"][random.randint(0,1)]

def random_directory():
    random_first = ["admin", "customer", "index", ""]
    random_second = ["form.html", "data.txt", "photo.jpg", "robot.txt"]

    outstring = f"/{random_first[random.randint(0,2)]}"
    if outstring != "/":
        outstring += "/"
    if random.randint(0,1):
        outstring += random_second[random.randint(0,3)]
    return outstring

def payload_size(dir):
    if "." in dir:
        match dir.split("/")[2]:
            case "form.html":
                return 1534
            case "data.txt":
                return 8151
            case "photo.jpg":
                return 400575
            case "robot.txt":
                return 522
            case _:
                return 966
    else:
        return 665        

def generate_logs(num_lines:int):
    logs = []
    timestamp = datetime(2022, 6, 10, 15, 33, 30)

    for _ in range(num_lines):
        timestamp += timedelta(minutes=random.randint(0,2), seconds=random.randint(0,59))
        dir = random_directory()
        logs.append(
            f"{random_ip()} - - [{timestamp.strftime('%d/%b/%Y:%H:%M:%S')} -0500] \"{random_http_request_type()} {dir} HTTP/1.1\" 200 {payload_size(dir)}\n"
        )
    
    return logs

def write_file(output:str, logs:str):
    with open(output, "w") as outfile:
        outfile.writelines(logs)

if __name__ == "__main__":
    logs = generate_logs(random.randint(10,15))
    write_file("sample_logs.log", logs)
