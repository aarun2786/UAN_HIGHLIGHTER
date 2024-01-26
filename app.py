from flask import Flask,render_template, request, redirect,send_file,url_for
from backend import get_excel_data,pdf_highlight
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        EXCEL = request.files['excel']
        PDF = request.files['pdf']
        excel =  get_excel_data(EXCEL)
        PDF.save(PDF.filename)
        global pdf
        pdf = PDF.filename
        pdf_highlights = pdf_highlight(excel,pdf)
        return render_template("input.html",page_no=set(pdf_highlights))
    return render_template("home.html")

@app.route('/download')
def download_file():
    filename = pdf
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

