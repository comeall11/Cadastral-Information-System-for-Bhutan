import os
import json
import jinja2
import psycopg2
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#DB connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="esakor",
        user='postgres',
        password='yeshey010')
    return conn

# created app to point to plot html through server api
@app.get('/plotid')
def plot():
    return render_template('plot.html')

#App for plotid post from the user end using plot.html
@app.post('/plot')
def get_plotid():
    conn = get_db_connection()
    cur = conn.cursor()
    eplotid = request.form['plot_id'] # "NAJ-3101" 
    print(eplotid)
    cur.execute(
        "SELECT * FROM vthram WHERE eplotid = %s", [eplotid])
    plot = cur.fetchall()
    print(plot)
    return jsonify(plot) 

# Displaying Index welcome image app 
image_folder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = image_folder
@app.route('/')
@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'mainimage.jpeg')
    return render_template("index.html", user_image = full_filename)

#chart app for Thram holders
@app.get('/thramchart')
def homepage():     
#db connector
    def get_db_connection():
        conn = psycopg2.connect(
        host="localhost",
        database="esakor",
        user='postgres',
        password='yeshey010')
        return conn

    #engine = create_engine("postgresql:///?User=postgres&;Password=postgres&Database=esakor&Server=127.0.0.1&Port=5432")
    conn = get_db_connection()
    cur = conn.cursor()
    df=cur.execute("SELECT adescr, count(cthram) FROM vthram group by adescr")
    print(df)

# stroing into different ARRAY/ list for bargraphs
    District = []
    Thrams = []

    for i in cur:
        District.append(i[0])
        Thrams.append(i[1])
	
    print("Name of District = ", District)
    print("Number of Thrams = ", Thrams)

	# Return the components to the HTML template
    return render_template(
		template_name_or_list='thramchart.html',
		data=Thrams,
		labels=District,
	)

#chart app for Plot districtwise
@app.get('/plotchart')
def homepage1():     
#db connector
    def get_db_connection():
        conn = psycopg2.connect(
        host="localhost",
        database="esakor",
        user='postgres',
        password='yeshey010')
        return conn

    #engine = create_engine("postgresql:///?User=postgres&;Password=postgres&Database=esakor&Server=127.0.0.1&Port=5432")
    conn = get_db_connection()
    cur = conn.cursor()
    df=cur.execute("SELECT adescr, sum(etosarea) FROM vthram group by adescr")
    print(df)

# stroing into different ARRAY/ list for bargraphs
    District = []
    plotA = []
    
    for i in cur:
        District.append(i[0])
        plotA.append(i[1])
	
    print("Name of District = ", District)
    print("Total Area = ", plotA)
    
	# Return the components to the HTML template
    return render_template(
		template_name_or_list='plotchart.html',
		data=plotA,
		labels=District,
	)


#chart app for Landtype
@app.get('/landtypechart')
def homepage2():     
#db connector
    def get_db_connection():
        conn = psycopg2.connect(
        host="localhost",
        database="esakor",
        user='postgres',
        password='yeshey010')
        return conn

    #engine = create_engine("postgresql:///?User=postgres&;Password=postgres&Database=esakor&Server=127.0.0.1&Port=5432")
    conn = get_db_connection()
    cur = conn.cursor()
    df=cur.execute("SELECT fdescr, sum(etosarea) FROM vthram group by fdescr")
    print(df)

# stroing into different ARRAY/ list for bargraphs
    Landtype = []
    TArea = []
    
    for i in cur:
        Landtype.append(i[0])
        TArea.append(i[1])
	
    print("Landtype = ", Landtype)
    print("Total Area = ", TArea)
    
	# Return the components to the HTML template
    return render_template(
		'landtypechart.html',
		data=TArea,
		labels=Landtype,
	)


#Search by Thram part

@app.route('/district')
def get_district():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT adzongkhag, adescr FROM district')
    districts = cur.fetchall()
    cur.close()
    conn.close()
    print(districts)
    return render_template('searchthram.html', edistricts=districts)


@app.route("/get_gewog", methods=["POST", "GET"])
def get_gewog():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        district_id = request.form['district_id']
        print(district_id)
        cur.execute(
            "SELECT bgewog,bdescr FROM block WHERE bdzongkhag = %s", [district_id])
        gewogs = cur.fetchall()
        print(gewogs)
    return jsonify({'htmlresponse': render_template('gewog.html', gewog=gewogs)})


@app.route("/get_thram", methods=["POST", "GET"])
def get_thram():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        gewog_id = request.form['gewog_id']
        print("hello motto")
        print(gewog_id)
        cur.execute(
            "SELECT cgewog,cthram,cvillage FROM thram WHERE cgewog = %s", [gewog_id])
        tharms = cur.fetchall()
        print(tharms)
    return jsonify({'htmlresponse': render_template('tharm.html', tharm=tharms)})


@app.route("/plot_thram", methods=["POST", "GET"])
def plot_thram():
    conn = get_db_connection()
    cur = conn.cursor()
    toplots = []
    if request.method == 'POST':
        tharm_id = request.form['tharm_id']
        print("hello")
        print(tharm_id)
        cur.execute(
            "SELECT * FROM vparcel WHERE sheet_id = %s", [tharm_id])
        toplots = cur.fetchall()
        for row in toplots:
            district = str(row[0])
            district_id = row[1]
            subdist_id = row[2]
            sub_district = str(row[3])
            sheet_no = row[4]
            village_name = str(row[5])
            own_id = row[6]
            owner_name = str(row[7])
            tenure_type = str(row[8])
            plot_id = str(row[9])
            plot_name = str(row[10])
            plot_area = row[11]
            land_use = str(row[12])
            geometry = str(row[13])
            geojson = geometry
            print(geojson)
        """ return jsonify(geometry) """
        return render_template('map.html', data=geojson)

@app.route("/map")
def showmap():
    parcel = plot_thram().get_json()
    return render_template('map.html', geojson=parcel)


if __name__ == "__main__":
    
    app.run(debug=True)
