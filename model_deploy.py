from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('Model1.pk1', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        feature = [float(i) for i in request.form.values()]
        feature = [np.array(feature)]
        y_pred = model.predict(feature)

    return render_template('index.html', predict_Attrition=" Attrition : {}".format(y_pred))


if __name__ == '__main__':
    app.run(debug=True)
