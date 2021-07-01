import requests

def servicesMenu():
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

def checkCountryInfo(service, country):
    if service == 1:
        proxy = {
            'https': 'http://megaproxy.rotating.proxyrack.net:222',
            'http': 'http://megaproxy.rotating.proxyrack.net:222'
        }
    elif service == 2:
        proxy = {
            'https': 'http://premium.residential.proxyrack.net:9000',
            'http': 'http://premium.residential.proxyrack.net:9000'
        }
    elif service == 3:
        proxy = {
            'https': 'http://private.residential.proxyrack.net:10000',
            'http': 'http://private.residential.proxyrack.net:10000'
        }
    elif service == 4:
        proxy = {
            'https': 'http://us.mobile.proxyrack.net:10000',
            'http': 'http://us.mobile.proxyrack.net:10000'
        }
    elif service == 5:
        proxy = {
            'https': 'usa.rotating.proxyrack.net:333',
            'http': 'usa.rotating.proxyrack.net:333'
        }
    elif service == 6:
        proxy = {
            'https': 'mixed.rotating.proxyrack.net:444',
            'http': 'mixed.rotating.proxyrack.net:444'
        }
    elif service == 7:
        proxy = {
            'https': 'canada.rotating.proxyrack.net:9000',
            'http': 'canada.rotating.proxyrack.net:9000'
        }        
    elif service == 8:
        proxy = {
            'https': 'usa.shared.proxyrack.net:10000',
            'http': 'canada.rotating.proxyrack.net:9000'
        }   
    

    url = 'http://api.proxyrack.net/countries/' + country + '/count'

    r = requests.get(url, proxies=proxy)

    print(r.json())

servicesMenu()
service = int(input('Enter which service you would like to test: '))
# authMenu()
# auth = int(input('What authentication method would you like to use: '))
country = input('Country Abbreviation: ')
checkCountryInfo(service, country)