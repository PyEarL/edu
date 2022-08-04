def normalize_url(url):
    if url[:8] == 'https://':
        return url
    elif url[:7] == 'http://':
        return 'https://' + url[7:]
    else:
        return 'https://' + url

url = "http://google.com"
print(normalize_url(url))