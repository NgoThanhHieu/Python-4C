from flask import Flask,  render_template
from flask import request

app = Flask(__name__)

messages = [{'title': 'Prezidentos',
             'content': ' '},]
president = 0
age = 0 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uvod')
def uvod():
    return render_template('uvod.html')

@app.route('/first/<int:id>/<username>')
def první(id,username):
    return render_template('1.html', id=id , username=username)

@app.route('/second')
def druhá():
        return render_template('2.html', messages=messages)

@app.route('/form',  methods=["POST"])
def třetí( age=None, fname=None, president=None):
    if request.method == "POST":
        fname = request.form.get("fname")
        age = (int(request.form.get("age")))  
    if age > 39:
        title = "Mužeš být prezidentem"
    else:
        president = 40 - age
        president = president + 2023
        title = "Mužeš být prezidentem až v roce " + str(president)
    return render_template('form.html',title=title, age=age, fname=fname, president=president)

@app.route('/fourth')
def čtvrtá():
    return render_template('4.html')
@app.route('/fifth')
def patá():
    return render_template('5.html')

if __name__ == '__main__':
    app.run(debug=True)
