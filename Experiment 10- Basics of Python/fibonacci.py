def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    series = fibonacci(n - 1)
    series.append(series[-1] + series[-2])
    return series

num = int(input("Enter the number of terms: "))
print("Fibonacci Series:", fibonacci(num))