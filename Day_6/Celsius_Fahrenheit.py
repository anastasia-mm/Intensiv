a = input("f - fahr, c - cels ")
if "f" in str(a):
    f = int(input())
    c = (f - 32) * (5/9)
    print(c)
elif "c" in str(a):
    c = int(input())
    f = c * (9/5) + 32
    print(f)

