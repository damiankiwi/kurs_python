cities = [
    ("New York", 8419000),
    ("Los Angeles", 3980000),
    ("Chicago", 2716000),
    ("Houston", 2328000),
    ("Phoenix", 1690000),
    ("Philadelphia", 1584000),
    ("San Antonio", 1543000),
    ("San Diego", 1424000),
    ("Dallas", 1343000),
    ("San Jose", 1035000)
]

def is_population_greater_than_2_million(city):
    name, population = city
    return population > 2000000

large_cities = list(filter(is_population_greater_than_2_million, cities))

print("Cities with a population greater than 2 million:")
print(large_cities)