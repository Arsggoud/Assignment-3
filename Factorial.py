b = int(input("Enter the number --> "))

def factorial(a):
    if a < 2:
        return 1
    else:
        return a * (factorial(a-1))

answer = factorial(b)
print(answer)