import re

para='my number is 415-234-1234 and we have another 456-234-9898'
phonNumReg=re.compile(r'\d{3}-\d{3}-\d{4}')
mo=phonNumReg.search(para)
print('found : '+mo.group())

print()
#grouping
print('#grouping')
para='my number is 415-234-1234 and we have another 456-234-9898'
phonNumReg=re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo=phonNumReg.search(para)
print('found 1 : '+mo.group(1))
print('found 2: '+mo.group(2))
print('found all: '+mo.group(0))
print('found : '+str(mo.groups()))           #groups method to find all the groups
areacode,mainnumber=mo.groups()              #assign a name to the diff group
print(areacode)
print(mainnumber)

print()
#paranthesis
print('#paranthesis')
string1='number is (0416) (2247352)'
p=re.compile(r'(\(\d\d\d\d\)) (\(\d\d\d\d\d\d\d\))')
mo=p.search(string1)
print(mo.group())

print()
#multiple group with the pipe
print('multiple group with the pipe')
s='hello Navneet Singh navneet singh navkiran navpreet'
p1=re.compile(r'(dsfas|sfvsdaf)|(navneet|singh)')
o=p1.search(s)
print(o.group(1))
print(o.group(2))
print(str(o.groups()))

p2=re.compile(r'nav(kiran|neet|preet)')
o1=p2.search(s)
print(str(o1.group()))
print(str(o1.group(1)))

print()
#optional matching with ?
print('#optional matching with ?')
p=re.compile(r'Bat(wo)?man')
o=p.search('the advanture of Batwoman')
print(o.group())
print(p.findall('the advanture of Batwoman'))

print()
#match zero or more with *
print('#match zero or more with *')
p=re.compile(r'Bat(wo)*man')
o=p.search('the advanture of Batman, Batwoman, Batwowowowowoman')
print(o.group())
print(p.findall('the advanture of Batman, Batwoman, Batwowowowowoman'))

print()
#match one or more with +
print('#match one or more with +')
p=re.compile(r'Bat(wo)+man')
o=p.search('the advanture of Batman, Batwoman, Batwowowowowoman')
print(o.group())
print(p.findall('the advanture of Batman, Batwoman, Batwowowowowoman'))

print()
#match specify repition with match
print('#match specify repition with match')
p=re.compile(r'(wo){2,5}')
o=p.search('the advanture of Batman, Batwoman, Batwowowowowoman')
print(o.group())
p.findall('the advanture of Batman, Batwoman, Batwowowowowoman')


xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, '
                  '7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
