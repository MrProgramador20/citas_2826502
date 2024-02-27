from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from .config import Config
##crear objeto de aplicacion  
app = Flask(__name__)

#configurar el objeto flask
app.config.from_object(Config)

##crear un objeto sql
db = SQLAlchemy(app)

##objeto para migraciones
migrate =   Migrate(app, db)

##importar modelos
from .models import Paciente, Medico, Consultorio, Cita

##ejecutar el objeto
if __name__ == '__main__':
    app.run()
