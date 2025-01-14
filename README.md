![Screenshot 2024-12-31 012202](https://github.com/user-attachments/assets/758ccd94-3c75-4b5a-b4d3-8a3e715044ed)
# Fake News Detection Using Machine Learning
This project is designed to detect fake news using various machine learning algorithms. 
The script preprocesses the news text, vectorizes it, and then applies several classifiers to predict whether the news is fake or true.

## Table of Contents
1. Introduction
2. Features
3. Requirements
4. Installation
5. Usage
6. Algorithms Used
7. Results
8. Contributing

## Introduction
Fake news has become a significant problem in the digital age. This project uses natural language processing (NLP) and machine learning (ML) techniques to classify news articles as fake or true.
The project leverages various machine learning models to provide accurate predictions.

## Features
* Data loading and preprocessing
* Text preprocessing (stop word removal, stemming)
* Text vectorization using TF-IDF
* Implementation of multiple classifiers:
    * Logistic Regression
    * Decision Tree Classifier
    * Gradient Boosting Classifier
    * Random Forest Classifier
* Model evaluation and performance metrics
* Manual testing of news articles

## Requirements
Python 3.6+
pandas
numpy
seaborn
matplotlib
scikit-learn
nltk
Google Colab (optional for mounting Google Drive)

## Installation
Clone the repository:

git clone https://github.com/nikhil-keshri2213/fake-news-detection.git
cd fake-news-detection

Install the required libraries:

pip install pandas numpy seaborn matplotlib scikit-learn nltk

Download NLTK stopwords:

import nltk
nltk.download('stopwords')

## Usage
1. Ensure your datasets (True.csv and Fake.csv) are available in the specified paths.
2. Run the script:
    -> python fake_news_detection.py
3. The script will preprocess the data, train the models, and display the performance metrics.
4. For manual testing, enter the news text when prompted.

## Algorithms Used
1. Logistic Regression: A linear model used for binary classification.
2. Decision Tree Classifier: A non-linear model that splits data based on feature values.
3. Gradient Boosting Classifier: An ensemble method that builds multiple models sequentially.
4. Random Forest Classifier: An ensemble method that builds multiple decision trees and merges them.

## Results
The script outputs the classification reports for each model, showing precision, recall, f1-score, and accuracy. You can manually test the models by inputting news articles, and the script will provide predictions from all four models.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
