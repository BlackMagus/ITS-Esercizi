class Movie:
    def __init__(self, movie_id:str, title:str, director:str, is_rented:bool):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    
    def rent(self) -> None:
        if self.is_rented == False:
            self.is_rented = True
        else:
            raise ValueError(f"Il film {self.title} è già noleggiato")
        
    def return_movie(self) -> None:
        if self.is_rented == True:
            self.is_rented = False

        else:
            raise ValueError(f"Il film {self.title} non è stato noleggiato")
        
    
class Customer:
    def __init__(self, customer_id:str, name:str, rented_movies:list[Movie]):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = rented_movies[Movie]


    def rent_movie(self, movie:Movie) -> None:
        if movie == False:
            self.rented_movies.append(movie)
        else:
            raise ValueError(f"Il film {movie.title} è già nopleggiato")
        
    def return_movie(self, movie:Movie) -> None:
        if movie == True:
            self.rented_movies.remove(movie)
        else:
            raise ValueError(f"Il film {movie.title} non è stato noleggiato da nessuno")
        