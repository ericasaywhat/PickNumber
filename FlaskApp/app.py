from flask import Flask, render_template, request
import sqlite3 as sql
import random

app = Flask(__name__)

@app.route("/")
def main():
  return render_template('index.html')

@app.route("/displayNumber", methods=["POST"])
def displayNumber():
  if request.method == "POST":
    try:
      inputName = request.form['inputName']
      print(inputName, "help")
      number = random.randint(1, 100)
      with sql.connect("data.db") as con:
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, num TEXT)')
        cur.execute('INSERT INTO users (name,num) VALUES (?,?)',(inputName,number))
        con.commit()
        msg = "Record successfully added"
    except:
      con.rollback()
      msg = "error in insert operation"

    finally:
      return render_template('displayNumber.html', name=inputName, number=number, msg=msg)
      con.close()


@app.route('/viewTable')
def viewTable():
  con = sql.connect("data.db")
  con.row_factory = sql.Row

  cur = con.cursor()
  cur.execute("select * from users")

  rows = cur.fetchall();
  return render_template('viewTable.html', rows = rows)

if __name__ == "__main__":
	app.run()
