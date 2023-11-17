from smtplib import SMTPDataError
import requests
from send_email import send_email

# you can choose the topic of news articles sent by entering a topic in the varialble below
topic = "ENTER A TOPIC HERE"

# enter your api key below to create a working function. API key can be created at newsapi.org
api_key = "ENTER_YOUR_API_KEY_HERE"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2023-10-17&"
       "sortBy=publishedAt&"
       "apiKey=ENTER_YOUR_API_KEY_HERE&"
       "language=en")

# makes request
request = requests.get(url)

# retrieve dictionary information
content = request.json()

# access articles titles and description, then sends an email via the send_email function
try:
    body = ""
    for article in content["articles"][0:20]:
        if article is not None:
            body = "Subject: Today's News" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

    body = body.encode("utf-8")
    send_email(message=body)
except SMTPDataError:
    pass
