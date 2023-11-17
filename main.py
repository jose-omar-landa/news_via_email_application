from smtplib import SMTPDataError

import requests
from send_email import send_email

topic = "nintendo"

api_key = "962f77d727f94dc5b71f251f868edb02"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2023-10-17&"
       "sortBy=publishedAt&"
       "apiKey=962f77d727f94dc5b71f251f868edb02&"
       "language=en")

# make request
request = requests.get(url)

# retrieve dictionary data
content = request.json()

# access articles titles and description
try:
    body = ""
    for article in content["articles"][0:20]:
        if article is not None:
            body = "Subject: Today's News" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

    body = body.encode("utf-8")
    send_email(message=body)
except SMTPDataError:
    pass
