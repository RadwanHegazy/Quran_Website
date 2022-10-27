from app.models import Ayah, Surah
from django.shortcuts import render
# Create your views here.


def home (request) :
    if 'q' in request.GET:
        q = request.GET['q']
        all_surah = Surah.objects.filter(surah_name_2__icontains=q)
    else :
        all_surah = Surah.objects.all()
    return render(request,'index.html',{'surahs':all_surah})

def read (request, uid):
    get_surah = Surah.objects.get(surah_uid=uid)
    ayahs = Ayah.objects.filter(surah=get_surah)
    
    words = []
    audio = []

    for i in ayahs :
        words.append(i.text)
        audio.append(i.audio)

    contx = {
        'name':get_surah.surah_name,
        'type':get_surah.surah_type,
        'ayahs_num':get_surah.number_of_ayahs,
        'words':'@'.join(words),
        'audio':'@'.join(audio),
    }
    return render(request,'quran.html',contx)
