import random

class Atm(object):
    def __init__(self, cardnum, pin):
        self.cardnum = cardnum
        self.pin = pin

    input('Enter your card number: ')
    input('Enter your pin: ')   

    def withdrawl(self):
        m = input('How much cash do you want to withdraw? ')
        print(str(m) + ' rupees have been withdrawn from your account!')
    
    def balance(self):
        b = random.randint(1000000, 7000000)
        print('Your balance is currently ' + str(b) + ' rupees.')

Mahathi = Atm('1234567898765432', '7777')

Mahathi.withdrawl()
Mahathi.balance()

