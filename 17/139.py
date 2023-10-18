import socket

def sprawdz_adres_ip(adres):
    try:
        socket.inet_aton(adres)
        return True
    except socket.error:
        return False

adres1 = "192.168.1.1"
adres2 = "256.0.0.1"
adres3 = "google.com"

print(f'Czy {adres1} to poprawny adres IP? {sprawdz_adres_ip(adres1)}')
print(f'Czy {adres2} to poprawny adres IP? {sprawdz_adres_ip(adres2)}')
print(f'Czy {adres3} to poprawny adres IP? {sprawdz_adres_ip(adres3)}')
