import io
import os
from data_structs import *
from datetime import datetime, timedelta
import tarfile
import time

def generate_schmitt_and_trusnik():
    session = MessagingSesssion(
        Persona.SCHMITT.value, Persona.TRUSNIK.value, IPVersion.IPV6.value
    )

    sequence = 12892
    timestamp = datetime(2023, 6, 10, 15, 33, 30)
    session.add_message(
        int(timestamp.timestamp()),
        sequence,
        session.participant_ips[0], 
        session.participant_ips[1],
        random.randint(1, 65535),
        "Yo, can you get these annoying students out of my classroom?"
    )
    sequence += 1

    timestamp += timedelta(minutes=27, seconds=22)
    session.add_message(
        int(timestamp.timestamp()), 
        sequence,
        session.participant_ips[1], 
        session.participant_ips[0],
        random.randint(1, 65535),
        "Sorry, not much I can do atm. Who's being annoying in particular?"
    )
    sequence += 1

    timestamp += timedelta(minutes=3, seconds=18)
    session.add_message(
        int(timestamp.timestamp()), 
        sequence,
        session.participant_ips[0], 
        session.participant_ips[1],
        random.randint(1, 65535),
        "They're all so annoying I can't pick a single one."
    )
    return session

def generate_lee_and_rosales():
    session = MessagingSesssion(
        Persona.LEE.value, Persona.ROSALES.value, IPVersion.IPV4.value
    )
    timestamp = datetime(2023, 5, 18, 8, 10, 00)
    sequence = 10489

    session.add_message(
        int(timestamp.timestamp()),
        sequence,
        session.participant_ips[0], 
        session.participant_ips[1],
        random.randint(1, 65535),
        "I just noticed that you added more stuff to the windows block, when are you going to be done adding more content?"
    )
    sequence += 1

    timestamp += timedelta(minutes=12, seconds=22)
    session.add_message(
        int(timestamp.timestamp()), 
        sequence,
        session.participant_ips[1], 
        session.participant_ips[0],
        random.randint(1, 65535),
        "bahahaha sorry man, can't stop wont stop"
    )

    return session

def generate_rosales_and_tracy():
    session = MessagingSesssion(
        Persona.TRACY.value, Persona.ROSALES.value, IPVersion.IPV4.value
    )

    timestamp = datetime(2023, 6, 29, 8, 10, 00)
    sequence = 623
    session.add_message(
        int(timestamp.timestamp()),
        sequence,
        session.participant_ips[0], 
        session.participant_ips[1],
        random.randint(1, 65535),
        "hey I got a quick question for you"
    )
    sequence += 1

    timestamp += timedelta(minutes=2, seconds=1)
    session.add_message(
        int(timestamp.timestamp()),
        sequence,
        session.participant_ips[1], 
        session.participant_ips[0],
        random.randint(1, 65535),
        "shoot"
    )
    sequence += 1

    timestamp += timedelta(minutes=1, seconds=32)
    session.add_message(
        int(timestamp.timestamp()),
        sequence,
        session.participant_ips[0], 
        session.participant_ips[1],
        random.randint(1, 65535),
        "you know your mentee that got his germany drop?"
    )
    sequence += 1
    
    timestamp += timedelta(minutes=9, seconds=29)
    session.add_message(
        int(timestamp.timestamp()), 
        sequence,
        session.participant_ips[1], 
        session.participant_ips[0],
        random.randint(1, 65535),
        "yeah what about him"
    )
    sequence += 1

    timestamp += timedelta(minutes=19, seconds=00)
    session.add_message(
        int(timestamp.timestamp()), 
        sequence,
        session.participant_ips[0], 
        session.participant_ips[1],
        random.randint(1, 65535),
        "i would like assignment taken away immediately. contact AFPC at once"
    )
    sequence += 1

    timestamp += timedelta(minutes=6, seconds=15)
    session.add_message(
        int(timestamp.timestamp()), 
        sequence,
        session.participant_ips[1], 
        session.participant_ips[0],
        random.randint(1, 65535),
        "LOL whys that"
    )
    sequence += 1

    timestamp += timedelta(minutes=3, seconds=76)
    session.add_message(
        int(timestamp.timestamp()), 
        sequence,
        session.participant_ips[0], 
        session.participant_ips[1],
        random.randint(1, 65535),
        "he's always getting stuff wrong in class, we can't send him over there"
    ) 
    return session


if __name__ == "__main__":
    session1 = generate_lee_and_rosales()
    session2 = generate_rosales_and_tracy()
    session3 = generate_schmitt_and_trusnik()

    encoded_s1 = session1.encode()
    encoded_s2 = session2.encode()
    encoded_s3 = session3.encode()

    encoded_s1.extend(encoded_s2)
    encoded_s1.extend(encoded_s3)

    random.shuffle(encoded_s1) # randomize array
    outdata_1 = encoded_s1[:len(encoded_s1)//3].copy()
    outdata_2 = encoded_s1[len(encoded_s1)//3:].copy()
    
    
    outdata_1_header = int(datetime.now().timestamp()).to_bytes(length=4) + len(outdata_1).to_bytes(length=4) \
    + sum([len(du) for du in outdata_1]).to_bytes(length=6)

    outdata_2_header = int(datetime.now().timestamp()).to_bytes(length=4) + len(outdata_2).to_bytes(length=4) \
    + sum([len(du) for du in outdata_2]).to_bytes(length=6)

    outdata_1.insert(0, outdata_1_header)
    outdata_2.insert(0, outdata_2_header)

    with tarfile.open("example.tar.gz", mode="w:gz") as tar:
        o1_bytes = b''.join(outdata_1)
        o1_io = io.BytesIO(o1_bytes)
        o1_tarinfo = tarfile.TarInfo("file1.binmsg")
        o1_tarinfo.mtime = time.time()
        o1_tarinfo.size=len(o1_bytes)

        tar.addfile(tarinfo=o1_tarinfo, fileobj=o1_io)

        o2_bytes = b''.join(outdata_2)
        o2_io = io.BytesIO(o2_bytes)
        o2_tarinfo = tarfile.TarInfo("file2.binmsg")
        o2_tarinfo.mtime = time.time()
        o2_tarinfo.size=len(o2_bytes)

        tar.addfile(tarinfo=o2_tarinfo, fileobj=o2_io)
