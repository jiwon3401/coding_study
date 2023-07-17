
numbers=set(range(1,10001))
generator = set()
for num in numbers:
    for i in str(num):
        num += int(i)
    generator.add(num)
self_num = numbers - generator
for i in sorted(self_num):
    print(i)