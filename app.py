from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('spam_detection_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        email_text = request.form['email'] 
        prediction = model.predict([email_text])[0]
        result = "Spam" if prediction == 1 else "Ham"
        return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
