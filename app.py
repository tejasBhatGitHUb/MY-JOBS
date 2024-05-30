from flask import Flask, render_template,jsonify
from Employee_database import get_job,delete_job,update_location,update_salary,add_job,initialize_db,get_all_jobs


connection,cursor=initialize_db()
app = Flask(__name__, template_folder="template")

def load_jobs():
    cursor.execute(get_all_jobs())
    temp=cursor.fetchall()
    connection.commit()
    return temp
@app.route("/")
def start():
    JOBS=load_jobs()
    print(JOBS)
    return render_template('home.html',
                           jobs=JOBS
                           )
@app.route("/add")
def create():
    cursor.execute(add_job(title="Backend Developer" , location="Bengaluru",responsibilities="Manage and build REST API",requirements="Flask,PostgreSQL,Python",salary=1000000,currency="Rs")
)
    connection.commit()
    return "CREATED!!!!"
@app.route('/delete')
def delete():
    cursor.execute(delete_job(id=1))
    connection.commit()
    return "DELETED"
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5000)