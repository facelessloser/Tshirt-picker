import random
import os

class Thelist(object):

    def pickert(self):
        # Opens the file so it can be read 
        a = open ('tshirt.txt', 'r')
        # Loads the list to be used as a list using the eval command
        newlist = eval(a.read())
        # Randomly picks an item from the list
        self.randomly = random.choice(newlist)
        # Removes the item you randomly picked earlyer
        newlist.remove(self.randomly)
        # Prints the T-shirt to wear
        # Writes the list to file and closes the file to save it
        f = open ('tshirt.txt', 'w')
        f.write(str(newlist))
        f.close()

    def addlist(self):
        # Opens the file so it can be read
        a = open ('tshirt.txt', 'r')
        # Loads the list to be used as a list using the eval command
        newlist = eval(a.read())
        # Shows you what you have in your list so you know what to add to it
        print "Here is the list so far %s" % sorted(newlist)
        print "There are %s t-shirts in the list" % len(newlist)
        # Asks you what you want to add to the list
        addit = raw_input("Enter number you want to add to the list > or exit to exit > ")
        while addit != 'exit':
            # Adds the raw_input to the list
            newlist.append(addit)
            print "%s has been added to the list" % addit
            print "Here is what's in the list %s" % sorted(newlist)
            # Opens the files to be writen
            f = open ('tshirt.txt', 'w')
            # Writes the list to the files
            f.write(str(newlist))
            # Closes the file
            f.close()
            addit = raw_input("Enter number you want to add to the list > or exit to exit > ")
            if addit == 'exit':
                exit()
        
    def firsttime(self):
        # Empty list
        newlist = []
        addit = raw_input("Enter number you want to add to the list > ")
        # Adds the raw_input to the list
        newlist.append(addit)
        print "%s has been added to the list" % addit
        print "Here is what's in the list %s" % sorted(newlist)
        # Opens the files to be writen
        f = open ('tshirt.txt', 'w')
        # Writes the list to the files
        f.write(str(newlist))
        # Closes the file
        f.close()
        exit()
        
    def removelist(self):
        # Opens the file so it can be read
        a = open ('tshirt.txt', 'r')
        # Loads the list to be used as a list using the eval command
        newlist = eval(a.read())
        # Shows you what you have in your list so you know what to add to it
        print "Here is the list so far %s" % sorted(newlist)
        # Asks you what you want to add to the list
        removeit = raw_input("Enter ether a number of a t-shirt or a description > ")
        # Adds the raw_input to the list
        newlist.remove(removeit)
        print "%s Has been removed from the list" % removeit
        print "Here is what's in the list %s" % sorted(newlist)
        # Opens the files to be writen
        f = open ('tshirt.txt', 'w')
        # Writes the list to the files
        f.write(str(newlist))
        # Closes the file
        f.close()
        
if __name__ == '__main__':
    start = Thelist()
print '''
ooooooooooo       oooooooo8 oooo        o88                o8   
88  888  88      888         888ooooo   oooo  oo oooooo  o888oo 
    888 ooooooooo 888oooooo  888   888   888   888    888 888   
    888                  888 888   888   888   888        888   
   o888o         o88oooo888 o888o o888o o888o o888o        888o 
                                                                
oooooooooo  o88             oooo                                
 888    888 oooo   ooooooo   888  ooooo ooooooooo8 oo oooooo    
 888oooo88   888 888     888 888o888   888oooooo8   888    888  
 888         888 888         8888 88o  888          888         
o888o       o888o  88ooo888 o888o o888o  88oooo888 o888o

ver 0.2.0 aplha       
 '''
# This looks to see if there is anything in the tshirt.txt file by reading the bytes
lenthlist = os.stat("tshirt.txt").st_size
# If there is nothing in the file it sends you to add items to your list
if lenthlist <=0:
    print "There is nothing in your list"
    start.firsttime()
else:
    a = open ('tshirt.txt', 'r')
    newlist = eval(a.read())
    print "This is what's in the list %s\n" % sorted(newlist)
    asking = raw_input("""Enter the number of what you want to do:\n
'1'> pick
'2'> add
'3'> remove
'4'> exit
> """)
    if asking == "1":
        start.pickert()
        print "%s has been randomly pick for you to wear" % start.randomly    
    elif asking == "2":
        start.addlist()
    elif asking == "3":
        start.removelist()
    elif asking == "4":
        exit()
    else:
        print "Something went wrong"
