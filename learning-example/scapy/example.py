from scapy.all import *
import scapy_http.http as http

def p_func(p):
    if p.haslayer(http.HTTPRequest):
        # http_header = p[http.HTTPRequest].fields
        # headers = http_header['Headers']
        p.show()


dpkt = sniff(filter='tcp', prn=p_func)


