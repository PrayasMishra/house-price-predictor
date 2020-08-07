from flask import Flask, request, jsonify,render_template
import util

app = Flask(__name__,template_folder='client')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['squareft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    #return 'total sqft : '+str(total_sqft)+'Location : '+str(location)+'BHK : '+str(bhk)+'bath : '+str(bath)

    
    return str(util.get_estimated_price(location,total_sqft,bhk,bath)[0])

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_model()
    app.run()