from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
    'id': 1,
    'title': 'Data Scientist',
    'location': 'New York',
    'salary': '$100,000'
}, {
    'id': 2,
    'title': 'Data Analysis',
    'location': 'New India',
    'salary': '$100,000'
}, {
    'id': 3,
    'title': 'PHP Developer',
    'location': 'Kanpur',
    'salary': '$100,000'
},{
     'id': 4,
     'title': 'Java Developer',
     'location': 'Lucknow',
     'salary': '$10000'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def job_list():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
