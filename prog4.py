loop = 1
while loop ==1:
      
   print(" Nathan Prasad")
   print(" ID# 3458124")
   print("Program 4  Functions")

   print("Please select a number: 1,2,3,4,5,6 and 7");
   print("1. AREA (SQUARE)");
   print("2. AREA (RECTANGLE)"); 
   print("3. AREA (CIRCLE)");
   print("4. PERMIMETER (SQUARE)");
   print("5. PERMIMETER (RECTANGLE)");
   print("6. PERMIMETER(CIRCLE)");
   print("7.EXIT"); 

   choice = input("Enter choice: ");
   

   if choice == '1':
       print(" You have selected AREA OF A SQUARE") 
       side=int(input("Size of the square side?"))
       area=side*side
       print("area is: {}".format(area))
      

   elif choice == '2':
       print(" You have selected AREA OF A RECTANGLE") 
       length=int(input("Size of the length side?"))
       width=int(input("Size of the width side?"))
       area=length*width
       print("area is: {}".format(area))

   elif choice == '3':
       print(" You have selected AREA OF A CIRCLE") 
       pie=3.14
       radius=int(input("Size of the radius?"))
       area=pie*(radius**2)
       print("area is: {}".format(area))

   elif choice == '4':
      print(" You have selected PERMIMETER OF A SQAURE") 
      side=int(input("Size of a side?"))
      perm=side*4 
      print("permimeter is: {}".format(perm))

   elif choice == '5':
      print(" You have selected PERMIMETER OF A RECTANGLE") 
      length=int(input("Size of the length side?"))
      width=int(input("Size of the width side?"))
      perm= 2*(length + width) 
      print("permimeter is: {}".format(perm))

   elif choice == '6':
      print(" You have selected PERMIMETER OF A CIRCLE") 
      pie=3.14
      radius=int(input("Size of the radius?"))
      perm=2*(pie*radius)
      print("permimeter is: {}".format(perm))

   elif choice == '7':
       exit() 

