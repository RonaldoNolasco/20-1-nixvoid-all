import requests

url = "https://www.falabella.com.pe/falabella-pe/category/cat6370551/"

myGetRequest = requests.get(url)

print("HEADERS", myGetRequest.headers, end="\n-----------\n")
print("COOKIES", myGetRequest.cookies, end="\n-----------\n")
print("HTTP STATUS CODE", myGetRequest.status_code, end="\n-----------\n")
print("BODY RESPONSE", myGetRequest.text[:250], end="\n-----------\n")
