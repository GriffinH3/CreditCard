'''
Function for regular Expression to find credit card info for Visa, MasterCard, Amex
With option to load it into a packet sniffer
'''
import re

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

    