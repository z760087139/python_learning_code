from scapy.all import *
from scapy.error import Scapy_Exception
import scapy_http.http as HTTP


def pktTCP(pkt):

    if HTTP.HTTPRequest or HTTP.HTTPResponse in pkt:

        src=pkt[IP].src

        srcport=pkt[IP].sport

        dst=pkt[IP].dst

        dstport=pkt[IP].dport

        test=pkt[TCP].payload

        if HTTP.HTTPRequest in pkt:

            #print "HTTP Request:"

            #print test

            print("======================================================================")

        if HTTP.HTTPResponse in pkt:

            print("HTTP Response:")

            try:

                headers,body= str(test).split("\r\n\r\n", 1)

                print(headers)

            except Exception as e:

                print(e)

            print("======================================================================")

    else:

        #print pkt[IP].src,pkt[IP].sport,'->',pkt[TCP].flags

        print('other')


sniff(filter='ip src www.baidu.com',prn=lambda x:x.show())
