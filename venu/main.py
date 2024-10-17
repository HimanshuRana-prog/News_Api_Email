import requests
from send_email import send_email

api_key = "4287e57336d7459fbd8b64d3dce7ddb9"
url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2024-09-17&sortBy=publishedAt&"\
    "apikey=4287e57336d7459fbd8b64d3dce7ddb9"

# Make a request
request = requests.get(url)
# get a dictionary with data
content = request.json()


# Access the article titles and description
body = " "
for article in content["articles"]:
    if article["title"]  is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
    
    