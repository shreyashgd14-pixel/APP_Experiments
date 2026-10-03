class Movie:
    def __init__(self, name: str, rating: float, ticket_price: float):
        self.name = name
        self.rating = rating
        self.ticket_price = ticket_price

   
    def category(self) -> str:
      
        if self.rating >= 7.5:
            return "Hit"
        elif 5.0 <= self.rating < 7.5:
            return "Average"
        else:
            return "Flop"

    def __str__(self) -> str:
        return (
            f"Title: {self.name:<20} | "
            f"Rating: {self.rating:.1f}/10 | "
            f"Price: ₹{self.ticket_price:,.2f} | "
            f"Status: {self.category}"
        )


class Cinema:
    def __init__(self, cinema_name: str):
        self.cinema_name = cinema_name
        self.movies = []

    def add_movie(self, name: str, rating: float, ticket_price: float) -> None:
        """Create and add a new movie to the cinema's collection."""
        movie = Movie(name, rating, ticket_price)
        self.movies.append(movie)
        print(f"Added '{name}' to {self.cinema_name}.")

    def display_all_movies(self) -> None:
        """Display all movie details in a formatted table."""
        print(f"\n{'=' * 70}")
        print(f"               {self.cinema_name.upper()} - MOVIE CATALOG")
        print(f"{'=' * 70}")

        if not self.movies:
            print("No movies currently available in the catalog.")
            return

        for movie in self.movies:
            print(movie)

        print(f"{'=' * 70}")



if __name__ == "__main__":
    
    pvr = Cinema("PVR Cinemas")

   
    pvr.add_movie("Inception", 8.8, 350.00)     
    pvr.add_movie("The Matrix", 8.7, 300.00)    
    pvr.add_movie("Casual Comedy", 6.2, 200.00) 
    pvr.add_movie("B-Grade Action", 3.5, 120.00) 

  
    pvr.display_all_movies()
