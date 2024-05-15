original_list = ['red', 'black', 'white', 'green', 'orange']

def find_elements_with_substring(lst, substring):
    result = list(filter(lambda x: substring in x, lst))
    return result

substring1 = "ack"
print("Original list:")
print(original_list)
print("Substring to search:", substring1)
print("Elements of the said list that contain specific substring:")
print(find_elements_with_substring(original_list, substring1))

substring2 = "abc"
print("\nSubstring to search:", substring2)
print("Elements of the said list that contain specific substring:")
print(find_elements_with_substring(original_list, substring2))