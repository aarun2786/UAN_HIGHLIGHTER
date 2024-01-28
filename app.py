from flask import Flask,render_template, request, redirect,send_file,url_for
from backend import get_excel_data,pdf_highlight
app = Flask(__name__)
import time
import os
pdf = ""
@app.route('/',methods=['POST','GET'])
def home():
    global pdf
    if request.method == 'POST':
        EXCEL = request.files['excel']
        PDF = request.files['pdf']
        color = tuple(request.form['color'])
        excel =  get_excel_data(EXCEL)
        PDF.save(PDF.filename)
        pdf = PDF.filename
        pdf_highlights = pdf_highlight(excel,pdf,color)
        
        return render_template("input.html",page_no=set(pdf_highlights))
    return render_template("home.html")

@app.route('/download')
def download_file():
    global pdf
    filename = pdf
    return send_file(filename, as_attachment=True)

@app.route('/delete')
def delete_file():
    global pdf
    filename = pdf
    os.remove(filename)
    return "file delete"
if __name__ == "__main__":
    app.run()

