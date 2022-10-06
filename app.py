from re import template
from tkinter import Button
from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
@app.route("/home")
def home ():
    return render_template("home.html")


@app.route("/jogos")
def quemsomos():
    return render_template("jogos.html")
    

@app.route("/celulares")
def contato():
    return render_template("celulares.html")

    @app.route("/jogos")
def quemsomos():
    return render_template("jogos.html")
    

@app.route("/celulares")
def contato():
    return render_template("celulares.html")

if __name__=='__main__':
    app.run(debug=True)