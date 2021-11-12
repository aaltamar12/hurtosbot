from flask import Flask, render_template, request
from teachBot import startTraining, BOSEH
from training import newTraining

app = Flask(__name__)

startTraining()
		
@app.route('/training')
def training():
   return  render_template("training.html")

@app.route('/')
def hello_world():
   return  render_template("index.html")


@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	
	return BOSEH(userText)

@app.route('/add',methods=['POST'])
def add():
    if request.method=='POST':
        tag = request.form['tag']
        patrones = request.form.getlist('patron[]')
        respuestas = request.form.getlist('respuesta[]')
        newTraining(tag, patrones, respuestas)
        return render_template("index.html")

if __name__ == "__main__":
	#app.run(host="0.0.0.0", port="80")
    app.run()