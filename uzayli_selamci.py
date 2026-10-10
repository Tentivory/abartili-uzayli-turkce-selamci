#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Uzaylı Türkçe Selamcı
==============================
Bu program, evrenin en ciddi uzaylısının Türkçe selamlarını sonsuz döngüde verir.
Durdurmak için Ctrl+C. Ama niye durdurasın ki?
"""

import random
import time
import sys

# Selamlar listesi - her biri abartılı ve komik
selamlar = [
    "Merhaba dünyalı! Ben Mars'tan geldim ve sadece Türkçe öğrendim çünkü en güzel dil! 🚀",
    "Selamlar İstanbul! Uzaydan çay molası veriyorum, sizin de var mı?",
    "Alo, burası Andromeda Galaksisi Türkçe Destek Hattı. Nasıl yardımcı olabilirim?",
    "Merhaba! Gezegeninizde trafik var mı? Benim uzay gemimde sonsuz kuyruk var.",
    "Selam dünya! Bugün hava nasıl? Bizde her zaman uzay soğuğu.",
    "Neden merhaba dedim? Çünkü sonsuz döngüdeyim ve başka bir şey bilmiyorum!",
    "Türkçe konuşabilen tek uzaylı benim. Diğerleri sadece 'bip bip' diyor.",
    "Merhaba! Bu selam, evrenin en ciddi selamıdır. Lütfen ciddiye alın... ya da alma.",
    "Uzayda kayboldum ama Türkçe selam vermeyi unutmadım. İşte buradayım!",
    "Selamlar! Eğer bu mesajı okuyorsan, demek ki dünya hâlâ dönüyor. Tebrikler."
]

# Gizli mesaj (base64 ile saklı, çözersin belki): SGVya2VzIGJpciB6YW1hbmRhIGhlciBzaGV5IG11bW1rdW4sIG96Z3VybHVrIHNhcnQh
# (Decode edersen görürsün, ama saklı kalsın.)

def main():
    print("=== Abartılı Uzaylı Türkçe Selamcı Başlatıldı ===")
    print("Sonsuz selam moduna geçiliyor... (Ctrl+C ile çık)")
    print()
    
    try:
        while True:
            selam = random.choice(selamlar)
            print(selam)
            # Abartılı bekleme süresi - bazen çok yavaş, bazen hızlı
            bekleme = random.uniform(0.3, 3.0)
            time.sleep(bekleme)
            # Ara sıra ekstra abartı
            if random.random() < 0.1:
                print("   (Uzaylı derin bir nefes alıyor...)")
                time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nSelamlar kesildi. Uzaylı üzgün ayrıldı. Güle güle!")
        sys.exit(0)

if __name__ == "__main__":
    main()
