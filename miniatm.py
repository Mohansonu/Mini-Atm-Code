account={
    "name":"Mohan Banoth",
    "balance":5000,
    "pin":"1234",
    "type":"savings account"
}
print("===MINI ATM===")
pin=input("Enter your pin: ")
if pin==account["pin"]:
        while True:
            print("1.Check balance: ")
            print("2.Deposit Balance: ")
            print("3.Withdraw balance: ")
            print("4.Balance Details: ")
            print("EXIT")
            choice=input("Enter your choice: ")
            if choice=="1":
                print("Your Balance is: ",account["balance"])
            elif choice=="2":
                amount=int(input("Enter your amount to depost: "))
                if amount>0:
                    account["balance"]=account["balance"]+amount
                    print("Money Succesfully Deposited")
                    print("New Balance", account["balance"])
                else:
                    print("INVALID AMOUNT")
            elif choice=="3":
                amount=int(input("Enter your amount: "))
                if amount<=0:
                    print("Ivalid amount")
                elif amount>account["balance"]:
                    print("Insufficient balance")
                else:
                    account["balance"]=account["balance"]-amount
                    print("Collect your cash")
                    print("New balance: ", account["balance"])
            elif choice=="4":
                 print("\nAccount Holder name: ",account["name"])
                 print("\nAccount Balance: ",account["balance"])
                 print("\nAccount Type: ",account["type"])
            elif choice=="5":
                 print("Thank you")
                 break
            else:
                 print("Invalid choice")
else:
     print("Invalid pin")
     print("Acess Denied, Enter correct pin")
