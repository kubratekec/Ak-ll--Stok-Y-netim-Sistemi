# 1. VERİ YAPISINI TANIMLAYALIM
stoklar = {
    "laptop": [15, 25000],
    "mouse": [50, 500],
    "klavye": [8, 1200],
    "monitor": [12, 5000]
}

print("--- AKILLI STOK YÖNETİM SİSTEMİ ---")

# 2. KULLANICIDAN VERİ ALALIM
urun = input("İşlem yapılacak ürün adını giriniz: ").lower() # Küçük harfe çevirir

# 3. KONTROL VE HESAPLAMA MANTIĞI
if urun in stoklar:
    # Ürün varsa buraya girer (4 boşluk içerde)
    mevcut_stok = stoklar[urun][0]
    fiyat = stoklar[urun][1]
    
    print(f"{urun} ürününden stokta {mevcut_stok} adet var. Birim fiyat: {fiyat} TL")
    adet_input = input("Kaç adet satıldı/çıkış yapıldı?: ")
    
    if adet_input.isdigit(): # Sayı olup olmadığını kontrol eder
        adet = int(adet_input)
        
        if adet <= mevcut_stok:
            # Satış işlemleri (8 boşluk içerde)
            stoklar[urun][0] -= adet
            kalan_stok = stoklar[urun][0]
            toplam_tutar = adet * fiyat
            
            print(f"\n✅ Satış Başarılı! Toplam Tahsilat: {toplam_tutar} TL")
            print(f"Kalan {urun} stoku: {kalan_stok}")
            
            # Kritik Stok Kontrolü (8 boşluk içerde)
            if kalan_stok < 10:
                print(f"⚠️ DİKKAT: {urun} stoku kritik seviyenin altına düştü!")
        else:
            print("❌ Hata: Yetersiz stok!")
    else:
        print("❌ Hata: Lütfen geçerli bir sayı giriniz!")
else:
    print("❌ Hata: Ürün depoda bulunamadı.")
