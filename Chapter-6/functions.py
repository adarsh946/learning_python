

# def greet(name, endin):
    
#     print(f"Good Morning, " + name)
#     print(endin)

# greet("adarsh", "thanks")

# def factorial(n):
#     if(n == 0 or n == 1) :
#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter the number: "))
# print(f"the factorial of {n} is {factorial(n)}")

# def greatest(a, b, c):
    

#     if(a> b and a> c):
#         print(f"{a} is the greatest no.")
#     elif(b> a and b> c):
#         print(f"{b} is the greatest no.")
#     else: 
#         print(f"{c} is the greatest no.")
        

# greatest(10, 12, 8)

# def Farenheit(celcius):
#     far = (celcius *(9/5) + 32)
#     print(f"the conversion of {celcius}C in farenheit is {far}F")

# Farenheit(50)

# print("addy")
# print("maddy")
# print("shaddy ", end = "")
# print("lady", end="")


# def sum_of_n(n):
#     if(n == 1 ):
#         return 1
#     return n + sum_of_n(n -1)

# print(f"the sum of n natural no. is : {sum_of_n(10)}")

def pattern(n) :
    if (n == 0):
        return
    print( "*" * n)
    pattern(n-1)

pattern(9)