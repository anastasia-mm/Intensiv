M, N = map(int, input("put two numbers ").split())
for number in range(M, N+1):
    if number % 3 == 0:
        print(number)
