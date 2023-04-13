"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect("postgres://todoapp_165_user:qrBgQbmnKLwr68tMF7SRQVmANMSDRslh@dpg-cgrpvf9mbg5e4khpshm0-a/todoapp_165")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
