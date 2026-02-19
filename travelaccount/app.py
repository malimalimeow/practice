import sqlite3
import json
from flask import Flask, redirect, render_template,request,session,g
from helper import get_rate
app = Flask(__name__)
app.secret_key = "super-secret"



with open("code.json","r",encoding="utf-8")as json_file:
    currency_code=json.load(json_file)

def get_db(): 
    if "db" not in g:
        g.db = sqlite3.connect("travel.db", check_same_thread=False) 
        g.db.row_factory = sqlite3.Row 
    return g.db
    
@app.teardown_appcontext
def close_db(exception): 
    db = g.pop("db", None) 
    if db is not None: 
        db.close()
        

@app.route("/",methods=["POST","GET"])
def index():
    db=get_db()
    cur=db.cursor()

    if request.method=="POST":
        if request.form.get("name"):
            name=request.form.get("name")   
            if name:
                session.clear()
                cur.execute("INSERT INTO travel(name) VALUES (?)",(name,))
                db.commit()
                session["travel_id"]=cur.lastrowid          
                return redirect("/receipt")
    
    trip=cur.execute("SELECT * FROM travel").fetchall()
    if len(trip)==0:
        trip=None
    
    return render_template("index.html",trip=trip)
        
        
    
@app.route("/receipt", methods=["POST","GET"])
def receipt():
    db=get_db()
    cur=db.cursor()

    if request.method =="POST":
        
        date=request.form.get("date")
        company=request.form.get("company")
        travel_code=request.form.get("travel_code")
        home_code=request.form.get("home_code")
        payment=request.form.get("payment")
        
        rate=get_rate(home_code,travel_code)
        travel_id = session["travel_id"]
        cur.execute("INSERT INTO receipt(travel_id, date, company, currency, rate, payment) VALUES(?,?,?,?,?,?)",(travel_id,date,company,travel_code,rate,payment))
        db.commit()
        session["receipt_id"] = cur.lastrowid
        
        return redirect("/items")
    
    return render_template("receipt.html",currency_code=currency_code, origin="",destination="")

@app.route("/items", methods=["POST","GET"])
def items():
    db=get_db()
    cur=db.cursor()

    if request.method=="POST":
        name=request.form.get("name")
        quantity=request.form.get("quantity")
        cost=request.form.get("cost")
        receipt_id = session["receipt_id"]
        cur.execute("INSERT INTO item (receipt_id,name, quantity, cost) VALUES(?,?,?,?)",(receipt_id,name,quantity,cost))
        db.commit()
        
        if request.form.get("add"):
            return redirect("/items")
        
        if request.form.get("new"):
            session.pop("receipt_id",None)
            return redirect("/")
    
    return render_template("items.html")



@app.route("/rate", methods=["POST","GET"])
def rate():
    db=get_db()
    cur=db.cursor()

    if request.method=="POST":
        origin=request.form.get("origin")
        destination=request.form.get("destination")
        amount=float(request.form.get("amount"))
        
        rate=get_rate(origin,destination)
        after_exchange=amount * rate
        symbol=currency_code[destination]
        
        session["last_o"] = origin 
        session["last_d"] = destination
        
        return render_template("rate.html",currency_code=currency_code,after_exchange=after_exchange,symbol=symbol,origin=origin,destination=destination)
    
    origin=session.get("last_o","")
    destination=session.get("last_d","")
    
    return render_template("rate.html",currency_code=currency_code,origin=origin,destination=destination)
        
@app.route("/historylist")
def historylist():
    db=get_db()
    cur=db.cursor()
    trip=cur.execute("SELECT * FROM travel").fetchall()
    if len(trip)==0:
        trip=None
    
    return render_template("historylist.html",trip=trip)
       
@app.route("/history/<int:trip_id>",methods=["GET", "POST"])  
def history(trip_id):
    db=get_db()
    cur=db.cursor()

    row=cur.execute("SELECT * FROM travel WHERE id=?",(trip_id,)).fetchone()
    travel_id=row["id"]
    trip_name=row["name"]
    
    if request.method=="POST":
        session["travel_id"]=travel_id
        return redirect("/receipt")
    
    history=cur.execute("SELECT * FROM receipt JOIN item ON receipt.id=item.receipt_id WHERE travel_id=?",(travel_id,)).fetchall()
    
    return render_template("history.html",history=history,trip_name=trip_name)
    
    
    
    
        
        
    
    
    
    

    
    
    
