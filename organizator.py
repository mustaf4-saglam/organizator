import os
import shutil
import time
os.environ["GRPC_DNS_RESOLVER"] = "native"
from google import genai
from google.genai import types
client=genai.Client(api_key="GOOGLE_API_KEY_HERE")

def dosya_turu_belirle(dosya_adi):
   resim_uzantilari = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg", ".tif", ".tiff"]
   ses_uzantilari = [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".oga", ".wma"]
   video_uzantilari = [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".webm", ".m4v"]
   uzanti = os.path.splitext(dosya_adi)[1].lower()
   if uzanti in resim_uzantilari:
      return "Resimler"
   if uzanti in ses_uzantilari:
      return "Sesler"
   if uzanti in video_uzantilari:
      return "Videolar"
   return None

def tahmin_ai(dosya_adi, satirlar, mevcut_klasorler):
 prompt = f"""
Sen akıllı bir dosya düzenleyicisin. Şu dosya adını ve ilk  7  satırını analiz et analiz et: dosya adı; '{dosya_adi}' içeriği; {satirlar}
    
    Bulunduğun dizinde şu ana kadar şu klasörler var: {mevcut_klasorler}
    
    KURALLAR:
    1. Eğer bu dosya yukarıdaki mevcut klasörlerden birinin içine mantıken uyuyorsa, SADECE o klasörün adını yaz (birebir aynı yazıma dikkat et).
    2. Eğer dosya mevcut klasörlerin HİÇBİRİNE uymuyorsa, içeriğine uygun yepyeni bir klasör adı uydur (tek veya iki kelime).
    3. Kod dosyaları (örneğin .py, .c, .js vb.) mantıklı bir şekilde gruplanmalı.
    4. Sadece klasör adını yaz, nokta veya açıklama ekleme.
"""
 response = client.models.generate_content(
        model='gemini-3.1-flash-lite',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.0
            )
    )
 return response.text.strip()

dosya_yolu=os.getcwd()
dosyalar=os.listdir()
adet=0
for dosya in dosyalar:
   if dosya == "organizator.py" or dosya.startswith("."):
      continue
   if os.path.isdir(dosya):
      continue

   mevcut_klasorler = [k for k in os.listdir() if os.path.isdir(k) and not k.startswith(".")]
   hedef_klasor = dosya_turu_belirle(dosya)
   if hedef_klasor is None:
      with open(dosya, "r", encoding="utf-8") as dosya1:
         satirlar = dosya1.readlines()[:7]
      hedef_klasor = tahmin_ai(dosya, satirlar, mevcut_klasorler)

   os.makedirs(hedef_klasor, exist_ok=True)
   eski_konum=os.path.join(dosya_yolu, dosya)
   yeni_konum=os.path.join(dosya_yolu, hedef_klasor, dosya)
   if os.path.exists(f"{hedef_klasor}/{dosya}"):
      continue
   shutil.move(eski_konum, yeni_konum)
   adet += 1
   time.sleep(15)

   print(f"taşındı {dosya}--> {hedef_klasor}")

print(f"işlem tamamlandı {adet} adet dosya taşındı.")