import requests

api_key = "962f77d727f94dc5b71f251f868edb02"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-10-17&"
       "sortBy=publishedAt&apiKey=962f77d727f94dc5b71f251f868edb02")

# make request
request = requests.get(url)

# retrieve dictionary data
content = request.json()

# access articles titles and description
for article in content["articles"]:
    print(article["title"])
