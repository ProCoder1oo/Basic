#//-- This script is made by Yusuf Qureshi.
#//-- If you want to get help from it, dm me in discord username: wolverine1oo#8628


def comparison():

    
    name = input("Hello there, enter your name:")
    
    Is_Pro = input("Are you a pro?")
    
    Is_Tall = input("Are you tall?")
    
    if Is_Pro == "Yes" and Is_Tall == "Yes":
       print("Hello,")
       print(name)
       print("You are pro and tall.")

    if Is_Pro == "Yes" and Is_Tall == "No":
        print("Hello,")
        print(name)
        print("you are a pro but not tall.")
    
    if Is_Pro == "No" and Is_Tall == "Yes":
        print("Hello,")
        print(name)
        print("you are not a pro but tall.")
    
    if Is_Pro == "No" and Is_Tall == "No":
        print("Hello,")
        print(name)
        print("You are neither tall nor pro.")
    


def Num_ply():
   name = input("Hello there, please enter your name.")
   num_1 = input("Hello, " + name + " please enter a number.")
   num_2 = input("Hello, " + name + " please enter another number.")
   operator = input("Hello, " + name + " please enter an operator.")
   num_1 = float(num_1)
   num_2 = float(num_2)

   if operator == "+":
       Result_sum = (num_1) + (num_2)
       print(name + ", the sum is:")
       print(Result_sum)

   if operator == "-":
       Result_Diff = (num_1) - (num_2)
       print(name + ", the difference is:")
       print(Result_Diff) 

   if operator == "*":
       Result_prod = (num_1) * (num_2)
       print(name + ", the product is:")
       print(Result_prod)

   if operator == "/":
       Result_Divide = (num_1) / (num_2)
       print(name + ", the quotient is:")
       print(Result_Divide)

      




comparison()
Num_ply()   