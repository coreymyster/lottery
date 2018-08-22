# Corey Sokol

from random import *
import time

# Creates a user for the game
class UserAccount:
    def __init__(self, name):
        splitNames = name.split(' ')
        self.first = splitNames[0]
        self.last = splitNames[1]
        
    def getName(self):
        return self.first + ' ' + self.last
    
    def generateTicket(self, dollarAmount):
        userTickets = []
        ticketNumber = randrange(1000, 1050)
        tickets = dollarAmount
        for t in range(int(tickets)):
            ticketNumber = randrange(1000, 1050)
            userTickets.append(ticketNumber)
        return userTickets
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
        
    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    # Sets the head and tail of the node to keep track of the front and end of the list
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Checks if the list is empty by checking if there is a head
    def isEmpty(self):
        return self.head == None
    
    # Returns the size of the queue. The counter increments as it works
    # through the queue and stops once cuurent becomes None.
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    
    # Creates a new node and adds a new item to the queue. 
    def enqueue(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
 
    # Removes oldest item from the queue. Sets head to the next node after the oldest node to remove
    # the first item in the queue.
    def deque(self):
        self.head = self.head.getNext()
        current = self.head
        previous = None
  
        while current != None:
            previous = current
            current = current.getNext()
    
    # Searches the list for a specific item and returns whether it's found or not. 
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def bubbleSort(alist):
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if alist[i]>alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp

        
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
    
    ticketList = UnorderedList()
    
    print("""
Your ticket numbers are below {}, good luck!
""".format(user.getName()))
    
    # For testing purposes we're creating the competition
    jim = UserAccount("Jim Jones")
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
   
    sandy = UserAccount("Sandy Sandoval")
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    
    moneybags = UserAccount("Moneybags McGee")
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    ticketList.enqueue(randrange(1000, 1050))
    
    # For any ticket you bought, add it to the queue
    for ticket in userTickets:
        print(ticket)
        ticketList.enqueue(ticket)
    
    #print(ticketList.size())
    
    time.sleep(2)
    
    
    winningTicket = randrange(1000, 1050)
    print("Let the drawing begin!")
    
    print('This weeks winning number is: {}'.format(winningTicket))
    
    print("""Let's see if you hold the winning ticket.
Searching....""")
    time.sleep(3)
    
    if ticketList.search(winningTicket) == True:
        print("Congratualtions! You won this week's lottery!")
    else:
        print("Sorry, you didn't win this week. Better luck next week!")
            
main()
