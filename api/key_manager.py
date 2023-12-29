import os


def generate_key(client_ip, server_ip):
    clients_exist = os.path.exists("/etc/wireguard/clients")
    current_client_exist = False
    if clients_exist:
        current_client_exist = (client_ip in os.listdir("/etc/wireguard/clients"))
    if clients_exist and current_client_exist:
        print('exist')
    else:
        os.system(f"sudo bash /usr/local/bin/wireguard-keygen.sh -c {client_ip} -s {server_ip}")
    config_file = open(f"/etc/wireguard/clients/{client_ip}/client.conf").read()
    return config_file


if __name__ == "__main__":
    generate_key("10.0.0.0", requests.get('https://checkip.amazonaws.com').text.strip())
