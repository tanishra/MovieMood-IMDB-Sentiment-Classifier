import streamlit as st
import pickle
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required resources
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Load model and vectorizer from pickle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Text cleaning function
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = text.lower()  # Lowercase
    text = re.sub(f"[{re.escape(string.punctuation)}]", '', text)  # Remove punctuation
    tokens = text.split()
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Streamlit UI
st.set_page_config(page_title="SentimentScope", layout="centered")
st.title("🎬 MovieMood: IMDb Sentiment Classifier")
st.write("Enter a movie review below and let the model predict the sentiment!")

# Input box
review = st.text_area("📝 Your Movie Review", height=200)

# Prediction
if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a valid review.")
    else:
        cleaned_review = clean_text(review)
        review_vector = vectorizer.transform([cleaned_review])
        prediction = model.predict(review_vector)

        if prediction[0] == 1:
            st.success("✅ Positive Review")
        else:
            st.error("❌ Negative Review")
