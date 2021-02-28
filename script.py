from flask import Flask, render_template, request, redirect, url_for
import back

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def onetowm():
    
    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args['name']
            return render_template('base.html', n = back.ReturnGeodata(str(name)))
  
    return render_template('base.html')
    

@app.route("/twotowns", methods=['GET', 'POST'])
def twotowns():
    if request.method == 'GET':
        if 'name1' and 'name2' in request.args:
            name1 = request.args['name1']
            name2 = request.args['name2']
            return render_template('index.html', m = back.ReturnGeodataTwoTowns(str(name1), str(name2)))
    
    return render_template('index.html')


@app.route("/numbertown", methods=['GET', 'POST'])
def numbertown():
    if request.method == 'GET':
        if "number" in request.args:
            number = request.args['number']
            return render_template('numbertowns.html', l = back.ReturnFewTowns(int(number)))
    return render_template('numbertowns.html')


@app.errorhandler(Exception)
def defaultHandler(e):
   return render_template('index.html'), 500
   

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000)




    




