def dot_product(a, b):
    # Vektörlerin aynı boyutta olup olmadığını kontrol ediyoruz
    if len(a) != len(b):
        raise ValueError("Vektör boyutları aynı olmalı!")

    total = 0
    # Hazır kütüphane kullanmadan, matematiği kendi döngümüzle kuruyoruz
    for i in range(len(a)):
        total += a[i] * b[i]

    return total

# YKS matematiğini koda döktüğümüz test aşaması
vektor1 = [1, 2, 3]
vektor2 = [4, 5, 6]

sonuc = dot_product(vektor1, vektor2)
print("Nokta Çarpım Sonucu:", sonuc)