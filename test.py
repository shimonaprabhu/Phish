import requests
try:
    response = requests.get('https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_redirect_webpage')
    if response.history:
        print("Request was redirected")
        for resp in response.history:
            print(resp.status_code, resp.url)
        print("Final destination:")
        print(response.status_code, response.url)
    else:
        print("Request was not redirected")
except Exception as ex:
    template = "An exception of type {0} occurred."
    message = template.format(type(ex).__name__)
    print(message)
