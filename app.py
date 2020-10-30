from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hi():
    ip = '198.192.1.1/255'
    return "dello, sina"

#some text
#its ok 
#don't worry yes
#hahah
