class atm(object):
    def __init__(self, user, card_num, pin_num, balance):
        self.user = user
        self.card = user
        self.card_num = card_num
        self.pin_num = pin_num
        self.balance = balance

    def BalanceEnquiry(self):
        self.balance = input("What is your initial balance : ")
        print("Your balance is $" + self.balance)
    def CashWithdrawl(self):
        withdrawl = input("How much would you like to withdraw : ")
        self.balance = int(self.balance) - int(withdrawl)
        print("You balance is now $" + str(self.balance))

Sai = atm("Sai Tanish", 3234567853, 1125, 2000)
Sai.BalanceEnquiry()
Sai.CashWithdrawl()