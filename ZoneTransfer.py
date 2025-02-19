import dns.query
import dns.zone
import dns.resolver

def get_dns_servers(domain):
    """Finds the authoritative nameservers for the domain"""
    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        return [str(ns.target) for ns in ns_records]
    except Exception as e:
        print(f"[!] Error fetching nameservers: {e}")
        return []

def attempt_zone_transfer(domain, nameserver):
    """Attempts a DNS zone transfer from the given nameserver"""
    try:
        print(f"[*] Trying Zone Transfer on {nameserver} for {domain}...")
        zone = dns.zone.from_xfr(dns.query.xfr(nameserver, domain))
        subdomains = [f"{name}.{domain}" for name in zone.nodes.keys()]
        print(f"[+] Zone Transfer Successful on {nameserver}!")
        return subdomains
    except Exception:
        print(f"[-] Zone Transfer Failed on {nameserver}.")
        return []

def main():
    domain = input("Enter the target domain: ")
    
    print(f"[*] Finding nameservers for {domain}...")
    nameservers = get_dns_servers(domain)
    
    if not nameservers:
        print("[!] No nameservers found. Exiting.")
        return

    all_subdomains = set()
    
    for ns in nameservers:
        subdomains = attempt_zone_transfer(domain, ns)
        all_subdomains.update(subdomains)
    
    if all_subdomains:
        print("\n[+] Discovered Subdomains via Zone Transfer:")
        for sub in sorted(all_subdomains):
            print(sub)
    else:
        print("\n[-] No subdomains found via Zone Transfer.")

if __name__ == "__main__":
    main()
