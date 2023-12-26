def czy_trend_wzrostowy(sekwencja):
    for i in range(1, len(sekwencja)):
        if sekwencja[i] <= sekwencja[i - 1]:
            return False
    return True

input1 = [1, 2, 3, 4]
input2 = [1, 2, 5, 3, 4]
input3 = [-1, -2, -3, -4]
input4 = [-4, -3, -2, -1]
input5 = [1, 2, 3, 4, 0]

output1 = czy_trend_wzrostowy(input1)
output2 = czy_trend_wzrostowy(input2)
output3 = czy_trend_wzrostowy(input3)
output4 = czy_trend_wzrostowy(input4)
output5 = czy_trend_wzrostowy(input5)

print(f"Wejściowe dane: {input1}\nCzy sekwencja ma trend wzrostowy? {output1}")
print(f"Wejściowe dane: {input2}\nCzy sekwencja ma trend wzrostowy? {output2}")
print(f"Wejściowe dane: {input3}\nCzy sekwencja ma trend wzrostowy? {output3}")
print(f"Wejściowe dane: {input4}\nCzy sekwencja ma trend wzrostowy? {output4}")
print(f"Wejściowe dane: {input5}\nCzy sekwencja ma trend wzrostowy? {output5}")