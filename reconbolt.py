def display_flashing_banner():
    """Display a flashing banner effect for ReconBolt"""
    import time
    import os
    
    normal_banner = r"""
 ____                       ____        _ _   
|  _ \ ___  ___ ___  _ __ | __ )  ___ | | |_ 
| |_) / _ \/ __/ _ \| '_ \|  _ \ / _ \| | __|
|  _ <  __/ (_| (_) | | | | |_) | (_) | | |_ 
|_| \_\___|\___\___/|_| |_|____/ \___/|_|\__|
                                           
    ⚡⚡⚡ [ By koreyhacks_ ] ⚡⚡⚡
                 
    [ Automated Reconnaissance Tool - For Ethical Hacking Only ]
    """
    
    inverted_banner = r"""
 ____                       ____        _ _   
|  _ \ ___  ___ ___  _ __ | __ )  ___ | | |_ 
| |_) / _ \/ __/ _ \| '_ \|  _ \ / _ \| | __|
|  _ <  __/ (_| (_) | | | | |_) | (_) | | |_ 
|_| \_\___|\___\___/|_| |_|____/ \___/|_|\__|
                                           
    ☇☇☇ [ By koreyhacks_ ] ☇☇☇
                 
    [ Automated Reconnaissance Tool - For Ethical Hacking Only ]
    """
    
    # Clear screen function - works on both Windows and Unix-like systems
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    
    # Flash the banner 5 times
    for _ in range(5):
        clear()
        print(normal_banner)
        time.sleep(0.3)
        clear()
        print(inverted_banner)
        time.sleep(0.3)
    
    # Final display of the normal banner
    clear()
    print(normal_banner)#!/usr/bin/env python3
# ReconBolt - A comprehensive reconnaissance automation tool
# Author: koreyhacks_
# Created for ethical hacking and penetration testing purposes only

import argparse
import os
import subprocess
import sys
import json
import time
import concurrent.futures
from datetime import datetime

