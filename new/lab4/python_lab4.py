"""
    Lab 4 is focused around string/file manipulation for log ingestion.
    Ingest the logs from the given file, 'sample_logs.log'. These logs mimic an Apache Web Servers logs.
    The final output of your code should be a list of dictionaries, with each dictionary having the following
    keys: timestamp (int), request_ip (str), http_method (str), requested_resource (str), http_response (str), 
    and response_size (int). The list should be in REVERSE chronological order.

    The logs are in this format:
    request_ip - - [timestamp UTC offset] "HTTP_METHOD requested_resource" http_response response_size

    The data processing should start, and end with the ingest_logs and format_logs methods. Helper methods are 
    encouraged. The output should be from format_logs

    Do NOT change the function declaration of format_logs if you wish for any of the test cases to work.
"""


def ingest_logs(file_path)->list[str]:

    return

def format_logs(string_list:list[str])->list[dict]:

    return 


if __name__ == "__main__":
    string_list = ingest_logs("sample_logs.log")
    output = format_logs(string_list)

    print("Log Output:")
    for log in output:
        print(log)