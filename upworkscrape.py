auth_iovation=['0400R9HVeoYv1gsNf94lis1zttBaVgjxlOd9G5mKV1GZGzZSop9ypcPEXI5oXH2S9TyVNt+dt8oFkemEzbpe+buO7ZwSX/4nfMUVFpGdpVdVZ9NIwoY8ye2u0nVLKa5eUqvJ5dzgojLfFGvNZhMeU+JzHjGwbDZvHiYDvdxJYa0BAEAM9YLJcLTb+jC3o7rRuIcSieg/NH4QANooDvlKqcW/vqfjwy10nuf9GcsmEc9b0eK4xI1RTIYC8ouD71qCKcmZqa+c5UMfdLNXqLz+1vlqUAr9dE2jcfl0wgroQBfpyuK8rgZQmCLWSUmWqRbhankLVTw2C4oQ2p5KKlg2xwOLLtPtb5t32w+KwETIiPVSFifcStSNu1Xl/oLYP7ufXeh80VF0M8rwDyTDFE5gSrQclvq/WjGqvCm4898GnyP1mBxLEwrNkykUlAfOtP2LQF5swOGCmEaWeJamIif/iDuMCcLUB69g4E97xS9GTGQ/PXFcWfw6O4RWL8Cq9DH/qIFm+sD1cMLQtEUYRC+C1LD9N0OJ8ud7B93n1PXpN4zl2IQd/tZS2Kh2RIP19pEO+L+3J45cZKiZUIgGYUlMgPn7ZM3X8S8pWAYm7BFQVjvF0CKqWvTbz/c+r/WjyaLSKzyo5wV+AgR7vF857RHFZltZDHAARpnNaAPVT2H7xPRDcqJLh7h/QYTtLZw9tL9V8801cEW7a1ahvQSx5yLUw5qeIeCISazs9PD83/seKcOlvXrGxhKauwqEWLxUN0sYF8r08f8uCcC0xODcb+CqMKE6vZMBKj/vc4afHLamj4IfhjZMyPpjzYuuV+VhT2JQxvTdC24eZzo97tw16kQoiglK7BJDLfM/X8TvBZEph1nGneOS+l5gRh5xMwBs2slzAHmN+Z4baa9a0Da8VDdLGBfK9PH/LgnAtMTg/gz07uVSINAgzJ8FJa/++5dWoUSzxwidSY6DD27PAgoZ0j9B+el+NDmOz8ZKqlmCvGiUptSOhmfBhN1g6f3z3kFzXk4iBuEQLR05gJiGtJ/q3RrqkMib4nQiDB8wZGY2RgEqSehE5i2JsumimGcck5FSZLiQIceTtCd2sYZWcCQSXOjeK/DsKWxVYQhoLMwdw7yV1babUQ9E2YEMBkBTaOCnD/2Q9s6iZrisYxTUesMY/8C7OhCeBALsvmlxeuEfK36i8/SM0OL7FCcyNrG/WRRQDekNcfNFqzj8ZFJeItA4lrpTmKkV78jwjs5Ca2/wBdhim9vK/Ussl2RE758GOmPo8x0kvlsULg81FSfhWxvC9MW7pFSuew0Q6TwETk3CDw0jf8W5P+OtTHsYDK11f6QyD9AsUse5s1uDU9Qb5zoCbVPsheC1RMCLEoEF84TtY+iSZF0uVkHtNR+ZL9tds1oWgWjzTLaCDMsixzjjzthVJqKtzBRNTsBEyIj1UhYn3ErUjbtV5f6C2D+7n13ofNFRdDPK8A8kwxROYEq0HJb6v1oxqrwpuHvyqvlZTukHxnFOYX7+puQ=']
import requests
import re
from lxml import html
header = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)"}
login_url = 'https://www.upwork.com/ab/account-security/login'
session_requests = requests.session()
#get csrf
result = session_requests.get(login_url)
tree=html.fromstring(result.text)
auth_token = list(set(tree.xpath('//*[@name="login[_token]"]/@value')))
#auth_iovat = list(set(tree.xpath('//*[@name="login[iovation]"]/@value')))
# create payload
payload = {
	"login[username]": "addft@gmail.com", 
	"login[password]": "sdlkfjowe", 
	"login[_token]": auth_token,
        "login[iovation]": auth_iovation, 
        "login[redir]": "/home" 
}

#perform login
scrapeurl='https://www.upwork.com/ab/find-work/'
result=session_requests.post(login_url, data = payload, headers = dict(referer = login_url))
print result.text












