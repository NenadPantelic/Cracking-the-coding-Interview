#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:01:50 2020

@author: nenad
"""


class Animal:
    def __init__(self, name, id):
        self._name = name
        self._id = id
    
    # setters and getters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    

class Dog(Animal):
    #idGenerator = 1
    def __init__(self, name, id=None):
        super().__init__(name, None)
        #Dog.idGenerator += 1
        
    def __str__(self):
        return "Dog - Name = {}, id = {}".format(self._name, self.id)
    
class Cat(Animal):
    #idGenerator = -1
    def __init__(self, name, id=None):
        super().__init__(name, None)
        #Cat.idGenerator -= 1
        
    def __str__(self):
        return "Cat - Name = {}, id = {}".format(self._name, self.id)


class AnimalShelter:
    def __init__(self):
        self._dogQueue = []
        self._catQueue = []
        self._gen = 1

        
    def enqueue(self, animal):
        
        if isinstance(animal, Dog):
            animal.id = self._gen
            self._gen += 1
            self._dogQueue.append(animal)
        else:
            animal.id = self._gen
            self._gen += 1
            self._catQueue.append(animal)
            
    def dequeueAny(self):
        firstDog, firstCat = None, None
        
        if len(self._dogQueue) == 0:
            return self.dequeueCat()
        if len(self._catQueue) == 0:
            return self.dequeueDog()
        
        firstDog = self._dogQueue[0]
        firstCat = self._catQueue[0]
        # dog arrived first
        if firstDog.id < firstCat.id:
            self._dogQueue.pop(0)
            return firstDog
        else:
            self._catQueue.pop(0)
            return firstCat
    def dequeueDog(self):
        if len(self._dogQueue):
            return self._dogQueue.pop(0)
        return None
    
    def dequeueCat(self):
        if len(self._catQueue):
            return self._catQueue.pop(0)
        return None
    

a1 = Cat("Jacky")
a2 = Cat("Becky")
a3 = Dog("Micky")
a4 = Dog("Ricky")

animalShelter = AnimalShelter()
animalShelter.enqueue(a3)
animalShelter.enqueue(a1)
animalShelter.enqueue(a2)
animalShelter.enqueue(a4)
print(animalShelter.dequeueAny())
print(animalShelter.dequeueDog())
print(animalShelter.dequeueAny())
print(animalShelter.dequeueDog())
print(animalShelter.dequeueCat())
print(animalShelter.dequeueAny())
print(animalShelter._gen)
animalShelter.enqueue(Cat("Lisa"))
animalShelter.enqueue(Dog("Johny"))
print(animalShelter._gen)
#animalShelter.