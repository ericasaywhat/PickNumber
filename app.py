from flask import Flask, render_template, request, g, redirect
import sqlite3 as sql
import pandas as pd
import random

app = Flask(__name__)

inputNumber = ""

@app.route("/", methods=["GET", "POST"])
def main():
  global capacity
  datalist = getAvailableNames()
  # try:
  if request.method == "POST":
    capacity = request.form['capacity']
    setCapacityValue(capacity)
    # setattr(g, 'capacity', capacity)
    return render_template('index.html', capacity=capacity, datalist=datalist)
  capacity = getCapacity();
  return render_template('index.html', capacity=capacity, datalist=datalist)

  con.close()

def getNames():
  file = pd.read_csv('spec_raffle.csv')
  names = file.Name.tolist()
  return [name.strip() for name in names]

def getExistingNames():
  with sql.connect("data.db") as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, num INTEGER)')
    cur.execute('SELECT * FROM users')
    result = cur.fetchall()
    if result is None:
      return []
    else:
      return [name.strip() for name, number in result]
def getAvailableNames():
  allNames = getNames()
  usedNames = getExistingNames()
  print(usedNames)
  return [name for name in allNames if name not in usedNames]

def getCapacity():
  capacity = "None"
  with sql.connect("persistentData.db") as pd:
    pdc = pd.cursor()
    pdc.execute('CREATE TABLE IF NOT EXISTS data (name TEXT, data TEXT)')
    pdc.execute('SELECT * FROM data WHERE name=?', ("capacity",))
    result = pdc.fetchone()
    if result is None:
      return None
    else:
      name, capacity = result
      return capacity

def setCapacityValue(capacity):
  with sql.connect("persistentData.db") as pd:
    pdc = pd.cursor()
    print(capacity, "setCapacityValue")
    pdc.execute('CREATE TABLE IF NOT EXISTS data (name TEXT, data TEXT)')
    existingCapacity = getCapacity()
    if existingCapacity is not None:
      pdc.execute('UPDATE data SET data=?',(capacity,))
    else:
      pdc.execute('INSERT INTO data (name, data) VALUES (?,?)', ("capacity", capacity))
    pd.commit()

@app.route("/printNumber<string:variable>")
def printNumber(variable):
  global inputName
  global number
  print(inputName)
  return render_template('printNumber.html', name=variable, number=number)

@app.route("/setCapacity")
def setCapacity():
  capacity = getCapacity()
  # capacity = getattr(g,'capacity', None)
  # capacity = g.get('capacity', 100)
  return render_template('setCapacity.html', capacity = capacity)

@app.route("/displayNumber", methods=["POST"])
def displayNumber():
  global inputName
  global number
  datalist = getAvailableNames()
  capacity = getCapacity()
  if request.method == "POST":
    try:
      inputName = request.form['inputName']
      number = None
      msg=""
      print(datalist, ",", inputName, capacity)
      if inputName in datalist:
        with sql.connect("data.db") as con:
          cur = con.cursor()
          cur.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, num INTEGER)')
          print("here1")
          if capacity is not None:
            number, msg = getUnique(cur, int(capacity), 1)
            if number is not None:
              cur.execute('INSERT INTO users (name,num) VALUES (?,?)',(inputName,number))
            con.commit()
          else:
            number = None
            msg = "Please set capacity"
            # return render_template('displayNumber.html', name = name, number = number, msg=msg)
      else:
        number = None
        msg = "Name not found"
    except:
      con.rollback()
    finally:
      return render_template('displayNumber.html', name=str(inputName), number=number, msg=msg)
      con.close()

def getUnique(cur, capacity, index):
  number = random.randint(1, int(capacity))
  cur.execute('SELECT * FROM users WHERE num=?', (number,))
  entry = cur.fetchall()
  print(len(entry), "here4")
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
  try:
    con = sql.connect("data.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM users ORDER BY num ")

    rows = cur.fetchall();
  except:
    rows = []
    print("nope")
  finally:
    return render_template('viewTable.html', rows = rows, availableNames = getAvailableNames())

@app.route('/deleteTable')
def deleteTable():
  con = sql.connect("data.db")
  cur = con.cursor();
  cur.execute('DROP TABLE users')

  return redirect("/viewTable")
if __name__ == "__main__":
	app.run()
