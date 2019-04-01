import openpyxl
from openpyxl.styles import Font, NamedStyle  # changed

wb = openpyxl.Workbook()
sheet = wb['Sheet']  # changed
italic24Font = NamedStyle(name="italic24Font")  # changed
italic24Font.font = Font(size=24, italic=True)  # changed
sheet['A1'].style = italic24Font  # changed
sheet['A1'] = 'Hello world!'
#wb.save('styled.xlsx')

# 2nd practice

fontObj1 = Font(name='Times New Roman', bold=True)
styleObj1 = NamedStyle(name="styleObj1")  # changed
styleObj1.font = fontObj1  # added
sheet['A1'].style = styleObj1  # changed
sheet['A1'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
styleObj2 = NamedStyle(name="StyleObj2")  # changed
styleObj2.font = fontObj2  # added
sheet['B3'].style = styleObj2 # changed
sheet['B3'] = '24 pt Italic'

wb.save('styles.xlsx')
