# Corey Sokol

from random import *
import time

# Creates a user for the game
class UserAccount:
    def __init__(self, name):
        # Requires the user to enter a first and last name
        splitNames = name.split(' ')
        self.first = splitNames[0]
        self.last = splitNames[1]
    
    # Returns user's name
    def getName(self):
        return self.first + ' ' + self.last
    
    # Set the tickets to the user
    def setTickets(self, tickets):
        self.tickets = tickets
        return self.tickets
    
    # Get the tickets the user has
    def getTickets(self, winningTicket):
        if winningTicket in self.tickets:
            print("Congratualtions to {}, who won this week's lottery!".format(self.first))
            return True
            
    
    # Generates lottery tickets for the user based on the number of tickets they want to buy.
    # Random numbers are generated for each ticket.
    def generateTicket(self, dollarAmount):
        userTickets = []
        ticketNumber = randrange(1000, 1050)
        tickets = dollarAmount
        for t in range(int(tickets)):
            ticketNumber = randrange(1000, 1050)
            userTickets.append(ticketNumber)
        return userTickets

class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
        
    def insert(self, data):
        # Checks duplicates
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
        
    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
        
    def preorder(self):
        print (str(self.value))
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print (str(self.value))
                
    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print (str(self.value))
        if self.rightChild:
            self.rightChild.inorder()

        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
        
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    
    def preorder(self):
        print("preorder")
        self.root.preorder()
        
    def postorder(self):
        print("postorder")
        self.root.postorder()
        
    def inorder(self):
        print("inorder")
        self.root.inorder()

        
def main():
    print("**********  Welcome to the lottery!!!  **********")
    print("""For every dollar you put into the lottery pool, you receive a lottery ticket.
For example, if you add $5 to the pool, you get 5 separate tickets. If your ticket
matches the number drawn, you win and the winnings from the lottery will be deposited
to your account. The drawing occurs weekly.
""")
    name = input("Since this is your first time here, tell us your first and last name: ")
    dollarAmount = input("How much do you want to add to the pool? Enter single numbers only (ex. 5 for $5) $")
    
    # Creates you as a user for the game
    user = UserAccount(name)
    userTickets = user.generateTicket(dollarAmount)
    user.setTickets(userTickets)
    
    
    ticketList = BinaryTree()
    
    print("""
Your ticket numbers are below {}, good luck!
""".format(user.getName()))
    
    # For testing purposes we're creating the competition
    jim = UserAccount("Jim Jones")
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
   
    sandy = UserAccount("Sandy Sandoval")
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    
    moneybags = UserAccount("Moneybags McGee")
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    ticketList.insert(randrange(1000, 1050))
    
    # For any ticket you bought, add it to the queue
    for ticket in userTickets:
        print(ticket)
        ticketList.insert(ticket)
    
    #print(ticketList.size())
    
    time.sleep(2)
    
    
    winningTicket = randrange(1000, 1050)
    print("Let the drawing begin!")
    
    print('This weeks winning number is: {}'.format(winningTicket))
    
    print("""Let's see if you hold the winning ticket.
Searching....""")
    time.sleep(3)
    
    #ticketList.preorder()
    
    if ticketList.find(winningTicket) == True and user.getTickets(winningTicket) == True:
        print("You win the cash prize of ") #${}".format(ticketList.size()))
    else:
        print("There is no winner this week, better luck next week!")
            
main()
