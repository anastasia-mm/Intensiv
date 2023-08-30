def f(data, step):
    return data[-(step % len(data)):] + data[:-(step % len(data))]
print(f([1,2,3,4,5], 6))