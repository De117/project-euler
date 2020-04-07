square = lambda x: x**2

def sum_of_squares(N):
    return sum(map(square, range(1, N+1)))

def square_of_sum(N):
    return square(sum(range(1, N+1)))

assert square_of_sum(10) - sum_of_squares(10) == 2640
print(square_of_sum(100) - sum_of_squares(100))
