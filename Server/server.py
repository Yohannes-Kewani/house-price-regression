from flask import Flask,request, jsonify
import util
# create flask app
app= Flask(__name__)
# step 2 define route
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({'locations': util.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/predict_home_price', methods=['GET','POST'])
def predict_house_price():
   total_sqft = float(request.form['total_sqft'])
   location = request.form['location']
   bath = int(request.form['bath'])
   bhk = int(request.form['bhk'])

   response = jsonify({'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)})

   response.headers.add('Access-Control-Allow-Origin', '*')
   return response
# step 3 run the app
if __name__ == '__main__':
    print("Starting Python Flask server for home price prediction...")
    util.load_saved_artifacts()
    app.run()
    