#This project allows you to apply the knowledge gained from all Python modules covered in the learning platform. 
#The knowledge from each module is essential for implementing certain functionalities in this project.
#In this project, you will simulate bank account operations using object-oriented programming (OOP). 
#You should create a class called BankAccount, specializing in all banking operations, including:
#Objectives
#By the end of this project, you will be able to:
#Create a class for the bank account operation.
#Implement multiple functions, in which each function specialized in only one operation of the banking account.
#Test your bank account class by applying multiple operations.

import random
import time
import os

class BankAccount:
    
    
    #Implement a constructor for creating an account once an object of this class is created.
    #The constructor arguments should be named (username), accountType (checking or saving), and balance (zero by default).
    def __init__(self, userName, accountType ,balance = 0):
        self.__userName = userName
        if accountType == "checking" or accountType == "saving":
            self.__accountType = accountType
        else:
            print("wrong account type")
        self.__balance = balance

        #In the constructor function, generate an ID for the new account and create a new file containing all user transactions.
        #The specified file naming format requires including the user's name, account type, and user ID, ensuring adherence to a particular pattern.
        self.__accountNumber= random.randint(1000, 10000)
        self.__filename=str(self.__accountNumber)+"_"+self.__accountType+"_"+self.__userName+".txt"
        self.__transactionFile = open(self.__filename, "a")
        self.createAccount();
    
    #Creating an Account.
    def createAccount(self):
        self.__transactionFile.write("Account Created"+str(time.time()))
        
        
    #Depositing Money. 
    #Implement a function for depositing money into the account. 
    #This transaction should be stored in the statement file of the user.
    def depositMoney(self,amount):
        if amount >=0:
            self.__balance += amount
            self.__transactionFile.write("Amount Deposited = "+str(amount)+str(time.time()))       
        else:
            print("amount less than 0")
        
    #Withdrawing Money.
    #Implement a function for withdrawing money from the account. 
    #This transaction should be stored in the statement file of the user.
    #Notice that the user can’t withdraw money higher than its balance.
    def withdrawMoney(self,amount):
        if self.__balance-amount>=0:
            self.__balance -= amount
            self.__transactionFile.write("Amount withdrew = "+str(amount)+str(time.time()))
        else:
            print("Not enough funds in the account")
            self.__transactionFile.write("Transaction failed! No funds in the acount "+str(time.time()))
            
            
    #Checking the balance.  
    #Implement a function for getting the account’s balance.
    def checkBalance(self):
        self.__transactionFile.write("balance checked "+str(time.time()))
        print(self.__balance)
        return self.__balance
        
        
    #Getting the Account number.    
    def getAccountNum(self):
        print(self.__accountNumber)
        return self.__accountNumber
        
        
    #Getting the Account type.    
    def getAccountType(self):
        print(self.__accountType)
        return self.__accountType
        
        
    #Getting the Holder name.
    def holderName(self):
        print(self.__userName)
        return self.__userName
        
        
    #Keeping a transaction history. 
    #Implement a function for getting transaction history by reading the statement file.
    def transactionHistory(self):
        if os.path.isfile(self.__filename) != True :
            return None
        file = open(self.__filename, "r")
        lines = file.readlines()
        for line in lines:
            print(line)
        file.close
            
        

#Implement three separate functions for retrieving the user ID, username, and account type
#Test your code by creating multiple objects and applying different transactions.        

account1 = BankAccount("Satinder","saving")
account1.checkBalance()
account1.depositMoney(200)
account1.checkBalance()
account1.withdrawMoney(20)
account1.checkBalance()
account1.getAccountNum()
account1.getAccountType()
account1.holderName()
account1.getAccountNum()
account1.transactionHistory()
