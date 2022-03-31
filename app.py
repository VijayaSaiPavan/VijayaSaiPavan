
#First importing the Flask module
from flask import Flask

#Now importing the render template
from flask import render_template

#importing request module for get and post
from flask import request

# importing csv module for storing the data in csv file
import csv

app = Flask(__name__)

#routing the index page using @app.route
@app.route("/")
def index():
    title = "Introduction"
    data = {
        'title': title
    }
    # Render HTML with count variable
    return render_template("index.html", data=data)



#routing the education webpage using @app.route
@app.route("/education")
def education():
    title = "Education"
    

    #creating a variable filename and intialising the file
    filename = "education.csv"

    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file by giving filename and read method
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
     
        # extracting field names through first row
        fields = next(csvreader)
 
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
            
    data = {"title": title}
    return render_template("education.html", data=data, rows = rows)


#routing the skills page using @app.route
@app.route("/skills")
def skills():
    title = "Technical skills"
    # csv file name
    filename = "skills.csv"
    # initializing the titles and rows list
    fields = []
    rows = []
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
     
        # extracting field names through first row
        fields = next(csvreader)
 
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
            
    data = {"title": title}
    return render_template("skills.html", data=data, rows = rows)


#routing the projects page using @app.route
@app.route("/projects")
def projects():
    title = "My Projects Page"
    # csv file name
    filename = "projects.csv"
    # initializing the titles and rows list
    fields = []
    rows = []


    # reading the csv file using read method 
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
     
        # extracting field names through first row
        fields = next(csvreader)
 
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    data = {"title": title}
    return render_template("projects.html", data=data, rows=rows)


#routing the add projects page using @app.route and POST method
@app.route("/add_project", methods=['POST'])
def add_project():
    title = "Adding Project Info"
    project_name = request.form['project_name']
    project_desc = request.form['project_desc']
    tools_tech = request.form['tools_tech']
   

    # Append-adds at last
    file1 = open("projects.csv", "a")  # append mode
    

    #checking if the user entered the data or not
    if(file1.write(project_name+","+project_desc+","+tools_tech+"\n")):
        operation = 1
    else:
        operation = 0
    file1.close()
    data = {
        'title':title,
        'operation':operation
    }
    return render_template('add_project.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)