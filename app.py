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
        fun = request.form['type']
        excel =  get_excel_data(EXCEL)
        clr = color_selecton(color)
        PDF.save(PDF.filename)
        pdf = PDF.filename

        
        if fun == 'ESI':
            if compay == "only micron":
                esic_page = ESIC(pdf)
                only_micron = only_micron_esi(excel,pdf,esic_page,clr)
                return render_template("input.html",page_no=only_micron,com = compay)
            else:
                esic_page = ESIC(pdf)
                for_all = highlight_for_all_esic(excel,pdf,esic_page,clr)
                return render_template("input.html",page_no=for_all,com = compay)
        else:
            if compay == "only micron":
                pf_page = PF(pdf)
                only_micron = only_micron_pf(excel,pdf,pf_page,clr)
                return render_template("input.html",page_no=only_micron,com = compay)
            else:
                pf_page = PF(pdf)
                for_all = highlight_for_all_pf(excel,pdf,pf_page,clr)
                return render_template("input.html",page_no=for_all,com = compay)
                
        
    return render_template("home.html")



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

