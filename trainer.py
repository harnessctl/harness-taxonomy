import json
import httpx
from collections import Counter
from pathlib import Path
import sys

def fetch_so_tags():
    print("Fetching StackOverflow tags...")
    url = "https://api.stackexchange.com/2.3/tags?pagesize=50&order=desc&sort=popular&site=stackoverflow"
    try:
        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
        return [item["name"] for item in response.json().get("items", [])]
    except Exception as e:
        print(f"Failed to fetch SO tags: {e}")
        return []

def fetch_github_topics():
    print("Fetching GitHub popular topics...")
    url = "https://api.github.com/search/repositories?q=stars:>5000&sort=updated&order=desc&per_page=50"
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
        return [topic for topic, count in topic_counter.most_common(50)]
    except Exception as e:
        print(f"Failed to fetch GH topics: {e}")
        return []

def train():
    so_tags = fetch_so_tags()
    gh_topics = fetch_github_topics()
    
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
