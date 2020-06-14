def addition(x, y):
   return x + y;

def subtraction(x, y):
   return x - y;

def multiplication(x, y):
   return x * y;

def division(x, y):
   return x / y;

def exponent(x, y):
   return x ** y;

def remainder(x, y):
    return x % y ;


loop = 1
while loop ==1:
      
   print(" Nathan Prasad")
   print(" ID# 3458124")
   print("Program 1 Math Functions") 
   print("Please select a function via a number 1,2,3,4,5 and 6.:");
   print("1. Addition");
   print("2. Subtraction");
   print("3. Multiplication");
   print("4. Division");
   print("5. Exponent");
   print("6. Remainder");

   choice = input("Enter choice: ");

   num1 = int(input("Enter first number: "));
   num2 = int(input("Enter second number: "));

   if choice == '1':
      print(num1, "+" ,num2, "=", addition(num1, num2));

   elif choice == '2':
      print(num1, "-", num2, "=", subtraction(num1, num2));

   elif choice == '3':
      print(num1, "*", num2, "=", multiplication(num1, num2));

   elif choice == '4':
      print(num1, "/", num2, "=", division(num1, num2));

   elif choice == '5':
      print(num1, "**", num2, "=", exponent(num1, num2));

   elif choice == '6':
      print(num1, "%", num2, "=", remainder(num1, num2));

   else:
      print("Please select a valid input.");

  
