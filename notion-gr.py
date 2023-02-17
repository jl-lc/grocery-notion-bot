import json, requests

file = open("TOKEN.json") 
data = json.load(file)

# token & database id
TOKEN = data["id"]
DATABASE_ID = data["database"]

file.close()

headers = {
    "Authorization": "Bearer " + TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    #
    import json
    with open("db.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    return results


pages = get_pages()
for page in pages:
    prop = page["properties"]
    dish = prop["Dish"]["title"][0]["text"]["content"]
    price = prop["Price (Walmart)"]["number"]
    print(dish, price)