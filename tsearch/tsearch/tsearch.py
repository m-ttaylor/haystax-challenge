import os
from twitter import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance
app.config.from_object(__name__) # load config from this file

app.config.from_envvar('TSEARCH_SETTINGS', silent=True)

@app.route('/', methods=['GET','POST'])
def form():
    # text = request.form['text']
    if request.method == 'POST':
        searchterm = request.form['searchterm']

        twitter = Twitter(auth = OAuth(app.config['ACCESS_KEY'], app.config['ACCESS_SECRET'],
    				 app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET']))

        user = 'twitterAPI'
        # results = twitter.users.search(q='twitter API')
        results = twitter.statuses.user_timeline(screen_name = searchterm, count=5)

        entries = []
        for i in range(5):
            if i < len(results):
                text = results[i]['text']
                data = {'text': text,
                        'date': results[i]['created_at'],
                        'count': len(text.split())}
                entries.append(data)
            else:
                entries.append({'text': "not enough entries",
                                'date': "",
                                'count': "N/A"})

        return render_template("index.html",entries=entries)

    return """
        <html>
            <link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
            <head>
                <title>tsearch</title>
            </head>
            <body>
                <h2>Search a twitter user:</h2>
                <form method="post">
                    <p><input type=text name=searchterm>
                </form>
            </body>
        </html>
    """
