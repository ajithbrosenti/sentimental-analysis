import pandas as pd
import numpy as np
from project.settings import BASE_DIR
import re
import os
import emoji
import contractions
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
nltk.download('punkt')
nltk.download('stopwords')
import joblib

def demojize(text):
    text = emoji.demojize(text)
    return text

def replace_url(text, default_replace=""):
    text = re.sub('(http|https):\/\/\S+', default_replace, text)
    return text

def replace_hashtag(text, default_replace=""):
    text = re.sub('#+', default_replace, text)
    return text

def to_lowercase(text):
    text = text.lower()
    return text

def word_repetition(text):
    text = re.sub(r'(.)\1+', r'\1\1', text)
    return text

def punct_repetition(text, default_replace=""):
    text = re.sub(r'[\?\.\!]+(?=[\?\.\!])', default_replace, text)
    return text

def fix_contractions(text):
    text = contractions.fix(text)
    return text

def custom_tokenize(text,
                        keep_punct = False,
                        keep_alnum = False,
                        keep_stop = False,
                        verbose = False):
    token_list = word_tokenize(text)
    if verbose: print("Post general tokenization: {}\n".format(token_list))

    if not keep_punct:
        token_list = [token for token in token_list
                    if token not in string.punctuation]

    if verbose: print("Post punctuation removal: {}\n".format(token_list))

    if not keep_alnum:
        token_list = [token for token in token_list if token.isalpha()]

    if not keep_stop:
        stop_words = set(stopwords.words('english'))
        stop_words.discard('not')
        stop_words.update(["'s", ])
        token_list = [token for token in token_list if not token in stop_words]

    if verbose: print("Post stopword removal: {}\n".format(token_list))

    return token_list
def stem_tokens(tokens, stemmer):
    token_list = []
    for token in tokens:
        token_list.append(stemmer.stem(token))
    return token_list

def process_text(text, verbose=False):
    if verbose: print("Initial text: {}\n".format(text))
    ## Twitter Features
    text = replace_url(text) # replace url
    text = replace_hashtag(text) # replace hashtag
    if verbose: print("Post Twitter processing tweet: {}\n".format(text))

    ## Word Features
    text = to_lowercase(text) # lower case
    text = fix_contractions(text) # replace contractions
    text = punct_repetition(text) # replace punctuation repetition
    text = text.replace('.',' ')
    text = word_repetition(text) # replace word repetition
    text = demojize(text) # replace emojis
    if verbose: print("Post Word processing tweet: {}\n".format(text))

    ## Tokenization & Stemming
    tokens = custom_tokenize(text, keep_alnum=True, keep_stop=False) # tokenize
    stemmer = SnowballStemmer("english") # define stemmer
    stem = stem_tokens(tokens, stemmer) # stem tokens
    return stem

def process_sentiment(sentiment):
    switcher = {
        "sad":0,
        "joy":1,
        "love":2,
        "anger":3,
        "fear":4,
        "surprise":5
    }
    return switcher.get(sentiment,5)

def preprocess_dataset():
    dataset_path = os.path.join(BASE_DIR,*["sentiment","emotional_dataset.csv"])
    df = pd.read_csv(dataset_path)

def lambdafun_fix(text):
    return text

def fit_tfidf(text_corpus):
    tf_vect = TfidfVectorizer(preprocessor=lambdafun_fix,tokenizer=lambdafun_fix)
    TfidfVectorizer.__module__ = "apps"
    tf_vect.fit(text_corpus)
    return tf_vect

def fit_lr(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def emotion(text):
    processed_text = process_text(text)
    X = joblib.load("Xvar.pkl")
    tf = fit_tfidf(X)
    transformed_text = tf.transform([processed_text])
    model = joblib.load("lrmodel.pkl")
    prediction = model.predict(transformed_text)
    if prediction == 0:
        return "Sentiment is sad"
    elif prediction == 1:
        return "Sentiment is joy"
    elif prediction == 2:
        return "Sentiment is love"
    elif prediction == 3:
        return "Sentiment is anger"
    elif prediction == 4:
        return "Sentiment is fear"
    elif prediction == 5:
        return "Sentiment is surprise"

