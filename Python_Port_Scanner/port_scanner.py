import socket

def main():

    obiettivo_ip =  input("Inserire l'indirizzo IP da sannerizzare: ") #chiediamo all'utente di inserire l'idirizzo IP
    intervallo_porte = input("Inserisci il range di porte da scannerizzare (es:0-65535): ") #chiediamo all'utente di inserire il range di porte

    porta_bassa = int(intervallo_porte.split("-")[0]) #estrae i valori minimi delle porte dall'input dell'utente
    porta_alta = int(intervallo_porte.split("-")[1]) #estrae i vaolri massimi delle porte dall'input dell utente

    print(f"Scansione host", {obiettivo_ip}, "da porta", {porta_bassa}, "a porta", {porta_alta})
    scanner(porta_bassa, porta_alta, obiettivo_ip)

def scanner(porta_bassa, porta_alta, obiettivo_ip):

    for porta in range(porta_bassa, porta_alta):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status = s.connect_ex((obiettivo_ip, porta)) #tentativo di connessione alla porta indicata
        if status == 0: #se la connessione ha successo vuol dire che la porta è aperta
            print("*** Port", porta, "- APERTA ***")
        # se non restituisce niente vuol dire che la porta è chiusa

    s.close()

if __name__ == "__main__":
    main()
