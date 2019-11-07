from flask import Flask, render_template

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///msgs.db'

@app.route('/')
def index():
    return  render_template ('index.html')

@app.route('/formulario')
def formulario():
    return render_template ('formulario.html')

app.run(debug=True)


