import io
from data_structs import *
from datetime import datetime, timedelta
import tarfile
import time
import os
import random

def generate_schmitt_and_trusnik():
    conversation = list()

    sequence = 12892
    timestamp = datetime(2023, 6, 10, 15, 33, 30)
    destination_port = random.randint(1, 65535)

    p1 = User.SCHMITT.value.ip
    p2 = User.TRUSNIK.value.ip

    conversation.append(DataUnit(
        6,
        timestamp,
        sequence,
        p1, 
        p2,
        random.randint(1, 65535),
        destination_port,
        "Yo, can you get these annoying students out of my classroom?"
    ))
    sequence += 1

    timestamp += timedelta(minutes=27, seconds=22)
    conversation.append(DataUnit(
        6,
        timestamp, 
        sequence,
        p2, 
        p1,
        random.randint(1, 65535),
        destination_port,
        "Sorry, not much I can do atm. Who's being annoying in particular?"
    ))
    sequence += 1

    timestamp += timedelta(minutes=3, seconds=18)
    conversation.append(DataUnit(
        6,
        timestamp, 
        sequence,
        p1, 
        p2,
        random.randint(1, 65535),
        destination_port,
        "They're all so annoying I can't pick a single one."
    ))
    return conversation

def generate_lee_and_rosales():
    conversation = list()

    timestamp = datetime(2023, 5, 18, 8, 10, 00)
    sequence = 10489
    destination_port = random.randint(1, 65535)

    p1 = User.LEE.value.ip
    p2 = User.ROSALES.value.ip

    conversation.append(DataUnit(
        4,
        timestamp,
        sequence,
        p1, 
        p2,
        random.randint(1, 65535),
        destination_port,
        "I just noticed that you added more stuff to the windows block, when are you going to be done adding more content?"
    ))
    sequence += 1

    timestamp += timedelta(minutes=12, seconds=22)
    conversation.append(DataUnit(
        4,
        timestamp, 
        sequence,
        p2, 
        p1,
        random.randint(1, 65535),
        destination_port,
        "bahahaha sorry man, can't stop wont stop"
    ))

    return conversation

def generate_rosales_and_tracy():
    conversation = list()

    timestamp = datetime(2023, 6, 29, 8, 10, 00)
    sequence = 623
    destination_port = random.randint(1, 65535)

    p1 = User.TRACY.value.ip
    p2 = User.ROSALES.value.ip

    conversation.append(DataUnit(
        4,
        timestamp,
        sequence,
        p1, 
        p2,
        random.randint(1, 65535),
        destination_port,
        "hey I got a quick question for you"
    ))
    sequence += 1

    timestamp += timedelta(minutes=2, seconds=1)
    conversation.append(DataUnit(
        4,
        timestamp,
        sequence,
        p2, 
        p1,
        random.randint(1, 65535),
        destination_port,
        "shoot"
    ))
    sequence += 1

    timestamp += timedelta(minutes=1, seconds=32)
    conversation.append(DataUnit(
        4,
        timestamp,
        sequence,
        p1, 
        p2,
        random.randint(1, 65535),
        destination_port,
        "you know your mentee that got his germany drop?"
    ))
    sequence += 1
    
    timestamp += timedelta(minutes=9, seconds=29)
    conversation.append(DataUnit(
        4,
        timestamp, 
        sequence,
        p2, 
        p1,
        random.randint(1, 65535),
        destination_port,
        "yeah what about him"
    ))
    sequence += 1

    timestamp += timedelta(minutes=19, seconds=00)
    conversation.append(DataUnit(
        4,
        timestamp, 
        sequence,
        p1, 
        p2,
        random.randint(1, 65535),
        destination_port,
        "i would like his assignment taken away immediately. contact AFPC at once"
    ))
    sequence += 1

    timestamp += timedelta(minutes=6, seconds=15)
    conversation.append(DataUnit(
        4,
        timestamp, 
        sequence,
        p2, 
        p1,
        random.randint(1, 65535),
        destination_port,
        "LOL whys that"
    ))
    sequence += 1

    timestamp += timedelta(minutes=3, seconds=76)
    conversation.append(DataUnit(
        4,
        timestamp, 
        sequence,
        p1, 
        p2,
        random.randint(1, 65535),
        destination_port,
        "he's always getting stuff wrong in class, we can't send him over there"
    ))
    return conversation

if __name__ == "__main__":
    combined = list()
    combined.extend(generate_lee_and_rosales())
    combined.extend(generate_rosales_and_tracy())
    combined.extend(generate_schmitt_and_trusnik())

    random.shuffle(combined) # randomize array
    file1_messages = combined[:len(combined)//3].copy()
    file2_messages = combined[len(combined)//3:].copy()

    file1 = BinaryMessage()
    for message in file1_messages:
        file1.add_message(message)
    
    file2 = BinaryMessage()
    for message in file2_messages:
        file2.add_message(message)

    outdata1 = file1.encode()
    outdata2 = file2.encode()

    tar_output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    with tarfile.open(os.path.join(tar_output_dir, "example.tar.gz"), mode="w:gz") as tar:
        o1_io = io.BytesIO(outdata1)
        o1_tarinfo = tarfile.TarInfo("file1.binmsg")
        o1_tarinfo.mtime = time.time()
        o1_tarinfo.size=len(outdata1)

        tar.addfile(tarinfo=o1_tarinfo, fileobj=o1_io)

        o2_io = io.BytesIO(outdata2)
        o2_tarinfo = tarfile.TarInfo("file2.binmsg")
        o2_tarinfo.mtime = time.time()
        o2_tarinfo.size=len(outdata2)

        tar.addfile(tarinfo=o2_tarinfo, fileobj=o2_io)
