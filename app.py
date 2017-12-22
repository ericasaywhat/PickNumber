from flask import Flask, render_template, request, g, redirect
import sqlite3 as sql
import pandas as pd
import random

app = Flask(__name__)

inputNumber = ""

@app.route("/", methods=["GET", "POST"])
def main():
  global capacity
  # datalist = getNames()
  # try:
  if request.method == "POST":
    capacity = request.form['capacity']
    setCapacityValue(capacity)
    print(capacity, "capacity")
    # setattr(g, 'capacity', capacity)
    return render_template('index.html', capacity=capacity)
  capacity = getCapacity();
  return render_template('index.html', capacity=capacity)
  # except:
  #   print("eyyy")
  #   with sql.connect("persistentData.db") as con:
  #     cur = con.cursor()
  #     cur.execute('CREATE TABLE IF NOT EXISTS data (name TEXT, data TEXT)')
  #   return redirect("/setCapacity")

  con.close()

def getNames():
  file = pd.read_csv('spec_raffle.csv')
  return file.Name.to_string()

def getCapacity():
  capacity = "None"
  with sql.connect("persistentData.db") as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS data (name TEXT, data TEXT)')
    cur.execute('SELECT * FROM data WHERE name=?', ("capacity",))
    result = cur.fetchone()
    if result is None:
      return None
    else:
      name, capacity = result
      return capacity

def setCapacityValue(capacity):
  with sql.connect("persistentData.db") as con:
    cur = con.cursor()
    print(capacity, "setCapacityValue")
    cur.execute('CREATE TABLE IF NOT EXISTS data (name TEXT, data TEXT)')
    existingCapacity = getCapacity()
    if existingCapacity is not None:
      cur.execute('UPDATE data SET data=?',(capacity,))
    else:
      cur.execute('INSERT INTO data (name, data) VALUES (?,?)', ("capacity", capacity))
    con.commit()

@app.route("/printNumber")
def printNumber():
  global inputName
  global number
  return render_template('printNumber.html', name=inputName, number=number)

@app.route("/setCapacity")
def setCapacity():
  global capacity
  capacity = getCapacity()
  print(type(capacity))
  print(capacity, "help")
  # capacity = getattr(g,'capacity', None)
  # capacity = g.get('capacity', 100)
  return render_template('setCapacity.html', capacity = capacity)

@app.route("/displayNumber", methods=["POST"])
def displayNumber():
  global capacity
  global inputName
  global number
  if request.method == "POST":
    try:
      inputName = request.form['inputName']
      number = None
      msg=""
      with sql.connect("data.db") as con:
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, num TEXT)')
        if capacity is not None:
          # print(getUnique(cur,capacity, 1))
          number, msg = getUnique(cur, int(capacity), 1)
          print (number, msg)
          cur.execute('INSERT INTO users (name,num) VALUES (?,?)',(inputName,number))
          con.commit()
        else:
          number = None
          msg = "Please set capacity"
          # return render_template('displayNumber.html', name = name, number = number, msg=msg)
    except:
      con.rollback()
    finally:
      return render_template('displayNumber.html', name=str(inputName), number=number, msg=msg)
      con.close()

def getUnique(cur, capacity, index):
  number = random.randint(1, int(capacity))
  cur.execute('SELECT * FROM users WHERE num=?', (number,))
  entry = cur.fetchall()
  while len(entry) != 0:
    number = random.randint(1, int(capacity))
    cur.execute('SELECT * FROM users WHERE num=?', (number,))
    entry = cur.fetchall()
    index += 1
    if index > capacity:
      return None, "Capacity Reached"
    # getUnique(cur, capacity, index+1)
  return number, "Record successfully added"


@app.route('/viewTable')
def viewTable():
  global capacity
  try:
    con = sql.connect("data.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from users")

    rows = cur.fetchall();
  except:
    rows = []
    print("nope")
  finally:
    return render_template('viewTable.html', rows = rows)

@app.route('/deleteTable')
def deleteTable():
  con = sql.connect("data.db")
  cur = con.cursor();
  cur.execute('DROP TABLE users')

  return redirect("/viewTable")
if __name__ == "__main__":
	app.run()
