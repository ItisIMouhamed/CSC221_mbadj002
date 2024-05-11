from datasets import load_dataset

# Load the IMDb dataset
imdb_dataset = load_dataset("imdb")

# Function to fetch reviews
def fetch_reviews(dataset, num_reviews=10):
    reviews = dataset["train"]["text"][:num_reviews]
    return reviews

# Display reviews
def display_reviews(reviews):
    for i, review in enumerate(reviews, 1):
        print(f"Review {i}: {review}\n")

# Fetch IMDb reviews
reviews = fetch_reviews(imdb_dataset, num_reviews=5)

# Display reviews
display_reviews(reviews)
