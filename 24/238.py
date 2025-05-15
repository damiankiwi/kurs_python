def retrieve_value(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return None

def main():
    try:
        person_data = {"name": "Bonifaas Shyam", "age": 25, "city": "Paris"}
        search_key = "age"

        result = retrieve_value(person_data, search_key)

        if result is None:
            print(f"Key '{search_key}' not found.")
        else:
            print(f"The value for key '{search_key}' is:", result)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()