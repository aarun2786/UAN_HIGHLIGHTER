from flask import Flask,render_template, request, redirect,send_file,url_for,flash
from backend import *
app = Flask(__name__)
app.secret_key = 'akr'
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
                esic_page = ESIC(pdf)
                esic = only_micron_pf(excel,pdf,esic_page,clr)
                return render_template('input.html',pfpage_no=esic,com=compay)

        elif compay == 'for all':
            if fun == 'PF':
                pf_page =PF(pdf)
                pf = highlight_for_all_pf(excel,pdf,pf_page,clr)
                return render_template('input.html',page_no =pf,com=compay)
            else:
                esic_page = ESIC(pdf)
                esic = highlight_for_all_esic(excel,pdf,esic_page,clr)
                return render_template('input.html',page_no=esic,com=compay)

        else:
            just_highlight = highlight_only(excel,pdf,clr)
            return render_template('input.html',page_no=just_highlight,com="other")



    return render_template("home.html")
@app.route("/input")
def input():
    return render_template('input.html')

@app.route('/download')
def download_file():
    global pdf
    filename = pdf
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        flash(f"{filename} not found","error")
        return redirect(url_for("input"))
@app.route('/delete')
def delete_file():
    global pdf
    filename = pdf
    try:
        os.remove(filename)
        flash("File deleted",'success')
        return redirect(url_for("input"))
    except:
        flash('FILE ALREDY DELETE','error')
        return redirect(url_for("input"))        
if __name__ == "__main__":
    app.run(debug=True)

