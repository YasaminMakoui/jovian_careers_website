from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'Data Analyst',
    'location':'Tehran,Iran',
    'salary':'50000£' },
    {'id':2,
    'title': 'Data Scientist',
    'location':'Tehran,Iran',
    'salary':'60000£'},
    {'id':3,
    'title': 'Front-end Engineer',
    'location':'Remote',
    'salary':'40000£'},
    {'id':4,
    'title': 'Backend Engineer',
    'location':'Tehran,Iran',
    'salary':'60000£'}
]
@app.route("/")

def hello_world():
  return render_template("home.html", jobs=JOBS)





if __name__ == "__main__":
  app.run(host='0.0.0.0' , debug = True)
