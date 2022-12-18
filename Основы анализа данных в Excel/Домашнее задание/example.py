import xlwings as xw
wb = xw.Book('table.xlsx')
sheet = wb.sheets['Sheet1']
sheet.range('A1').value = 'From Script'
wb.save('table(1).xlsm')