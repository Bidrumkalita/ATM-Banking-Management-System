# atm machine management 

pin = "9395"
balance = 100000

transaction = []

attempts = 3
while attempts > 0:
    entered_pin = input("ENTER YOUR PIN:")

    if entered_pin == pin :
        print("\nLOGIN SUCCESSFUL")
        break

    else: 
        attempts -= 1
        print ("WRONG PIN ")
        print("attempts left :", attempts)


if attempts == 0 :
    print("account locked")
    print("try after 24 hours ")
    exit()

while True :

    print("\n ====== ATM MENU ======")
    print(" 1. check balance")
    print(" 2. deposit money")
    print(" 3. withdraw money")
    print(" 4. transaction history")
    print(" 5 . change pin")
    print(" 6. exit")

    choice = input("select your option: ")

    if  choice == "1" :
        print("balance :", balance )

    elif choice == "2" :
        amount = float(input ( "enter you amount:"))
        if amount > 0:
          balance += amount 
          transaction.append(f"deposited {amount}")
          print("deposit.succesful")
        elif amount < 0:
            print("invalid  request")

    elif choice == "3":
         amount = float(input("enter your amount: "))

         if amount > 0 and amount <= balance: 
             balance -= amount
             transaction.append(f"withdrawl {amount}")
             print("collect cash")
             print("remaining balance = ", balance)

         else:
             print("insufficient balance")

    elif choice == "4":

       if len(transaction) == 0:
           print("no transation found")

       else :
           print("\ntransaction history")
           for i in transaction:
               print(i)

    elif choice == "5" :
        old_pin = input("enter your old pin:")

        if old_pin == pin :
            new_pin = input("enter your new pin :")
            pin = new_pin
            print("pin change succesfully ")
        else :
            print("incorrect pin")

    elif choice == "6":
        print("thank you for using atm ")
        break

    else:
        print("invalid choice")
        print("please try again ")