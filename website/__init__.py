import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
from flask import Flask, render_template, make_response, send_from_directory, g
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template
from distutils.log import error
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for, abort)
from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db, db_insert, db_fetch, db_fetch_dict
import os

from dateutil.relativedelta import relativedelta
from flask_mobility.decorators import mobile_template
import time
import pandas as pd


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config["MAX_CONTENT_LENGTH"] = 120 * 1024 * 1024
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'website.sqlite'))
    Mobility(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # host sitemap
    @app.route('/sitemap', methods=["GET"])
    def sitemap():
        template = render_template('sitemap.xml')
        response = make_response(template)
        response.headers['ContentType'] = 'application/xml'
        return response

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.route("/")
    @mobile_template('home/home.html')
    def home(template):
        return render_template(template)
    
    
    @app.route("/form1", methods=('GET', 'POST'))
    @mobile_template('home/form1.html')
    def form1(template):

        if not g.user:
            return redirect(url_for('auth.google_login'))
        if request.method=='POST':
            user_id = g.user[0]
            num = request.form['num']
            gender = request.form['gender']
            college = request.form['college']
            insta = request.form['insta']
            f1 = request.form['f1']
            f2 = request.form['f2']
            reco = request.form.getlist('reco')
            reco = ",".join(reco)
            
            q1 = request.form['q1']
            q2 = request.form['q2']
            q3 = request.form['q3']
            q4 = request.form['q4']
            q5 = request.form['q5']
            q6 = request.form['q6']
            q7 = request.form['q7']
            q8 = request.form['q8']
            q9 = request.form['q9']
            q10 = request.form['q10']

            E = int(q1)*20 + 100 - int(q6)*20
            A = 100 - int(q2)*20 + int(q7)*20
            C = int(q3)*20 + 100 - int(q8)*20
            N = int(q4)*20 + 100 - int(q9)*20
            O = int(q5)*20 + int(q10)*20
            
            db_connection = get_db()
            db = db_connection.cursor()
            db.execute("UPDATE `cult` SET `num`=%s, `gender`=%s, `college`=%s, `insta`=%s, `f1`=%s, `f2`=%s, `reco`=%s, `E`=%s, `A`=%s, `C`=%s, `N`=%s, `O`=%s WHERE `id`=%s",(num, gender, college, insta, f1, f2, reco, E, A, C, N, O, user_id))
            db_connection.commit()
            flash("Your Password has been changed", "success")
        return render_template(template)
    
    @mobile_template('home/form2.html')
    def form2(template):

        if not g.user:
            return redirect(url_for('auth.google_login'))

        if request.method=='POST':
            q1 = request.form['q1']
            q2 = request.form['q2']
            q3 = request.form['q3']
            q4 = request.form['q4']
            q5 = request.form['q5']

            E = int(q1)*5/5
            A = 100 - int(q2)*5/5
            C = int(q3)*5/5
            N = int(q4)*5/5
            O = int(q5)*5/5
        return render_template(template)
    
    @app.route("/form3", methods=('GET', 'POST') )
    @mobile_template('home/form3.html')
    def form3(template):
        if not g.user:
            return redirect(url_for('auth.google_login'))
        
        if request.method=='POST':
            q1 = request.form['q1']
            q2 = request.form['q2']
            q3 = request.form['q3']
            q4 = request.form['q4']
            q5 = request.form['q5']

            E = int(q1)*20
            A = int(q2)*20
            C = 100 - int(q3)*20
            N = int(q4)*20
            O = int(q5)*20
        return render_template(template)
    
    @app.route("/form4", methods=('GET', 'POST') )
    @mobile_template('home/form4.html')
    def form4(template):

        if not g.user:
            return redirect(url_for('auth.google_login'))
        
        if request.method=='POST':
            q1 = request.form['q1']
            q2 = request.form['q2']
            q3 = request.form['q3']
            q4 = request.form['q4']
            q5 = request.form['q5']

            E = 100 - int(q1)*20
            A = int(q2)*20
            C = 100 - int(q3)*20
            N = 100 - int(q4)*20
            O = int(q5)*20
        return render_template(template)
    
    @app.route("/form5", methods=('GET', 'POST') )
    @mobile_template('home/form5.html')
    def form5(template):

        if not g.user:
            return redirect(url_for('auth.google_login'))
        
        if request.method=='POST':
            q1 = request.form['q1']
            q2 = request.form['q2']
            q3 = request.form['q3']
            q4 = request.form['q4']
            q5 = request.form['q5']

            E = int(q1)*20
            A = 100 - int(q2)*20
            C = int(q3)*20
            N = int(q4)*20
            O = int(q5)*20
        return render_template(template)
    
    @app.route("/form6", methods=('GET', 'POST') )
    @mobile_template('home/form6.html')
    def form6(template):

        if not g.user:
            return redirect(url_for('auth.google_login'))
        
        if request.method=='POST':
            q1 = request.form['q1']
            q2 = request.form['q2']
            q3 = request.form['q3']
            q4 = request.form['q4']
            q5 = request.form['q5']

            E = 100 - int(q1)*20
            A = int(q2)*20
            C = int(q3)*20
            N = 100 - int(q4)*20
            O = 100 - int(q5)*20
        return render_template(template)
    
    @app.route("/form7", methods=('GET', 'POST') )
    @mobile_template('home/form7.html')
    def form7(template):

        if not g.user:
            return redirect(url_for('auth.google_login'))
        
        if request.method=='POST':
            q1 = request.form['q1']
            q2 = request.form['q2']
            q3 = request.form['q3']
            q4 = request.form['q4']
            q5 = request.form['q5']

            E = int(q1)*20
            A = 100 - int(q2)*20
            C = int(q3)*20
            N = int(q4)*20
            O = int(q5)*20
        return render_template(template)
    
    
    @app.route("/form8", methods=('GET', 'POST') )
    @mobile_template('home/form8.html')
    def form8(template):

        if not g.user:
            return redirect(url_for('auth.google_login'))
        
        if request.method=='POST':
            q1 = request.form['q1']
            q2 = request.form['q2']
            q3 = request.form['q3']
            q4 = request.form['q4']
            q5 = request.form['q5']
            q6 = request.form['q6']

            E = int(q1)*20
            A = 100 - int(q2)*20
            C = int(q3)*20
            N = int(q4)*20
            O = int(q5)*20
        return render_template(template)
    
    

    @app.route("/form/check")
    @mobile_template('home/form.html')
    def formcheck(template):
        if not g.user:
            return redirect(url_for('auth.google_login'))
        SHEET_ID = '1zH9rS4lvhpRZcfvgQsRwK3YK2_2i2G8OLIhq9DSa3tk'
        SHEET_NAME = 'Form Responses 1'
        url = 'https://docs.google.com/spreadsheets/d/1zH9rS4lvhpRZcfvgQsRwK3YK2_2i2G8OLIhq9DSa3tk'
        df = pd.read_csv(url, on_bad_lines='skip')
        print(df.iloc[1])
        row = df[df.values  == g.user['email']]
        return render_template(template)
    # user authentication
    from . import auth
    app.register_blueprint(auth.bp)


    return app

app = create_app()
