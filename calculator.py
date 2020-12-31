#normal calculator
def normalcalci():
   print("\t\tWhat you want to do ?")
   print("\t\tEnter 'add'       : to add n elements\n\t\tEnter 'subtract'  : to implement substract")
   print("\t\tEnter 'multiply'  : to multiply n elements\n\t\tEnter 'divide'    : to implement division")
   print("\t\tEnter 'power'     : to implement division\n\t\tEnter 'sqrt'      : to square of any number")
   print("\t\tEnter 'back'      : to go one step back\n\t\tEnter 'exit'      : to exit the calci")

   user_input = input("\n\t\tEnter your choice : ")
   
   # adding n elements
   if user_input == "add":
      try:
         print("\n\t\tYou are adding n elements \n")
         add = 0;
         num = int(input("\t\tEnter the total number of elemens : "))
         print("\t\tEnter",num,"Elements")
         for i in range(num):
            ele = float(input("\t\t"))
            add = add+ele
         print("\n\t\tThe answer is ",add,"\n\n")
         normalcalci()
      except (ValueError, TypeError):
         print("Error occurred")
             
   # Subtracts two numbers
   elif user_input == 'subtract':
      try:
         print("\n\t\tyou are implementing subtraction\n")
         num1 = float(input("\t\tEnter the first number : "))
         num2 = float(input("\t\tEnter the second number : "))
         print("\n\t\tThe answer is ",num1-num2,"\n\n")
         normalcalci()
      except (ValueError, TypeError):
         print("Error occurred")
        
   # Multiplies two numbers
   elif user_input == "multiply":
      try:
         print("\n\t\tYou are multiplying n elements \n")
         mul = 1
         num = int(input("\t\tEnter the total number of elemens : "))
         print("\t\tEnter",num,"Elements")
         for i in range(num):
            ele = float(input("\t\t"))
            mul = mul*ele
         print("\n\t\tThe answer is ",mul,"\n\n")
         normalcalci()
      except (ValueError, TypeError):
         print("Error occurred")
        
   # Divides two numbers
   elif user_input == "divide":
      try:
         print("\n\t\tyou are implementing division\n")
         num1 = float(input("\t\tEnter the first number : "))
         num2 = float(input("\t\tEnter the second number : "))
         print("\n\t\tThe answer is ",num1/num2)
         print("\t\tThe quitient is ",num1//num2)
         print("\t\tThe reminder is ",num1%num2,"\n\n")
         normalcalci()
      except ZeroDivisionError:
         print("An error has occurred due to zero division")
      except (ValueError, TypeError):
         print("Error occurred")

   #power of x upto y
   elif user_input == 'power':
      try:
         print("\n\t\tYou are powering of x upto y\n")
         x = float(input("\t\tEnter the value of x : "))
         y = float(input("\t\tEnter the value of y : "))
         print("\n\t\tThe answer is",x**y,"\n\n")
         normalcalci()
      except (ValueError, TypeError):
         print("Error occured")

   #squareroot of a number
   elif user_input == 'sqrt':
      try:
         print("\n\t\tYou are impleamenting squareroot of a number\n")
         x = float(input("\t\tEnter your number : "))
         print("\t\tThe answer is",x**(1/2),"\n\n")
         normalcalci()
      except (ValueError, TypeError):
         print("Error Occured")

   elif user_input == 'back':
      main()

   elif user_input == 'exit':
      exit;


   else :
      print("\n\t\tWrong Input\nTry again (y/n)")
      c = input()
      if c == 'y' or c == 'Y':
         normalcalci()
      else:
         main()


#scientific calculator
def scientificcalci():
   print("\n\t\tWhat you want to do ?\n")
   #Listing Operations of normal calculator
   print("\t\tEnter 'logb'    : to find log of x with base b")
   print("\t\tEnter 'sin'     : to find sin of a number")
   print("\t\tEnter 'cos'     : to find cosine of a number")
   print("\t\tEnter 'tan'     : to find tangent of a number")
   print("\t\tEnter 'fact'    : to find factorial of a number")
   print("\t\tEnter 'temp'    : to temperature convertor")
   print("\t\tEnter 'back'    : to go one step back")
   print("\t\tEnter 'exit'    : to exit the calci")
   
   user_input = input("\n\t\tEnter your choice : ")

   #finding log of x with base b
   if user_input == 'logb':
      try:
         print("\n\t\tYou are impleamenting log of a number with base b\n")
         x = float(input("\t\tEnter your number : "))
         b = float(input("\t\tEnter the base value : "))
         print("\n\t\tThe answer is",math.log(x,b),"\n\n")
         scientificcalci()
      except (ValueError, TypeError):
         print("Error Occured")

   #finding sin of a number
   elif user_input == 'sin':
      try:
         print("\n\t\tYou are finding sin of a number\n")
         x = float(input("\t\tEnter your number : "))
         print("\n\t\tThe answer is",math.sin(x),"\n\n")
         scientificcalci()
      except (ValueError, TypeError):
         print("Error Occured")

   #finding cosine of a number
   elif user_input == 'cos':
      try:
         print("\n\t\tYou are finding cosine of a number\n")
         x = float(input("\t\tEnter your number : "))
         print("\n\t\tthe answer is",math.cos(x),"\n\n")
         scientificcalci()
      except (ValueError, TypeError):
         print("Error Occured")

   #finding tangent of number
   elif user_input == 'tan':
      try:
         print("\n\t\tYou are finding tangent of a number\n")
         x = float(input("\t\tEnter your number : "))
         print("\n\t\tThe answer is",math.tan(x),"\n\n")
         scientificcalci()
      except (ValueError, TypeError):
         print("Error Occured")

   #finding factorial of a number
   elif user_input == 'fact':
      try:
         print("\n\t\tYou are finding fctorial of a number\n")
         x = float(input("\t\tEnter your number : "))
         print("\n\t\tThe answer is",math.factorial(x),"\n\n")
         scientificcalci()
      except (ValueError, TypeError):
         print("Error Occured")

   #temperature convertor
   elif user_input == 'temp':
      try:
         print("\n\t\tYou are using temperature convertor\n")
         x = input("\t\tFrom which you want to convert(c/f/k) : ")
         y = input("\t\tWhich you want to convert in(c/f/k) : ")
         if x == 'c' and y == 'f':
            v = float(input("\t\tEnter temperature in celcius : "))
            temp = (v * 9/5) + 32
            print("\t\tTemperature in fehranheit is",temp,"\n\n")
         elif x == 'c' and y == 'k':
            v = float(input("\t\tEnter temperature in celcius : "))
            temp = v + 273.15
            print("\t\tTemperature in kelvin is",temp,"\n\n")

         elif x == 'f' and y == 'c':
            v = float(input("\t\tEnter temperature in fehrenheit : "))
            temp = (v - 32)* (5/9)
            print("\t\tTemperature in celcius is",temp,"\n\n")
         elif x == 'f' and y == 'k':
            v = float(input("\t\tEnter temperature in fehrenheit : "))
            temp = ((v * 9/5) + 32) + 273.5
            print("\t\tTemperature in kelvin is",temp,"\n\n")
         elif x == 'k' and y == 'c':
            v = float(input("\t\tEnter temperature in kelvin : "))
            temp = v - 273.15
            print("\t\tTemperature in celcius is",temp,"\n\n")
         elif x == 'k' and y == 'f':
            v = float(input("\t\tEnter temperature in kelvin : "))
            temp = (v - 273.15) * 9/5 + 32
            print("\t\tTemperature in fehrenheit is",temp,"\n\n")
         else:
            v = float(input("\n\t\tinvalid input"))
         scientificcalci()
      except (ValueError, TypeError):
         print("Error Occured")

   elif user_input == 'back':
      main()

   elif user_input == 'exit':
      exit;

   else :
      print("\n\n\t\tWrong Input\nTry again (y/n)")
      c = input()
      if c == 'y' or c == 'Y':
         scientificcalci()
      else:
         main()


#main function
def main():
   print("\n\n\t\t.......Welcome to A2Z Calculator........\n\n")
   print("\t\t1. Normal Calculator\n\t\t2. Scintific Calculator\n\t\t3. Exit") 
   choice = int(input("\n\t\tEnter your choice : "))
   if choice == 1:
      print("\n\n\t\t......Welcome to Normal Calculator......\n\n")
      print("\t\tHope you are enjoying a2z calculator\n")
      normalcalci()
   elif choice == 2:
      print("\n\n\t\t......Welcome to Scientific Calculator........\n\n")
      print("\t\tHope you are enjoying a2z calculator\n") 
      scientificcalci()
   elif choice == 3:
      exit;
   else:
      print("\n\t\tInvalid Input ! Try again (y/n)")
      x = input()
      if x == 'y' or x == 'Y':
         main()
      elif x == 'n' or x == 'N':
         exit;

import math
main()
