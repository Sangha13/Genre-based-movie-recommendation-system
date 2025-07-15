import pandas as pd

def load_and_prepare_data(csv_path="Data/movies_ratings_merged.csv"):
    """
    Loads and prepares the dataset for genre-based recommendations.
    """
    df = pd.read_csv(csv_path)

    # Drop rows with missing genres
    df = df.dropna(subset=['genres'])

    # Split genres into list
    df['genres'] = df['genres'].str.split('|')

    # Explode genre list into rows
    df_exploded = df.explode('genres')

    # Compute average rating and rating count per movie
    movie_stats = df.groupby('title').agg({
        'rating': ['mean', 'count']
    }).reset_index()
    movie_stats.columns = ['title', 'avg_rating', 'rating_count']

    # Merge stats back into exploded dataframe
    df_exploded = df_exploded.merge(movie_stats, on='title')

    return df_exploded


def recommend_by_genres(preferred_genres, df_exploded, top_n=10):
    """
    Recommends top-rated movies from selected genres.

    Parameters:
    - preferred_genres: list of genres (1-3 strings)
    - df_exploded: DataFrame with exploded genres
    - top_n: number of movies to return

    Returns:
    - DataFrame with recommended movies
    """
    # Filter rows where genres match user preference
    filtered = df_exploded[df_exploded['genres'].isin(preferred_genres)]

    # Sort by rating count and average rating
    recommendations = filtered.sort_values(
        by=['rating_count', 'avg_rating'],
        ascending=False
    ).drop_duplicates('title').head(top_n)

    return recommendations[['title', 'genres', 'avg_rating', 'rating_count']]
