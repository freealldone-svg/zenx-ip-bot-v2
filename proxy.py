import os


def get_proxy(filename):
    if not os.path.exists(filename):
        return None

    with open(filename, "r") as f:
        proxies = f.readlines()

    if len(proxies) == 0:
        return None

    proxy = proxies[0].strip()

    with open(filename, "w") as f:
        f.writelines(proxies[1:])

    return proxy
