def is_pythagorean_triplet(a, b, c):
    x, y, z = sorted([a, b, c])  
    return x**2 + y**2 == z**2
print(is_pythagorean_triplet(3, 4, 5)) 
print(is_pythagorean_triplet(5, 12, 13))  
print(is_pythagorean_triplet(6, 8, 10))  
print(is_pythagorean_triplet(1, 2, 3))  
