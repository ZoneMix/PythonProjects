def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

gen = count_up_to(5)

for num in gen:
    print(num)
