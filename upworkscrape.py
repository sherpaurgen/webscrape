import requests
from lxml import html
payload = {
	"login[username]": "abc123@gmail.com", 
	"login[password]": "abcdxyz", 
	"login[_token]": "",
        "login[iovation]": "", 
        "login[redir]": "/home" 
}
header = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)"}
login_url = 'https://www.upwork.com/ab/account-security/login'
session_requests = requests.session()
result = session_requests.get(login_url)
tree=html.fromstring(result.text)
authenticity_token = list(set(tree.xpath('//*[@name="login[_token]"]/@value')))
print authenticity_token
print type(authenticity_token)

    
