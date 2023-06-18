from app.controller import Controller
from config.sources import sources

nesha = sources['Nesha']

control = Controller(nesha)

data = control.Extract()
transf_data = control.Transform(data)
control.Load(transf_data)