from flask import Flask, request

app = Flask(__name__)


@app.route("/") #default route
def default():
    return "<p>Type your name</p>"

#Format must be like: /addName?name=afif
@app.route("/addName", methods=['GET', 'POST']) #name function route
def addName(): 
    name = request.args.get('name') #variable to store the name from header
    return "<p style='display:inline'>Welcome </p>" + name + "<p style='display:inline'> !</p>" #demo: Welcome <name> !

if __name__ == "__main__":  #main function to run the app
    app.run(debug=True) #host = '0.0.0.0'