from flask import Flask, render_template, request
from joblib import load
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
import numpy as np

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    request_type = request.method

    if request_type == 'GET':
        return render_template('index.html')
    else:
        entered = request.form['entered_job']
        model_in = load('model.joblib')
        prediction = str(model_in.predict([str(entered)])) if entered != "" else "N/A"
        return '''
        {stay}
        <div class="alert alert-success" role="alert" style="width: 95%; text-align: center; font-size: 20pt; margin-top:10px; margin-left: auto; margin-right: auto;">{entered}: {prediction}</div>
        '''.format(stay=render_template('index.html'), prediction=prediction.strip('[]'), entered=entered.upper()) if prediction != 'N/A' else '''
        {stay}
        <div class="alert alert-danger" role="alert" style="width: 95%; text-align: center; font-size: 20pt; margin-top:10px; margin-left: auto; margin-right: auto;">Please enter the job title to predict the industry</div>
        '''.format(stay=render_template('index.html'))

if __name__ == "__main__":
    app.run()