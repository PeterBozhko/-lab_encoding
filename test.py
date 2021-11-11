x = 256
y = x
count = 0
while x > 0:
    count += 1
    x //= 256
print(count)
z = y.to_bytes(count, "big")
ans = ""
for i in z:
    t = bin(i).replace("0b", "")
    t = '0' * (8 - len(t)) + t
    ans += t
print(ans)
print(int(ans, 2))
print(y == int(ans, 2))
print(bin(y))
print((len(bin(y)) - 2))
count = (len(bin(y)) - 2) // 8
if (len(bin(y)) - 2) % 8 != 0:
    count += 1
print(count)
