from crypt import methods

from flask import render_template, request
from app import app

@app.route('/',methods=['GET','POST'])
def home():
    name = "Mosudi I. O."
    return  f"""<H1> my app {name}</H1>"""

@app.route('/second', methods=['GET'])
def second():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>"""

@app.route('/justroutename',methods=['GET','POST'])
def form():
    print(request.method)
    if request.method == "POST":
        print("Yes truly there exist a post method")
        thename = request.form.get('myname')
        return render_template('form.html', thename=thename )
    return render_template('form.html')


