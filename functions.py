import requests
from shared import getProductName, getProxyURL
import json

def checkIPInfo():
    print('check IP info')

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
    print(product)
    print(port)

def checkSessionsInfo(product, port):
    print(product)
    print(port)

def releaseSession(product, port):
    print(product)
    print(port)

def getStats(product, port):
    print(product)
    print(port)

def getThreads(product, port):
    print(product)
    print(port)
