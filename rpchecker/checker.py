from http.client import HTTPConnection
from urllib.parse import urlparse


def check_sites_online(url, timeout=2):
    """
    :param url:
    :param timeout:
    :return: True if the site is online
    :raise: Exceptions if otherwise
    """

    error = Exception("Unknown errors")
    parser = urlparse(url)
    # uses the or operator to extract the hostname from the target URL.
    host = parser.netloc or parser.path.split("/")[0]
    # loop over http and https, check if sites available on either port
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as err:
            error = err
        finally:
            connection.close()
    raise error
