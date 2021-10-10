import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model1.bin'
dv_file = 'dv.bin'

##/.local/bin/jupyter-notebook
##pipenv install scikit-learn==1.0 numpy flask gunicorn
##pipenv run gunicorn --bind 0.0.0.0:9696 Homework_05:app
##sudo docker build -t homework_05 .
##sudo docker run -it --rm --entrypoint=bash homework_05
##sudo docker run -it --rm -p 9696:9696 homework_05

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)
    
with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
