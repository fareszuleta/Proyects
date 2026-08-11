#!/usr/bin/env python3
import concurrent.futures
import random

from scapy.all import IP, TCP, send, sr1


def scanner(target, port):

    sport = random.randint(1024, 65535)

    packet = IP(dst=target) / TCP(sport=sport, dport=port, flags="S")  # Encapsulation

    response = sr1(packet, timeout=1, verbose=0)
    if response is None:
        return "Filtered or No Response"
    if response.haslayer(TCP):
        if response[TCP].flags == 0x12:  # SYN-ACK
            send(IP(dst=target) / TCP(sport=sport, dport=port, flags="R"), verbose=0)
            return "OPEN"
        elif response[TCP].flags == 0x14:  # RST-ACK
            return "CLOSED"
    return "UNKNOWN"


if __name__ == "__main__":
    target = "192.168.0.1"
    ports = range(1, 101)
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        responses = executor.map(
            lambda p: (p, scanner(target, p)), ports
        )  # map(function, iterable)
    for port, response in responses:
        if response:
            print(f"Port {port}: {response}")
