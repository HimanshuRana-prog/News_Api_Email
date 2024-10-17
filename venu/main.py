import requests

api_key = "4287e57336d7459fbd8b64d3dce7ddb9"
url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2024-09-17&sortBy=publishedAt&"\
    "apikey=4287e57336d7459fbd8b64d3dce7ddb9"

# Make a request
request = requests.get(url)
# get a dictionary with data
content = request.json()
# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])