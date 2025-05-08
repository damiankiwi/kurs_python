def empty_string_handling(string_list):
    for s in string_list:
        if s:
            print(s)
        else:
            print(None)

def main():
    try:
        text_list = ["Python", "", "Java", "C++", "", "C#"]
        empty_string_handling(text_list)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()