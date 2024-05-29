!pip install googletrans==4.0.0-rc1
!pip install requests
!pip install langdetect

import requests
from langdetect import detect
from googletrans import Translator

API_ANAHTARI = 'API ANAHTARI YOK'
ARAMA_MOTORU_ID = 'YOK'

çevirmen = Translator()

def google_arama(sorgu):
    url = f"https://www.googleapis.com/customsearch/v1?key={API_ANAHTARI}&cx={ARAMA_MOTORU_ID}&q={sorgu}"
    yanıt = requests.get(url)
    veri = yanıt.json()
    if 'items' in veri and veri['items']:
        return veri['items'][0]['snippet'].replace("...", "")
    else:
        return "Üzgünüm, aradığınızı bulamadım."

def dil_tespit_et(metin):
    try:
        return detect(metin)
    except:
        return "en"

def genel_sorular():
    kullanıcı_girişi = input("1 Genel Sorular\n2 İngilizce Türkçe Çeviri\n3 Türkçe İngilizce Çeviri\n4 Matematiksel İşlemler\nLütfen seçiminizi yapın (çıkmak için 'çık' yazın): ")
    if kullanıcı_girişi == '1':
        return genel_soru_işle()
    elif kullanıcı_girişi == '2':
        return ingilizce_turkce_çeviri()
    elif kullanıcı_girişi == '3':
        return turkce_ingilizce_çeviri()
    elif kullanıcı_girişi == '4':
        return matematiksel_işlemler()
    elif kullanıcı_girişi.lower() == 'çık':
        return "Sonra Görüşürüz !"
    else:
        print("Aradığınız çevap bulunamadı.")
        return genel_sorular()

def giriş_işle(giriş):
    if "nasılsın" in giriş.lower() or "naber" in giriş.lower():
        return "Ben bir yapay zeka olduğum için duygularım yok, ancak size yardımcı olmak için buradayım!"
    else:
        yanıt = google_arama(giriş)
        dil = dil_tespit_et(yanıt)
        if dil == "tr":
            return yanıt
        else:
            return "Üzgünüm, aradığınızı bulamadım."

def genel_soru_işle():
    kullanıcı_girişi = input("Sorunuzu sorun (çıkmak için 'çık' yazın): ")
    if kullanıcı_girişi.lower() == 'çık':
        return "İşlem iptal edildi."
    else:
        return giriş_işle(kullanıcı_girişi)

def ingilizce_turkce_çeviri():
    kullanıcı_girişi = input("İngilizce metni girin (çıkmak için 'çık' yazın): ")
    if kullanıcı_girişi.lower() == 'çık':
        return "İşlem iptal edildi."
    else:
        çevrilen_metin = çevirmen.translate(kullanıcı_girişi, src='en', dest='tr').text
        return çevrilen_metin

def turkce_ingilizce_çeviri():
    kullanıcı_girişi = input("Türkçe metni girin (çıkmak için 'çık' yazın): ")
    if kullanıcı_girişi.lower() == 'çık':
        return "İşlem iptal edildi."
    else:
        çevrilen_metin = çevirmen.translate(kullanıcı_girişi, src='tr', dest='en').text
        return çevrilen_metin

def matematiksel_işlemler():
    kullanıcı_girişi = input("Matematiksel işlemi girin (çıkmak için 'çık' yazın): ")
    if kullanıcı_girişi.lower() == 'çık':
        return "İşlem iptal edildi."
    else:
        try:
            sonuç = eval(kullanıcı_girişi)
            return f"Sonuç: {sonuç}"
        except:
            return "Geçersiz işlem."

while True:
    yanıt = genel_sorular()
    if yanıt == "çık":
        print("Sonra Görüşürüz !")  
        break
    elif yanıt.lower() == "çık":
        print("Sonra Görüşürüz !")  
        break
    else:
        print(yanıt)
