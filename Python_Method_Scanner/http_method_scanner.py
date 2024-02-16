import http.client
def main():           #rende metodo gli input da inserire 
    IP = input("inserire IP target: ")
    porta = input("inserire porta target (default: 80): ")
    percorso = input("inserire percorso (default: /): ")
    metodi = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD']

    if porta == "":
        porta = 80
       
    if percorso == "":
        percorso = "/"
    scansione(IP, porta, percorso, metodi)

def scansione(IP, porta, percorso, metodi):    #rende metodo tutto quello scritto dopo
	try:
		for metodo in metodi:
			connection = http.client.HTTPConnection(IP, porta)   #stabilisce una connessione con il percorso stabilito
			connection.request(metodo, percorso)    #la connessione richiede che metodo e'attivo su quel percorso specifico
			risposta = connection.getresponse()   #cattura la risposta dalla connessione
			if risposta.status < 400:    
			    print(f"metodo {metodo} abilitato, codice {risposta.status}")
			else:
			    print(f"metodo {metodo} disabilitato, codice {risposta.status}")
		print(IP, "/", porta, "/", percorso)
	except ConnectionRefusedError:
		print("connessione fallita")
		print(IP, "/", porta, "/", percorso)
    
if __name__ == "__main__":   #rende metodo tutto il codice
    main()

