import requests
from .models import Surah
url = 'http://api.alquran.cloud/v1/surah/10/ar.alafasy'


# r = requests.get(url).json()

# ar_surah_name = r['data']['name']
# surah_id = r['data']['number']
# en_surah_name = r['data']['englishName']
# numberOfAyahs = r['data']['numberOfAyahs']
# revelationType = r['data']['revelationType']
# audio = r['data']['ayahs'][0]['audio']


# main = ''
# for i in r['data']['ayahs'] : 
    # ayah = str(i['text']).replace('\n','')
    # number_in_the_surah = i['numberInSurah']
    # main += f'{ayah} ({number_in_the_surah}) '
    # print(i['text'], i['audio'])
# print(main)



# WORK WITH SURAHs

u = 'http://api.alquran.cloud/v1/surah'

req = requests.get(u).json()




for i in req['data']: 
    old_name = i['name']
    new_name = ''
    for o in old_name:
        if o.isalnum():
            new_name += o
    new_name = new_name.replace('سورة','')

    rel = ''
    if i['revelationType'] == 'Meccan' : 
        rel ='مكية'
    else :
        rel = 'مدنية'


    print(
        i['name'],
        i['number'],
        rel,
        i['numberOfAyahs'],
        new_name
        )
