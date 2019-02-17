
import sys
import xlrd
import numpy as np
from datetime import date, datetime

excelFile = sys.argv[1]

def read_excel(filePath):
   content=[]
   merged_content=[]
   excelFile=xlrd.open_workbook(filePath)
   sheetNames = excelFile.sheet_names()
   for name in sheetNames:
      sheet = excelFile.sheet_by_name(name)
      for row in range(sheet.nrows):
         content.append(sheet.row_values(row))
      merged_content = sheet.merged_cells
   return content,merged_content

data,merged_struct = read_excel(excelFile)

print(data)

multi_data = np.array(data)

print(merged_struct)

for merge in merged_struct:
   (rs, re, cs, ce) = merge
   multi_data[rs:re, cs:ce] = multi_data[rs][cs]

print(multi_data)
