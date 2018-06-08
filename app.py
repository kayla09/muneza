
from flask import Flask , render_template
from flask_mysqldb import MySQL 

app = Flask(__name__)

# config db 
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)



@app.route('/', method=['GET', 'POST'])
def index():
    return render_template('index.html')
    if requested.method == 'POST':

        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        color = userDetails['Favorite color']
        CATS OR DOGS = userDetails['CAT OR DOG']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Users(name,favorite color, CATS OR DOGS) VALUES(%s,%s, %s)",(name, email, CATS OR DOGS))
        mysql.connection.commit()
        cur.close()
        return 'success'

@app.route("/users")
def users():
    return render_template('users')
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM USERS")
    if resultValue > 0:
       userDetails = cur.fetchall()
       return render_template('users.html',userDetails=userDetails)

@app.route('/signUp')
def signUp():
    # create user code will be here !!

if __name__ == "__main__":
    app.run(debug=True)


  

