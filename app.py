from flask import Flask,render_template, request, redirect,send_file,url_for,flash
from backend import get_excel_data,pdf_highlight,color_selecton
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
        color = request.form['color']
        excel =  get_excel_data(EXCEL)
        clr = color_selecton(color)
        PDF.save(PDF.filename)
        pdf = PDF.filename
        pdf_highlights = pdf_highlight(excel,pdf,clr)
        
        return render_template("input.html",page_no=sorted(set(pdf_highlights)))
    return render_template("home.html")

@app.route('/download')
def download_file():
    global pdf
    filename = pdf
    try:
        return send_file(filename, as_attachment=True)
    except FileNotFoundError as e:
        return f"{filename} not found"

@app.route('/delete')
def delete_file():
    global pdf
    filename = pdf
    try:
        os.remove(filename)
        return "file delete"
    except:
        return 'FILE ALREDY DELETE'
if __name__ == "__main__":
    app.run()

