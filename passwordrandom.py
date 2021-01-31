import random
s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2 = "0123456789"
s3 = "~!@#$%^&*()_+{}[\]:/"
s = s1.upper() + s1. lower() + s2 +s3
password = ""
for i in range (15):
    p = random.choice(s)
    password = password + p
print(f"New password [{i}]: {password}")
