import docxpip, documents #importing the docx module to handle document

import os
from pathlib import Path

print(Path.cwd())    #changing the working dir

os.chdir('/home/navneet/Documents/pyxlproj')

print(Path.cwd())  #print working dir

d= docx.document('/home/navneet/Documents/pyxlproj/demo.docx')  #Document fun crreate a document object and open the doc
print(d.paragraphs)       #print paragraphs obj

print(d.paragraphs[0].text)  #print the Ist paragraph

#in a paragraph we have a diff run(every style have diff run()

p = d.paragraphs[1]  #save second paragraph into p
print(p.runs)  #print list of run object

#a paragrap having some bold and some italic
#------run1------------|-r2-|-r3-----|-r4---  this is four run according to style and normal

print(p.runs[0])


p.runs[3].text='italic and underlined'  #change the r3 text(and some) into
d.save('/home/navneet/Documents/pyxlproj/demo2.docx')  #save the changes into the document and save as anew demo2

#paragraph have astyle member variable

print(p.style)   #print the style of paragraph
p.style='title'  # now you change the title of whole paragraph
d.save('/home/navneet/Documents/pyxlproj/demo3.docx')

#how to change the text and modified the style

d=docx.Document()  #create a documnet file which exist in mem
d.add_paragraph("String") #adding the paragraph

d.save('/home/navneet/Documents/pyxlproj/demo4.docx') #crete a document

p=d.paragraphs[0]
p.add_run('string')  #add run into the paragraph

print(p.runs)

p.runs[1].bold = True  #added a bold style to this para
d.save('/home/navneet/Documents/pyxlproj/demo5.docx')

#modify the existing documnet

#open the existing one

def getText(filename):   #fun to  get the all paragraphs
    doc =doc8.Document(filename)   #doc obj to open word file
    fullText=[]     #list hold all the paragraph
    for para in doc.paragraphs:  #loop over all the para
        fullText.append(para.text)
    return '\n'.join(fullText)  #join -> gives singel string

print(getText('/home/navneet/Documents/pyxlproj/demo.docx'))
