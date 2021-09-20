print("*********Namaste!*********")
print("***COVID RELIEF FUND***")
print("In these challenging times, when everybody is struggling to maintain their work-life",
      "balance, many citizens of our nation are deprived of basic necessities of life.",
      "\nWe have taken upon the responsibilty to aid those in need, and we need your help.",
      "\n---------------------------------------------------------------------------------")
loginid = 'admin'
passwrd = 'admin123'
print("Login: ")
username = input("Enter Username: ")
passwrd1 = input("Enter password: ")
d1={}
d = {}

while True:
    #for admin
    if (username == loginid) and (passwrd1 == passwrd):
        print("Welcome Admin!")
        print("Menu: \n1.View total charity items \n2.View total amount collected \n3.Exit")
        adminchoice = int(input("Select an option to go further: "))

        if adminchoice == 1:
            print(d1)
            f = open("covid.txt","r")
            a = f.read()
            print(a)
            f.close()

        elif adminchoice == 2:
            
            print("Total amount collected: ")
            print(d)
            f = open("covid.txt","r")
            a = f.read()
            print(a)
            

        elif adminchoice == 3:
            break
            
    #non-admin user
    elif (username != loginid) and (passwrd1 !=passwrd):
        print("Welcome User",username,"!")
        print("Here's what you can do to help and support us!")
        print("Menu: \n1.Provide financial support \n2.Donate necessities \n3.Exit")
        userchoice = int(input("Select an option to go further: "))
        
            
        #financial support
        if userchoice == 1:
            
            print("**********Financial Support********")
            amt = int(input("Enter the amount: "))
            print("Mode of payment: \n1.Online \t2.Cash")
            paymode = int(input("Enter your choice of payment mode: "))
            
            #online payment
            if paymode == 1:
                 import random
                 f = open("covid.txt","a+")
                 f.write("Mode of payment: Online")             
                 s = "1234567890"
                 otp = "".join(random.sample(s,6))
                 print("OTP: ",otp)
                 otp1 = input("Confirm your OTP: ")
                 if otp==otp:
                     print("...Processing")
                     print("...Success!")
                     print("Donation Made! Thank you!")
                     print("Your donation will surely help in making the circumstances better!")
                     f.write("Payment has been successfully made.")
                 else:
                     print("Invalid OTP /nSorry your payment could not be processed.")
                     f.write("Payment failed.")
                     f.close()

            #cash payment
            elif paymode == 2:
                f = open("covid.txt","a+")
                f.write("Mode of payment: Cash")
                f.write("Payment has been successfully made.")
                l1 = [2000,500,200,100,50,10]
                l2 = []
                for i in range(1,7):
                    val = int(input("Enter notes of denominations: "))
                    l2 = l2.append(val)
                d[l1] = l2
                print(d)
                f.write(str(d))
                f.close()
                print("...Processing")
                print("...Success!")
                print("Donation Made! Thank you!")
                print("Your donation will surely help in making the circumstances better!")

        #necessities donation
        elif userchoice == 2:
            print("**********Donate Necessities********")           
            print("Item donations can be of type: clothes/food/footwear/books/misc")
            itemname = input("Enter item name: ")
            f = open("covid.txt","w")
            qty = int(input("Enter quantity: "))
            d1[itemname] = qty
            f.write(str(d1))
            f.close()
            print("...Success!")
            print("Please send the donations at our nearest facility")
            print("Thankyou for your support")
            print("Your donation will surely help in making the circumstances better!")
            
                
        elif userchoice == 3:
            break


       
        
