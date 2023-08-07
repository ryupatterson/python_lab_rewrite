from enum import Enum
from io import BytesIO, StringIO
from datetime import datetime
from base64 import b64decode
from ipaddress import ip_address
import csv

class HeaderField:
    def __init__(self, header_name, size):
        self.name = header_name
        self.size = size

class IPv4Header(Enum):
    HEADER_LENGTH = HeaderField("header_length", 1)
    IP_VERSION = HeaderField("ip_version", 1)
    TIMESTAMP = HeaderField("timestamp", 4)
    SEQUENCE = HeaderField("sequence", 2)
    SRC_IP = HeaderField("source_ip", 4)
    DST_IP = HeaderField("dest_ip", 4)
    SRC_PORT = HeaderField("source_port", 2)
    DST_PORT = HeaderField("dest_port", 2)
    PROTOCOL_NUM = HeaderField("protocol_num", 1)
    PAYLOAD_LENGTH = HeaderField("payload_length", 4)

class IPv4Constants(Enum):
    HEADER_LENGTH = 25
    IP_VERSION = 4
    PROTOCOL_NUM = 6


class IPv6Header(Enum):
    HEADER_LENGTH = HeaderField("header_length", 1)
    IP_VERSION = HeaderField("ip_version", 1)
    TIMESTAMP = HeaderField("timestamp", 4)
    SEQUENCE = HeaderField("sequence", 2)
    SRC_IP = HeaderField("source_ip", 16)
    DST_IP = HeaderField("dest_ip", 16)
    SRC_PORT = HeaderField("source_port", 2)
    DST_PORT = HeaderField("dest_port", 2)
    PROTOCOL_NUM = HeaderField("protocol_num", 1)
    PAYLOAD_LENGTH = HeaderField("payload_length", 4)

class IPv6Constants(Enum):
    HEADER_LENGTH = 49
    IP_VERSION = 6
    PROTOCOL_NUM = 6

class BinaryMessageHeader(Enum):
    TIMESTAMP = HeaderField("timestamp", 4)
    DATA_UNIT_NUM = HeaderField("number_data_units", 4)
    TOTAL_PAYLOAD_LENGTH = HeaderField("total_payload_length", 6)


class BinaryMessage:
    def __init__(self, timestamp=0, message_num=0, payload_size=0):
        self.timestamp = timestamp
        self.message_num = message_num
        self.payload_size = payload_size
        self.messages = list()
    
    def to_csv(self):
        output = StringIO()
        writer = csv.writer(output, delimiter=",")
        for message in self.messages:
            writer.writerow(message.to_csv())
        return output.getvalue()

    def to_dict(self):
        return [message.to_dict() for message in self.messages]


class DataUnit:
    def __init__(self, header_length: int, ip_version: int, timestamp: datetime, sequence: int, sip: str, dip: str, sport: int, \
                 dport: int, protocol_num: int, payload_length: int, payload: str):
        self.header_length = header_length
        self.ip_version = ip_version
        self.timestamp = timestamp
        self.sequence = sequence
        self.sip = sip
        self.dip = dip
        self.sport = sport
        self.dport = dport
        self.protocol_num = protocol_num
        self.payload_length = payload_length
        self.payload = payload
    
    # return as a list because csv.writeline() takes a list
    def to_csv(self) -> list:
        return [self.header_length,self.ip_version,self.timestamp,self.sequence,self.sip,self.dip, \
        self.sport,self.dport, self.protocol_num, self.payload_length,self.payload]

    def to_dict(self) -> dict:
        return {
            IPv4Header.HEADER_LENGTH.value.name: self.header_length,
            IPv4Header.IP_VERSION.value.name: self.ip_version,
            IPv4Header.TIMESTAMP.value.name: self.timestamp,
            IPv4Header.SEQUENCE.value.name: self.sequence,
            IPv4Header.SRC_IP.value.name: self.sip,
            IPv4Header.DST_IP.value.name: self.dip,
            IPv4Header.SRC_PORT.value.name: self.sport,
            IPv4Header.DST_PORT.value.name: self.dport,
            IPv4Header.PROTOCOL_NUM.value.name: self.protocol_num,
            IPv4Header.PAYLOAD_LENGTH.value.name: self.payload_length,
            "payload": self.payload
        }

    def __str__(self):
        return self.payload

    def __repr__(self):
        return f"\"{self.payload}\""
    
class BinaryMessageParser:
    def parse(self, file: bytes) -> BinaryMessage:
        input_stream = BytesIO(file)
        
        binmsg = BinaryMessage(
            timestamp=int.from_bytes(input_stream.read(BinaryMessageHeader.TIMESTAMP.value.size)),
            message_num=int.from_bytes(input_stream.read(BinaryMessageHeader.DATA_UNIT_NUM.value.size)),
            payload_size=int.from_bytes(input_stream.read(BinaryMessageHeader.TOTAL_PAYLOAD_LENGTH.value.size))
        )
        while input_stream.tell() != len(file):
            header_length_bytes = input_stream.read(IPv4Header.HEADER_LENGTH.value.size)
            header_length = int.from_bytes(header_length_bytes)
            rest_of_header = input_stream.read(header_length-IPv4Header.HEADER_LENGTH.value.size)
            header = header_length_bytes + rest_of_header
            payload_length = int.from_bytes(header[-4:])
            payload = input_stream.read(payload_length)
            binmsg.messages.append(BinaryMessageParser.parse_message(header, payload))
        
        return binmsg
        
    def parse_message(header, payload):
        ip_version = int.from_bytes(header[IPv4Header.HEADER_LENGTH.value.size:IPv4Header.HEADER_LENGTH.value.size+IPv4Header.IP_VERSION.value.size])
        if ip_version == IPv4Constants.IP_VERSION.value:
            header_enum = IPv4Header
        elif ip_version == IPv6Constants.IP_VERSION.value:
            header_enum = IPv6Header
        else:
            raise ValueError("This message does not have the proper IP Version value")
        
        stream = BytesIO(header)
        header_length = stream.read(header_enum.HEADER_LENGTH.value.size)
        ip_version = stream.read(header_enum.IP_VERSION.value.size)
        timestamp = stream.read(header_enum.TIMESTAMP.value.size)
        sequence = stream.read(header_enum.SEQUENCE.value.size)
        sip = stream.read(header_enum.SRC_IP.value.size)
        dip = stream.read(header_enum.DST_IP.value.size)
        sport = stream.read(header_enum.SRC_PORT.value.size)
        dport = stream.read(header_enum.DST_PORT.value.size)
        protocol_num = stream.read(header_enum.PROTOCOL_NUM.value.size)
        payload_length = stream.read(header_enum.PAYLOAD_LENGTH.value.size)

        return DataUnit(
            int.from_bytes(header_length),
            int.from_bytes(ip_version),
            datetime.fromtimestamp(int.from_bytes(timestamp)),
            int.from_bytes(sequence),
            ip_address(int.from_bytes(sip)).exploded,
            ip_address(int.from_bytes(dip)).exploded,
            int.from_bytes(sport),
            int.from_bytes(dport),
            int.from_bytes(protocol_num),
            int.from_bytes(payload_length),
            b64decode(payload).decode()
        ) 
