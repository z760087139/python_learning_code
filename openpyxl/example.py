import openpyxl
# load from excel
wb = openpyxl.load_workbook('tmp.xlsx')
# wb = openpyxl.load_workbook(..,read_only=True|write_only=True)
# useful wb function
# wb.active , wb.close() , wb.sheetnames , wb['Sheet1']

ws = wb.active
# useful ws function
# ws[1] , ws['A'] , ws.rows , ws.cols , ws.values

# create excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'new_title'
new_ws = wb.create_sheet('create_sheet')
new_ws.append([[1,2,3],[4,5,6]]) # can be list tuple range dict

# vaildation data
from openpyxl.worksheet.datavalidation import DataValidation
dv = DataValidation(type="list", formula1='"Dog,Cat,Bat"', allow_blank=True)
dv.error ='Your entry is not in the list'
dv.errorTitle = 'Invalid Entry'
# Optionally set a custom prompt message
dv.prompt = 'Please select from the list'
dv.promptTitle = 'List Selection'
# Add the data-validation object to the worksheet
ws.add_data_validation(dv)
dv.add(c2)

# merge cells / unmerge cells
ws.merge_cells('A2:D2')
ws.unmerge_cells('A2:D2')