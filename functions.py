import requests
from shared import getProductName, getProxyURL
import json

def checkIPInfo(product, port, auth):
    print(product)
    print(port)
    print(auth)

def checkCountryInfo(product, port):
    country = input('Country Abbreviation: ')

    proxy = getProxyURL(product, port)

    url = 'http://api.proxyrack.net/countries/' + country + '/count'

    r = requests.get(url, proxies=proxy)
    result = r.json()
    productName = getProductName(product)
    print(f'We currently have {result} {productName} IPs available in {country}.')

def getCountryList(product, port):
    proxy = getProxyURL(product, port)

    url = 'http://api.proxyrack.net/countries'

    r = requests.get(url, proxies=proxy)
    result = r.json()
    results = ', '.join(result)
    productName = getProductName(product)
    print(f'We currently have {productName} IPs available in the following countries: {results}.')

def getCityList(product, port):
    country = input('Country Abbreviation: ')

    proxy = getProxyURL(product, port)

    url = 'http://api.proxyrack.net/countries/' + country + '/cities'

    r = requests.get(url, proxies=proxy)
    result = r.json()
    results = ', '.join(result)
    productName = getProductName(product)
    print(f'We currently have {productName} IPs available in the following {country} cities: {results}.')

def getISPList(product, port):
    country = input('Country Abbreviation: ')

    proxy = getProxyURL(product, port)

    url = 'http://api.proxyrack.net/countries/' + country + '/isps'

    r = requests.get(url, proxies=proxy)
    result = r.json()
    results = ', '.join(result)
    productName = getProductName(product)
    print(f'We currently have {productName} IPs available with the following {country} ISPs: {results}.')

def checkSessionsInfo(product, port):
    proxy = getProxyURL(product, port)

    url = 'http://api.proxyrack.net/sessions'

    r = requests.get(url, proxies=proxy)
    result = r.json()
    print(json.dumps(result, indent=2))

def releaseSession(product, port):
    proxy = getProxyURL(product, port)

    url = 'http://api.proxyrack.net/release'

    r = requests.get(url, proxies=proxy)
    result = r.json()
    print(json.dumps(result, indent=2))

def getStats(product, port):
    print(product)
    print(port)

def getThreads(product, port):
    print(product)
    print(port)
