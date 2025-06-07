# Swartz Official Şifre Kırıcı
Proje Hakkında
Swartz Official Şifre Kırıcı, AES-256 şifreleme ile korunan log dosyalarını çözmek için Python ve Tkinter kullanılarak geliştirilmiş masaüstü uygulamasıdır. Şifrelenmiş log dosyalarınızı seçip, güvenli şekilde çözerek içerikleri .txt formatında dışa aktarır.

Projede 32 bayt uzunluğunda AES anahtarı kullanılması hedeflenmiştir ancak örnek kodda anahtar 16 bayt olarak verilmiştir. Projenin asıl amacı, CBC modunda AES şifrelenmiş JSON formatındaki logları çözmek ve okunabilir hale getirmektir.

# Özellikler
AES CBC Mode ile şifre çözme: Base64 kodlanmış şifreli mesaj ve IV kullanılarak güvenli şifre çözümü.

Dosya bazlı işleyiş: JSON formatındaki şifreli log dosyalarını okuyup, çözülmüş içerikleri .txt olarak kaydeder.

Kullanıcı dostu GUI: Tkinter tabanlı arayüz ile kolay dosya seçimi ve kaydetme işlemleri.

Hata yönetimi: Dosya okuma, yazma ve şifre çözme sırasında oluşan hatalar kullanıcıya bilgilendirici şekilde gösterilir.



# Kurulum 

1. Projeyi klonla (Git yüklü ise)
  * git clone https://github.com/kullaniciadi/Swz_Sifre_Kirici.git

2. Proje klasörüne gir
  * cd Swz_Sifre_Kirici

3. Gerekli kütüphaneyi yükle
 *  pip install pycryptodome

4. Uygulamayı çalıştır
 *  python3 Swz_Şifre_Kırıcı.py


# İletişim
Her türlü soru, öneri veya destek talebi için aşağıdaki kanallardan bana ulaşabilirsiniz:

* E-posta: sihirbazswz@gmail.com

* İnstagram : [https://www.instagram.com/sihirbaz.swz](https://www.instagram.com/sihirbaz.swz)
