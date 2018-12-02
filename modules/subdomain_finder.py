import sys
from re import findall
from tld import get_fld
from requests import get

results = {}


def subdomains():
    using = '\33[91musing\33[00m(\33[92;1msubdomain_finder\33[0m) '
    host = input(using + 'host<( ')
    response = get('https://findsubdomains.com/subdomains-of/' + get_fld(host, fix_protocol=True)).text
    parts = response.split('data-row')
    for part in parts:
        matches = findall(
            r'rel="nofollow" href="([^/]*)" target="_blank"|href="https://dnstable.com/ip/(.*)"', part)
        try:
            if matches[1][1] not in results:
                results[matches[1][1]] = []
            results[matches[1][1]].append(matches[0][0])
        except IndexError:
            pass
    for result in results.items():
        sys.stdout.write(result[0] + '\n')
        for subdomain in result[1]:
            sys.stdout.write('    ' + subdomain + '\n')

