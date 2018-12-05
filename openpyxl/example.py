import openpyxl
wb = openpyxl.load_workbook('tmp.xlsx')
# wb = openpyxl.load_workbook(..,read_only=True|write_only=True)
# useful wb function
# wb.active , wb.close() , wb.sheetnames , wb['Sheet1']

ws = wb.active
# useful ws function
# ws[1] , ws['A'] , ws.rows , ws.cols , ws.values