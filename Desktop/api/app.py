from flask import Flask 
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    return "Hello World!"

if __name__ =="__name__" :
  helloworld.run(host="0.0.0.0" , port=("5000") , debug=True)
