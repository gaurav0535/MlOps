from flask import Flask

app = Flask(__name__)

# API endpoints

@app.route('/', methods=['GET'])
def anything():
    # this func will automatically execute
    return "<h1> Hello there.!! </h1>"

@app.route('/ping', methods=['GET'])
def ping():
    return {"message": "Why are you pining me?"}