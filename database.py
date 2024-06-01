import os
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()
connection = psycopg2.connect(
    host=os.getenv("hostname"),
    dbname=os.getenv("database"),
    user=os.getenv("user_name"),
    password=os.getenv("pwd"),
    port=os.getenv("portnum")
)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


def add_job(application):
    cursor.execute(f'''INSERT INTO jobs(id,role,location,company,website,salary,currency,responsibilities,requirements,experience,email)
                VALUES('{application['id']}',
                        '{application['role']}',
                        '{application['location']}',
                        '{application['company']}',
                        '{application['website']}',
                        {application['salary']},
                        '{application['currency']}',
                        '{application['responsibilities']}',
                        '{application['requirements']}',
                        '{application['experience']}',
                        '{application['email']}');''')
    connection.commit()



def get_job(id):
    v=f'''SELECT id,role,location,company,website,salary,currency,responsibilities,requirements,created_at FROM jobs
               WHERE id='{id}';'''
    print(v)
    cursor.execute(v)
    x = cursor.fetchall()
    connection.commit()
    return x


def get_all_jobs():
    cursor.execute(f'''SELECT id,role,location,company,website,salary,currency,responsibilities,requirements,created_at FROM jobs
                       ORDER BY created_at DESC''')
    x = cursor.fetchall()
    connection.commit()
    return x

def add_application_to_db(application,id):
    try:
        cursor.execute(f'''INSERT INTO applications(id,full_name,email,highest_education,years_of_experience,skills,linkedin_url,resume_url)
                           VALUES('{id}',
                                   '{application['name']}',
                                   '{application['email']}',
                                   '{application['education']}',
                                   {application['experience']},
                                   '{application['skills']}',
                                   '{application['linkedin']}',
                                   '{application['resume']}')''')
        connection.commit()
        return True
    except :
        return False