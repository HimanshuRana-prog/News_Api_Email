import requests
from send_email import send_email

api_key = "4287e57336d7459fbd8b64d3dce7ddb9"
url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2024-09-17&sortBy=publishedAt&"\
    "apikey=4287e57336d7459fbd8b64d3dce7ddb9&language=en"

# Make a request
request = requests.get(url)
# get a dictionary with data
content = request.json()

# Check if the request was successful
if request.status_code == 200:
    content = request.json()

# Access the article titles and description
body = " "
for article in content["articles"]:
    title = article.get("title")
    description = article.get("description")
    article_url = article.get("url")


    if title:
            body += f"{title}\n{description}\n{article_url}\n\n"

    body = body.encode("utf-8")
    send_email(message=body)
else:
    print(f"Error: {request.status_code} - {request.text}")
    
#     if article["title"]  is not None:
#         body = body + article["title"] + "\n" + article["description"]+"\n" + article["url"] + 2*"\n"

# body = body.encode("utf-8")
# send_email(message=body)
    
    