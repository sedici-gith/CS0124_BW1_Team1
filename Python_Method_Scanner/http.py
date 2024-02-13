import http.client

IP = input("inserire IP target: ")
porta = input("inserire porta target (default: 80): ")
metodi = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS']

if porta == "":
    porta = 80

for metodo in metodi:
    try:

        connection = http.client.HTTPConnection(IP, porta)
        connection.request(metodo, "/")
        risposta = connection.getresponse()
        if risposta.status < 400:
            print(f"metodo {metodo} abilitato")
        elif risposta.status > 400:
            print(f"metodo {metodo} disabilitato")
    except ConnectionRefusedError: 
        print(f"connessione fallita")
    
    connection.close()

