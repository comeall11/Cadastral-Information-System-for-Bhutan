# Required packages for the application
import os
import json
import jinja2
import psycopg2
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

###------INDEX PAGE-----------####

# Defining the path for Images used in the page


image_folder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = image_folder

# PostgresSQL database connection


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="esakor",
        user='postgres',
        password='1111')
    return conn

# Function to load the index page


@app.route('/')
@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'mainimage.jpeg')
    developer = os.path.join(app.config['UPLOAD_FOLDER'], 'developerse.png')
    nova_logo = os.path.join(app.config['UPLOAD_FOLDER'], 'NOVA_IMS_Logo.png')
    return render_template("index.html", user_image=full_filename, developers=developer, NOVA_IMS_Logo=nova_logo)

# Function to create the charts of no. of thrams vs districts under the Overview button


@app.get('/thramchart')
def homepage():
    conn = get_db_connection()
    cur = conn.cursor()
    df = cur.execute(
        "SELECT adescr, count(cthram) FROM vthram group by adescr")
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

# Function to create the charts of no. of plots vs districts under the Overview button


@app.get('/plotchart')
def homepage1():
    conn = get_db_connection()
    cur = conn.cursor()
    df = cur.execute(
        "SELECT district, sum(plot_area) FROM vparcel group by district")
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
# Function to create the charts of area of land type vs districts under the Overview button


@app.get('/landtypechart')
def homepage2():
    conn = get_db_connection()
    cur = conn.cursor()
    df = cur.execute(
        "SELECT fdescr, sum(etosarea) FROM vthram group by fdescr")
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

###------END OF INDEX PAGE-----------####

###------Search By Thram Page-----------####

# Function to retrive the list of districts and pust to the html form for the option


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

# Function to retrive the list of Gewogs(Subdistrict) based on the user inputed district_id and pust to the html form for the option


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

# Function to retrive the list of Thrams(Title) based on the user inputeed district_if and Gewog_id and pust to the html as options


@app.route("/get_thram", methods=["POST", "GET"])
def get_thram():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        gewog_id = request.form['gewog_id']
        print("hello motto")
        print(gewog_id)
        cur.execute(
            "SELECT cgewog,cthram,cvillage,cownname FROM thram WHERE cgewog = %s", [gewog_id])
        tharms = cur.fetchall()
        print(tharms)
    return jsonify({'htmlresponse': render_template('tharm.html', tharm=tharms)})

# Function to retrive the list of plots based on the user inputted district_id, gewog_id and thram_id and return the data for mapping


@app.route("/plot_thram", methods=["POST", "GET"])
def plot_thram():
    conn = get_db_connection()
    cur = conn.cursor()
    toplots = []
    if request.method == 'POST':
        tharm_id = request.form['tharm_id']
        thram_gewog = request.form['cgewog']
        print("hello")
        print(tharm_id)
        print(thram_gewog)
        cur.execute(
            "SELECT * FROM vparcel WHERE subdist_id = %s AND sheet_id = %s", (thram_gewog, tharm_id))
        toplots = cur.fetchall()
        plots = {
            "type": "FeatureCollection",
            "features": [],
            "property": {
                "name": "Thrams",
                "id": tharm_id
            }
        }
        for row in toplots:
            plots["features"].append({
                "type": "Feature",
                "geometry": json.loads(row[13]),
                "property": {
                    "district": row[0],
                    "district_id": row[1],
                    "subdist_id": row[2],
                    "sub_district": row[3],
                    "thram_no": row[4],
                    "owner_id": row[5],
                    "owner_name": row[6],
                    "tenure_type": row[7],
                    "village_name": row[8],
                    "plot_id": row[9],
                    "plot_name": row[10],
                    "plot_area": row[11],
                    "land_use": row[12],
                }
            })
        print(toplots)
        return jsonify(plots)

###------End Search By Thram Page-----------####

###------Search by Plor Id PAGE-----------####


# Function to redirect to the search by plot_id page


@app.get('/plotid')
def plot():
    return render_template('plot.html')

# Function to receive the input plot id from the frontend, search from the database and return back to the frontend to map and display


@app.post('/plot')
def get_plotid():
    conn = get_db_connection()
    cur = conn.cursor()
    plot = []
    if request.method == 'POST':
        Plot_id = request.form['plot_id']
        cur.execute(
            "SELECT * FROM vparcel WHERE plot_id = %s", [Plot_id])
        plot = cur.fetchall()
        print(plot)
    return render_template('mapplot.html', Plot=plot)

###------End of Search by Plor Id PAGE-----------####


if __name__ == "__main__":

    app.run(debug=True)
