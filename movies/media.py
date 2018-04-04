import webbrowser

class Video:        
    """This class is parent class for Movie and TvShow."""
    
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        
class Movie(Video):
    """This class provides a way to story movie trailers and poster images."""
    
    valid_ratings = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)    
        
        

class TvShow(Video):
    
    def __init__(self, tv_show_title, season, episode, tv_station):
        self.title = tv_show_title
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
        
    def get_local_listing(self):
        pass    