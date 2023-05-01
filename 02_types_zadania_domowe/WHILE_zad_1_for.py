#1 Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
#Napisz rozwiązanie z użyciem pętli FOR.

fahr = 0
for fahr in range(0,220,20):
    celc = round(5/9*(fahr - 32),2)
    print(f"temp {fahr} F-> {celc} C")
    fahr += 20