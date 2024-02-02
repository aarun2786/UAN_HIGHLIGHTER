from flask import Flask,render_template, request, redirect,send_file,url_for,flash
from backend import *
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
        compay = request.form['com']
        excel =  get_excel_data(EXCEL)
        clr = color_selecton(color)
        PDF.save(PDF.filename)
        pdf = PDF.filename
        if compay == "only micron":
            only_mic = only_micron(pdf)
            pdf_highlights = pdf_highlight(excel,pdf,only_mic,clr)
            return render_template("input.html",page_no=pdf_highlights)
        else:
            all_comp = all(pdf)
            all_pdf_highlight = highlight_all(excel,pdf,all_comp,clr)
            return render_template("input.html",page_no=all_pdf_highlight)
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
    app.run(debug=True)