class ReconBolt:
    def __init__(self, target, output_dir="recon_results", threads=5, verbose=False):
        self.target = target
        self.threads = threads
        self.verbose = verbose
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_dir = f"{output_dir}_{self.timestamp}"
        self.results = {}
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
        
        print(f"[+] Initialized ReconBolt with target: {self.target}")
        print(f"[+] Results will be saved to: {self.output_dir}")

    def run_command(self, command, tool_name):
        """Execute a shell command and return its output"""
        try:
            if self.verbose:
                print(f"[*] Running command: {' '.join(command)}")
            
            output_file = os.path.join(self.output_dir, f"{tool_name}_output.txt")
            
            # Run the command and capture output
            process = subprocess.run(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Write output to file
            with open(output_file, 'w') as f:
                f.write(process.stdout)
                if process.stderr:
                    f.write("\n\n=== ERRORS ===\n")
                    f.write(process.stderr)
            
            print(f"[+] {tool_name} scan completed. Results saved to {output_file}")
            return process.stdout
        
        except Exception as e:
            print(f"[!] Error running {tool_name}: {str(e)}")
            return None

    def run_nmap(self):
        """Run Nmap scan on the target"""
        print("\n[+] Starting Nmap scan...")
        
        # Basic command with service detection and OS fingerprinting
        command = [
            "nmap", 
            "-sS", "-sV", "-sC", "-O",
            "--min-rate", "1000",
            "-oN", os.path.join(self.output_dir, "nmap_scan.nmap"),
            self.target
        ]
        
        output = self.run_command(command, "nmap")
        self.results['nmap'] = output
        return output

    def run_whois(self):
        """Run WHOIS lookup on the target"""
        print("\n[+] Starting WHOIS lookup...")
        
        command = ["whois", self.target]
        output = self.run_command(command, "whois")
        self.results['whois'] = output
        return output

    def run_dnsrecon(self):
        """Run DNSRecon on the target"""
        print("\n[+] Starting DNSRecon scan...")
        
        command = [
            "dnsrecon", 
            "-d", self.target,
            "-t", "std,rvl,srv,axfr"
        ]
        
        output = self.run_command(command, "dnsrecon")
        self.results['dnsrecon'] = output
        return output

    def run_subfinder(self):
        """Run Subfinder to discover subdomains"""
        print("\n[+] Starting Subfinder scan...")
        
        output_file = os.path.join(self.output_dir, "subfinder_results.txt")
        command = [
            "subfinder", 
            "-d", self.target,
            "-o", output_file
        ]
        
        output = self.run_command(command, "subfinder")
        
        # Read the results file if it exists
        if os.path.exists(output_file):
            with open(output_file, 'r') as f:
                subdomains = f.read()
            self.results['subfinder'] = subdomains
            return subdomains
        return output

    def run_all_parallel(self):
        """Run all recon tools in parallel using ThreadPoolExecutor"""
        print("\n[+] Running all reconnaissance tools in parallel mode...")
        
        tools = {
            'nmap': self.run_nmap,
            'whois': self.run_whois,
            'dnsrecon': self.run_dnsrecon,
            'subfinder': self.run_subfinder
        }
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            future_to_tool = {executor.submit(func): name for name, func in tools.items()}
            for future in concurrent.futures.as_completed(future_to_tool):
                tool_name = future_to_tool[future]
                try:
                    future.result()
                    print(f"[+] {tool_name} completed successfully")
                except Exception as e:
                    print(f"[!] {tool_name} generated an exception: {str(e)}")

    def run_all_sequential(self):
        """Run all recon tools sequentially"""
        print("\n[+] Running all reconnaissance tools sequentially...")
        
        self.run_whois()
        self.run_dnsrecon()
        self.run_subfinder()
        self.run_nmap()  # Run Nmap last as it's usually the most time-consuming
    
    def generate_report(self):
        """Generate a summary report of all reconnaissance results"""
        print("\n[+] Generating summary report...")
        
        report_file = os.path.join(self.output_dir, "summary_report.txt")
        json_file = os.path.join(self.output_dir, "results.json")
        
        # Write JSON results
        with open(json_file, 'w') as f:
            json.dump(self.results, f, indent=4)
        
        # Generate a human-readable report
        with open(report_file, 'w') as f:
            f.write(f"ReconBolt Reconnaissance Report\n")
            f.write(f"==============================\n\n")
            f.write(f"Target: {self.target}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write(f"Tools executed:\n")
            for tool in self.results.keys():
                f.write(f"- {tool}\n")
            
            f.write(f"\nResults Summary:\n")
            f.write(f"===============\n\n")
            
            # Add tool-specific summaries
            if 'whois' in self.results and self.results['whois']:
                f.write("WHOIS Information:\n")
                f.write("=================\n")
                # Extract and format key WHOIS information
                whois_lines = self.results['whois'].split('\n')
                for line in whois_lines[:20]:  # First 20 lines for summary
                    if ':' in line and not line.startswith('%'):
                        f.write(f"{line.strip()}\n")
                f.write("\n")
            
            if 'subfinder' in self.results and self.results['subfinder']:
                f.write("Discovered Subdomains:\n")
                f.write("=====================\n")
                subdomains = self.results['subfinder'].strip().split('\n')
                for subdomain in subdomains[:10]:  # First 10 subdomains
                    f.write(f"- {subdomain}\n")
                if len(subdomains) > 10:
                    f.write(f"- ... and {len(subdomains) - 10} more\n")
                f.write("\n")
            
            f.write("\nFull results for each tool can be found in their respective output files.\n")
        
        print(f"[+] Summary report generated: {report_file}")
        print(f"[+] JSON results saved: {json_file}")
        
        return report_file

def check_dependencies():
    """Check if all required tools are installed"""
    dependencies = ["nmap", "whois", "dnsrecon", "subfinder"]
    missing = []
    
    for tool in dependencies:
        try:
            subprocess.run(
                ["which", tool], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                check=True
            )
        except subprocess.CalledProcessError:
            missing.append(tool)
    
    if missing:
        print("[!] The following dependencies are missing:")
        for tool in missing:
            print(f"    - {tool}")
        print("\n[!] Please install missing dependencies before running this tool.")
        print("    For Kali Linux, you can use: apt install -y " + " ".join(missing))
        return False
    
    return True

def main():
    # Display the flashing banner
    display_flashing_banner()
    
    parser = argparse.ArgumentParser(description="ReconBolt - A comprehensive reconnaissance automation tool")
    parser.add_argument("target", help="Target domain or IP address")
    parser.add_argument("-o", "--output", default="recon_results", help="Output directory name")
    parser.add_argument("-t", "--threads", type=int, default=4, help="Number of concurrent threads (for parallel mode)")
    parser.add_argument("-p", "--parallel", action="store_true", help="Run tools in parallel mode")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()
    
    # Check dependencies before proceeding
    if not check_dependencies():
        sys.exit(1)
    
    # Initialize and run the tool
    recon_tool = ReconBolt(
        target=args.target,
        output_dir=args.output,
        threads=args.threads,
        verbose=args.verbose
    )
    
    start_time = time.time()
    
    if args.parallel:
        recon_tool.run_all_parallel()
    else:
        recon_tool.run_all_sequential()
    
    # Generate summary report
    recon_tool.generate_report()
    
    elapsed_time = time.time() - start_time
    print(f"\n[+] Reconnaissance completed in {elapsed_time:.2f} seconds")
    print(f"[+] All results saved to {recon_tool.output_dir}")

if __name__ == "__main__":
    main()
