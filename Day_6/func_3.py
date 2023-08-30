from random import randint
def gen_random_list(data, n, MIN, MAX):
    for _ in range(n):
        data.append(randint(MIN, MAX))
    return data
print(gen_random_list([83834, 933, 949, -38954], 5, -100, 200))