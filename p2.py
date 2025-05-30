from bs4 import BeautifulSoup

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def extract_persons(soup):
    persons = []
    person_divs = soup.find_all("div", class_="persons")

    for person in person_divs:
        name = person.find("h1").text.split(":")[1].strip()
        city = person.find("h2").text.split(":")[1].strip()
        company = person.find("h3").text.split(":")[1].strip()
        designation = person.find("p").text.split(":")[1].strip()

        persons.append({"name": name,"city": city,"company": company,"designation": designation})

    return persons

html_content = load_html("p2.html")
soup = BeautifulSoup(html_content, "html.parser")

people = extract_persons(soup)

for person in people:
    print(f"Name: {person['name']}")
    print(f"City: {person['city']}")
    print(f"Company: {person['company']}")
    print(f"Designation: {person['designation']}")
    print("--------------------------------------------------")
