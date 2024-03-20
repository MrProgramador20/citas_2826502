from . import app, db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request, flash, redirect

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
    return render_template ("consultorios.html", consultorios=consultorios )

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
    cita =  Cita.query.get(id)
    return render_template("cita.html", cit = cita)

@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    #return "id del medico" + str(id)
    consultorio =  Consultorio.query.get(id)
    return render_template("consultorio.html", con = consultorio)

#ruta para crear nuevo medico
@app.route("/medicos/create", methods = ["GET", "POST"])
def create_medico():
    if(request.method == "GET" ):
        especialidades = [
        "Cardiologia", "Pediatria", "Alergologia"
    ]
        return render_template("medico_form.html", especialidades = especialidades) 
    elif(request.method == "POST"):
        new_medico =  Medico(nombres = request.form["nombre"], apellidos = request.form["apellido"], tipo_identificacion = request.form["ti"], numero_identificacion = request.form["ni"], registro_medico = request.form["rm"], especialidad = request.form["es"]) 
        db.session.add(new_medico)
        db.session.commit()
        flash("Medico registrado correctamente")
        return redirect ("/medicos")

@app.route("/pacientes/create", methods = ["GET", "POST"])
def create_paciente():
    if(request.method == "GET" ):
        tipo_sangre = [
        "A+", "O+", "B+", "AB"
    ]
        return render_template("paciente_forms.html", tipo_sangre = tipo_sangre) 
    elif(request.method == "POST"):
        new_paciente =  Paciente(nombres = request.form["nombre"], apellidos = request.form["apellido"], tipo_identificacion = request.form["ti"], numero_identificacion = request.form["ni"], altura = request.form["alt"], tipo_sangre = request.form["ts"]) 
        db.session.add(new_paciente)
        db.session.commit()
        return "paciente registrado"
    
@app.route("/consultorios/create", methods = ["GET", "POST"])
def create_consultorio():
    if(request.method == "GET" ):
        numero = [
        "201", "301", "401", "501", "502", "402", "302", "202"
    ]
        return render_template("consultorio_forms.html", numero = numero) 
    elif(request.method == "POST"):
        new_consultorio =  Consultorio(numero = request.form["num"]) 
        db.session.add(new_consultorio)
        db.session.commit()
        return "consultorio registrado"
    
#Actualizacion y eliminacion de Medico    

@app.route("/medicos/update/<int:id>", methods = ["POST","GET"])
def update_medico(id):
    especialidades = [
        "Cardiologia", "Pediatria", "Alergologia"
    ]
    medico_update = Medico.query.get(id)
    if(request.method == "GET"):
        return render_template("medico_update.html", medico_update = medico_update, especialidades = especialidades)
    elif(request.method == "POST"):
        medico_update.nombres =  request.form["nombre"]
        medico_update.apellidos =  request.form["apellido"]
        medico_update.tipo_identificacion =  request.form["ti"]
        medico_update.numero_identificacion =  request.form["ni"]
        medico_update.registro_medico =  request.form["rm"]
        medico_update.especialidad =  request.form["es"]
        db.session.commit()
        return "Medico Actualizado"
    
@app.route("/medicos/delete/<int:id>")
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect("/medicos")

#Actualizacion y eliminacion de Paciente

@app.route("/pacientes/update/<int:id>", methods = ["POST","GET"])
def update_paciente(id):
    tipo_sangre = [
        "A+", "O+", "B+", "AB"
    ]
    paciente_update = Paciente.query.get(id)
    if(request.method == "GET"):
        return render_template("paciente_update.html", paciente_update = paciente_update , tipo_sangre = tipo_sangre)
    elif(request.method == "POST"):
        paciente_update.nombres =  request.form["nombre"]
        paciente_update.apellidos =  request.form["apellido"]
        paciente_update.tipo_identificacion =  request.form["ti"]
        paciente_update.numero_identificacion =  request.form["ni"]
        paciente_update.altura =  request.form["alt"]
        paciente_update.tipo_sangre =  request.form["ts"]
        db.session.commit()
        return "Paciente Actualizado"
    
@app.route("/pacientes/delete/<int:id>")
def delete_paciente(id):
    paciente_delete = Paciente.query.get(id)
    db.session.delete(paciente_delete)
    db.session.commit()
    return redirect("/pacientes")

#Actualizacion y eliminacion de Consultorio
@app.route("/consultorios/update/<int:id>", methods = ["POST","GET"])
def update_consultorio(id):
    numero = [
        "201", "301", "401", "501", "502", "402", "302", "202"
    ]
    consultorio_update = Consultorio.query.get(id)
    if(request.method == "GET"):
        return render_template("consultorio_update.html", consultorio_update = consultorio_update , numero = numero)
    elif(request.method == "POST"):
        consultorio_update.numero =  request.form["num"]
    db.session.commit()
    return "Consultorio Actualizado"

@app.route("/consultorios/delete/<int:id>")
def delete_consultorios(id):
    consultorio_delete = Consultorio.query.get(id)
    db.session.delete(consultorio_delete)
    db.session.commit()
    return redirect("/consultorios")

#Actualizacion y eliminacion de Citas
@app.route("/citas/update/<int:id>", methods = ["POST","GET"])
def update_cita(id):
    cita_update = Cita.query.get(id)
    if(request.method == "GET"):
        return render_template("cita_update.html", cita_update = cita_update)
    elif(request.method == "POST"):
        cita_update.fecha =  request.form["fec"]
        cita_update.paciente_id =  request.form["pid"]
        cita_update.medico_id =  request.form["mid"]
        cita_update.consultorio_id =  request.form["cid"]
        cita_update.valor =  request.form["val"]
        db.session.commit()
        return "Cita Actualizado"
    

