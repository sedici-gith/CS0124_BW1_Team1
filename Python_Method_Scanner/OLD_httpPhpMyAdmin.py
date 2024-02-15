import http.client

IP = input("inserire IP target: ")
porta = input("inserire porta target (default: 80): ")
metodi = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS']

if porta == "":
    porta = 80

def scansione():
    for metodo in metodi:
        connection = http.client.HTTPConnection(IP, porta)
        connection.request(metodo, "/phpMyAdmin/")
        risposta = connection.getresponse()
        if risposta.status < 400:
            print(f"metodo {metodo} abilitato")
        else:
            print(f"metodo {metodo} disabilitato")
    print(IP, "/", porta)
    
try: 
    scansione()

except ConnectionRefusedError:
    print("connessione fallita")
    print(IP, "/", porta)
