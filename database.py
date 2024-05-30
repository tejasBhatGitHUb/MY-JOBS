import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
load_dotenv()
def initialize_db():
    connection = psycopg2.connect(
        host=os.getenv("hostname"),
        dbname=os.getenv("database"),
        user=os.getenv("user_name"),
        password=os.getenv("pwd"),
        port=os.getenv("portnum")
    )
    cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)
    return connection,cursor
def add_job(title , location,responsibilities,requirements,salary=None,currency=None):
    return f'''INSERT INTO jobs(title,location,salary,currency,responsibilities,requirements )
                VALUES('{title}','{location}',{salary},'{currency}','{responsibilities}','{requirements}');'''


def delete_job(id):
    return f'''DELETE FROM jobs
               WHERE id={id};'''


def update_location(id, new_location):
    return f'''UPDATE jobs
               SET location='{new_location}',updated_at=CURRENT_TIMESTAMP
               WHERE id={id};'''


def update_salary(id, new_salary):
    return f'''UPDATE employee
               SET location={new_salary},updated_at=CURRENT_TIMESTAMP
               WHERE id={id};'''


def get_job(id):
    return f'''SELECT title,location,salary,currency,responsibilities,requirements FROM jobs
               WHERE id={id};'''
def get_all_jobs():
    return f'''SELECT title,location,salary,currency,responsibilities,requirements FROM jobs;'''
