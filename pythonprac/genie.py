import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#제목
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(15) > td.info > a.title.ellipsis

#순위
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number

#가수명
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

genie = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for doc in genie:
    title = doc.select_one('td.info > a.title.ellipsis').text
    rank = doc.select_one('td.number').text[0:2].strip()
    artist = doc.select_one('td.info > a.artist.ellipsis').text

    if title.find('19금') >= 0:
        title = title.replace('19금', '')

    print(rank, title.strip(), artist)
