class MovieCatalog:

    def __init__(self) -> None:
        self.setCatalog()


    def setCatalog(self) -> None:
        self.catalog : dict[str, list[str]] = {}


    def getCatalog(self)-> dict[str, list[str]]:
        return self.catalog
    

    def add_movie(self, director_name: str, movies: list[str]) -> None:
        if not director_name:
            print("Fornire un nome valido per il regista")

        elif not movie:
            print("Fornire una lista di film che non sia vuota")

        else:
            if director_name in self.catalog:
                for movie in movies:
                    if movie in self.catalog[director_name]:
                        print(f'il film movie è già presente nel catalogo')

                    else:
                        self.catalog[director_name].append(movie)

            
#    def __str__(self):
 #       string : str = ""
#
 #       for key, value in self.catalog.items():
  #          string = "\n" + key + ": " + str(value)
            
    def remove_Movie(self, director_name:str, movie:str) -> None:
        if not director_name:
            print("Fornire un nome valido per il regista")

        elif not movie:
            print("Fornire una lista di film che non sia vuota")

        else:
            if director_name in self.catalog and movie in self.catalog[director_name]:
                self.catalog[director_name].remove(movie)

            if not self.catalog[director_name]:
                del self.catalog[director_name]