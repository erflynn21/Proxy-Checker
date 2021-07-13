from functions import checkIPInfo, checkCountryInfo, getCityList, getISPList, checkSessionsInfo, releaseSession, getStats, getThreads, getCountryList

def servicesMenu():
    print('[1] Check IP Information')
    print('[2] Check Number of IPs in a Country')
    print('[3] Get List of Available Countries')
    print('[4] Get List of Available Cities')
    print('[5] Get List of Available ISPs')
    print('[6] Check Sessions Information')
    print('[7] Release a Sticky Session')
    print('[8] Get Stats')
    print('[9] Get Current Thread Usage')

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

servicesMenu()
service = int(input('What would you like to do: '))

productMenu()
product = int(input('Enter which proxy product you would like to test: '))
if (product == 3) or (product == 4) or (product == 8) or (service == 6):
    port = 2
    port = int(input('Which sticky port would you like to use: '))
else:
    portMenu()
    port = int(input('Which type of port would you like to use: '))
    if port == 2:
        port = int(input('Which sticky port would you like to use: '))


if service == 1:
    authMenu()
    auth = int(input('What authentication method would you like to use: '))
    checkIPInfo(product, port, auth)
elif service == 2:
    checkCountryInfo(product, port)
elif service == 3:
    getCountryList(product, port)
elif service == 4:
    getCityList(product, port)
elif service == 5:
    getISPList(product, port)
elif service == 6:
    checkSessionsInfo(product, port)
elif service == 7:
    releaseSession(product, port)
elif service == 8:
    getStats(product, port)
elif service == 9:
    getThreads(product, port)