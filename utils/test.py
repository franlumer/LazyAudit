from dataclasses import asdict
from models import CommandData, ScopeData, HostData
import json
import common
from pathlib import Path

#old_data = common.read_all(Path("utils/data.json"), CommandData)
#print(old_data)

#print(common.read_all(Path("utils/data.json"), CommandData)) # -> [Model(), Model()]

hosts = [
        HostData(
            ip="192.168.1.50",
            hostname="web-srv.test.local",
            ports=["22", "80", "443"],
            services=["OpenSSH 8.9p1", "Apache httpd 2.4.52"]
        ),
        HostData(
            ip="192.168.1.55",
            hostname="db-srv.test.local",
            ports=["3306"],
            services=["MySQL 8.0.32"]
        ),
        HostData(
            ip="10.10.20.15",
            hostname="dc01.corp.local",
            ports=["53", "88", "389", "445"],
            services=["DNS", "Kerberos", "LDAP", "SMB"]
        )
    ]

for host in hosts:
    print(host)

old_host = HostData(
            ip="192.168.1.50",
            hostname="web-srv.test.local",
            ports=["22", "80", "443"],
            services=["OpenSSH 8.9p1", "Apache httpd 2.4.52"]
        )

new_host = HostData(
            ip="nuevo",
            hostname="nuevo",
            ports=["nuevo"],
            services=["nuevo"]
        )

for host in hosts:
    if host == old_host:
        index = hosts.index(host)
        hosts[index] = new_host

for host in hosts:
    print(host)