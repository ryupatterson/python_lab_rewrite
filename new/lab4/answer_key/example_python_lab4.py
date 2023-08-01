"""
    Lab 4 is focused around string/file manipulation for log ingestion.
    Ingest the logs from the given file, 'sample_logs.log'. These logs mimic an Apache Web Servers logs.
    The final output of your code should be a JSON representation of a list of dictionaries, with each dictionary having the following
    keys: timestamp (int), request_ip (str), http_method (str), requested_resource (str), http_response (str), 
    and response_size (int). The list should be in REVERSE chronological order.

    The logs are in this format:
    request_ip - - [timestamp UTC offset] "HTTP_METHOD requested_resource" http_response response_size

    The data processing should start, and end with the ingest_logs and format_logs methods. Helper methods are 
    allowed. The output should be from format_logs, make sure the JSON uses an indent of 4.

    Do NOT change the function declaration of ingest_logs or format_logs if you wish for any of the test cases to work.
"""
import os, json
from datetime import datetime

def ingest_logs(file_path)->list[str]:
    string_list = []
    with open(file_path) as infile:
        string_list = infile.readlines()
        string_list = [line.strip() for line in string_list]
    return string_list

def format_logs(string_list:list[str]):
    output = []
    for line in string_list:
        separate = line.split()
        output.append({
            "timestamp": int(datetime.strptime(separate[3][1:], '%d/%b/%Y:%H:%M:%S').timestamp()),
            "request_ip": separate[0],
            "http_method": separate[5][1:],
            "requested_resource": separate[6],
            "http_response": separate[8],
            "response_size": int(separate[9])
        })

    return json.dumps(output, indent=4)


""" 
    =================================================================================================================
                                                    DO NOT TOUCH
                                                    DO NOT TOUCH
    =================================================================================================================
                    You should NOT have to change anything in the main method to get this to work.
"""
if __name__ == "__main__":
    # cwd changes based on what directory you are in when running the script
    # this basically finds the absolute path of sample_logs.log
    pwd = os.getcwd()

    input_file = "sample_logs.log"
    for root, _, files in os.walk(pwd):
        for file in files:
            if file == input_file:
                input_file = os.path.join(pwd, root, file)

    string_list = ingest_logs(input_file)

    output = ""
    if string_list:
        output = format_logs(string_list)

    output_dir = ""
    for root, _, files in os.walk(pwd):
        for file in files:
            if file == os.path.basename(__file__):
                output_dir = os.path.join(pwd, root)

    if output:
        with open(os.path.join(output_dir,"example_logs.json"), "w") as outfile:
            outfile.write(output)
    
        print("JSON Output:")
        print(output)