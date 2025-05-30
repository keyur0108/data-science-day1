from bs4 import BeautifulSoup

def load_html(file_path):  # Add file_path as parameter
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        return content
def extract_posts(soup):
    posts = []
    post_elements = soup.find_all(name="div",class_="post")

    for post in post_elements:
        username = post.find(name="h2",class_="username").text
        content = post.find(name="p",class_="content").text
        timestamp = post.find(name="span",class_="timestamp").text

        posts.append({"username":username,"content":content,"timestamp":timestamp})
        return posts

html_content = load_html("social_media.html")
soup = BeautifulSoup(html_content, "html.parser")

posts = extract_posts(soup)
#print(posts)

for post in posts:
    print(f"user:{post['username']}")
    print(f"post:{post['content']}")
    print(f"time:{post['timestamp']}")
    print("..............................")