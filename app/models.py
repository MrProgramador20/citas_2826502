##necesitamos sqlalchemy:
##definir los atributos de objeto
##pero con tipos a sql y mysql
from app import db
from datetime import datetime

class Medico(db.Model):
    
    __tablename__ = "medicos"
    id= db.Column(db.Integer, primary_key = True) 
    nombres = db.Column(db.String(120), nullable = True)
    apellidos  = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    registro_medico = db.Column(db.Integer)
    especialidad = db.Column(db.String(50))
    
    citas = db.relationship('Cita' , backref = 'medico' )
    
class Paciente(db.Model):
    
    __tablename__ = "pacientes"
    id= db.Column(db.Integer, primary_key = True) 
    nombres = db.Column(db.String(120), nullable = True)
    apellidos  = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    altura = db.Column(db.Integer)
    tipo_sangre = db.Column(db.String(2))
    
class Consultorio(db.Model):
    
    __tablename__ = "consultorios"
    id= db.Column(db.Integer, primary_key = True) 
    numero = db.Column(db.Integer)
    
class Cita(db.Model):
    __tablename__ = "citas"
    id= db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    paciente_id = db.Column (db.Integer, db.ForeignKey("pacientes.id"))
    medico_id = db.Column (db.Integer, db.ForeignKey("medicos.id"))
    consultorio_id = db.Column (db.Integer, db.ForeignKey("consultorios.id"))
    
   


''' for med in medicos:
 print('nombre:'+ med.nombres + ', apellido: '+ med.apellidos + ' especialidad: '+med.especialidad)
 
 
 m = Medico(nombres = "Arnulfo", apellidos = "perez",  tipo_identificacion = "CC", numero_identificacion = 37846384, registro_medico = 37463476, especialidad = "Oncologia")
 m2 = Medico(nombres = "jhing", apellidos = "lee",  tipo_identificacion = "CC", numero_identificacion = 3876543, registro_medico = 39876, especialidad = "Odontologia")
 p1 = Paciente(nombres = "carlos", apellidos = "castro",  tipo_identificacion = "CC", numero_identificacion = 876549, altura = 150, tipo_sangre = "b+")
 p2 = Paciente(nombres = "angie", apellidos = "suarez",  tipo_identificacion = "CC", numero_identificacion = 12345, altura = 170, tipo_sangre = "a+")
 c = Consultorio(numero = 301) 
 cita1 = Cita(fecha = '2024-02-29', paciente_id = p1.id, medico_id = m.id, consultorio_id = c.id)
 cita2 = Cita(fecha = '2024-02-29', paciente_id = p2.id, medico_id = m2.id, consultorio_id = c.id)
 '''