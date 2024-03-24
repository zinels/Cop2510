#Week 9 Lecture 1

#File i/o

# breedfile = open('popularbreedsUS.txt', 'r') #read mode
# breeds = breedfile.readlines() #readlines - read contents of the file and return a list
# breedfile.close()

# print(breeds)

# #Alternate example of how to read a text file
# with open('popularbreedsUS.txt', 'r') as breedfile:
#     breeds = breedfile.readlines() # reads contents of the file and returns a string
    #breedstr = breedfile.read() #read -- read contents of the file and return as a string
    # db = breedfile.readline() #read contents of the file and return one line at a time; loop is needed

# print(breedstr)
# print(breeds)
# print(db)

# #clean up list
# dogs = []
# for b in breeds:
#     d = b.rstrip() # removes whitespace after texts
#     dogs.append(d)
# print(dogs)

#---Example-- how to write to a file
#w- write mode ; a- append mode; r+,w+ -- represents updates to the file
# with open('experimentsentence.txt', 'w') as outfile:
#     outfile.write('Confirm plans for spring break.')
# with open('experimentsentence.txt', 'a') as outfile:
#     #outfile.write('Also get groceries.') ## this just overrides the whole thing.
#     outfile.write('Also get groceries')

#Intro to matplotlib plotting
import matplotlib.pyplot as plta

plta.ion()  # Enable interactive mode
x = [10, 20, 30, 40]
y = [15, 35, 75, 95]
plta.plot(x, y)
plta.show()

#Plot imported data
with open('gltmarch.csv', encoding = 'utf-8-sig') as pfile:
    gtemp=[]
    for g in pfile:
        gtemp.append(float(g))

years = range(1900,2016)
plta.plot(years,gtemp)
plta.xlabel('Year')
plta.ylabel('Global Temperature(F)')
plta.title('Global Temperature in March from March 1900 to March 2015')
plta.grid(True)
plta.show()
