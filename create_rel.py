import openpyxl    

class createExcel():
    def createandsave(self, all, cursor) -> None:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        
        headers = [column[0] for column in cursor.description]
        sheet.append(headers)
        
        for row in all:
            sheet.append(list(row))

        # Salva a planilha como um arquivo XLSX
        workbook.save('dados.xlsx')