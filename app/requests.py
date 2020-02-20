import urllib.request, json

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_URL']

def get_random_quote():
    """Obtains the quotes from the url"""

    with urllib.request.urlopen(base_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)
        print(quote_data)

    return quote_response