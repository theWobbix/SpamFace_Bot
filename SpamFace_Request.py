import urllib.parse as url_parse, urllib.request as url_request



def request(email, anmount):
    data = {"name": email}
    data_encoded = url_parse.urlencode(data)
    for x in range(0, anmount):
        url_request.urlopen("/login/device-based/regular/login/?login_attempt=1&amp;lwv=100", data_encoded)
    print("--------Job done!--------")



