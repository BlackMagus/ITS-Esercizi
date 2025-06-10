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
        
    
class VideoRentalStore:

    def __init__(self, movies:dict[str, Movie],customers:dict[str, Customer]):
        self.movies = movies
        self.customers = customers

    def add_movie(self, movie_id:str, title:str, director:str)-> None:
        lista1:list[movie_id:str, title:str, director:str]
        for element in self.movies:
            key = element[0]

        if movie_id in self.movies:
            print(f"Il film con ID {movie_id} esiste già")
        else:
            self.movies[key].append(lista1)

    def register_customer(self, customer_id:str, name:str)-> None:
        lista1:list[customer_id:str, name:str]
        for element in self.customers:
            key = element[0]

        if customer_id in self.customers:
            print(f"Il cliente con ID {customer_id} è già registrato")
        else:
            self.customers[key].append(lista1)

    def rent_movie(self, customer_id:str, movie_id:str)-> None:
        if movie_id not in self.movies and customer_id not in self.customers:
            print("Cliente o Film non trovato")

    def return_movie(self, customer_id:str, movie_id:str):
        if movie_id not in self.movies and customer_id not in self.customers:
            print("Cliente o Film non trovato")

    