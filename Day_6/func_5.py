def f(arg):
    data = [1, 1]
    for i in range(arg-2):
        data.append(data[-1]+data[-2])
    return data
print(f(6))