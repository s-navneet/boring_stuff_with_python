from pathlib import Path

p=Path('n2.txt')
p.write_text('hello spam thhis is new created file')
print(str(p.read_text()))
'''
print(Path.cwd())
open_file=open('/home/navneet/PycharmProjects/python_boring/n2.txt')
print(open_file)
'''
