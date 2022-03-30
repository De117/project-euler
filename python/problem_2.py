def fibo_generator(N):
    first, second = 1, 1
    while second < N:
        yield second
        first, second = second, (first + second)

print(sum( f for f in fibo_generator(4000000) if f%2==0 ))
