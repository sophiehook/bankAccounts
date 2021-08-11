# Importing random and datetime modules
import random 
import datetime

# Define class BasicAccount
class BasicAccount:
    # Setting a counter for creating serial account numbers
    acNum = 0
    
# Define the initialiser  
    def __init__(self, acName, openingBalance):

        # Assigns the passed parameters the variables name and balance
        self.name = acName
        self.balance = openingBalance
        self.cardNum = self.issueNewCard()
        self.cardExp = self.issueNewCard()

        # increments the serial acNum each time the class is initilalised 
        BasicAccount.acNum += 1

        # Overdraft boolean set to true 
        self.overdraft = False

# Define string representation of basic account object, includes name balance and overdaft details
    def __str__(self):
        return 'Account holder name: {self.name}\nBalance: £{self.balance}\nOverdraft: {self.overdraft}'.format(self=self)

    def deposit(self, amount):

        """
        deposit increases the balance of the account by amount
        Parameters:
            amount: float - the amount to deposit in 
        Returns:
            Nothing
        """

        # If the amount is a positive number then it can be deposited
        self.amount = float(amount)
        if amount > 0:
            self.balance += amount
            print("You deposited: £", self.amount, ". Your new balance: £", self.balance)
        else:
            print("Please deposit a positive amount of money")

    def withdraw(self, amount):

        """
        withdraw decreases the balance of the account by amount
        Parameters:
            amount: float - the amount to withdraw 
        Returns:
            Nothing
        """

        # If the amount is less than or equal to the avaliable balance then it can be subtracted
        self.amount = float(amount)
        if amount > 0:
            if self.amount <= self.getAvaliableBalance():
                self.balance -= self.amount
                print(self.name, "withdrew: £", self.amount, ". Your new balance: £", self.balance)
            else:
                print("You cannot withdraw: £", self.amount)
        else:
            print("Please deposit a positive amount of money")


    def getAvaliableBalance(self):

        """
        getAvaliableBalance returns the avalible balance of the class
        Paramaters: 
            Nothing
        Return:
            float - the avaliable account balance
        """

        # for BasicAccount it will just return the balance 
        balance = self.balance
        return float(balance)

    def getBalance(self):

        """
        getBalance returns the avalible balance of the class
        Paramaters: 
            Nothing
        Return:
            float - the account balance
        """

        return float(self.balance)

    def printBalance(self):

        """
        printBalance prints the balance of the account
        Paramaters: 
            Nothing
        Return:
            Nothing
        """

        print("Your account balance: £", float(self.balance))

    def getName(self):

        """
        getName returns the name of the account holder
        Paramaters: 
            Nothing
        Return:
            string - the name of the account holder
        """

        return self.name

    def getAcNum(self):

        """
        getAcNum returns the serial account number
        Paramaters: 
            Nothing
        Return:
            string - the number of the account
        """
        
        return str(self.acNum)
        

    def issueNewCard(self):

        """
        issueNewCard calculates a random 16 digit number and an expiry date
        Paramaters: 
            Nothing
        Return:
            Nothing
        """
        
        # Generates a random 16 digit number using the random module
        self.cardNum = str(random.randint(1000000000000000,9999999999999999))

        # Generates todays date using the datetime module
        today = datetime.datetime.now()

        # Adds 3 years to todays date
        cardExpDate = today + datetime.timedelta(days=3*365)

        # Accesses the month and the last two digits of the year in the tuple cardExp
        self.cardExp = (cardExpDate.month,cardExpDate.strftime("%y"))
        


    def closeAccount(self): 

        """
        closeAccount uses the withdraw method to remove the remaining balance 
        Paramaters: 
            Nothing
        Return:
            boolean - will always be true in this case
        """

        self.withdraw(self.balance)
        return True

    
    
# Define PremiumAccount class which is a subclass of BasicAccount
class PremiumAccount(BasicAccount):

    # Define the initilaliser which inherits acName and openingBalance from BasicAccount
    def __init__(self, acName, openingBalance, initialOverdraft):
        super().__init__(acName, openingBalance)

        # New parameter initialOverdraft is set to the variable overdraftLimit
        self.overdraftLimit = initialOverdraft

        # Overdraft boolean set to true 
        self.overdraft = True
        

# Define string representation of premium account object
    def __str__(self):
        return 'Account holder name: '+ self.name +'\nBalance: £'+ str(self.getAvaliableBalance()) +'\nOverdraft: '+ str(self.overdraft)+'\nOverdraft limit: £'+ str(self.overdraftLimit)+'\n'

    def setOverdraftLimit(self, newLimit):

        """
        setOverdraftLimit reassigns the overdraft limit variable 
        Paramaters: 
            newLimit: float - the limit that the account will be set to if valid
        Return:
            Nothing
        """

        # Ensures overdraftLimit isn't set to less than it currently is if the account has a negative balance
        if newLimit > -(self.balance):
            self.overdraftLimit = float(newLimit)

     
    def getAvaliableBalance(self):

        """
        getAvaliableBalance returns the avaliale balance of the account which includes the overdraft limit
        Paramaters: 
            Nothing
        Return:
            float - the avaliable balance 
        """

        # Need to sum balance and overdraft limit to calculate the avaliable balance
        balance = self.balance + self.overdraftLimit
        return float(balance)

    def printBalance(self):

        """
        printBalance print the account balance how much of the overdraft is unused
        Paramaters: 
            Nothing
        Return:
            Nothing 
        """

        balance = float(self.balance)

        # If the account is overdrawn it must calculte the overdraft remianing by adding the negative balance to the overdraft limit
        if self.balance < 0:
            print("Account balance: £", self.balance,"\nOverdraft remaining: £",(self.overdraftLimit + self.balance))

        # If the account isn't overdrawn then overdraft limit is unchanged 
        else:
            print("Account balance: £", self.balance, "\nOverdraft remaining: £", float(self.overdraftLimit))


    def closeAccount(self): 

        """
        closeAccount uses the withdraw method to remove the remaining balance if the account isn't overdrawn
        Paramaters:
            Nothing
        Return:
            boolean - true or false depending on wether the account is overdrawn 
        """
        
        # If the account is overdrawn then prints the message and returns false
        if self.balance <= 0:
            print("Cannot close the account due to customer being overdrawn by £", -(self.balance))
            return False
              
        # If the account isn't overdrawn then withdraws the balance and returns true
        else:
            self.withdraw(self.balance)
            return True

