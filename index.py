# file name : index.py
# pwd : /project_name/app/main/index.py
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
main = Blueprint('main', __name__, url_prefix='/')
@main.route('/main', methods=['GET'])
def std_weight(height, gender):
    m_weight = height*height*22*0.01*0.01
    m_weight = round(m_weight, 2)
    f_weight = height*height*21*0.01*0.01
    f_weight = round(f_weight, 2)
    if gender == "male":
        print("gender : {0}, height : {1}cm, standard weight : {2}kg" .format(
            gender, height, m_weight))
    elif gender == "female":
        print("gender : {0}, height : {1}cm, standard weight : {2}kg" .format(
            gender, height, f_weight))
    return gender, height, f_weight, m_weight

gender = input("Your gender? : ")
height = int(input("Your height? : "))
std_weight(height, gender)
return render_template('/main/index.html', genderh=gender)