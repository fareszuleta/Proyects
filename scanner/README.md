# Port Scanner in Python

A simple multithreaded port scanner written in Python using **Scapy**.  
This project sends TCP SYN packets to a target host and checks the response to determine whether ports are **open**, **closed**, or **filtered**.

## Features

- TCP SYN port scanning
- Multithreaded scanning with `ThreadPoolExecutor`
- Uses `scapy` for packet crafting and network analysis
- Detects:
  - **OPEN**
  - **CLOSED**
  - **Filtered or No Response**

## Requirements

- Python 3.x
- Scapy

Install dependencies with:

```bash
pip install scapy
```

> **Note:** Depending on your system, you may need to run the script with administrator/root privileges because raw packets are used.

## Project Structure

```text
scanner/
└── Scanner.py
```

## How It Works

The scanner:

1. Builds a TCP SYN packet for each port.
2. Sends the packet to the target machine.
3. Waits for a response:
   - **SYN-ACK** → port is **OPEN**
   - **RST-ACK** → port is **CLOSED**
   - No response → port is **Filtered or No Response**
4. Prints the result for each scanned port.

## Usage

Run the script with:

```bash
python3 Scanner.py
```

By default, the script scans the target set in the code:

```python
target = "192.168.0.1"
ports = range(1, 101)
```

You can modify these values directly in the script to scan another host or different port range.

## Example Output

```text
Port 1: CLOSED
Port 2: OPEN
Port 3: Filtered or No Response
```

## Disclaimer

This tool is intended for educational and authorized testing purposes only.  
Only scan systems you own or have explicit permission to test.

## License

Add a license if you plan to share or distribute this project.
