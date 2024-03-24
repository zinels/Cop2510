#Week 11 Lecture 1

#inttro to classes
#class - recipe(blueprint) for objects that define what the object has(or is)
#object - entity that has both state ( data, attributes) and behaviour (methods)


#how (not) to create class

class Test:
    pass #place holder for meaningful code

#better way to create a class
class Television:
    #create an initializer method 
    def __init__(self):#runs automatically when an object is created
        self.__channel = 1#self is a placeholder for the object
        self.__volume = 1#attributes : channel, volume, power
        self.power = False # on is True; off is False



    #accessor (getter) methods - get a value from attribute
    def getchannel(self):
        return self.__channel
    
    def getvolume(self):
        return self.__volume
    def getpower(self):
        if self.__power:
            status = 'On'
        else:
            status = 'Off'
        return status

    #mutator (setter) methods -  change values in your attributes
    def setchannel(self, ch):
        self.__channel = ch

    def setvolume(self, vol):
        self.__volume = vol

    def setpower(self, p):
        self.__power = p







#---end of class definition----

def main():
    test1 = Test()
    print(test1)
    test1.name = 'Programming Exam 1' # create an attribute to store data
    print(f'{test1.name} is on Thursday March 21st.')

    #create a television object
    tv1 = Television()

    #test mutator
    tv1.setchannel(60)
    #test accessor
    print(f'The TV is set to channel {tv1.getchannel()}')
    
main()