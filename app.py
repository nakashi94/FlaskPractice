from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', \
        title="Template sample", \
        message='This is sample page.' )

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')