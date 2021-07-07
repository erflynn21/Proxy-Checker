def getProxyURL(product, port):
    if product == 1 and port == 1:
        proxy = {
            'https': 'http://megaproxy.rotating.proxyrack.net:222',
            'http': 'http://megaproxy.rotating.proxyrack.net:222'
        }
    elif product == 1 and port != 1:
        proxy = {
            'https': f'http://megaproxy.rotating.proxyrack.net:{port}',
            'http': f'http://megaproxy.rotating.proxyrack.net:{port}'
        }
    elif product == 2 and port == 1:
        proxy = {
            'https': 'http://premium.residential.proxyrack.net:9000',
            'http': 'http://premium.residential.proxyrack.net:9000'
        }
    elif product == 2 and port != 1:
        proxy = {
            'https': f'http://premium.residential.proxyrack.net:{port}',
            'http': f'http://premium.residential.proxyrack.net:{port}'
        }
    elif product == 3:
        proxy = {
            'https': f'http://private.residential.proxyrack.net:{port}',
            'http': f'http://private.residential.proxyrack.net:{port}'
        }
    elif product == 4:
        proxy = {
            'https': f'http://us.mobile.proxyrack.net:{port}',
            'http': f'http://us.mobile.proxyrack.net:{port}'
        }
    elif product == 5 and port == 1:
        proxy = {
            'https': 'http://usa.rotating.proxyrack.net:333',
            'http': 'http://usa.rotating.proxyrack.net:333'
        }
    elif product == 5 and port != 1:
        proxy = {
            'https': f'http://usa.rotating.proxyrack.net:{port}',
            'http': f'http://usa.rotating.proxyrack.net:{port}'
        }
    elif product == 6 and port == 1:
        proxy = {
            'https': 'http://mixed.rotating.proxyrack.net:444',
            'http': 'http://mixed.rotating.proxyrack.net:444'
        }
    elif product == 6 and port != 1:
        proxy = {
            'https': f'http://mixed.rotating.proxyrack.net:{port}',
            'http': f'http://mixed.rotating.proxyrack.net:{port}'
        }
    elif product == 7 and port == 1:
        proxy = {
            'https': 'http://canada.rotating.proxyrack.net:9000',
            'http': 'http://canada.rotating.proxyrack.net:9000'
        }   
    elif product == 7 and port != 1:
        proxy = {
            'https': f'http://canada.rotating.proxyrack.net:{port}',
            'http': f'http://canada.rotating.proxyrack.net:{port}'
        }      
    elif product == 8:
        proxy = {
            'https': f'http://usa.shared.proxyrack.net:{port}',
            'http': f'http://usa.shared.proxyrack.net:{port}'
        }   
    
    return proxy 

def getProductName(product):
    if product == 1:
        productName = 'Unmetered Residential'
        return productName
    if product == 2:
        productName = 'Premium GEO Residential'
        return productName
    if product == 3:
        productName = 'Private Residential'
        return productName
    if product == 4:
        productName = 'Mobile'
        return productName
    if product == 5:
        productName = 'USA Rotating Datacenter'
        return productName
    if product == 6:
        productName = 'Global Rotating Datacenter'
        return productName
    if product == 7:
        productName = 'Canada Rotating Datacenter'
        return productName
    if product == 8:
        productName = 'Static USA Datacenter'
        return productName