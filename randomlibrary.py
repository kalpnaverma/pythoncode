# import random
# my_dice=["one","two","three","four","five","six"]
# print_dice=random.randint(0,5)
# print(my_dice[print_dice])


# import random 
# my_numb=[1,2,3,4,5,9,0,5,]
# print_numb=random.randint(0,7)
# print(my_numb[print_numb])

def pyramid(n):
    for i in range(1, n + 1):

      for j in range(n - i):  
             print(" ", end="") 
      for k in range(1, 2*i):  
             print("*", end="")  
      print()
pyramid(5)  

# Function to print full pyramid pattern
def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()
   
# full_pyramid(5)

            