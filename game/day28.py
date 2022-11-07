# iterative 
# for i in range(3):
#     x = i
#     print(x+x*i)

# def recurse(x):
#     if x > 100:
#         return x
#     else:
#         print(x)
#         return recurse(x+1)

# recurse(1)


# recursion
def factorial(x):
    if x == 1:
        return x
    else:
        return (x * factorial(x-1))
        
num = 3

print("the factorial of ", num, "is", factorial(num))