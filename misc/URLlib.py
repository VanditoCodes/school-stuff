import urllib as ul
import webbrowser 

html = ul.request.urlopen('https://www.google.com')
parsing = ul.parse.urlparse('https://www.google.com')
print(parsing, '\n')

unparse = ul.parse.urlunparse(parsing)
print(unparse, '\n')

source = html.read()
status = html.getcode()
headers = html.headers
infor = html.info()
url = html.geturl()

webbrowser.open_new_tab('https:\\reddit.com')

print(source,'\n')
print(status,'\n')
print(headers,'\n')
print(infor,'\n')
print(url,'\n')
