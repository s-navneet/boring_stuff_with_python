import openpyxl,os

os.chdir('/home/navneet/Documents/pyxlproj') #change crunnet working directory
workbook = openpyxl.load_workbook('example.xlsx')
print(type(workbook))

print(workbook.get_sheet_names())

sheet=workbook.get_sheet_by_name('Sheet1')
print(type(sheet))

cell=sheet['A1']
print(str(cell.value))

print(str(sheet['B1'].value))

for i in range(1,8):
    for j in range(1,4):
        print(i,j,sheet.cell(row=i, column=j).value)
