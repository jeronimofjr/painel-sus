from flask import Flask
from atendimentos import atendimentos_bp

app = Flask(__name__)

app.register_blueprint(atendimentos_bp, url_prefix='/api/v1/')

@app.route("/")
def home():
    return {"message" : "Painel SUS"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8001) 
