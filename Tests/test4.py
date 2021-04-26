print("Test 4")
n = ["a" if i % 2 == 0 else "b" for i in range(5)]
n.sort(reverse=True)

i = 0
while i < len(n):
    print(n[i])
    i += 1
