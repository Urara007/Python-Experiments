n = int(input("Enter number of movies: "))
movies = {}

for _ in range(n):
    m_name = input("\nMovie Name: ")
    year = int(input("Release Year: "))
    director = input("Director: ")
    cost = float(input("Production Cost: "))
    earnings = float(input("Collection: "))
    
    movies[m_name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "earnings": earnings
    }

# a. Print all movie details
print("\n--- All Movie Details ---")
for name, info in movies.items():
    print(f"{name}: {info}")

# b. Movies released before 2015
print("\nMovies released before 2015:")
for name, info in movies.items():
    if info["year"] < 2015:
        print(name)

# c. Movies that made a profit
print("\nProfitable Movies:")
for name, info in movies.items():
    if info["earnings"] > info["cost"]:
        print(f"{name} (Profit: {info['earnings'] - info['cost']})")

# d. Movies directed by a particular director
search_dir = input("\nEnter director name to search: ")
print(f"Movies directed by {search_dir}:")
for name, info in movies.items():
    if info["director"].lower() == search_dir.lower():
        print(name)