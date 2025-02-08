def test():
    for i in range(1, 11):
        return f"{i}"

def test2():
    for i in range(1, 11):
        yield f"{i}"


for i in test():
    print(i)

print("--------------------------")

for i in test2():
    print(i)