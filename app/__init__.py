"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(host="dpg-cgrpvf9mbg5e4khpshm0-a.singapore-postgres.render.com",database="todoapp_165",user="todoapp_165_user",password="qrBgQbmnKLwr68tMF7SRQVmANMSDRslh")
 
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
