import random
words=['hello',
       'navneet',
       'how are you',
       'fine',
       'tell me about ypur self']
print(words[random.randint(0,len(words)-1)])

name='NAVNEET'
for i in name:
    print('******'+i+'*******')

#modified the string

name1='navneet is a boy'
newName1 = name1[0:8]+ 'the' +name1[12:16]
print(newName1)


s1='navneet'
s2='singh'
s3='ramgharia'
s1=s1+' singh'+' ram'

print(s1)
#news=s1+s2+s3
print(s1,s2,s3, sep=' ')
