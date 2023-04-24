from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
  return render_template('home.html')

# Página de login
@app.route("/login")
def login():
  return "login"

# Inicializador
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug=True)
