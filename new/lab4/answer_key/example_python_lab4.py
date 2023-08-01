"""
    Lab 4 is focused around string/file manipulation for log ingestion.
    Ingest the logs from the given file, 'sample_logs.log'. These logs mimic an Apache Web Servers logs.
    The final output of your code should be a list of dictionaries, with each dictionary having the following
    keys: timestamp (int), request_ip (str), http_method (str), requested_resource (str), http_response (str), 
    and response_size (int). The list should be in REVERSE chronological order.

    The logs are in this format:
    request_ip - - [timestamp UTC offset] "HTTP_METHOD requested_resource" http_response response_size

    Format the code however you would like, but the final output should be returned from the format_logs method.
    Do NOT change the function declaration of format_logs if you wish for any of the test cases to work.
"""
from datetime import datetime

def ingest_logs(file_path)->list[str]:
    string_list = []
    with open(file_path) as infile:
        string_list = infile.readlines()
        string_list = [line.strip() for line in string_list]
    return string_list

def format_logs(string_list:list[str])->list[dict]:
    output = list()
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

    return output


if __name__ == "__main__":
    string_list = ingest_logs("sample_logs.log")
    output = format_logs(string_list)

    print("Log Output:")
    for log in output:
        print(log)