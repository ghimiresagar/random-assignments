def calculateInterest(amountBorrowed, annualInterest):
    """
        Calculate the interest amount per month
    :param amountBorrowed: total amount borrowed
    :param annualInterest: annual interest
    :return:
    """
    return (amountBorrowed * (annualInterest/12))/100

def takeValues(str, type=""):
    """
        Error handling for individual values
        Checks if values are greater than 0
        Also checks if rate is below 30
    :param str: Prompt for user
    :param type: "rate" for question type of rate
    :return float: correct value
    """
    while True:                         # run until we return a value
        try:
            value = float(input(str))
            if value >= 0:              # check if value is not negative
                if type == "rate":      # if rate check if rate is less than 30
                    if value <= 30:
                        return value
                    else:
                        print("[Error] Annual rate is too large, should be between 0% - 30%")
                else:
                    return value
            else:
                print("[Error] Value can't be negative")
        except ValueError:
            print("[Error] Value error, not a number")

def inputValue():
    """
        takes input
        checks for interest amount less than monthly payment amount
    :return amountBorrowed: float
    :return annualInterest: float
    :return monthlyRepayment: float
    """
    while True:     # run again if fails
        # take values
        amountBorrowed = takeValues("Enter the amount borrowed: ")
        annualInterest = takeValues("Enter annual interest (0% - 30%): ", "rate")
        monthlyRepayment = takeValues("Enter monthly repayment amount: ")

        # calculate interest
        interestAmount = calculateInterest(amountBorrowed, annualInterest)
        if interestAmount <= monthlyRepayment:          # check if interest is less than monthly payment
            return amountBorrowed, annualInterest, monthlyRepayment
        else:
            print("[Error] Monthly Repayment ${} too low for Interest Amount of ${} with Annual Rate of {}%".format(monthlyRepayment, interestAmount, annualInterest))
            print("[Info] Please try again.")
            print("---------------------------------------------------------------------------------")

def start():
    """
        Main logic of the program
    """
    # take values
    amountBorrowed, annualInterest, monthlyRepayment = inputValue()
    # initialize some default values
    interest = 0
    cumInterest = 0
    x = 1
    # print header
    print("---------------------------------------------------------------------------------")
    print("--------------------------------Repayment Plan-----------------------------------")
    print("---------------------------------------------------------------------------------")
    print("\tMonth Number\t Debt Balance\t Monthly Interest\t Cumulative Interest")
    # run until amount is greater than 0 and less than interest
    while(amountBorrowed >= 0):
        interest = calculateInterest(amountBorrowed, annualInterest)        # new interest every loop
        print("\t\t{}\t\t\t\t {}\t\t\t\t {}\t\t\t\t {}".format(x, round(amountBorrowed, 2), round(interest, 2), round(cumInterest, 2)))
        amountBorrowed = amountBorrowed + interest - monthlyRepayment       # new amount every loop
        cumInterest += interest         # cumulative interest
        x += 1                          # for month number
    print("\t\t{}\t\t\t\t {}\t\t\t\t {}\t\t\t\t {}".format(x, 0 if amountBorrowed<0 else round(amountBorrowed, 2), round(interest, 2), round(cumInterest, 2)))

# starts the program once with true value
check = 'y'
while(check.lower() == 'y'):
    print("---------------------------------------------------------------------------------")
    # run the program initializer
    start()
    check = input("Do you want a new loan repayment calculation: ('y' to run again): ")
print("Thanks for taking your time!")