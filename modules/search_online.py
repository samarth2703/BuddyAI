import requests

class OnlineSearch:
    def __init__(self):
        self.url = "https://api.duckduckgo.com/"

    def search(self, query):
        params = {
            "q": query,
            "format": "json",
            "no_redirect": 1,
            "no_html": 1
        }

        try:
            response = requests.get(self.url, params=params, timeout=5)
            data = response.json()

            abstract = data.get("AbstractText", "")
            related_topics = data.get("RelatedTopics", [])

            if abstract:
                return abstract

            for item in related_topics:
                if "Text" in item:
                    return item["Text"]

            return "No result found."
        except Exception as e:
            return f"Search failed: {e}"


# FUNCTION FOR main.py
search_engine = OnlineSearch()

def web_search(query):
    return search_engine.search(query)
