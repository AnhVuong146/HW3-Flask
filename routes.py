from flask import flash, request
from flask import redirect, render_template, url_for
from app import myapp_obj

@myapp_obj.route("/", methods=("POST", "GET"))
def home():     
    name = "Lisa"
    req = request.form
    city_names = ["Paris", "London", "Rome", "Tahiti"]
    user_input = input
    if request.method == "POST":  
        flash(f"{user_input}")
        return redirect(url_for('home'))

    return render_template('home.html', name = name, city_names = city_names, req = req)