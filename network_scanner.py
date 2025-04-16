import nmap
import datetime

import pyfiglet
from termcolor import colored

text = pyfiglet.figlet_format("Blackout Cyber")
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

for i, line in enumerate(text.split("\n")):
    print(colored(line, colors[i % len(colors)]))


def scan_network(target_ip):
    scanner = nmap.PortScanner()
    try:
        print(f"Scanning {target_ip}...")
        scanner.scan(hosts=target_ip, arguments='-sV')

        report = f"Network Vulnerability Report\nTarget: {target_ip}\nGenerated: {datetime.datetime.now()}\n\n"

        # Simple CVE matching database (expandable)
        known_vulns = {
            'OpenSSH': ['CVE-2018-15473', 'CVE-2020-15778'],
            'Apache': ['CVE-2021-41773'],
            'vsftpd': ['CVE-2011-2523'],
            'Microsoft IIS': ['CVE-2017-7269'],
        }

        for host in scanner.all_hosts():
            report += f"Host: {host} ({scanner[host].hostname()})\n"
            report += f"State: {scanner[host].state()}\n"

            for proto in scanner[host].all_protocols():
                report += f"\nProtocol: {proto}\n"
                lport = scanner[host][proto].keys()
                for port in sorted(lport):
                    state = scanner[host][proto][port]['state']
                    name = scanner[host][proto][port]['name']
                    product = scanner[host][proto][port].get('product', '')
                    version = scanner[host][proto][port].get('version', '')
                    service_str = f"{name} {product} {version}".strip()

                    report += f"Port: {port}\tState: {state}\tService: {service_str}\n"

                    # Remediation Suggestions
                    if state == 'open':
                        if 'http' in name:
                            report += "  > Recommendation: Use HTTPS and keep the web server updated.\n"
                        elif 'ssh' in name:
                            report += "  > Recommendation: Use key-based SSH authentication. Disable root login.\n"
                        elif 'ftp' in name:
                            report += "  > Recommendation: Replace FTP with SFTP or FTPS.\n"
                        elif 'telnet' in name:
                            report += "  > Recommendation: Disable Telnet and use SSH instead.\n"

                    # CVE matching
                    for service_key in known_vulns:
                        if service_key.lower() in service_str.lower():
                            for cve in known_vulns[service_key]:
                                report += f"  ⚠ CVE Found: {cve} - https://cve.mitre.org/cgi-bin/cvename.cgi?name={cve}\n"

        report += "\nScan completed successfully.\nReport generated by Blackout Cyber.\n"
        return report
    except Exception as e:
        return f"Error scanning {target_ip}: {e}"

# Example usage
if __name__ == "__main__":
    target = input("Enter target IP or domain (e.g., scanme.org): ")
    result = scan_network(target)
    with open("final_scan_report.txt", "w") as file:
        file.write(result)
    print("Scan complete. Report saved to final_scan_report.txt")
