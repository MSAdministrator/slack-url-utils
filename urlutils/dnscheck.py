import multiprocessing
import requests

import dns.resolver
from dns.resolver import NXDOMAIN


class DNSCheck(object):

    __results = []

    _dns_records = [
        'NONE',
        'A',
        'NS',
        'MD',
        'MF',
        'CNAME',
        'SOA',
        'MB',
        'MG',
        'MR',
        'NULL',
        'WKS',
        'PTR',
        'HINFO',
        'MINFO',
        'MX',
        'TXT',
        'RP',
        'AFSDB',
        'X25',
        'ISDN',
        'RT',
        'NSAP',
        'NSAP-PTR',
        'SIG',
        'KEY',
        'PX',
        'GPOS',
        'AAAA',
        'LOC',
        'NXT',
        'SRV',
        'NAPTR',
        'KX',
        'CERT',
        'A6',
        'DNAME',
        'OPT',
        'APL',
        'DS',
        'SSHFP',
        'IPSECKEY',
        'RRSIG',
        'NSEC',
        'DNSKEY',
        'DHCID',
        'NSEC3',
        'NSEC3PARAM',
        'TLSA',
        'HIP',
        'CDS',
        'CDNSKEY',
        'CSYNC',
        'SPF',
        'UNSPEC',
        'EUI48',
        'EUI64',
        'TKEY',
        'TSIG',
        'IXFR',
        'AXFR',
        'MAILB',
        'MAILA',
        'ANY',
        'URI',
        'CAA',
        'TA',
        'DLV',
        ]

    def __get_dns_info(self, domain):
        return_list = []
        for item in self._dns_records:
            try:
                answers = dns.resolver.query(domain, item)
                for server in answers:
                    return_list.append({
                        item: server.to_text()
                    })
            except:
                pass
        return return_list
        

    def __get_multiple_dns(self, job_id, data_slice):
        #return_list = []
        for domain in data_slice:
            self.__results.append({
                domain: self.__get_dns_info(domain)
            })
           
            

    def __chunks(self, l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

    def __dispatch_jobs(self, data, job_number):
        total = len(data)
        chunk_size = int(total / job_number)
        slice = self.__chunks(data, chunk_size)
        jobs = []

        for i, s in enumerate(slice):
            j = multiprocessing.Process(target=self.__get_multiple_dns, args=(i, s))
            jobs.append(j)
        for j in jobs:
            j.start()

    def run_processes(self, domain_list, processes=8):
        self.__dispatch_jobs(domain_list,processes)
        return self.__results

    def get_dns(self, domain):
        return_string = 'Here is the DNS Info for *{}*\n'.format(domain)
        for item in self.__get_dns_info(domain):
            for key,val in item.items():
                return_string += "*{key}*: {val}\n".format(key=key,val=val)
        return return_string