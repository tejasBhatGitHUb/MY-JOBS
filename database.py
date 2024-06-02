import os
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()
connection = psycopg2.connect(
    host="oval-fawn-9402.8nk.gcp-asia-southeast1.cockroachlabs.cloud",
    dbname="defaultdb",
    user="User",
    password="ewc1sR5I_dGSoxQA4NdzdA",
    port=26257)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


def add_job(application):
    try:
        cursor.execute(f'''INSERT INTO jobs(id,role,location,company,website,salary,currency,responsibilities,requirements,experience,email)
                    VALUES('{application['id'].strip()}',
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
        return True
    except:
        return False


def get_job(id):
    v = f'''SELECT id,role,location,company,website,salary,currency,responsibilities,requirements,created_at FROM jobs
               WHERE id='{id}';'''
    cursor.execute(v)
    x = cursor.fetchall()
    connection.commit()
    return x


def get_all_jobs():
    cursor.execute(f'''SELECT id,role,location,company,website,salary,currency,responsibilities,requirements,created_at FROM jobs;''')
    x = cursor.fetchall()
    connection.commit()
    return x


def delete_application(id,email,linkedin):
    cursor.execute(f'''DELETE  FROM applications
                           WHERE (id='{id}' AND (email='{email}' OR linkedin_url='{linkedin}'));
                        ''')
    connection.commit()


def add_application_to_db(application, id):
    try:
        name=application['name'].strip()
        email=application['email'].strip()
        linkedin=application['linkedin'].strip()
        resume=application['resume'].strip()
        if already_applied(id,email,linkedin):
            delete_application(id,email,linkedin)
        cursor.execute(f'''INSERT INTO applications(id,full_name,email,highest_education,years_of_experience,skills,linkedin_url,resume_url)
                           VALUES('{id}',
                                   '{name}',
                                   '{email}',
                                   '{application['education']}',
                                   {application['experience']},
                                   '{application['skills']}',
                                   '{linkedin}',
                                   '{resume}')''')
        connection.commit()
        return True
    except:
        connection.commit()
        return False


def is_present(id):
    cursor.execute(f'''SELECT id FROM jobs
                       WHERE id='{id}';''')
    x = cursor.fetchall()
    connection.commit()
    return True if x else False


def already_applied(id,email,linkedin):
    cursor.execute(f'''SELECT  id,applicant_id,email,linkedin_url FROM applications
                       WHERE (id='{id}' AND (email='{email}' OR linkedin_url='{linkedin}'));
                    ''')
    t = cursor.fetchall()
    connection.commit()
    return True if t else False
