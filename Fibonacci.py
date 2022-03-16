# Function for nth Fibonacci number
def Fibonacci(n):

    # Check if input is 0 then it will

    if n < 0 or n == 0:
        print("Incorrect input")

    # Check if n is 1
    # it will return 0
    elif n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci(9))


def fibonacci_series(n):
    series = []
    for i in range(1, n+1):
        series.append(Fibonacci(i))

    return series


print(fibonacci_series(10))
