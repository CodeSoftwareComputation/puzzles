def calc(a, b):
    if b > 10000:
        return
    print a + b
    calc(b, a+b)

if __name__ == "__main__":
    calc(0, 1)
