import requests

def google_search(query, serpapi_api_key, num_results=20):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "hl": "ja",
        "num": num_results,
        "api_key": serpapi_api_key
    }

    response = requests.get(url, params=params)
    results = response.json()

    search_results = []
    for item in results.get("organic_results", []):
        search_results.append({
            "title": item.get("title"),
            "snippet": item.get("snippet"),
            "link": item.get("link")
        })

    return search_results
