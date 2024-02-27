##necesitamos sqlalchemy:
##definir los atributos de objeto
##pero con tipos a sql y mysql
from app import db
from datetime import datetime

class Medico(db.Model):
    
    __tablename__ = "medicos"
    i= db.Column(db.Integer, primary_key = True) 
    nombres = db.Column(db.String(120), nullable = True)
    apellidos  = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    registro_medico = db.Column(db.Integer)
    especialidad = db.Column(db.String(50))
    
class Paciente(db.Model):
    
    __tablename__ = "pacientes"
    i= db.Column(db.Integer, primary_key = True) 
    nombres = db.Column(db.String(120), nullable = True)
    apellidos  = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    altura = db.Column(db.Integer)
    tipo_sangre = db.Column(db.String(2))
    
class Consultorio(db.Model):
    
    __tablename__ = "consultorios"
    i= db.Column(db.Integer, primary_key = True) 
    numero = db.Column(db.Integer)
    
class Cita(db.Model):
    __tablename__ = "citas"
    i= db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    paciente_i = db.Column (db.Integer, db.ForeignKey("pacientes.i"))
    medico_i = db.Column (db.Integer, db.ForeignKey("medicos.i"))
    consultorio_i = db.Column (db.Integer, db.ForeignKey("consultorios.i"))
