from flask import Flask,render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key= "proje"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "proje"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def articles():
    cursor = mysql.connection.cursor()

    sorgu = "Select * From projetablo"

    result = cursor.execute(sorgu)

    if result > 0:
        articles = cursor.fetchall()
        return render_template("articles.html",articles = articles)
    else:
        return render_template("articles.html")


if __name__ == "__main__":
    app.run(debug=True)
