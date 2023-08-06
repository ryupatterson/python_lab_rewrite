from enum import Enum
import socket, struct
from binascii import hexlify
from base64 import b64encode
from datetime import datetime

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

class DataUnit():
    def __init__(self, ip_version, timestamp: datetime, sequence: int, sip: str, dip: str, sport: int, dport: int, payload: str):
        self.ip_version = ip_version
        self.timestamp = timestamp
        self.sequence = sequence
        self.sip = sip
        self.dip = dip
        self.sport = sport
        self.dport = dport
        self.payload = payload
    
    def encode(self):
        encoded_message = b64encode(self.payload.encode())
        if self.ip_version == IPv4Constants.IP_VERSION.value:
            header_enum = IPv4Header
            constants = IPv4Constants
        elif self.ip_version == IPv6Constants.IP_VERSION.value:
            header_enum = IPv6Header
            constants = IPv6Constants
        else:
            raise TypeError("This message does not have the proper IP Version value")
        return (int.to_bytes(constants.HEADER_LENGTH.value, length=header_enum.HEADER_LENGTH.value.size) + \
            int.to_bytes(constants.IP_VERSION.value, length=header_enum.IP_VERSION.value.size) + \
            int(self.timestamp.timestamp()).to_bytes(length=header_enum.TIMESTAMP.value.size) + \
            self.sequence.to_bytes(length=header_enum.SEQUENCE.value.size) + \
            encode_ip(self.sip, constants.IP_VERSION.value) + encode_ip(self.dip, constants.IP_VERSION.value) + \
            self.sport.to_bytes(length=header_enum.SRC_PORT.value.size) + self.dport.to_bytes(length=header_enum.SRC_PORT.value.size) + \
            int.to_bytes(constants.PROTOCOL_NUM.value, length=header_enum.PROTOCOL_NUM.value.size) + \
            len(encoded_message).to_bytes(length=header_enum.PAYLOAD_LENGTH.value.size) + encoded_message)

    def __repr__(self):
        return f"DataUnit({self.sequence})"
    
class BinaryMessageHeader(Enum):
    TIMESTAMP = HeaderField("timestamp", 4)
    DATA_UNIT_NUM = HeaderField("number_data_units", 4)
    TOTAL_PAYLOAD_LENGTH = HeaderField("total_payload_length", 6)

class Persona:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

class User(Enum):
    LEE = Persona("LEE", "11.17.88.92")
    SCHMITT = Persona("SCHMITT", "1820:26db:91fe:c5a2:1d07:a0e1:0700:2d5a")
    TRACY = Persona("TRACY", "78.52.12.78")
    ROSALES = Persona("ROSALES", "201.78.52.72")
    TRUSNIK = Persona("TRUSNIK", "16d9:017c:c1ed:b740:0c46:24b1:3e86:5254")

def encode_ip(ip:str, ip_version):
    return int(hexlify(socket.inet_pton(socket.AF_INET6, ip)), 16).to_bytes(length=IPv6Header.SRC_IP.value.size) if ip_version == IPv6Constants.IP_VERSION.value else struct.unpack("!L", socket.inet_aton(ip))[0].to_bytes(length=IPv4Header.SRC_IP.value.size)

class BinaryMessage:
    def __init__(self):
        self.messages: list[DataUnit] = list()
    
    def add_message(self, message_object):
        self.messages.append(message_object)

    def encode(self) -> bytes:
        output = b""
        for message in self.messages:
            output += message.encode()
        output = int(datetime.now().timestamp()).to_bytes(length=BinaryMessageHeader.TIMESTAMP.value.size) + \
            len(self.messages).to_bytes(length=BinaryMessageHeader.DATA_UNIT_NUM.value.size) + \
            len(output).to_bytes(length=BinaryMessageHeader.TOTAL_PAYLOAD_LENGTH.value.size) + \
            output
        return output
        
