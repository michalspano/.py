print("Test 4")
n = ["a" if i % 2 == 0 else "b" for i in range(5)]
n.sort(reverse=True)
print(n)
