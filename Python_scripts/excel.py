
#import sys
import xlrd
import numpy as np
#from datetime import date, datetime

#excelFile = sys.argv[1]

def read_excel(filePath):
   sheets_content=[]
   excelFile=xlrd.open_workbook(filePath)
   sheetNames = excelFile.sheet_names()
   for name in sheetNames:
      data_content=[]
      merged_content=[]
      sheet = excelFile.sheet_by_name(name)
      for row in range(sheet.nrows):
         data_content.append(sheet.row_values(row))
      merged_content = sheet.merged_cells
      
      multi_data = np.array(data_content)
      for merge in merged_content:
         (rs, re, cs, ce) = merge
         multi_data[rs:re, cs:ce] = data_content[rs][cs]
      
      sheets_content.append(multi_data)
   return sheets_content


if __name__ == '__main__':
   print(read_excel(excelFile))
