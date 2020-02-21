import re,os,shutil
from pathlib import Path

print(str(Path.cwd()))

date_pattern=re.compile(r"""^(.*?)     #all text before the date
                        ((0|1)?\d)      #one or two digit for the month
                        ((0|1|2|3)?\d)  #one or two digit for the day
                        ((19|20)\d\d)   #four digit for the year
                        (.*?)$          #all text after the date
                        """,re.VERBOSE)

print(os.listdir('.'))
for filename in os.listdir('.'):
    mo=date_pattern.search(filename)
    if(mo==None):
        continue
    befor=mo.group(1)
    month=mo.group(2)
    day=mo.group(2)
    year=mo.group(2)
    after=mo.group(2)
    eurpianfile = befor+day+'-'+month+'-'+year+after
    print(str(europianfile))
    abswd=os.path.abspath('.')
    filename=os.path.join(abswd,filename)
    europianfile=os.path.join(abswd,europianfile)
    print(f'Renaming "{filename}" to "{europianfile}"...')
    shutil.move(filename,europianfile)
