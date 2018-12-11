# about @property

# 类似的还有classmethod

class C1(object):
    @property
    def value(self):
        return self._value        
    @value.setter
    def value(self,value):
        assert isinstance(value,int)
        self._value = value
        self._age = value + 10
    @property
    def age(self):
        return self._age


import traceback
from scapy.all import srp, Ether, ARP
IpScan = '192.168.114.1/24'
try:
    ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=IpScan), timeout=2)
except Exception as e:
    print(traceback.format_exc())
else:
    for send, rcv in ans:
        ListMACAddr = rcv.sprintf("%Ether.src%---%ARP.psrc%")
        print(ListMACAddr)
