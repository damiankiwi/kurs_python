def podziel_na_grupy(tekst):
    grupy = []
    stack = ['']

    for char in tekst:
        if char == '(':
            stack[-1] += char
        elif char == ')' and stack:
            stack[-1] += char
            grupy.append(stack.pop())
            stack.append('')
        elif char == ' ' and stack:
            stack[-1] += char

    return grupy

print(podziel_na_grupy("( ()) ((()()())) (()) ())"))
print(podziel_na_grupy("() (( ( )() ( )) ) ( ())"))