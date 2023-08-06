from binmsg_parser import BinaryMessageParser, IPv4Header
import tarfile
import os

def index_by_sip_dip(message_dict_list):
    sequence_nums = list()
    for message in message_dict_list:
        sequence_nums.append(message[IPv4Header.SEQUENCE.value.name])
    sequence_nums.sort()
    return sequence_nums

def message_by_sequence(message_dict_list, sequence):
    for message in message_dict_list:
        if message[IPv4Header.SEQUENCE.value.name] == sequence:
            return message
    raise LookupError(f"Could not find sequence number {sequence}")

IP_NAME_CROSSWALK = {
    "11.17.88.92": "Capt Lee",
    "1820:26db:91fe:c5a2:1d07:a0e1:0700:2d5a": "Capt Schmitt",
    "78.52.12.78": "Capt Tracy",
    "201.78.52.72": "Capt Rosales",
    "16d9:017c:c1ed:b740:0c46:24b1:3e86:5254": "Capt Trusnik"
}


def sorted_by_earliest_timestamp(conversations_dict): # l
    tuple_list = list()
    for key in conversations_dict.keys():
        tuple_list.append((key, conversations_dict[key][0][IPv4Header.TIMESTAMP.value.name]))
    sorted_tuples = sorted(tuple_list, key=lambda pair: pair[1])

    return [pair[0] for pair in sorted_tuples]

if __name__ == "__main__":
    csv_out = list()
    message_dict_list = list()

    main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    with tarfile.open(os.path.join(main_dir, "example.tar.gz")) as infile:
        for member in infile:
            parser = BinaryMessageParser()
            file = infile.extractfile(member)
            parser.parse(file.read())
            csv_out.append(parser.to_csv())
            message_dict_list.extend(parser.to_dict())
    
    answer_key_path = os.path.dirname(__file__)

    with open(os.path.join(answer_key_path, "example.csv"), "w") as outfile:
        outfile.write("".join(csv_out))

    sorted_sequences = index_by_sip_dip(message_dict_list)

    conversations = dict()
    for sequence in sorted_sequences:
        message = message_by_sequence(message_dict_list, sequence)
        key = "-".join(sorted([message[IPv4Header.SRC_IP.value.name], message[IPv4Header.DST_IP.value.name]]))
        if key in conversations:
            conversations[key].append(message)
        else:
            conversations[key] = [message]
    
    sorted_keys = sorted_by_earliest_timestamp(conversations) # sorts the keys based on the earliest timestamp in each conversation

    bin_convos = list()
    for key in sorted_keys:
        ip1, ip2 = key.split("-")
        convo = ""
        p1, p2 = sorted([IP_NAME_CROSSWALK[ip1], IP_NAME_CROSSWALK[ip2]]) # get name, sorted by alphabetical order
        convo+=f"{p1} and {p2}:\n"
        for message in conversations[key]:
            convo+=f"\t[{message[IPv4Header.TIMESTAMP.value.name]}] {IP_NAME_CROSSWALK[message[IPv4Header.SRC_IP.value.name]]}: "\
                f"\"{message['payload']}\"\n"
        bin_convos.append(convo.strip())
    with open(os.path.join(answer_key_path, "example_output.txt"), "w") as outfile:
        outfile.write("\n\n".join(bin_convos))