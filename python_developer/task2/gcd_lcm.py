import math

def gcd_lcm(a, b):
    gcd = math.gcd(a, b)  
    lcm = abs(a * b) // gcd  
    return gcd, lcm

a = int(input("Enter first no: "))
b = int(input("Enter second no: "))

gcd, lcm = gcd_lcm(a, b)
print("GCD:", gcd)
print("LCM:", lcm)
