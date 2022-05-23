from flask import Blueprint

present_students = Blueprint('present_students', __name__)

@present_students.route('/')
def get_present_studnets():
    return "succes"