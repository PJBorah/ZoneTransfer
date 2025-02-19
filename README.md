# ZoneTransfer
simple DNS Zone Transfer tool written in Python. It attempts a zone transfer (AXFR) on a given domain to find subdomains. If the target DNS server allows zone transfers, it will reveal a list of subdomains and records.

Install dependencies if not already installed:
pip install dnspython

Run the script:

python zonetransfer.py

Enter the target domain (e.g., example.com)
The tool will attempt Zone Transfer (AXFR) on all authoritative nameservers and list subdomains if successful.

Example Output

Enter the target domain: example.com
[*] Finding nameservers for example.com...
[*] Trying Zone Transfer on ns1.example.com for example.com...
[+] Zone Transfer Successful on ns1.example.com!

[+] Discovered Subdomains via Zone Transfer:
admin.example.com
mail.example.com
shop.example.com
vpn.example.com
