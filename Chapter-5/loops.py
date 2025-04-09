# table = int(input("Enter the Number"))

# i =1
# while(i< 11):
#     print (f" {table} x {i} = {table* i}")
#     i = i + 1

# for i in range (1, 4):
#     for j in range(1,4):
#        print("*")
#     print("\n")

# factorial 

# number = int(input("Enter the number: "))

# product = 1

# for i in range ( 1,  number + 1):
#     product = product * i
# print(product)

# n = int(input("Enter the number : "))
# for i in range (1, n+1):
    
#     print(" " * (n-i), end = "")
#     print("*" * (2*i - 1), end = "")  
#     print("")

# for i in range (1 , n+1):
#     print("*"* (i), end="")
#     print(" "* (n-i), end="")
#     print("")
    

n = int(input("Enter the number : "))

i = 10
for i in range(10, 0):
    product = i * n
    print(f"{n * i} = {product}")