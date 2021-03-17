from OpenSSL import SSL
import socket
from threading import Thread
from ssl import PROTOCOL_TLSv1


def get_cert(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        sock.connect((host, int(port)))
    except socket.timeout as e:
        print(f'{host}, {port}, {e}')
        return
    except ConnectionRefusedError as e:
        print(f'{host}, {port}, {e}')
        return
    sock.settimeout(None)
    osobj = SSL.Context(PROTOCOL_TLSv1)
    oscon = SSL.Connection(osobj, sock)
    oscon.set_tlsext_host_name(host.encode())
    oscon.set_connect_state()
    try:
        oscon.do_handshake()
    except SSL.SysCallError as e:
        print(f'{host}, {port}, {e}')
        return
    except SSL.Error:
        print(f'{host}, {port}, {e}')
        return
    cert = oscon.get_peer_certificate()
    sock.close()
    print(f'{host}, {port}, {cert}')
    return cert

ports = [
    443,
    8081,
    8443,
    8083,
]

def main():
    for host in hosts:
        for port in ports:
            # cert = get_cert(host, port)
            thread = Thread(target=get_cert, args=[host, port])
            thread.start()


hosts = [
    # "google.com",
    # "facebook.com",
    # "youtube.com",
    # "twitter.com",
    # "spotify.com",

    "10.106.192.1",
    "10.106.192.2",
    "10.106.192.3",
    "10.106.192.4",
    "10.106.192.5",
    "10.106.192.6",
    "10.106.192.7",
    "10.106.192.8",
    "10.106.192.9",
    "10.106.192.10",
    "10.106.192.11",
    "10.106.192.12",
    "10.106.192.13",
    "10.106.192.14",
    "10.106.192.15",
    "10.106.192.16",
    "10.106.192.17",
    "10.106.192.18",
    "10.106.192.19",
    "10.106.192.20",
    "10.106.192.21",
    "10.106.192.22",
    "10.106.192.23",
    "10.106.192.24",
    "10.106.192.25",
    "10.106.192.26",
    "10.106.192.27",
    "10.106.192.28",
    "10.106.192.29",
    "10.106.192.30",
    "10.106.192.31",
    "10.106.192.32",
    "10.106.192.33",
    "10.106.192.34",
    "10.106.192.35",
    "10.106.192.36",
    "10.106.192.37",
    "10.106.192.38",
    "10.106.192.39",
    "10.106.192.40",
    "10.106.192.41",
    "10.106.192.42",
    "10.106.192.43",
    "10.106.192.44",
    "10.106.192.45",
    "10.106.192.46",
    "10.106.192.47",
    "10.106.192.48",
    "10.106.192.49",
    "10.106.192.50",
    "10.106.192.51",
    "10.106.192.52",
    "10.106.192.53",
    "10.106.192.54",
    "10.106.192.55",
    "10.106.192.56",
    "10.106.192.57",
    "10.106.192.58",
    "10.106.192.59",
    "10.106.192.60",
    "10.106.192.61",
    "10.106.192.62",
    "10.106.192.63",
    "10.106.192.64",
    "10.106.192.65",
    "10.106.192.66",
    "10.106.192.67",
    "10.106.192.68",
    "10.106.192.69",
    "10.106.192.70",
    "10.106.192.71",
    "10.106.192.72",
    "10.106.192.73",
    "10.106.192.74",
    "10.106.192.75",
    "10.106.192.76",
    "10.106.192.77",
    "10.106.192.78",
    "10.106.192.79",
    "10.106.192.80",
    "10.106.192.81",
    "10.106.192.82",
    "10.106.192.83",
    "10.106.192.84",
    "10.106.192.85",
    "10.106.192.86",
    "10.106.192.87",
    "10.106.192.88",
    "10.106.192.89",
    "10.106.192.90",
    "10.106.192.91",
    "10.106.192.92",
    "10.106.192.93",
    "10.106.192.94",
    "10.106.192.95",
    "10.106.192.96",
    "10.106.192.97",
    "10.106.192.98",
    "10.106.192.99",
    "10.106.192.100",
    "10.106.192.101",
    "10.106.192.102",
    "10.106.192.103",
    "10.106.192.104",
    "10.106.192.105",
    "10.106.192.106",
    "10.106.192.107",
    "10.106.192.108",
    "10.106.192.109",
    "10.106.192.110",
    "10.106.192.111",
    "10.106.192.112",
    "10.106.192.113",
    "10.106.192.114",
    "10.106.192.115",
    "10.106.192.116",
    "10.106.192.117",
    "10.106.192.118",
    "10.106.192.119",
    "10.106.192.120",
    "10.106.192.121",
    "10.106.192.122",
    "10.106.192.123",
    "10.106.192.124",
    "10.106.192.125",
    "10.106.192.126",
    "10.106.192.127",
    "10.106.192.128",
    "10.106.192.129",
    "10.106.192.130",
    "10.106.192.131",
    "10.106.192.132",
    "10.106.192.133",
    "10.106.192.134",
    "10.106.192.135",
    "10.106.192.136",
    "10.106.192.137",
    "10.106.192.138",
    "10.106.192.139",
    "10.106.192.140",
    "10.106.192.141",
    "10.106.192.142",
    "10.106.192.143",
    "10.106.192.144",
    "10.106.192.145",
    "10.106.192.146",
    "10.106.192.147",
    "10.106.192.148",
    "10.106.192.149",
    "10.106.192.150",
    "10.106.192.151",
    "10.106.192.152",
    "10.106.192.153",
    "10.106.192.154",
    "10.106.192.155",
    "10.106.192.156",
    "10.106.192.157",
    "10.106.192.158",
    "10.106.192.159",
    "10.106.192.160",
    "10.106.192.161",
    "10.106.192.162",
    "10.106.192.163",
    "10.106.192.164",
    "10.106.192.165",
    "10.106.192.166",
    "10.106.192.167",
    "10.106.192.168",
    "10.106.192.169",
    "10.106.192.170",
    "10.106.192.171",
    "10.106.192.172",
    "10.106.192.173",
    "10.106.192.174",
    "10.106.192.175",
    "10.106.192.176",
    "10.106.192.177",
    "10.106.192.178",
    "10.106.192.179",
    "10.106.192.180",
    "10.106.192.181",
    "10.106.192.182",
    "10.106.192.183",
    "10.106.192.184",
    "10.106.192.185",
    "10.106.192.186",
    "10.106.192.187",
    "10.106.192.188",
    "10.106.192.189",
    "10.106.192.190",
    "10.106.192.191",
    "10.106.192.192",
    "10.106.192.193",
    "10.106.192.194",
    "10.106.192.195",
    "10.106.192.196",
    "10.106.192.197",
    "10.106.192.198",
    "10.106.192.199",
    "10.106.192.200",
    "10.106.192.201",
    "10.106.192.202",
    "10.106.192.203",
    "10.106.192.204",
    "10.106.192.205",
    "10.106.192.206",
    "10.106.192.207",
    "10.106.192.208",
    "10.106.192.209",
    "10.106.192.210",
    "10.106.192.211",
    "10.106.192.212",
    "10.106.192.213",
    "10.106.192.214",
    "10.106.192.215",
    "10.106.192.216",
    "10.106.192.217",
    "10.106.192.218",
    "10.106.192.219",
    "10.106.192.220",
    "10.106.192.221",
    "10.106.192.222",
    "10.106.192.223",
    "10.106.192.224",
    "10.106.192.225",
    "10.106.192.226",
    "10.106.192.227",
    "10.106.192.228",
    "10.106.192.229",
    "10.106.192.230",
    "10.106.192.231",
    "10.106.192.232",
    "10.106.192.233",
    "10.106.192.234",
    "10.106.192.235",
    "10.106.192.236",
    "10.106.192.237",
    "10.106.192.238",
    "10.106.192.239",
    "10.106.192.240",
    "10.106.192.241",
    "10.106.192.242",
    "10.106.192.243",
    "10.106.192.244",
    "10.106.192.245",
    "10.106.192.246",
    "10.106.192.247",
    "10.106.192.248",
    "10.106.192.249",
    "10.106.192.250",
    "10.106.192.251",
    "10.106.192.252",
    "10.106.192.253",
    "10.106.192.254",
    "10.109.0.1",
    "10.109.0.2",
    "10.109.0.3",
    "10.109.0.4",
    "10.109.0.5",
    "10.109.0.6",
    "10.109.0.7",
    "10.109.0.8",
    "10.109.0.9",
    "10.109.0.10",
    "10.109.0.11",
    "10.109.0.12",
    "10.109.0.13",
    "10.109.0.14",
    "10.109.0.15",
    "10.109.0.16",
    "10.109.0.17",
    "10.109.0.18",
    "10.109.0.19",
    "10.109.0.20",
    "10.109.0.21",
    "10.109.0.22",
    "10.109.0.23",
    "10.109.0.24",
    "10.109.0.25",
    "10.109.0.26",
    "10.109.0.27",
    "10.109.0.28",
    "10.109.0.29",
    "10.109.0.30",
    "10.109.0.31",
    "10.109.0.32",
    "10.109.0.33",
    "10.109.0.34",
    "10.109.0.35",
    "10.109.0.36",
    "10.109.0.37",
    "10.109.0.38",
    "10.109.0.39",
    "10.109.0.40",
    "10.109.0.41",
    "10.109.0.42",
    "10.109.0.43",
    "10.109.0.44",
    "10.109.0.45",
    "10.109.0.46",
    "10.109.0.47",
    "10.109.0.48",
    "10.109.0.49",
    "10.109.0.50",
    "10.109.0.51",
    "10.109.0.52",
    "10.109.0.53",
    "10.109.0.54",
    "10.109.0.55",
    "10.109.0.56",
    "10.109.0.57",
    "10.109.0.58",
    "10.109.0.59",
    "10.109.0.60",
    "10.109.0.61",
    "10.109.0.62",
    "10.109.0.63",
    "10.109.0.64",
    "10.109.0.65",
    "10.109.0.66",
    "10.109.0.67",
    "10.109.0.68",
    "10.109.0.69",
    "10.109.0.70",
    "10.109.0.71",
    "10.109.0.72",
    "10.109.0.73",
    "10.109.0.74",
    "10.109.0.75",
    "10.109.0.76",
    "10.109.0.77",
    "10.109.0.78",
    "10.109.0.79",
    "10.109.0.80",
    "10.109.0.81",
    "10.109.0.82",
    "10.109.0.83",
    "10.109.0.84",
    "10.109.0.85",
    "10.109.0.86",
    "10.109.0.87",
    "10.109.0.88",
    "10.109.0.89",
    "10.109.0.90",
    "10.109.0.91",
    "10.109.0.92",
    "10.109.0.93",
    "10.109.0.94",
    "10.109.0.95",
    "10.109.0.96",
    "10.109.0.97",
    "10.109.0.98",
    "10.109.0.99",
    "10.109.0.100",
    "10.109.0.101",
    "10.109.0.102",
    "10.109.0.103",
    "10.109.0.104",
    "10.109.0.105",
    "10.109.0.106",
    "10.109.0.107",
    "10.109.0.108",
    "10.109.0.109",
    "10.109.0.110",
    "10.109.0.111",
    "10.109.0.112",
    "10.109.0.113",
    "10.109.0.114",
    "10.109.0.115",
    "10.109.0.116",
    "10.109.0.117",
    "10.109.0.118",
    "10.109.0.119",
    "10.109.0.120",
    "10.109.0.121",
    "10.109.0.122",
    "10.109.0.123",
    "10.109.0.124",
    "10.109.0.125",
    "10.109.0.126",
    "10.4.21.1",
    "10.4.21.2",
    "10.4.21.3",
    "10.4.21.4",
    "10.4.21.5",
    "10.4.21.6",
    "10.4.21.7",
    "10.4.21.8",
    "10.4.21.9",
    "10.4.21.10",
    "10.4.21.11",
    "10.4.21.12",
    "10.4.21.13",
    "10.4.21.14",
    "10.4.21.15",
    "10.4.21.16",
    "10.4.21.17",
    "10.4.21.18",
    "10.4.21.19",
    "10.4.21.20",
    "10.4.21.21",
    "10.4.21.22",
    "10.4.21.23",
    "10.4.21.24",
    "10.4.21.25",
    "10.4.21.26",
    "10.4.21.27",
    "10.4.21.28",
    "10.4.21.29",
    "10.4.21.30",
    "10.4.21.31",
    "10.4.21.32",
    "10.4.21.33",
    "10.4.21.34",
    "10.4.21.35",
    "10.4.21.36",
    "10.4.21.37",
    "10.4.21.38",
    "10.4.21.39",
    "10.4.21.40",
    "10.4.21.41",
    "10.4.21.42",
    "10.4.21.43",
    "10.4.21.44",
    "10.4.21.45",
    "10.4.21.46",
    "10.4.21.47",
    "10.4.21.48",
    "10.4.21.49",
    "10.4.21.50",
    "10.4.21.51",
    "10.4.21.52",
    "10.4.21.53",
    "10.4.21.54",
    "10.4.21.55",
    "10.4.21.56",
    "10.4.21.57",
    "10.4.21.58",
    "10.4.21.59",
    "10.4.21.60",
    "10.4.21.61",
    "10.4.21.62",
    "10.4.21.63",
    "10.4.21.64",
    "10.4.21.65",
    "10.4.21.66",
    "10.4.21.67",
    "10.4.21.68",
    "10.4.21.69",
    "10.4.21.70",
    "10.4.21.71",
    "10.4.21.72",
    "10.4.21.73",
    "10.4.21.74",
    "10.4.21.75",
    "10.4.21.76",
    "10.4.21.77",
    "10.4.21.78",
    "10.4.21.79",
    "10.4.21.80",
    "10.4.21.81",
    "10.4.21.82",
    "10.4.21.83",
    "10.4.21.84",
    "10.4.21.85",
    "10.4.21.86",
    "10.4.21.87",
    "10.4.21.88",
    "10.4.21.89",
    "10.4.21.90",
    "10.4.21.91",
    "10.4.21.92",
    "10.4.21.93",
    "10.4.21.94",
    "10.4.21.95",
    "10.4.21.96",
    "10.4.21.97",
    "10.4.21.98",
    "10.4.21.99",
    "10.4.21.100",
    "10.4.21.101",
    "10.4.21.102",
    "10.4.21.103",
    "10.4.21.104",
    "10.4.21.105",
    "10.4.21.106",
    "10.4.21.107",
    "10.4.21.108",
    "10.4.21.109",
    "10.4.21.110",
    "10.4.21.111",
    "10.4.21.112",
    "10.4.21.113",
    "10.4.21.114",
    "10.4.21.115",
    "10.4.21.116",
    "10.4.21.117",
    "10.4.21.118",
    "10.4.21.119",
    "10.4.21.120",
    "10.4.21.121",
    "10.4.21.122",
    "10.4.21.123",
    "10.4.21.124",
    "10.4.21.125",
    "10.4.21.126",
]


if __name__ == '__main__':
    main()
