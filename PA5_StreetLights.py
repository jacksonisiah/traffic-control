import random
import time

class Queue(object):
    def __init__(self, size):
        self.__maxSize = size
        self.__que = [None] * size
        self.__front = 1
        self.__rear = 0
        self.__nItems = 0
    
    def insert(self, item):
        if self.isFull():
            raise Exception("Queue overflow")
        self.__rear += 1
        if self.__rear == self.__maxSize:
            self.__rear = 0
        self.__que[self.__rear] = item
        self.__nItems += 1
        return True
    
    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        front = self.__que[self.__front]
        self.__que[self.__front] = None
        self.__front += 1
        if self.__front == self.__maxSize:
            self.__front = 0
        self.__nItems -= 1
        return front
    
    def peek(self):
        return None if self.isEmpty() else self.__que[self.__front]

    def isEmpty(self): 
        return self.__nItems == 0
    
    def isFull(self):  
        return self.__nItems == self.__maxSize
    
    def __len__(self): 
        return self.__nItems
    
    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            j = i + self.__front
            if j >= self.__maxSize:
                j -= self.__maxSize
            ans += str(self.__que[j])
        ans += "]"
        return ans

def traffic_light_controller():
    # Queue Initialization: Creates a queue for each street, with a maximum size of 10.
    queues = { }
    

    # Start with the first street in the light order
    # Always start with one green light in the North
    # Track the number of iterations
    
    # A Loop that simulates the behavior of cars arriving at each street and the operation of the traffic lights.
    # Random Car Generation: Each iteration randomly generates cars for the streets (35% chance per street). 
    # If a car is added, it prints the car ID and the current queue.
        
    # Print the current status of all traffic lights and their queues is printed for monitoring
    # Check if any queue has reached 6 cars or if the current queue is empty
    # If the current street's queue is empty or reaches 6 cars, 
    # it checks all streets to find the one with the most cars (or at least 6). 
    # The traffic light then changes to that street.        
    # Allow cars to pass if the light is green
    # If the current green light is active and there are cars in the queue, 
    # the first car is removed from the queue and the action is logged.
        
    # Pause the program after 10 iterations
    