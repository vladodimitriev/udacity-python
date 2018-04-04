import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.title + ":", toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/200px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.title + ":", avatar.storyline)
#avatar.show_trailer()
movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.valid_ratings)
#print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)