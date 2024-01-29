import openpyxl
import fitz
def get_excel_data(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook['UAN']
    max_row = sheet.max_row
    data_list = []
    for index, row in enumerate(sheet.iter_rows(min_row=1, max_row=max_row, values_only=True), start=1):
        data_list.extend((list(row)))
    workbook.close()
    return data_list
def pdf_highlight(excel,pdf,color):
    page_start = 0
    doc = fitz.open(pdf)
    page_num = []
    for uan in excel:
          for i in range(page_start,len(doc)):
            page_no = doc[i]
            text = page_no.search_for(uan,quads=True)
            if text:
                htext =  page_no.add_highlight_annot(text)
                htext.set_colors(stroke=[0,0,1])
                htext.update(opacity=0.5)
                page_num.append(i+1)
                page_start = i
                break
    doc.save(pdf,incremental=True,encryption=0)
    doc.close
    return page_num
