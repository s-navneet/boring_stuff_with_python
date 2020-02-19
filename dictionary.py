
# dictionary it is imutable type use {} braces
'''
birthday = {'navneet': 'july_1', 'navkiran': 'may_16'}
    while(True):
    print('enter the name or blank to quit')
    name=input()
    if(name==''):
        break
    if(name in birthday):
        print(birthday[name]+'is the birthday of' +name)
    else:
        print('do not found add in list')
        print('birthdya date : ')
        date=input()
        birthday[name]=date
        print('add')

for v in birthday.values():
    print(v)

for v in birthday.keys():
    print(v)

for k,v in birthday.items():
    print('key : '+k+', value : '+v)

print(birthday.get('navneet',0))        #get method to check key exist in dictionry if exist return value of that key

birthday.setdefault('surya','dec_10')
print(birthday)

msg="hello my name is navneet singh and i am a developer"
count={}
for ch in msg:
    count.setdefault(ch,0)
    count[ch]+=1
    print(count)
'''

'''
# list inside list

allguest = {'alice': {'apple': '2', 'banana': '3'},
            'bob': {'sandwitch': '4', 'apple': '3'},
            'carlo': {'cup': '2', 'apple': '4'}
            }
def total(guests, item):
    num = 0
    for k, v in guests.items():
        print(k);
        print(v)
        print()
        num = num + int(v.get(item, 0))
    return num
print('num of thing being brought')
print('apple    '+str(total(allguest, 'apple')))
print('sandwitch    '+str(total(allguest, 'sandwitch')))
print('banana    '+str(total(allguest, 'banana')))
print('cup    '+str(total(allguest, 'cup')))
'''

#dictionary box
decbox = {'rope': '1',
       'torch': '6',
       'goldcoin': '42',
       'dagger': '1',
       'arrow': '12'}
#function to display total items in the decbox
def displaybox(decbox):
    num=0
    for k,v in decbox.items():
        print(v,'',end='')
        print(k)
        num = num + int(decbox.get(k, 0))
    return num
print('total number of item is : ' +str(displaybox(decbox)))

#another list of item, we want to add in decbox and update the decbox
list=['goldcoin','dagger','goldcoin','goldcoin','ruby']
#fun to add the list item into decbox and count
def addTodecbox(decbox,list):
    for item in list:
        decbox.setdefault(item,0)
        decbox[item]=int(decbox[item])+1
    return decbox
decbox=addTodecbox(decbox,list)
print(decbox)
print('total number of item is : ' +str(displaybox(decbox)))



