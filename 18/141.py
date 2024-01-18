import socket

def pobierz_nazwe_domeny(adres_ip):
    try:
        nazwa_domeny, _, _ = socket.gethostbyaddr(adres_ip)
        return nazwa_domeny
    except socket.herror:
        return "Nieznane"

ip1 = "8.8.8.8"
ip2 = "13.251.106.90"
ip3 = "8.8.4.4"
ip4 = "23.23.212.126"

print("Nazwa domeny przy użyciu rekordów DNS PTR dla", ip1 + ":", pobierz_nazwe_domeny(ip1))
print("Nazwa domeny przy użyciu rekordów DNS PTR dla", ip2 + ":", pobierz_nazwe_domeny(ip2))
print("Nazwa domeny przy użyciu rekordów DNS PTR dla", ip3 + ":", pobierz_nazwe_domeny(ip3))
print("Nazwa domeny przy użyciu rekordów DNS PTR dla", ip4 + ":", pobierz_nazwe_domeny(ip4))