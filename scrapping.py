import webbrowser
#webbrowser.open('https://google.com')
import webbrowser,sys, pyperclip
# sys variable store the comandline argument into list
#sys.argv #['scrappinf.py','map_address']
# check if command line argument is passed
'''if(len(sys.argv)>1):
    #['scrapping.py','map_address'] ->(combine into a single string)->scrapping maps_ddress
    address=' '.join(sys.argv[1:])
else:
address = pyperclip.paste()


webbrowser.open('https://google.com/maps/place/banerpune')
'''

import requests   #request module is us to dnld the file from the web
res=requests.get('http://automatetheboringstuff.com/files/rj.txt')  #get used for going the url and dnld
print(str(res.status_code))  #res_status_code used to know the succcessfull status of res object
print(str(len(res.text)))   #print length of file in char

print(res.text[:500])   #print upto 500 char
res.raise_for_status()  #success or not raise exception


dnldfile=open('romeojuliat.txt','wb')       #creat new file name dnldfile in writebinary mode
for chunk in res.iter_content(100000):      #forloop for dnld in chunks(group of byts here 100000 byts in one chunk
    dnldfile.write(chunk)                    #write these chunk into file(dnld)

dnldfile.close()
