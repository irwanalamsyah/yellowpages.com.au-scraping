import requests
from bs4 import BeautifulSoup

term = input('Enter Business type or name : ')
loc = input('Enter Location : ')
count = 0
for page in range(1, 7):
    url = 'https://www.yellowpages.com.au/search/listings?clue={0}&locationClue={1}&pageNumber={2}&referredBy=www.yellowpages.com.au&eventType=pagination'.format(term, loc, page)
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36',
        'cookie': 'JSESSIONID=2746C63911384D9F9F4CDC07AC496CCD; yellow-guid=bd7c4e57-f530-4441-8473-9a6568174984; _vwo_uuid_v2=DD19903F02B1CDA06AA6899BE7BF937E7|8d1c2af443e1451537163fa0c21bc77a; clue=Doctor; locationClue=Melbourne; AMCVS_8412403D53AC3D7E0A490D4C%40AdobeOrg=1; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; s_ecid=MCMID%7C65401007638058842270830069805895736299; _vwo_uuid=DD19903F02B1CDA06AA6899BE7BF937E7; _vwo_sn=0%3A1; AMCV_8412403D53AC3D7E0A490D4C%40AdobeOrg=1585540135%7CMCIDTS%7C18728%7CMCMID%7C65401007638058842270830069805895736299%7CMCAAMLH-1618679456%7C3%7CMCAAMB-1618679456%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1618081857s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; _vwo_ds=3%3At_0%2Ca_0%3A-1%241618074660%3A52.1875544%3A%3A%3A3_0%3A0; _fbp=fb.2.1618074658254.473697131; _gcl_au=1.1.1405099532.1618074658; _sdsat_Postcode=; s_cc=true; _wingify_pc_uuid=dfc9673d788646358bf50088c3cf4e98; wingify_donot_track_actions=0; _awl=3.1618074666.0.4-1b928cab-db5accd3e228a653695228b0a4202c04-6763652d617369612d6561737431-6071dc2a-0'

    }
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.findAll('div', 'listing listing-search listing-data')
    for item in items:
        nama = item.find('a', 'listing-name').text
        count += 1
        print(count, nama)
