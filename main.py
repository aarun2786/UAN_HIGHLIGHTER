from flask import Flask,render_template, request, redirect,send_file,url_for,flash,Blueprint
from backend import *
from file_operation import *
Main = Blueprint("Main", __name__)

@Main.route(rule = '/', methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        EXCEL = request.files['excel']
        PDF = request.files['pdf']
        color = request.form['color']
        company = request.form['com']
        fun = request.form['type']
        Project_name = request.form['Project_Name']
        
        name = Change_filename(PDF.filename, Project_name)      
        save_file(PDF, Project_name)
        
    #try:  
        clr = color_selecton(color)
        path = f"{folder}/{name}"
        excel = get_excel_data(EXCEL,fun)
        if company == "Only Micron":
            if fun == 'PF':
                pf_page = PF(path)
                pf = only_micron_pf(excel, path, pf_page, clr)
                update_json(Project_name.title(), pf, fun, name)
            else:
                esic_page = ESIC(path)
                esic = only_micron_esi(excel, path, esic_page, clr)
                update_json(Project_name.title(), esic, fun, name)

        elif company == 'For all':
            if fun == 'PF':
                pf_page = PF(path)
                pf = highlight_for_all_pf(excel, path, pf_page, clr)
                update_json(Project_name.title(), pf, fun, name)
            else:
                esic_page = ESIC(path)
                esic = highlight_for_all_esic(excel, path, esic_page, clr)
                update_json(Project_name.title(), esic, fun, name)

        else:
                page = highlight_only(excel,path,clr)
                update_json(Project_name,page ,fun,name)
        return redirect(url_for("Main.home"))
    
    #except Exception as error:
    #    flash(f"{error}",'error')
    #    return redirect(url_for("Main.home"))  
    json_data = get_json()
    return render_template('home.html',name=json_data)


@Main.route(rule = '/download/<name>')
def download(name):
     with open(f"static/PDF/{name}",'r') as file:         
         return send_file(file.name, as_attachment=True)

