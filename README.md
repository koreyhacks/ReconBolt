# ReconBolt ⚡

<p align="center">
  <img src="https://img.shields.io/badge/python-3.6+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/platform-Linux%20%7C%20Kali-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/maintained%3F-yes-brightgreen.svg" alt="Maintained">
</p>

A lightning-fast, all-in-one reconnaissance automation tool for ethical hackers and penetration testers. ReconBolt combines the power of multiple reconnaissance tools into a single, efficient utility.

## 🔋 Features

- **Integrated Toolset**: Seamlessly combines `nmap`, `whois`, `dnsrecon`, and `subfinder` in one tool
- **Parallel Execution**: Optional concurrent scanning for significantly faster results
- **Comprehensive Reporting**: Generates both detailed and summary reports in multiple formats
- **Automated Analysis**: Extracts and highlights the most relevant information from scan results
- **Interactive Banner**: Features a dynamic, flashing banner for a professional look and feel
- **Easy to Use**: Simple interface with sensible defaults for quick deployment

## 💻 Installation

### Prerequisites

ReconBolt requires Python 3.6+ and the following tools:

- nmap
- whois
- dnsrecon
- subfinder

### Quick Setup for Kali Linux

Most dependencies are pre-installed on Kali. If anything is missing:

```bash
# Install core dependencies
sudo apt update
sudo apt install -y python3 python3-pip nmap whois dnsrecon

# Install subfinder (if not already installed)
GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder
```

### Installing ReconBolt

```bash
# Clone the repository
git clone https://github.com/koreyhacks/reconbolt.git
cd reconbolt

# Make executable
chmod +x reconbolt.py

# Optional: Install globally
sudo ln -s $(pwd)/reconbolt.py /usr/local/bin/reconbolt
```

## 🚀 Usage

### Basic Usage

```bash
python3 reconbolt.py example.com
```

### Command Options

```
usage: reconbolt.py [-h] [-o OUTPUT] [-t THREADS] [-p] [-v] target

ReconBolt - A comprehensive reconnaissance automation tool

positional arguments:
  target                Target domain or IP address

optional arguments:
  -h, --help            Show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output directory name (default: recon_results)
  -t THREADS, --threads THREADS
                        Number of concurrent threads (default: 4)
  -p, --parallel        Run tools in parallel mode
  -v, --verbose         Enable verbose output
```

### Examples

**Basic scan:**
```bash
python3 reconbolt.py example.com
```

**Parallel scan with 8 threads:**
```bash
python3 reconbolt.py example.com -p -t 8
```

**Custom output directory:**
```bash
python3 reconbolt.py example.com -o my_target_recon
```

**Verbose output:**
```bash
python3 reconbolt.py example.com -v
```

## 📊 Output

ReconBolt creates a timestamped directory with the following structure:

```
recon_results_YYYYMMDD_HHMMSS/
├── dnsrecon_output.txt     # DNS reconnaissance results
├── nmap_output.txt         # Nmap scan output
├── nmap_scan.nmap          # Nmap scan in .nmap format
├── results.json            # All results in JSON format
├── subfinder_results.txt   # Discovered subdomains
├── summary_report.txt      # Human-readable summary
└── whois_output.txt        # WHOIS lookup information
```

## 🔍 Tool Integration Details

ReconBolt leverages the following tools:

- **Nmap**: Network mapping, port scanning, service detection, and OS fingerprinting
- **Whois**: Domain registration information lookup
- **DNSRecon**: DNS enumeration, zone transfers, and record queries
- **Subfinder**: Fast passive subdomain enumeration

## 🛡️ Ethical Use Notice

This tool is designed for **ethical hacking and penetration testing purposes only**. Always ensure you:

1. Have explicit permission to scan targets
2. Comply with all applicable laws and regulations
3. Follow responsible disclosure practices
4. Only scan systems you own or are authorized to test

## 👨‍💻 Author

Created by **koreyhacks_**

*For educational purposes only. Use responsibly.*

---

<p align="center">
  <sub>⚡ Fast. Efficient. Comprehensive. ⚡</sub>
</p>
