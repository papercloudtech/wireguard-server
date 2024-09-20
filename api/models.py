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
    
from django.db import models
from django.utils import timezone
import secrets
from datetime import timedelta


class ApiKey(models.Model):
    key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        super().save(*args, **kwargs)

    def generate_key(self):
        return secrets.token_urlsafe(32)

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return self.key
