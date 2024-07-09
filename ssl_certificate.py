import ssl
import socket
from datetime import datetime


class GetSslExpiryDate:
    def __init__(self, url):
        self.url = url

    def get_ssl_expiry_date(self):
        context = ssl.create_default_context()
        with socket.create_connection((self.url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=self.url) as ssock:
                certificate = ssock.getpeercert()
                expiry_date = datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
                return expiry_date


if __name__ == "__main__":
    url = 'www.ultimateqa.com'
    getExpiry_date = GetSslExpiryDate(url)
    expiry_date = getExpiry_date.get_ssl_expiry_date()
    print(f"The certificate expires on {expiry_date} for the site {url}")
