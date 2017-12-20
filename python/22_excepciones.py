from libs.urlloader import load_url
from urllib.error import HTTPError

try:
    raise Exception('bu')
    print('funcionaraa?')
except Exception as error:
    print('ha fallao :',error)

try:
    load_url("http://estonoesistenide.com")
except Exception as error:
    print('ha fallao :',error)