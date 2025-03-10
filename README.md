# ReconBolt ⚡
![2025-03-09 22_36_31-KALI  Running  - Oracle VirtualBox _ 1](https://github.com/user-attachments/assets/2c5b23ac-8ca2-41a5-9207-aa4763604457)

A lightning-fast, all-in-one reconnaissance automation tool for ethical hackers and penetration testers. ReconBolt combines the power of multiple reconnaissance tools into a single, efficient utility.
<br>
<br>
🔋 Features
<br>
**Integrated Toolset**: Seamlessly combines `nmap`, `whois`, `dnsrecon`, and `subfinder` in one tool
<br>
**Parallel Execution**: Optional concurrent scanning for significantly faster results
<br>
**Comprehensive Reporting**: Generates both detailed and summary reports in multiple formats
<br>
**Automated Analysis**: Extracts and highlights the most relevant information from scan results
<br>
**Interactive Banner**: Features a dynamic, flashing banner for a professional look and feel
<br>
**Easy to Use**: Simple interface with sensible defaults for quick deployment
<br>
<br>
💻 Installation
<br>
Prerequisites:
<br>
ReconBolt requires Python 3.6+ and the following tools:
<br>
- nmap
- whois
- dnsrecon
- subfinder
<br>
<br>
Quick Setup for Kali Linux:
<br>
Most dependencies are pre-installed on Kali. If anything is missing:
<br>
Install core dependencies:
<br>
sudo apt update
<br>
sudo apt install -y python3 
<br>
python3-pip nmap whois dnsrecon
<br>
Install subfinder (apt install subfinder [may have to use sudo])
<br>
<br>
Installing ReconBolt:
<br>
Clone the repository:
git clone https://github.com/koreyhacks/reconbolt.git
<br>
cd reconbolt
<br>
Make executable:
<br>
chmod +x reconbolt.py
<br>
<br>
🚀 Usage
<br>
Basic Usage:
<br>
python3 reconbolt.py example.com (or target IP)
<br>
<br>
Command Options:

![2025-03-09 22_24_05-Claude](https://github.com/user-attachments/assets/a9e5acc5-1abb-4eca-8936-cbb9bb4275bf)

<br>
<br>
Examples:
<br>
Basic Scan:
<br>
python3 reconbolt.py example.com
<br>
Parallel scan with 8 threads:
<br>
python3 reconbolt.py example.com -p -t 8
<br>
Custom output directory:
<br>
python3 reconbolt.py example.com -o my_target_recon
<br>
Verbose output:
<br>
python3 reconbolt.py example.com -v
<br>
<br>
📊 Output
<br>
ReconBolt creates a timestamped directory with the following structure:
<br>
<br>
recon_results_YYYYMMDD_HHMMSS/
<br>
├── dnsrecon_output.txt            # DNS reconnaissance results
<br>
├── nmap_output.txt                # Nmap scan output
<br>
├── nmap_scan.nmap                 # Nmap scan in .nmap format
<br>
├── results.json                   # All results in JSON format
<br>
├── subfinder_results.txt          # Discovered subdomains
<br>
├── summary_report.txt             # Human-readable summary
<br>
└── whois_output.txt               # WHOIS lookup information
<br>
<br>
🔍 Tool Integration Details:
<br>
ReconBolt leverages the following tools:
<br>
**Nmap**: Network mapping, port scanning, service detection, and OS fingerprinting
<br>
**Whois**: Domain registration information lookup
<br>
**DNSRecon**: DNS enumeration, zone transfers, and record queries
<br>
**Subfinder**: Fast passive subdomain enumeration
<br>
<br>
🛡️ Ethical Use Notice
<br>
This tool is designed for **ethical hacking and penetration testing purposes only**. Always ensure you:
<br>
1. Have explicit permission to scan targets
<br>
2. Comply with all applicable laws and regulations
<br>
3. Follow responsible disclosure practices
<br>
4. Only scan systems you own or are authorized to test
<br>
<br>
👨‍💻 Author
<br>
Created by **koreyhacks_**
<br>
*For educational purposes only. Use responsibly.*
