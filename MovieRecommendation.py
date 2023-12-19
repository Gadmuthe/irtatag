class MovieRecommendation:
    def __init__(self):
        self.movies = {
            "The Shawshank Redemption": ["Drama", "Crime"],
            "Inception": ["Sci-Fi", "Action"],
            "The Godfather": ["Drama", "Crime"],
        }

    def recommend_movie(self, genre):
        recommended_movies = [title for title, genres in self.movies.items() if genre in genres]
        if recommended_movies:
            print(f"Recommended movie(s) in the {genre} genre:")
            for movie in recommended_movies:
                print(f"- {movie}")
        else:
            print(f"No movies found in the {genre} genre.")

recommendation = MovieRecommendation()
recommendation.recommend_movie("Drama")
recommendation.recommend_movie("Sci-Fi")