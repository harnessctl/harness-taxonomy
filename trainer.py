import json
import httpx
from collections import Counter
from pathlib import Path
import sys
import time

def fetch_so_tags(pages=5):
    print(f"Fetching {pages*100} StackOverflow tags...")
    tags = []
    for page in range(1, pages + 1):
        url = f"https://api.stackexchange.com/2.3/tags?page={page}&pagesize=100&order=desc&sort=popular&site=stackoverflow"
        try:
            response = httpx.get(url, timeout=10.0)
            response.raise_for_status()
            tags.extend([item["name"] for item in response.json().get("items", [])])
            time.sleep(0.5) # respect rate limit slightly
        except Exception as e:
            print(f"Failed to fetch SO tags on page {page}: {e}")
            break
    return tags

def fetch_github_topics():
    print("Fetching GitHub popular topics...")
    url = "https://api.github.com/search/repositories?q=stars:>5000&sort=updated&order=desc&per_page=100"
    headers = {
        "Accept": "application/vnd.github.v3+json", 
        "User-Agent": "Harness-Taxonomy-Bot"
    }
    try:
        response = httpx.get(url, headers=headers, timeout=10.0)
        response.raise_for_status()
        topic_counter = Counter()
        for repo in response.json().get("items", []):
            for topic in repo.get("topics", []):
                topic_counter[topic] += 1
        return [topic for topic, count in topic_counter.most_common(100)]
    except Exception as e:
        print(f"Failed to fetch GH topics: {e}")
        return []

def train():
    so_tags = fetch_so_tags(pages=5) # Fetches top 500 tags
    gh_topics = fetch_github_topics() # Fetches up to 100 topics
    
    tax_path = Path("taxonomy.json")
    if not tax_path.exists():
        print(f"Error: {tax_path} not found.")
        sys.exit(1)
        
    with open(tax_path, "r") as f:
        taxonomy = json.load(f)
        
    if "categories" not in taxonomy:
        taxonomy["categories"] = {}
        
    if "trending" not in taxonomy["categories"]:
        taxonomy["categories"]["trending"] = {
            "weight": 0.7,
            "concepts": {}
        }
        
    if so_tags:
        taxonomy["categories"]["trending"]["concepts"]["stack_overflow"] = so_tags
    if gh_topics:
        taxonomy["categories"]["trending"]["concepts"]["github"] = gh_topics
        
    with open(tax_path, "w") as f:
        json.dump(taxonomy, f, indent=2)
        
    print(f"Successfully trained taxonomy. Added {len(so_tags)} SO tags and {len(gh_topics)} GitHub topics.")

if __name__ == "__main__":
    train()
