from flask import Flask, render_template, request, session, url_for, redirect
from flask.views import MethodView
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    n = random.randrange(5, 10)
    data = []
    for N in range(n):
        data.append(random.randrange(0, 100))
    return render_template('index.html', \
        title="Template sample", \
        message='※合計を計算する：', \
        data=data )

@app.route('/next', methods=['GET'])
def next():
    return render_template('next.html', \
        title="Next page", \
        message="※これは、別のサンプルページです。", \
        data = ['One', 'Two', 'Three'] )

@app.template_filter('sum')
def sum_filter(data):
    total = 0
    for item in data:
        total += item
    return total

app.jinja_env.filters['sum'] = sum_filter

@app.context_processor
def sample_processor():
    def total(n):
        total = 0
        for i in range(n+1):
            total += i
        return total
    return dict(total=total)

app.secret_key = b'random string...'

class HelloAPI(MethodView):
    send = ''

    def get(self):
        if 'send' in session:
            msg = 'send:' + session['send']
            send = session['send']
        else:
            msg = '何か書いてください。'
            send = ''
        return render_template('next.html', \
            title='Next page', \
            message=msg, \
            send=send )

    def post(self):
        session['send'] = request.form['send']
        return redirect('/hello/')

app.add_url_rule('/hello/', view_func=HelloAPI.as_view('hello'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')