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

        if compay == "only micron":
            if fun == 'PF':
                pf_page =PF(pdf)
                pf = only_micron_pf(excel,pdf,pf_page,clr)
                return render_template('input.html',page_no =pf,com=compay)
            else:
                esic_page = ESIC(excel)
                esic = only_micron_pf(excel,pdf,esic_page,clr)
                return render_template('input.html',pfpage_no=esic,com=compay)

        elif compay == 'for all':
            if fun == 'PF':
                pf_page =PF(pdf)
                pf = highlight_for_all_pf(excel,pdf,pf_page,clr)
                return render_template('input.html',page_no =pf,com=compay)
            else:
                esic_page = ESIC(excel)
                esic = highlight_for_all_esic(excel,pdf,esic_page,clr)
                return render_template('input.html',page_no=esic,com=compay)

        else:
            just_highlight = highlight_only(excel,pdf,clr)
            return render_template('input.html',page_no=just_highlight,com="other")



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

