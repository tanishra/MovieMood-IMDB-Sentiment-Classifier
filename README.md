# 🎬 MovieMood: IMDb Sentiment Classifier

**MovieMood** is a machine learning-powered web app that analyzes the sentiment of IMDb movie reviews and classifies them as **Positive** or **Negative**. It uses natural language processing (NLP) techniques and a trained Multinomial Naive Bayes model to predict sentiments with high accuracy.

---

## 🚀 Features

- Clean and interactive **Streamlit** web interface
- Text preprocessing: HTML tag removal, stopword removal, punctuation cleaning, stemming
- Uses **Multinomial Naive Bayes** model trained on IMDb dataset
- Achieves an accuracy of **82.19%**
- Real-time sentiment prediction

---

## 🧠 Machine Learning Details

- **Dataset**: IMDb movie reviews dataset from [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- **Text Cleaning**: 
  - Removing HTML tags
  - Removing special characters & punctuation
  - Removing stop words
  - Stemming using Porter Stemmer
- **Models Tried**:
  - Gaussian Naive Bayes
  - Bernoulli Naive Bayes
  - ✅ **Multinomial Naive Bayes (Best)**

---

## 🧪 How to Run

1. **Install dependencies**  
   *(Create a virtual environment if preferred)*

   ```bash
   pip install -r requirements.txt
   ````
2. **Run the app**  
   ```bash
   streamlit run app.py
   ````

---

## 🤝 Contributions
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.


