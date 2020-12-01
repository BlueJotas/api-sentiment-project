from config.configuration import db,collection

def tweet(reason, airline, name, text, location):
    """
    Function to post a new tweet
    """

    dict_insert = { "negativereason": f"{reason}",
    "airline": f"{airline}",
    "name": f"{name}",
    "text": f"{text}",
    "tweet_location": f"{location}"
    }
    collection.insert_one(dict_insert)
