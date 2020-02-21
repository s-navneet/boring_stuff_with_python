from pathlib import Path
import os
#print(str(Path.cwd())) #show the current working directory
#print(str(Path.home())) #show the home directory

#os.makedirs('/home/navneet/PycharmProjects/python_boring_file2/n1/n2/n3')  #make subdirectoy directories

#Path('/home/navneet/PycharmProjects/python1').mkdir()    #make only one directory

#print(str(os.path.abspath('.')))
#print(str(os.path.relpath('.')))

print(os.path.getsize('/home/navneet/PycharmProjects/python_boring/list.py'))  #getting the size of one perticular file
print(os.listdir('/home/navneet/PycharmProjects/python_boring'))  # getting all the file in the folder

#getting size of diff diff file in one drctry
totalSize=0
for filename in os.listdir('/home/navneet/PycharmProjects/python_boring'):
    Size=int(os.path.getsize(os.path.join('/home/navneet/PycharmProjects/python_boring',filename)))
    totalSize+=int(os.path.getsize(os.path.join('/home/navneet/PycharmProjects/python_boring',filename)))
    print('size of file '+filename+' : '+str(Size))
print('total size of all file is :  '+str(totalSize))  #print total size of all the file


