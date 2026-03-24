#!/usr/bin/env python3
import argparse
import requests
import json
from datetime import datetime, timezone, timedelta

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', required=True)
    parser.add_argument('--since-minutes', type=int, default=10)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    import os
    token = os.environ.get("GH_TOKEN")
    
    headers = {"Accept": "application/vnd.github.v3.star+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
        
    url = f"https://api.github.com/repos/{args.repo}/stargazers"
    
    # We want stars since X minutes ago
    cutoff = datetime.now(timezone.utc) - timedelta(minutes=args.since_minutes)
    
    new_stars = []
    
    # Just fetch the first page for now, if it's very active we'd need to paginate backward
    # But GitHub API standard pagination gives oldest first, which is annoying.
    # For a personal repo, latest stargazers are usually at the end of the last page.
    # To be strictly correct, we should get the links, find the last page, and read it.
    try:
        response = requests.get(url, headers=headers, params={"per_page": 100})
        response.raise_for_status()
        
        # If there are multiple pages, we should really go to the last page.
        if "link" in response.headers:
            # simple trick to get last page URL
            links = response.headers["link"]
            for link in links.split(','):
                if 'rel="last"' in link:
                    last_url = link[link.find('<')+1:link.find('>')]
                    response = requests.get(last_url, headers=headers)
                    response.raise_for_status()
                    break

        data = response.json()
        for item in data:
            starred_at = datetime.fromisoformat(item["starred_at"].replace("Z", "+00:00"))
            if starred_at > cutoff:
                new_stars.append({"username": item["user"]["login"], "starred_at": item["starred_at"]})
                
    except Exception as e:
        print(f"Error fetching stargazers: {e}")

    with open(args.output, "w") as f:
        json.dump(new_stars, f, indent=2)

if __name__ == "__main__":
    main()
