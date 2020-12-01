# API Sentiment Project!

Welcome to my new project!

## This project focuses in a few things:

- This is a project where you can get some tweets and use a Sentiment Analyzer
to get the negativity or positivity of a given tweet. The tweets are only themed on one category: They are opinions about airlines and the
things that they want to complain or talk about, so you won't find tweets about
anything else here!

#### Also you can tweet your own things and have some fun analyzing you emotions later!


- First, we started an API using flask! This will get our clients in touch with
our database so they can make some queries.

- Secondly, we filled our database in MongoDB with some tweets so you can make
some calls to the database and get some info.

- Next, we made the API able to post some tweets of your own, so now you can post some things too!

- Last but not least, the fun of this project is to use the Sentiment Analyzer
to get some emotional feedback from the tweets. Don't hesitate to apply that
on your own tweets and on the tweets from other people in the database!

## GET PARAMETERS:

Everything is connected so you can make a very simple query and obtain the info that you want!

IMPORTANT: ALL THE SEARCHES ARE USER BASED. This means that you can get all the info by asking for a specific data and the username. We'll see how in the examples below.

What can you retrieve from the database? This collection stores as we've previously said the info from some tweets in relation with their user experience with some airlines, so this are the things that you can ask for:

#### The part of the URL that is static is this: 'http://localhost:5000'

Now, you can add the following endpoints:

- "/tweets/<username>" <-- This gets all the tweets from a specific username. Simply as that

- "/airline/<username>" <-- This displays the airline that a specific username took.

- "/location/<username>" <-- This displays the location of the username when the tweet was sent and its name.

- "/reason/<username>" <-- If any, it displays the negative reason that the user is complaining about.

- "/sentiment/<username>" <-- And finally, the user can analyze the sentiment of the tweet, being this your own tweet or other's. So have fun with this one!

## POST PARAMETERS:

This functionality is the one that you'll be using to create a new entry in our collection (one of the many storages that our database can have). So be careful and have fun posting some tweets!

- "/newtweet" <-- With this one you can post a tweet that follows this parameters which are essential to register a new tweet: 'reason, airline, name, text, location'. With those ones completed, you'll be able to post a new entry in our database!


#### Additional info:

Everything is connected to our MongoDB database so you can just get the info from
what's in there! Remember that this is not an enourmous database, so you can just fill it and make it bigger if you want to by posting lots of tweets!

Hope you enjoy the repo. Cheers!
