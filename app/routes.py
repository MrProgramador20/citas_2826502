from . import app, db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request

#crear ruta para medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template ("medicos.html", medicos=medicos )

@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template ("pacientes.html", pacientes=pacientes )

@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template ("consultorio.html", consultorios=consultorios )

@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template ("citas.html", citas=citas )

#crear ruta medicos por id (get)
@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template("medico.html", med = medico) 

@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    #return "id del medico" + str(id)
    paciente = Paciente.query.get(id)
    return render_template("paciente.html", pac = paciente)

@app.route("/citas/<int:id>")
def get_cita_by_id(id):
    #return "id del medico" + str(id)
    cita = Cita.query.get(id)
    return render_template("cita.html", cit = cita)

#ruta para crear nuevo medico
@app.route("/medicos/create", methods = ["GET", "POST"])
def create_medico():
    if(request.method == "GET" ):
        especialidades = [
        "Cardiologia", "Pediatria", "Alergologia"
    ]
        return render_template("medico_form.html", especialidades = especialidades) 
    elif(request.method == "POST"):
         request.form["es"]
    elif(request.method == "POST"):
        new_medico =  Medico(nombre = request.form["nombre"], apellido = request.form["apellido"], tipo_identificacion = request.form["ti"], numero_identificacion = request.form["ni"], registro_medico = request.form["rm"], especialidad = request.form["es"])
        db.session.add(new_medico)
        db.session.commit()
        return "medico registrado"


