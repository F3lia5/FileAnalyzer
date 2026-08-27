# python-file-analyzer

Basit bir Python scripti: bulunduğu (veya çalıştırıldığı) dizindeki dosya sayısını ve dosya uzantılarını listeler.

## Özellikler

- Çalışma dizinindeki toplam dosya sayısını gösterir
- Bulunan tüm benzersiz dosya uzantılarını listeler
- Her dosyayı numaralandırarak uzantısıyla birlikte yazdırır

## Gereksinimler

- Python 3.8+
- Ekstra bir kütüphane gerekmez (sadece standart kütüphane `os` kullanılıyor)

## Kurulum

```bash
# Repoyu klonla
git clone https://github.com/kullanici-adi/python-file-analyzer.git
cd python-file-analyzer

# (Opsiyonel ama önerilir) sanal ortam oluştur
python3 -m venv env

# Sanal ortamı aktifleştir
# Linux / macOS:
source env/bin/activate
# Windows (PowerShell):
env\Scripts\Activate.ps1
# Windows (cmd):
env\Scripts\activate.bat
```

> Not: Bu proje harici bir paket kullanmadığı için `requirements.txt` gerekmiyor. Sanal ortam kurmak zorunlu değil ama iyi bir alışkanlık.

## Kullanım

```bash
python3 main.py
```

Script, çalıştırıldığı dizindeki dosyaları tarar ve şu şekilde bir çıktı üretir:

```
------------------------------------------
Current working directory: /home/kullanici/proje-klasoru
Number of files: 5

File extensions:
(.py), (.txt), (.md),

------------------------------------------
1. main.py (.py)
2. notes.txt (.txt)
3. README.md (.md)
...
------------------------------------------
```

## Bilinen Sınırlamalar

- `os.listdir()` kullanıldığı için mevcut yol altındaki **klasörler de** listeye dahil olur (sadece dosyalar değil). Klasörlerin uzantısı boş (`''`) olarak görünür.
- Script yalnızca çalıştırıldığı dizini tarar; alt dizinlere inmez.
- Uzantısız dosyalar (`Makefile`, `LICENSE` gibi) boş uzantı (`''`) olarak sayılır.

## Yapılacaklar / Geliştirme Fikirleri

- [ ] Klasörleri hariç tutan bir filtre ekle (`os.path.isfile`)
- [ ] Farklı bir dizin yolu belirtebilmek için komut satırı argümanı ekle (`argparse`)
- [ ] Alt dizinlere de inebilen (`os.walk`) bir mod ekle
- [ ] Uzantıya göre dosya sayısını gruplandırıp gösterme

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
