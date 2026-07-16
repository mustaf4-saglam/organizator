# 🤖 AI Destekli Akıllı Dosya Düzenleyici (Smart File Organizer)

Bu proje, karmaşık ve dağınık klasörleri **Google Gemini AI** gücünü kullanarak akıllıca analiz eden ve dosyaları bağlamlarına uygun klasörlere otomatik olarak taşıyan bir otomasyon aracıdır. 

Klasik dosya düzenleyiciler dosyaları sadece uzantılarına (örn: `.pdf`, `.txt`) göre ayırırken; bu araç dosyanın ismini ve ne işe yaradığını yapay zeka ile yorumlayarak anlamsal bir sınıflandırma yapar (Örn: `nmap_tarama_sonuclari.txt` dosyasını "Text Dosyaları" yerine **Siber Güvenlik** klasörüne taşır).

## ✨ Özellikler

- **🧠 Akıllı Kategorizasyon:** Dosyaları bağlamına göre (Finans, Kod Projesi, Siber Güvenlik vb.) sınıflandırır.
- - **⏱️ API Kota Dostu:** Ücretsiz API sınırlarını (Rate Limit) aşmamak için dosya taşıma işlemleri arasına bekleme süresi koyarak kararlı çalışır.
  - 
## 🛠️ Kullanılan Teknolojiler
- **Dil:** Python 3
- **Yapay Zeka:** Google GenAI SDK (`gemini-3.1-flash-lite` modeli)
- **Kütüphaneler:** `os`, `shutil`, `time`, `python-dotenv`

---

## 🚀 Kurulum Adımları

Projeyi kendi yerel ortamınızda çalıştırmak için aşağıdaki adımları sırasıyla uygulayın.

### 1. Projeyi Klonlayın
```bash
git clone https://github.com/mustaf4-saglam/organizator.git
```
``` bash
cd organizator
```
## 2. Sanal Ortam (Virtual Environment) Oluşturun
Proje bağımlılıklarının sisteminizle çakışmaması için bir sanal ortam oluşturun ve aktifleştirin:


## Sanal ortam oluşturma
``` bash
python3 -m venv venv
```
## Linux / MacOS için aktifleştirme:
``` bash
source venv/bin/activate
```
## Windows için aktifleştirme:
``` bash
venv\Scripts\activate
```
3. Gerekli Kütüphaneleri Yükleyin
``` Bash
pip install -r requirements.txt
```
4. API Anahtarınızı Tanımlayın

API_KEY=sizin_google_api_anahtariniz_buraya_gelecek
## 💻 Kullanım
# Tüm kurulumları tamamladıktan sonra, düzenlemek istediğiniz dosyaların bulunduğu dizinde betiği çalıştırmanız yeterlidir:

``` Bash
python3 organizator.py
```
Çıktı Örneği:

Plaintext
Düzenleme işlemi başlıyor...
------------------------------
taşındı elektrik_faturasi.pdf --> Finans
taşındı main.c --> Kod_Projesi
taşındı port_scanner.py --> Siber_Guvenlik
Atlandı: 'readme.md' zaten Proje_Dokumanlari içinde mevcut.
işlem tamamlandı 3 adet dosya taşındı.
⚠️ Önemli Notlar
Çok fazla dosya içeren klasörlerde, Google API'nin ücretsiz limitlerine takılmamak için taşıma işlemi arasına time.sleep(15) eklenmiştir.
İşlem biraz sürebilir, terminali kapatmayın.
