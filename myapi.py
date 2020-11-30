from flask import Flask, request
import markdown.extensions.fenced_code
import random
import json
import tools.getdata as get
import tools.postdata as pos

app = Flask(__name__)

# JUST THE README:
@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string

# GET REQUESTS:
@app.route("/tweets/<username>")
def usertext(username):
    # function to obtain all the tweets from a certain user.
    phrase = get.text_by_user(username)
    return json.dumps(phrase)

@app.route("/airline/<username>")
def userairline(username):
    # function to obtain the airline that the user took.
    airlines = get.airline_by_user(username)
    return json.dumps(airlines)

@app.route("/location/<username>")
def location(username):
    # function to obtain the location of the user.
    local = get.location_of_the_user(username)
    return json.dumps(local)

@app.route("/reason/<username>")
def reasonwhy(username):
    # function to know the reason of the tweet by a certain user.
    reason = get.reason_by_user(username)
    return json.dumps(reason)

@app.route("/sentiment/<username>")
def analyzeSentiment(username):
    # function to analyze if a tweet is positive or negative.
    sentiment = get.sentiment_analysis(username)
    return json.dumps(sentiment)


# POST REQUESTS:
@app.route("/newtweet",methods=["POST"])
def tweet():
    # function to instert a new tweet from a user.
    reason = request.form.get.tweet("negativereason")
    airline = request.form.get.tweet("airline")
    name = request.form.get.tweet("name")
    text = request.form.get.tweet("text")
    location = request.form.get.tweet("tweet_location")
    pos.tweet(reason, airline, name, text, location)
    return "Mensaje introducido correctamente en la base de datos"



app.run(debug=True)
