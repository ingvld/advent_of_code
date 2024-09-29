from hashlib import md5


def adventcoin(key):
    hashedkey = key
    n = 1
    while hashedkey[:6] != '000000':
        hashedkey = md5(f'{key}{n}'.encode()).hexdigest()
        n += 1
    print(n-1)


secretkey = 'bgvyzdsv'
adventcoin(secretkey)
