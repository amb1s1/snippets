from netaddr import IPAddress


def check_for_private(func):
    def inside(src, dst):
        if IPAddress(src).is_private():
            print("This is a private IP. Public IP is needed")
            return
        func(src, dst)

    return inside


@check_for_private
def request_acl(src, dst):
    send = "acl from {} to {}".format(src, dst)
    print(send)
    return send

# first request
request_acl("8.8.8.8", "7.7.7.7")
# second request
request_acl("192.168.2.2", "7.7.7.7")
