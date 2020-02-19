import random

#list use []  braces

catName = []
while(True):
    print('enter the name of cat' + str(len(catName)+1) + 'or enter nothing to stop')
    name=input()
    if(name==''):
        break
    catName=catName+[name]      #concetinate the list
print('the cat name are :')
for name in catName:            #trevers every value in list
    print(' '+name)

print('enter a name : ' )
n=input()
if(n not in catName):           #not in or in opreter find element in list
    print('not in list')
else:
    print('its in list')

for index,item in enumerate(catName):   #enumrate use to get the index and value both
    print('index : '+str(index)+'  item : '+item)

print(random.choice(catName))       #chose randomly from the list

random.shuffle(catName)   #shuffel the list item in between list
print(catName)

#catName*=3                 #replicate the list item

print(catName)


getindex=catName.index('a')    #to get the index of given value if mutille item are there the fist one
print(getindex)

catName.append('billi')           #adding value in list ading append at any index
print(catName)

catName.insert(1,'black')         #adding at given index. these two are only the list menthod
print(catName)

catName.remove('black')         #removing value from the list.if value appear multiple time only first value remove
print(catName)                                #delete is good when you know the index of the value

catName.sort()                  #sorting value in list
print(catName)

catName.sort(reverse=True)     #in revers order
print(catName)
                               #you can not sort the list having both number and value
catName.reverse()
print(catName)


#so list is mutable data type we can modified the lis
#but string and tupple are not.its immutable data type
