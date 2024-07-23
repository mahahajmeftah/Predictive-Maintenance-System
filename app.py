from flask import Flask, render_template, request
from Predictive_Maintenance.pipelines.prediction import Prediction

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            type_value = request.form["type_value"]
            rpm = float(request.form['rpm'])
            torque = float(request.form['torque'])  # Fixed typo in 'torque'
            tool_wear = float(request.form['tool_wear'])
            air_temp = float(request.form['air_temp'])
            process_temp = float(request.form['process_temp'])
            
            predictor = Prediction()
            result = predictor.predict(type_value, rpm, torque, tool_wear, air_temp, process_temp)

            return render_template("predict.html", result=result)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something went wrong', 400
    else:
        # For GET requests, just render the form without any result
        return render_template("predict.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)