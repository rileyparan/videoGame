# write a recursive function that doesn't create a stack overflow 

# def recursiveSheep(x): 
#     if len(x) > 25: 
#         return x 
#     else: 
#         return recursiveSheep(x+"a")

# print(recursiveSheep("b"))

def hello(x):
    if x>0: 
        return (x+1)
    else: 
        return (x)
print(hello(254)) 
# stopped it from melting our computer 