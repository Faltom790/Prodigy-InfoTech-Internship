# Python Network Sniffer

## Overview

This Python script is a network sniffer implemented using Scapy, a powerful packet manipulation tool. It allows users to capture network packets on specified interfaces, apply filters based on protocols and ports, and display packet information in a structured format.

## Features

- **Packet Capture**: Capture packets on any network interface.
- **Custom Filters**: Filter packets based on protocols and ports.
- **Detailed Analysis**: Display packet details including timestamp, source, destination, protocol, and more in a structured format using PrettyTable.
- **Save Captured Data**: Optionally save captured packets to a .pcap file for further analysis.

## Requirements

- Python 3.x
- Scapy
- PrettyTable

## Usage

1. Clone the repository or download the script file.
2. Install the required dependencies:
3. Run the script with appropriate command-line arguments:


**Options:**
- `-i, --interface`: Specify the interface to sniff on (default: eth0).
- `-c, --count`: Specify the number of packets to capture.
- `-w, --write`: Specify the output file (in .pcap format) to save captured packets.
- `-f, --filters`: Specify protocol and port filters separated by comma (e.g., icmp,tcp,udp).

## Example

```bash
python sniffer.py -i eth0 -c 100 -w output.pcap -f tcp,udp

