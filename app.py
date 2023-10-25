#import flask
from flask  import Flask, render_template
from flask_mysqldb import MySQL

#main app
app = Flask (__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jeffshop' 


# init mysql

mysql = MySQL (app) 

#set route default
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/Features')
def Features():
    return render_template("Features.html")

@app.route('/brand')
def brand():
    cur = mysql.connection.cursor() 
    # eksekusi kueri
    cur.execute("Select * FROM tb_product")
    # fetch hasil kueri masukkan ke var data
    data  = cur.fetchall()
    #tutup koneksi 
    cur.close()
    return render_template("brand.html",tb_product=data)

@app.route('/login')
def login():
    return render_template("login.html")

#debug untuk automatic update server
if __name__ == "__main__":
    app.run(debug=True)