from flask import Flask,  render_template, request,  redirect
import sqlite3
import DB
app = Flask(__name__)

president = 0
age = 0 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def uvod():
    con = DB.open_db()
    #con.execute("DELETE from users WHERE id = 5 ")
    #con.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Miguel', 10))
    users = con.execute("SELECT * FROM users").fetchall()
    con.commit()
    con.close()
    return render_template('list.html' , users=users)
   

@app.route('/first/<int:id>/<username>')
def první(id,username):
    return render_template('1.html', id=id , username=username)

@app.route('/calculator')
def druhá():
        return render_template('2.html')


@app.route('/form',  methods=('GET', 'POST'))
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
    if request.method == "POST":
        con = DB.open_db()
        con.execute("INSERT INTO users (name, age) VALUES (?, ?)", (fname, age))
        con.commit()
        con.close()
    return render_template('form.html',title=title, age=age, fname=fname, president=president)

if __name__ == '__main__':
    app.run(debug=True)
    

