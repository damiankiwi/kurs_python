def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    # print(bmi)
    if bmi < 18.5:
        answer = read_from_file('underweight.txt')
    elif bmi < 25:
        answer = read_from_file('normal.txt')
    elif bmi < 30:
        answer = read_from_file('overweight.txt')
    else:
        answer = read_from_file('obese.txt')
    return answer


def read_from_file(filename):
    with open(filename, encoding = 'utf-8') as f:
        lines = f.read()
        return lines