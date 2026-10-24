print("----- Yaş Kayıt Sistemi -----")

kullanici_adi = input("Lütfen adınızı giriniz: ")

while True:
    try:
        yas = int(input("Lütfen yaşınızı giriniz: "))
        if yas < 18:
            print("Üzgünüz, yaşınız 18'den küçük olduğu için sisteme kayıt olamazsınız.")
            break 
        else:
            kullanici = {"ad": kullanici_adi, "yas": yas}
            print(f"Hoş geldiniz {kullanici['ad']}, yaşınız {kullanici['yas']}. Sisteme başarıyla kayıt oldunuz.")
            break 
    except ValueError:
        print("Hatalı giriş! Lütfen yaşınızı bir sayı olarak giriniz.")