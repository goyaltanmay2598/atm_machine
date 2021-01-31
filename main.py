import getpass
import pyttsx3
speaker = pyttsx3.init()
data = [[1001,"tanmay","redhat",1234,60000],[1002,"abc","abc",2345,12000],[1003,"xyz","xyz",3456,30000]]


def login(acc_no, passwd,atm_pin):
    is_login = False
    for acc, name, ps, pin,balance in data:
        if acc == acc_no:
            if ps == passwd:
                if atm_pin == pin:
                    print(f"Welcome back user {name}")
                    is_login = True
                    menu = """ choose any of the :
                    			1 == balance
                    			2 == withdraw balance
                    			3 == deposit balance
                    			4 == exit
                    			"""
                    print(menu)

                    voices = speaker.getProperty('voices')
                    speaker.setProperty('voice', voices[1].id)
                    speaker.say(menu)
                    speaker.runAndWait()



                    try:
                        # taking an option from user
                        option = int(input("Please enter your choose "))
                    except:
                        print("Please enter valid option")

                    # for option 1
                    if option == 1:
                        print(f"Your current balance is {balance}")

                    if option == 2:
                        withdraw_amount = int(input("please enter withdraw_amount "))

                        balance = balance - withdraw_amount

                        print(f"{withdraw_amount} is debited from your account")

                        print(f"your updated balance is {balance}")

                    if option == 3:
                        deposit_amount = int(input("please enter deposit_amount"))

                        balance = balance + deposit_amount

                        print(f"{deposit_amount} is credited to your account")

                        print(f"your updated balance is {balance}")

                    if option == 4:
                        break


                elif atm_pin != pin:
                    print("pin is wrong,try again ")

            elif ps!= passwd:
                    print("Invalid Password Try Again")


            break
    else:
     print("Account Does not Exists")
    return is_login

login((int(input("Acc no: "))) , input("Password: "),int(input("my atm_pin is : ")))



