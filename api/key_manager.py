import os
import requests
from settings.settings import SERVER_IP


def generate_key(client_ip):
    clients_exist = os.path.exists("/etc/wireguard/clients")
    current_client_exist = False
    if clients_exist:
        current_client_exist = (client_ip in os.listdir("/etc/wireguard/clients"))
    if clients_exist and current_client_exist:
        print('exist')
    else:
        os.system(f"sudo bash /usr/local/bin/wireguard-keygen.sh -c {client_ip} -s {SERVER_IP}")
    config_file = open(f"/etc/wireguard/clients/{client_ip}/client.conf").read()
    return config_file


if __name__ == "__main__":
    generate_key("10.0.0.0")
