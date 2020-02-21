import re

string1='number is (0416)-(2247352)'
p=re.compile(r'((\d\d\d\d))-(\(\d\d\d\d\d\d\d\))')
mo=p.search(string1)
print(mo.group())
