from flask import Flask , render_template


from predict import predict
app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict_route():
    return predict()


if __name__ == "__main__":
    app.run(debug=True)