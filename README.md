# Swartz Official Şifre Kırıcı
Proje Hakkında
Swartz Official Şifre Kırıcı, AES-256 şifreleme ile korunan log dosyalarını çözmek için Python ve Tkinter kullanılarak geliştirilmiş masaüstü uygulamasıdır. Şifrelenmiş log dosyalarınızı seçip, güvenli şekilde çözerek içerikleri .txt formatında dışa aktarır.

Projede 32 bayt uzunluğunda AES anahtarı kullanılması hedeflenmiştir. Projenin asıl amacı, CBC modunda AES şifrelenmiş JSON formatındaki logları çözmek ve okunabilir hale getirmektir.

# Özellikler
AES CBC Mode ile şifre çözme: Base64 kodlanmış şifreli mesaj ve IV kullanılarak güvenli şifre çözümü.

Dosya bazlı işleyiş: JSON formatındaki şifreli log dosyalarını okuyup, çözülmüş içerikleri .txt olarak kaydeder.

Kullanıcı dostu GUI: Tkinter tabanlı arayüz ile kolay dosya seçimi ve kaydetme işlemleri.

Hata yönetimi: Dosya okuma, yazma ve şifre çözme sırasında oluşan hatalar kullanıcıya bilgilendirici şekilde gösterilir.

# Kurulum
1- Projeyi klonla (Git yüklü ise)

* git clone [https://github.com/Sihirbaz99/Swz_Sifre_Kirici.git](https://github.com/Sihirbaz99/AES-Password-Cracking.git)

2- Gerekli kütüphaneyi yükle

* pip install pycryptodome

3- Uygulamayı çalıştır

* python3 Swz_Şifre_Kırıcı.py

# Notlar
* Programda kullanılan AES anahtarı:
key = b"Ex@mpleAESKey_32ByteLongAndStrg"
Bu, örnek amaçlı 32 baytlık (256 bit) sabit bir anahtardır.

* Şifre çözme işlemi, yalnızca bu anahtarla uyumlu şifreli dosyalarda çalışır.

* Farklı anahtarlar veya şifreleme metotlarıyla şifrelenmiş dosyalar için anahtar değiştirilmesi gerekir.

# İletişim
Her türlü soru, öneri veya destek talebi için aşağıdaki kanallardan bana ulaşabilirsiniz:

E-posta: sihirbazswz@gmail.com

İnstagram: [https://www.instagram.com/sihirbaz.swz](https://www.instagram.com/sihirbaz.swz)

