# -*- coding: utf-8 -*-
import feedparser
from flask import Flask

app = Flask(__name__)
FEED_SOURCE = "http://koponyeg.hu/idojaras_rss.php?regios=5"


@app.route("/")
def get_news():
    feed = feedparser.parse(FEED_SOURCE)["entries"][0]
    title = feed.get("title")
    summary = feed.get("summary")
    updated = feed.get("published")
    return """
    <html>
        <body>
            <h1>{0}</h1>
            <h2>{1}</h2>
            {2}
        </body>
    </html>""".format(title, updated, summary)

if __name__ == "__main__":
    print ("test")
    app.run(port=5000, debug = False)