from flask import Flask, render_template, jsonify, request

from database import get_job, get_all_jobs, add_application_to_db, add_job, is_present

app = Flask(__name__, template_folder="template")


@app.route("/")
def start():
    JOBS = get_all_jobs()[::-1]
    return render_template('home.html',
                           jobs=JOBS
                           )


@app.route('/jobs/<id>')
def display_job(id):
    try:
        temp = get_job(id)
        return render_template('jobpage.html', job=temp[0])
    except:
        return render_template('ERROR_page.html', message1="Something went wrong!",
                               message2="Encountered an unexpected ERROR while fetching your data.")


@app.route('/jobs/<id>/apply')
def apply_for_job(id):
    try:
        return render_template('application_form.html', job=get_job(id)[0])
    except:
        return render_template('ERROR_page.html')


@app.route('/jobs/<id>/apply/submission', methods=['POST', 'GET'])
def form_submission(id):
    try:
        application = request.form
        print(add_application_to_db(application, id))
        return render_template('application_submitted.html', application=application)
    except:
        return render_template('ERROR_page.html', message1="Something Went Wrong!",
                               message2="We're sorry, but something went wrong while processing your request. Please try again later.")


@app.route("/job-posting/submission", methods=["POST", "GET"])
def job_opening_submission():
    application = request.form
    if is_present(application['id'].strip()):
        return render_template('ERROR_page.html', message1="Job Posting Status",
                               message2="You have already posted this job.")
    add_job(application)
    return render_template("job_posting_confirmation.html", application=application)


@app.route('/job-posting')
def post_a_job():
    return render_template('job_posting_application.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
