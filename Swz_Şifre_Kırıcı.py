import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

# AES için anahtar (key) ve IV (Initialization Vector)
key = b"Ex@mpleAESKey_32ByteLongAndStrg"  # AES için 16 byte anahtar

# Şifre çözme fonksiyonu
def decrypt_message(encrypted_message_base64, iv_base64):
    encrypted_message = base64.b64decode(encrypted_message_base64)
    iv = base64.b64decode(iv_base64)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_message), AES.block_size)  # Unpad, padding'leri kaldırır
    return decrypted_message.decode('utf-8')

# Dosya yükleme ve çözme işlemi
def load_and_decrypt_file():
    # Dosya seçme penceresi
    filepath = filedialog.askopenfilename(title="Log Dosyasını Seç", filetypes=(("JSON Files", "*.log"), ("All Files", "*.*")))
    if filepath:
        try:
            with open(filepath, 'r', encoding='utf-8') as log_file:
                decrypted_logs = []
                for line in log_file:
                    log_entry = json.loads(line)
                    encrypted_message = log_entry.get("encrypted_message")
                    iv = log_entry.get("iv")
                    
                    # Mesajı çöz
                    decrypted_message = decrypt_message(encrypted_message, iv)
                    
                    # Çözülmüş log'u listeye ekle
                    decrypted_logs.append({
                        "timestamp": log_entry["timestamp"],
                        "user": log_entry["user"],
                        "decrypted_message": decrypted_message
                    })

                # Sonuçları kaydetme
                save_decrypted_logs(decrypted_logs)
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

# Çözülmüş logları bir .txt dosyasına kaydeden fonksiyon
def save_decrypted_logs(decrypted_logs):
    # Çözülmüş mesajları bir dosyaya yazma
    output_filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")), title="Dönüştürülmüş Log Dosyasını Kaydet")
    
    if output_filepath:
        try:
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                for log in decrypted_logs:
                    output_file.write(f"Timestamp: {log['timestamp']}, User: {log['user']}, Decrypted Message: {log['decrypted_message']}\n\n")
            messagebox.showinfo("Başarılı", f"Başarıyla kaydedildi: {output_filepath}")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

# Ana pencereyi oluşturuyoruz
root = tk.Tk()
root.title("Swartz Official")  # Uygulama başlığı
root.geometry("500x400")  # Pencere boyutlarını ayarladık

# Başlık etiketi
header_label = tk.Label(root, text="Swartz Official AES Şifre Çözümleme", font=("Arial", 18, "bold"))
header_label.pack(pady=20)

# Uygulama açıklaması
description_label = tk.Label(root, text="Swartz Official Şifre Kırma Uygulamasına Hoşgeldiniz.", font=("Arial", 12))
description_label.pack(pady=10)

# Dosya seçme butonu
select_button = tk.Button(root, text="Log Dosyasını Seç ve Çöz", command=load_and_decrypt_file, font=("Arial", 14))
select_button.pack(pady=20)

# Sonuç etiketi
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Uygulama başlatma
root.mainloop()
