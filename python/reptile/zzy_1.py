"""
    功能：爬取 https://tatoeba.org/cmn/audio/index/eng 句子、id、链接
    日期：03/12/2020
"""
import requests
from bs4 import BeautifulSoup


def main():
    for i in range(1, 100):
        url = 'https://tatoeba.org/cmn/audio/index/eng?page='+str(i)
        r = requests.get(url, timeout=30)
        bs = BeautifulSoup(r.text, 'lxml')

        info_div = bs.find_all('div', {'class': 'sentenceContent'})
        for div in info_div:
            id = div.get('data-sentence-id')
            text = div.text.strip()
            mp3_name = 'https://audio.tatoeba.org/sentences/eng/'+id+'.mp3'

            print(id, text, mp3_name)

if __name__ == '__main__':
    main()
