from flask import Flask,render_template,request
from kural import *
import threading
app = Flask(__name__)


@app.route('/')
def something():
    return render_template('index.html')

@app.route('/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        kuralnum = request.form["Kural Number"]
        definition = kuraldefinition(kuralnum) #get definition
        thread = threading.Thread(target=kuralgrabber, args=(kuralnum,))
        thread.start()

        return render_template('index.html', tamildef=definition[0], englishdef = definition[1])


if __name__ == '__main__':
    app.run()