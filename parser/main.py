from urllib.request import urlopen

url = "https://www.goodreads.com/shelf/show/science"

with urlopen(url) as resp:
    content = resp.read()
    print(content.decode("utf-8"))
