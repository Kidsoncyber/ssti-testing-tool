#!/usr/bin/env python3
"""
SSTI (Server-Side Template Injection) Vulnerability Scanner
Author: YourName
"""

import requests
import argparse
from urllib.parse import urlparse

# Payloads for different template engines
PAYLOADS = {
    'jinja2': {
        'test': '{{7*7}}',
        'confirm': '{{7*7}}',
        'expected': '49'
    },
    'twig': {
        'test': '{{7*7}}',
        'confirm': '{{7*7}}',
        'expected': '49'
    },
    'freemarker': {
        'test': '${7*7}',
        'confirm': '${7*7}',
        'expected': '49'
    },
    'velocity': {
        'test': '#set($x=7*7)${x}',
        'confirm': '#set($x=7*7)${x}',
        'expected': '49'
    }
}

def test_ssti(url, param, payload, expected, timeout=10):
    try:
        params = {param: payload}
        response = requests.get(url, params=params, timeout=timeout)
        
        if expected in response.text:
            return True, response.text
    except Exception as e:
        pass
    return False, None

def scan_url(url, timeout=10, verbose=False):
    parsed = urlparse(url)
    params = dict([p.split('=') for p in parsed.query.split('&')]) if parsed.query else {}
    
    if not params:
        print(f"[!] No parameters found in URL: {url}")
        return False
    
    vulnerabilities = []
    
    for param in params.keys():
        for engine, payload_data in PAYLOADS.items():
            if verbose:
                print(f"[*] Testing {param} for {engine} SSTI...")
            
            vulnerable, response = test_ssti(
                url, 
                param, 
                payload_data['test'], 
                payload_data['expected'],
                timeout
            )
            
            if vulnerable:
                confirm_vuln, _ = test_ssti(
                    url,
                    param,
                    payload_data['confirm'],
                    payload_data['expected'],
                    timeout
                )
                
                if confirm_vuln:
                    print(f"\n[+] VULNERABLE: {engine} SSTI found in parameter: {param}")
                    print(f"[*] URL: {url}")
                    print(f"[*] Payload: {payload_data['test']}")
                    print(f"[*] Expected: {payload_data['expected']}")
                    print(f"[*] Engine: {engine}\n")
                    vulnerabilities.append({
                        'parameter': param,
                        'engine': engine,
                        'payload': payload_data['test'],
                        'url': url
                    })
    
    return vulnerabilities

def main():
    parser = argparse.ArgumentParser(description="SSTI Vulnerability Scanner")
    parser.add_argument("-u", "--url", help="Target URL to scan")
    parser.add_argument("-f", "--file", help="File containing multiple URLs to scan")
    parser.add_argument("-t", "--timeout", type=int, default=10, help="Request timeout in seconds")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()
    
    if not args.url and not args.file:
        parser.print_help()
        return
    
    if args.url:
        scan_url(args.url, args.timeout, args.verbose)
    
    if args.file:
        with open(args.file, 'r') as f:
            urls = f.read().splitlines()
        
        for url in urls:
            scan_url(url.strip(), args.timeout, args.verbose)

if __name__ == "__main__":
    main()
