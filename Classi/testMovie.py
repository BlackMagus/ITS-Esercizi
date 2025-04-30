from Movie import MovieCatalog

catalog : MovieCatalog = MovieCatalog()

catalog.add_movie("Steven Spielberg", ["Casper", "Ritorno al Futuro"])



catalog.add_movie("Steven Spielberg", ["E.T."])

print(catalog.getCatalog())


catalog.add_movie("Tarantino", ["Kill Bill"])

print(catalog.getCatalog)

catalog.remove_Movie("Steven Spielberg", "E.T.")

catalog.remove_Movie("Steven Spielberg", "Ritorno al Futuro")

catalog.remove_Movie("Steven Spielberg", "Casper")

print(catalog.getCatalog)