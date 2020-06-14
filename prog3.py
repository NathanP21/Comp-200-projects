loop = 1
while loop ==1:

    print (" Nathan Prasad")
    print (" ID# 3458124 ")
    print (" Program 3 Loops and If Conditions")

    password = "hello"

    for x in range ( 9999999, 0 , -1):
        attempt = input("Password?:")
        if attempt == password:
            break
        else:
            print("Incorrect.")


    name = input("What is your Name?")

    if name == 'Madonna' or name == 'Cher':
        print("May I have your autograph, please? ") 
    else:
        print(" Thats a nice name " + name) 


