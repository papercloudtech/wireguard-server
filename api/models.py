from django.db import models
import ipaddress
import random
from .key_manager import generate_key, delete_key


class Client(models.Model):
    name = models.CharField(max_length=10)
    ip_address = models.GenericIPAddressField(protocol="ipv4", unique=True, null=True, blank=True)
    config = models.TextField(blank=True, null=True)
    SUBNET = "10.0.0.0/24"

    def gen_conf(self):
        return generate_key(self.ip_address)

    def _generate_unique_ip(self):
        network = ipaddress.ip_network(self.SUBNET)
        existing_ips = set(Client.objects.values_list('ip_address', flat=True))
        existing_ips.add("10.0.0.0")
        available_ips = [str(ip) for ip in network.hosts() if str(ip) not in existing_ips]

        if not available_ips:
            raise ValueError("Bla Failed")

        return random.choice(available_ips)

    def save(self, *args, **kwargs):
        if not self.ip_address:
            self.ip_address = self._generate_unique_ip()
        self.config = self.gen_conf()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        delete_key(self.ip_address)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.ip_address}'
