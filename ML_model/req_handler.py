from flask import Blueprint, request

present_students = Blueprint('present_students', __name__)

@present_students.route('/')
def get_present_studnets():
    # getting the arguments send in body
    args = request.get_json()
    return args