from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', \
        title="Template sample", \
        message='This is sample page.' )

@app.route('/next', methods=['GET'])
def next():
    return render_template('next.html', \
        title="Next page", \
        message="※これは、別のサンプルページです。", \
        data = ['One', 'Two', 'Three'] )

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')