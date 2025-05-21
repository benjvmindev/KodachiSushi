from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)