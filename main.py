from functions import checkCountryInfo

def servicesMenu():
    print('[1] Check IP Information')
    print('[2] Check Number of IPs in a Country')
    print('[3] Check Number of IPs in a City')
    print('[4] Check Number of IPs for an ISP')
    print('[5] Check Sessions Information')
    print('[6] Release a Sticky Session')
    print('[7] Get Stats')
    print('[8] Get Current Thread Usage')

def productMenu():
    print('[1] Unmetered Residential')
    print('[2] Premium GEO Residential')
    print('[3] Private Residential')
    print('[4] Mobile Proxies')
    print('[5] USA Datacenter')
    print('[6] Global Datacenter')
    print('[7] Canada Datacenter')
    print('[8] Static USA Datacenter')

def authMenu():
    print('[1] Username/Password')
    print('[2] IP Whitelisting')

def portMenu():
    print('[1] Rotating (New IP on each request)')
    print('[2] Sticky')

productMenu()
product = int(input('Enter which proxy product you would like to test: '))
if (product == 3) or (product == 4) or (product == 8):
    port = 2
else:
    portMenu()
    port = int(input('Which type of port would you like to use: '))
# authMenu()
# auth = int(input('What authentication method would you like to use: '))
country = input('Country Abbreviation: ')
checkCountryInfo(product, country, port)