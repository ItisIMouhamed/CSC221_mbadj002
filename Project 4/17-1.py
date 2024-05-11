import requests
import matplotlib.pyplot as plt

languages = ["JavaScript", "Ruby", "C", "Java", "Perl", "Haskell", "Go"]

# Initialize dictionaries to store repository data
repo_data = {lang: {"names": [], "stars": []} for lang in languages}

# Make API calls for each language
for lang in languages:
    url = f"https://api.github.com/search/repositories?q=language:{lang}+sort:stars"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")


    response_dict = r.json()
    print(f"Total repositories: {response_dict['total_count']}")
    print(f"Complete results: {not response_dict['incomplete_results']}")
    
    # Extract relevant information
    repo_dicts = response_dict.get("items", [])
    for repo_dict in repo_dicts:
        repo_data[lang]["names"].append(repo_dict["name"])
        repo_data[lang]["stars"].append(repo_dict["stargazers_count"])

# Create a bar chart for each language
for lang in languages:
    plt.figure(figsize=(10, 6))
    plt.bar(repo_data[lang]["names"], repo_data[lang]["stars"])
    plt.xlabel("Repository")
    plt.ylabel("Stars")
    plt.title(f"Top Starred {lang} Repositories")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
