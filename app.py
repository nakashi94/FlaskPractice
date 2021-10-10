from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = ["One", "Two", "Three"]
    person = {'name':'Taro', 'mail':'taro@yamada'}
    return render_template('jinja.html', \
        title="Template sample", \
        message='This is sample message.', \
        data=data, \
        person=person )

# @app.route('/', methods=['POST'])
# def form():
    # field = request.form['field']
    # ck = request.form.get('check')
    # rd = request.form.get('radio')
    # sel = request.form.getlist('sel')
    # return render_template('index.html', \
        # title="Form sample", \
        # message=[field, ck, rd, sel])

# @app.route('/<id>/<password>')
# def index2(id, password):
    # msg = 'id: %s, password: %s' % (id, password)
    # return render_template('index.html', \
        # title="Index with Jinja", \
        # message=msg)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')