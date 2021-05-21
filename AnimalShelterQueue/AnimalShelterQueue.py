'''
Cracking the coding interview
Chapter 3 - Stacks and Queues
Stacks and Queues: Animal Shelter Queue
----------------------------------------
Question: An animal shelter which holds only dogs and cards, operates strickly in "First in, First out" basis. People must adopt
either the oldest based on arrival of all animals at the shelter, or they can select whether they would prefer a dog or a cat. They cannot select
which specific animal they would like. Create a data structure to maintain this system and implement operations such as enqueue dequeueAny, dequeDog, dequeueCat
You may used the built in linked list functionality
Example: 
input: 
output: 
Constraits or Questions you need to ask:

Solution notes:

'''
#Animal Node
class animal(object):
    def __init__(self, animalName=None, animalType=None, next=None):
        self.animalName = animalName
        self.animaltype = animalType
        self.next = next
        self.timestamp = 0


class animalShelter(object):
    def __init__(self):
        self.headCat = None
        self.tailCat = None
        self.headDog = None
        self.tailDog = None
        self.animalNumber = 0

    def enqueue(self, animalName, animalType):
        self.animalNumber += 1
        newAnimal = animal(animalName,animalType)
        newAnimal.timestamp = self.animalNumber

        if animalType == 'cat':
            if not self.headCat:
                self.headCat = newAnimal
            if self.tailCat:
                self.tailCat.next = newAnimal
            self.tailCat = newAnimal

        elif animalType == 'dog':
            if not self.headDog:
                self.headDog = newAnimal
            if self.tailDog:
                self.tailDog.next = newAnimal
            self.tailDog = newAnimal

    def dequeueCat(self):
        if self.headCat:
            newAnimal = self.headCat
            self.headCat = newAnimal.next
            return str(newAnimal.animalName)
        else:
            return "No cats left!"

    def dequeueDog(self):
        if self.headDog:
            newAnimal = self.headDog
            self.headDog = newAnimal.next
            return str(newAnimal.animalName)
        else:
            return "No dogs left!"

    def dequeueAny(self):
        if self.headCat and not self.headDog:
            return self.dequeueCat()
        elif not self.headCat and self.headDog:
            return self.dequeueDog()
        elif self.headCat:
            if self.headCat.timestamp < self.headDog.timestamp:
                return self.dequeueCat()
            else:
                return self.dequeueDog()
        else:
            return "No animals left"

    def display(self):
        print('The list of cats: ')
        cats = self.headCat
        countCat = 1
        while cats != None:
            print("#{} : {}.".format(countCat,cats.animalName))
            cats = cats.next
            countCat += 1

        print('The list of dogs: ')
        dogs = self.headDog
        countDog = 1
        while dogs:
            print("#{} : {}.".format(countDog,dogs.animalName))
            dogs = dogs.next
            countDog += 1

AS = animalShelter()

AS.enqueue('Asim','cat')
AS.enqueue('Zoomaa','dog')
AS.enqueue('Formal','cat')
AS.enqueue('Scump','dog')
AS.display()



print(AS.dequeueCat())
print(AS.dequeueDog())
print(AS.dequeueAny())



               

        


     
    