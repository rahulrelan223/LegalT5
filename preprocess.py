import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag


def preprocess_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert text to lowercase
    text = text.lower()
    # Remove extra whitespaces
    text = ' '.join(text.split())
    # Remove stop words (optional)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    text = ' '.join(filtered_text)
    return (text)
 
def tokenize_and_tag(text):
    # Tokenize the input text
    tokens = word_tokenize(text)
    # Perform POS tagging on the tokens
    tagged_tokens = pos_tag(tokens)
    return tagged_tokens

