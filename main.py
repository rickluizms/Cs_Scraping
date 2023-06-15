from app.controller import Controller


control = Controller()

data = control.Extract()
transf_data = control.Trasnform(data)
control.Load(transf_data)