import sounddevice as sd
from scipy.io.wavfile import write

# Kullanıcıdan kayıt süresini al
sure = int(input("Kaç saniye ses kaydetmek istiyorsun? "))

# Ses kayıt ayarları
fs = 44100  # Örnekleme frekansı (Hz)
print("Ses kaydediliyor...")

# Ses kaydet
ses = sd.rec(int(sure * fs), samplerate=fs, channels=2, dtype='int16')
sd.wait()  # Kayıt tamamlanana kadar bekle

# Dosyayı kaydet
write("kayit.wav", fs, ses)
print("Ses kaydedildi: kayit.wav")
