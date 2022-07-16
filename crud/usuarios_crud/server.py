from flask import Flask, render_template,redirect,request,session
from models.users import Usuario
from flask_app.controllers import usuarios

from flask_app import app

if __name__=="__main__":
    app.run(debug=True)