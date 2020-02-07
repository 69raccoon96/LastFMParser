import requests
from bs4 import BeautifulSoup
import time


class Songs:
    def __init__(self, link):
        self.artist = None
        self.song = None
        self.listeners = None
        self.link = link


url = "https://www.last.fm/ru/music/+releases/out-now/popular"
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
coockie = {"trade": "lfmjs=1; lfmwebp=1; not_first_visit=1; _ga=GA1.2.636787651.1574597156; AMCVS_10D31225525FF5790A490D4D%40AdobeOrg=1; language_prompt_dismissed=1; CBS_INTERNAL=0; s_cc=true; csrftoken=a9XswkVHGsHfwZCIzPOimcaYYxmHidru; lfmjs=1; cbsiaa=29046198649426229666156704442364; AMCV_10D31225525FF5790A490D4D%40AdobeOrg=-894706358%7CMCMID%7C65485953258329136289098086807010055370%7CMCAID%7CNONE%7CMCOPTOUT-1574956923s%7CNONE%7CvVersion%7C2.3.0; s_sq=%5B%5BB%5D%5D; _gid=GA1.2.583226764.1575554129; sessionid=.eJyNkU1P4zAQhn9LcyaW7diOh1uh2e1qBV0EQaWXKK7HNFs328axwof2v28KHOCA2Nto5n1mHmmek6qO_aaKAbtqU4dNcppYdHX0fXKSBAyh-dNWjR3blKPSLFcpN7VOBVBMtROQKr5m0nHDKIORebfvBSvmi5vypwJQH4emXm-xPSa825EBDRmGgdT7fSDHEHmbk7ILZ2_Rkd_HLowIUznTKHIncDzMuQUwaBkql0uXCSOtrfPMUg5UKAZaCRBccQ5KKSZVToUQPFNioimdUJb5vLmUF7P5w2-ZVmI-oYSR61hG_9QM5nZ3cP7pFnj7YAeyShcyH66U2PxAkMUjfDvfwfmSLptOwmK6nR3u-aMxcXZWHIXDq7BwudWSMaM1ozUYidKsLVqDDjJN8b-FP9U1sN7eWc69v15Vv8zUF4dyekVYceGVmN3wOP_u-x7bcnW5HI5m_YtZG70_Scay6vD-9WNfOSR__wFAa6W-:1icrbb:ij8mx8dRoVlPUQ1mCtwWVj8IQJU; utag_main=v_id:016e9d4ddb8c00033c9b61f1357303073002306b00bd0$_sn:9$_ss:0$_st:1575555944316$_pn:2%3Bexp-session$ses_id:1575554127017%3Bexp-session"}


def get_and_build_soup(current_url):
    session = requests.session()
    r = session.get(current_url, cookies=coockie, headers=headers)
    return BeautifulSoup(r.text, "html.parser")


text = get_and_build_soup(url)
blocks = text.findAll("a", {"class": "link-block-target"})
links = []
for block in blocks:
    links.append(block.get("href"))
result =[]
for i in range(len(links)):
    result.append(Songs(links[i]))
for i in range(len(result)):
    current_soup = get_and_build_soup("https://last.fm"+result[i].link)
    time.sleep(3)
    title = current_soup.find("title").text
    position_to_delete = title.find("|")
    c = title[0:position_to_delete-1]
    artist_and_name = c.split('—')
    try:
        result[i].artist = artist_and_name[1]
        result[i].song = artist_and_name[0]
    except:
        result[i].artist = i
        result[i].song = i
    print("Исполнитель: " + result[i].artist + " Название песни: " + result[i].song)
