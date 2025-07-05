from collections import namedtuple
Food = namedtuple("Food", ["name", "price"])
food1 = Food("Pizza", 11.90)
food2 = Food("Burger", 7.45)
food3 = Food("Salad", 5.45)
food_dict = {
    food1.name: food1,
    food2.name: food2,
    food3.name: food3
}
for food_name, food_info in food_dict.items():
    print(f"Food: {food_name}, Price: ${food_info.price:.2f}")