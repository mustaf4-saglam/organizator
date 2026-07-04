import os
import shutil
import time
os.environ["GRPC_DNS_RESOLVER"] = "native"
from google import genai
client=genai.Client(api_key="GOOGLE_API_KEY")
def tahmin_ai(dosya_adi):
 prompt = f"""
Sen akıllı bir dosya düzenleyicisin. 
    Şu dosya adını analiz et: '{dosya_adi}'
    Bu dosya hangi klasöre gitmeli? 
    eğer bir kod projesi ise aynı klasöre koymayı unutma.
    Lütfen sadece klasör adını tek veya iki kelime olarak yaz. (Örn: Ders_Notları, Finans, Siber_Güvenlik, Kod_Projesi)
"""
 response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
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
   hedef_klasor = tahmin_ai(dosya)

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