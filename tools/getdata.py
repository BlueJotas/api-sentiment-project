from config.configuration import db, collection
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def text_by_user(username):
    """
    We create a query to obtain the tweets written by a certain user.
    """

    query = {"name": f"{username}"}
    text = list(collection.find(query, {"_id": 0, "name": 1, "text": 1}))
    return text

def airline_by_user(username):
    """
    We create a query to obtain the airline.
    """

    query = {"name": f"{username}"}
    lines = list(collection.find(query, {"_id": 0, "name": 1, "airline": 1}))
    return lines

def location_of_the_user(username):
    """
    We create a query to obtain the location of the user.
    """

    query = {"name": f"{username}"}
    locat = list(collection.find(query, {"_id": 0, "name": 1, "tweet_location": 1}))
    return locat

def reason_by_user(username):
    """
    We create a query to obtain the reason of the tweet via username.
    """

    query = {"name": f"{username}"}
    text = list(collection.find(query, {"_id": 0, "negativereason": 1, "name": 1, "text": 1}))
    return text

def sentiment_analysis(username):
    """
    We create a query to obtain the sentiment analysis of a tweet published
    by a given username.
    """

    query = {"name": f"{username}"}
    text = list(collection.find(query, {"_id": 0, "name": 1, "text": 1}))
    sia = SentimentIntensityAnalyzer()
    sentence = list(collection.find(query, {"_id": 0, "text": 1}))
    extract = [tweet['text'] for tweet in sentence]
    polarity = sia.polarity_scores(extract[0])
    return f'Text input and name: {text} The sentiment analysis shows: {polarity}'
