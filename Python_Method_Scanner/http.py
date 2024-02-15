import http.client
def main():
    IP = input("inserire IP target: ")
    porta = input("inserire porta target (default: 80): ")
    percorso = input("inserire percorso (default: /): ")
    metodi = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD']

    if porta == "":
        porta = 80
       
    if percorso == "":
        percorso = "/"
    scansione(IP, porta, percorso, metodi)

def scansione(IP, porta, percorso, metodi):
	try:
		for metodo in metodi:
			connection = http.client.HTTPConnection(IP, porta)
			connection.request(metodo, percorso)
			risposta = connection.getresponse()
			if risposta.status < 400:
			    print(f"metodo {metodo} abilitato, codice {risposta.status}")
			else:
			    print(f"metodo {metodo} disabilitato, codice {risposta.status}")
		print(IP, "/", porta, "/", percorso)
	except ConnectionRefusedError:
		print("connessione fallita")
		print(IP, "/", porta, "/", percorso)
    
if __name__ == "__main__":
    main()

