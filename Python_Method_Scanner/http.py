import http.client
def main():
    IP = input("inserire IP target: ")
    porta = input("inserire porta target (default: 80): ")
    percorso = input("ïnserire percorso (default: /): ")
    metodi = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD']

    if porta == "":
        porta = 80
        
    if percorso == "":
        percorso = "/"

    def scansione():
        for metodo in metodi:
            connection = http.client.HTTPConnection(IP, porta)
            connection.request(metodo, percorso)
            risposta = connection.getresponse()
            if risposta.status < 400:
                print(f"metodo {metodo} abilitato, codice {risposta.status}")
            else:
                print(f"metodo {metodo} disabilitato, codice {risposta.status}")
        print(IP, "/", porta, "/", percorso)
    
    try: 
        scansione()

    except ConnectionRefusedError:
        print("connessione fallita")
        print(IP, "/", porta, "/", percorso)
    
if __name__ == "__main__":
 main()
