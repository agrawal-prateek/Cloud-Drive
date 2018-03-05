import urllib.request

from requests import head


def get_page(url):
    """
    Fetch the content of a Webpage
    :param url: url of webpage
    :return: String
    """
    status = head(url).status_code

    if status == 200:
        file = urllib.request.urlopen(url)
        file = file.read().decode('utf-8')
        return file
    else:
        return False
