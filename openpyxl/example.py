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
