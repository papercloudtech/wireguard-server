# WireGuard Server

This Django project serves as a robust enterprise-grade platform, providing users with a seamless web interface to configure, manage and automate WireGuard settings.

## Introduction

WireGuard is a modern, open-source VPN (Virtual Private Network) protocol designed to be fast, secure, and easy to use. It was created by Jason A. Donenfeld in 2015 and has gained significant attention and adoption due to its simplicity, performance, and focus on security. GUI implementations of WireGuard exists for platforms like Windows, Android and iOS. This project focuses on bringing the WireGuard CLI to the web, where a user is displayed a web interface to manage connections.

## Features

- **Manage Clients:** Manage clients with the interactive GUI, with client configs created in one click. Easily connect your device to the WireGuard tunnel with the QR code.
- **Performance Metrics:** View real-time performance metrics for each client connected to the server.

## Requirements

WireGuard CLI must be installed before running the server. To install WireGuard CLI on Linux, run the following command:

```sh
sudo apt-get install update
sudo apt-get install wireguard
```

## Installation

To install the WireGuard server in your machine, clone this repository.

```sh
cd ./wireguard-server/

```

Now, set-up a Python virtual environment as follows:

```sh
virtualenv -q ./venv/ && source ./venv/bin/activate
pip3 install -r ./requirements.txt
```

After that, make the initial migrations to the database as follows. Make sure to change the password and username/email based on your needs.

```sh
python3 ./manage.py makemigrations api
python3 ./manage.py migrate

DJANGO_SUPERUSER_PASSWORD=ec2-user@12345 python3 ./manage.py createsuperuser --noinput --username=admin --email=test-admin@papercloud.tech
```

Now, run start the server with the following command. Change the host and port based on your needs.

```sh
python3 ./manage.py runserver 0.0.0.0:80
```

The server will be running locally and can be accessed over HTTP at `localhost:<port>`.

## Contributing

We welcome contributions from the community to improve the project. If you'd like to contribute, please follow these guidelines:

1. **Fork the Repository**: Start by forking the repository to your GitHub account.
2. **Clone the Repository**: Clone the forked repository to your local machine using the `git clone` command.
    ```sh
    git clone https://github.com/your-username/repository-name.git
    ```
3. **Create a Branch**: Create a new branch for your contribution.
    ```sh
    git checkout -b feature/your-feature
    ```
4. **Make Changes**: Make your desired changes to the codebase.
5. **Test Your Changes**: Ensure that your changes don't introduce any new issues and pass any existing tests.
    ```sh
    python3 ./manage.py test
    ```
7. **Commit Your Changes**: Commit your changes with a descriptive commit message.
    ```sh
    git commit -m "feature: your feature description"
    ```
8. **Push Changes**: Push your changes to your forked repository.
    ```sh
    git push origin feature/your-feature
    ```
9. **Submit a Pull Request**: Finally, submit a pull request from your forked repository to the main repository. Be sure to provide a clear description of your changes and any related issues.

Once your pull request is submitted, it will be reviewed by the project maintainers. Thank you for contributing!

If you have any questions or need further assistance, feel free to open an issue/discussion or reach out to the project maintainers. We appreciate your support and contributions to the project!
