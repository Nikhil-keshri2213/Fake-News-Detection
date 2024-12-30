from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load pre-trained model and initialize TF-IDF vectorizer
tfvect = TfidfVectorizer(stop_words='english', max_df=0.7)
loaded_model = pickle.load(open('model.pkl', 'rb'))

# Load and preprocess data
true_data = pd.read_csv('True.csv')
false_data = pd.read_csv('Fake.csv')

true_data['class'] = 1
false_data['class'] = 0

data_merge = pd.concat([true_data, false_data], axis=0)
data = data_merge.drop(['title', 'subject', 'date'], axis=1)
data.reset_index(drop=True, inplace=True)

x = data['text']
y = data['class']

# Split the data for training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Fit the TF-IDF vectorizer on the training data
tfid_x_train = tfvect.fit_transform(x_train)

def fake_news_det(news):
    """Predict if the given news is fake or real."""
    input_data = [news]
    vectorized_input_data = tfvect.transform(input_data)
    prediction = loaded_model.predict(vectorized_input_data)
    return prediction

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form.get('message', '')
        if not message:
            return "No message provided", 400

        pred = fake_news_det(message)
        result = "Fake News" if pred[0] == 0 else "Real News"
        return result  # Return only the result as plain text
    return "Invalid request", 400



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
