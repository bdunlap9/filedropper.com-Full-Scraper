import requests
from bs4 import BeautifulSoup as BS
urls = ['http://www.filedropper.com/lister.php?id=0', 'http://www.filedropper.com/lister.php?id=1', 'http://www.filedropper.com/lister.php?id=2', 'http://www.filedropper.com/lister.php?id=3', 'http://www.filedropper.com/lister.php?id=4', 'http://www.filedropper.com/lister.php?id=5', 'http://www.filedropper.com/lister.php?id=6', 'http://www.filedropper.com/lister.php?id=7', 'http://www.filedropper.com/lister.php?id=8', 'http://www.filedropper.com/lister.php?id=9', 'http://www.filedropper.com/lister.php?id=a', 'http://www.filedropper.com/lister.php?id=b', 'http://www.filedropper.com/lister.php?id=c', 'http://www.filedropper.com/lister.php?id=d', 'http://www.filedropper.com/lister.php?id=e', 'http://www.filedropper.com/lister.php?id=f', 'http://www.filedropper.com/lister.php?id=g', 'http://www.filedropper.com/lister.php?id=h', 'http://www.filedropper.com/lister.php?id=i', 'http://www.filedropper.com/lister.php?id=j', 'http://www.filedropper.com/lister.php?id=k', 'http://www.filedropper.com/lister.php?id=l', 'http://www.filedropper.com/lister.php?id=m', 'http://www.filedropper.com/lister.php?id=n', 'http://www.filedropper.com/lister.php?id=o', 'http://www.filedropper.com/lister.php?id=p', 'http://www.filedropper.com/lister.php?id=q', 'http://www.filedropper.com/lister.php?id=r', 'http://www.filedropper.com/lister.php?id=s', 'http://www.filedropper.com/lister.php?id=t', 'http://www.filedropper.com/lister.php?id=u', 'http://www.filedropper.com/lister.php?id=v', 'http://www.filedropper.com/lister.php?id=w', 'http://www.filedropper.com/lister.php?id=x', 'http://www.filedropper.com/lister.php?id=y', 'http://www.filedropper.com/lister.php?id=z']
for url in urls:
    req = requests.get(url, 'html.parse')
    soup = BS(req.text)
    for all_links in soup.find_all('a', href=True):
        print("URL:", all_links['href'])
        with open('output.txt', 'a') as f:
            f.write(all_links['href'] + '\n')
