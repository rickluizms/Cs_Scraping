from app.controller import Controller
from config.connnection import connection

control = Controller(connection)

data = control.Extract()
transf_data = control.Trasnform(data)
control.Load(transf_data)