from enum import Enum
import random
import socket, struct
from binascii import hexlify

class HeaderField:
    def __init__(self, header_name, size):
        self.name = header_name
        self.size = size

class IPv4DataUnit(Enum):
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
    PAYLOAD = HeaderField("payload", -1)

class IPv6DataUnit(Enum):
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
    PAYLOAD = HeaderField("payload", -1)


class BINMSG_Header(Enum):
    TIMESTAMP = HeaderField("timestamp", 4)
    DATA_UNIT_NUM = HeaderField("number_data_units", 4)
    TOTAL_PAYLOAD_LENGTH = HeaderField("total_payload_length", 6)

class Persona(Enum):
    LEE = "LEE"
    SCHMITT = "SCHMITT"
    TRACY = "TRACY"
    ROSALES = "ROSALES"
    TRUSNIK = "TRUSNIK"

class IPVersion(Enum):
    IPV6 = 6
    IPV4 = 4

IP_PERSONA_CROSSWALK = {
    IPVersion.IPV4.value: {
        Persona.TRACY.value: "78.52.12.78",
        Persona.LEE.value: "11.17.88.92",
        Persona.ROSALES.value: "201.78.52.72"
    }, 
    IPVersion.IPV6.value: {
        Persona.SCHMITT.value: "1820:26db:91fe:c5a2:1d07:a0e1:0700:2d5a",
        Persona.TRUSNIK.value: "16d9:017c:c1ed:b740:0c46:24b1:3e86:5254",
    }
}

CONSTANTS = {
    IPVersion.IPV6.value: {
        IPv6DataUnit.HEADER_LENGTH.value.name: 49,
    },
    IPVersion.IPV4.value: {
        IPv4DataUnit.HEADER_LENGTH.value.name: 25,
    }
}

def encode_ip(ip:str, ip_version):
    return int(hexlify(socket.inet_pton(socket.AF_INET6, ip)), 16).to_bytes(length=IPv6DataUnit.SRC_IP.value.size) if ip_version == IPVersion.IPV6.value else struct.unpack("!L", socket.inet_aton(ip))[0].to_bytes(length=IPv4DataUnit.SRC_IP.value.size)

class Message:
    def __init__(self, timestamp:int, sequence:int, sender, recipient, sport:int, dport:int, message):
        self.timestamp = timestamp
        self.sequence = sequence
        self.sender = sender
        self.recipient = recipient
        self.sport = sport
        self.dport = dport
        self.message = message

    def encode_to_binary(self, ip_version):
        return {
            IPv4DataUnit.TIMESTAMP.value.name: self.timestamp.to_bytes(length=IPv4DataUnit.TIMESTAMP.value.size),
            IPv4DataUnit.SEQUENCE.value.name: self.sequence.to_bytes(length=IPv4DataUnit.SEQUENCE.value.size),
            IPv4DataUnit.SRC_IP.value.name: encode_ip(self.sender, ip_version),
            IPv4DataUnit.DST_IP.value.name: encode_ip(self.recipient, ip_version),
            IPv4DataUnit.SRC_PORT.value.name: self.sport.to_bytes(length=IPv4DataUnit.SRC_PORT.value.size),
            IPv4DataUnit.DST_PORT.value.name: self.dport.to_bytes(length=IPv4DataUnit.SRC_PORT.value.size),
            IPv4DataUnit.PAYLOAD.value.name: self.message.encode(),
            IPv4DataUnit.PAYLOAD_LENGTH.value.name: len(self.message.encode()).to_bytes(length=IPv4DataUnit.PAYLOAD_LENGTH.value.size)
        }

class MessagingSesssion:
    def __init__(self, participant_1, participant_2, ip_version):
        self.participants = (participant_1, participant_2)
        self.participant_ips = (IP_PERSONA_CROSSWALK[ip_version][participant_1], IP_PERSONA_CROSSWALK[ip_version][participant_2])
        self.messages = list()
        self.ip_version = ip_version
        self.dest_port = random.randint(1, 1000)

    def add_message(self, timestamp, sequence, sender, recipient, sport, message): # sender and recipient are ip addrs
        self.messages.append(
            Message(
                timestamp,
                sequence,
                sender,
                recipient,
                sport,
                self.dest_port,
                message
            )
        )

    def encode(self):
        data_units = []
        if self.ip_version == IPVersion.IPV4.value:
            default_header = {
                IPv4DataUnit.HEADER_LENGTH.value.name: CONSTANTS[IPVersion.IPV4.value][IPv4DataUnit.HEADER_LENGTH.value.name].to_bytes(1),
                IPv4DataUnit.PROTOCOL_NUM.value.name: int.to_bytes(6, 1),
                IPv4DataUnit.IP_VERSION.value.name: IPVersion.IPV4.value.to_bytes(1)
            }
        else:
            default_header = {
                IPv6DataUnit.HEADER_LENGTH.value.name: CONSTANTS[IPVersion.IPV6.value][IPv6DataUnit.HEADER_LENGTH.value.name].to_bytes(1),
                IPv6DataUnit.PROTOCOL_NUM.value.name: int.to_bytes(6, 1),
                IPv6DataUnit.IP_VERSION.value.name: IPVersion.IPV6.value.to_bytes(1)
            }  
        for message in self.messages:
            message_header = default_header.copy()
            message_header.update(message.encode_to_binary(self.ip_version))
            bin_message = b""
            for field in IPv4DataUnit:
                print(field.value.name, message_header[field.value.name])
                bin_message += message_header[field.value.name]
            data_units.append(bin_message)
        
        return data_units
        