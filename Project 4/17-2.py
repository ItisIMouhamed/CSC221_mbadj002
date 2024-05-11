import requests
import matplotlib.pyplot as plt

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        if response_dict['type'] == 'story':
            submission_dict = {
                'title': response_dict['title'],
                'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
                'comments': response_dict['descendants'],
            }
            submission_dicts.append(submission_dict)
    except KeyError:
        pass

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Create a bar chart for the most active discussions.
titles = [submission_dict['title'] for submission_dict in submission_dicts]
comments = [submission_dict['comments'] for submission_dict in submission_dicts]

plt.figure(figsize=(10, 6))
plt.barh(titles, comments)
plt.xlabel("Number of Comments")
plt.ylabel("Submission Title")
plt.title("Most Active Discussions on Hacker News")
plt.gca().invert_yaxis()  # Invert y-axis to show highest comments at the top
plt.tight_layout()
plt.show()
