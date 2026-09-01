def dot_product(a, b):
    
    if len(a) != len(b):
        raise ValueError("Vector sizes must be same!")

    total = 0
    
    for i in range(len(a)):
        total += a[i] * b[i]

    return total


vektor1 = [1, 2, 3]
vektor2 = [4, 5, 6]

result = dot_product(vektor1, vektor2)
print("Nokta Çarpım Sonucu:", result)