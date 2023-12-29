import os


def generate_key(client_ip, server_ip):
    if client_ip in os.listdir(f"/etc/wireguard/clients"):
        print('exist')
    else:
        os.system(f"sudo bash /usr/local/bin/wireguard-keygen.sh -c {client_ip} -s {server_ip}")
    config_file = open(f"/etc/wireguard/clients/{client_ip}/client.conf").read()
    return config_file


generate_key("10.0.0.0", "20.111.24.98")
