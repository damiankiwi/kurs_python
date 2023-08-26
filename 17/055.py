import socket


def znajdz_lokalne_ip():
    lokalne_ip = []
    try:
        host_name = socket.gethostname()
        ip_adresy = socket.getaddrinfo(host_name, None)
        for ip in ip_adresy:
            if ip[1] == socket.SOCK_STREAM:
                lokalne_ip.append(ip[4][0])
    except socket.gaierror:
        pass

    return lokalne_ip


lokalne_ip = znajdz_lokalne_ip()

if lokalne_ip:
    print("Lokalne adresy IP:")
    for ip in lokalne_ip:
        print(ip)
else:
    print("Nie można znaleźć lokalnych adresów IP.")