'''
American express sniff using regular experession
'''

import re

def findCreditCard(raw):
    americaRe = re.findall("3[47][0-9]{13}",raw)
    if americaRe:
        print("[+] Found American Express Card: " + americaRe[0])
    
def main():
    tests = []
    tests.append(' I would like to buy 1 million dogs please')
    tests.append('My card is: 378282246310005 for \$333')

    for test in tests:
        findCreditCard(test)

if __name__ == "__main__":
    main()