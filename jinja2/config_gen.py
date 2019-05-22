from jinja2 import Template

device = {
    "hostname":
    "eos01.jfk15",
    "vendor":
    "arista",
    "stp_mode":
    "rstp",
    "users": [{
        "name": "admin",
        "hash": "sha512",
        "secret":
        "$6$GiRTv1P/fZu.2gXH$r0Q.8VBMYwJuRv0QXrlMw4qzCM8Nxonrpop5/8HiY",
        "priviledge": 15,
        "role": "network-admin"
    }, {
        "name": "admin1",
        "hash": "sha512",
        "secret":
        "f$5BKjFPbplejGbsFbMd78JjETMw1kja9XTnGaDqk39byr/EEV.lg3zR5UKWh",
        "priviledge": 15,
        "role": "network-admin"
    }],
    "interfaces": [{
        "ifname": "Ethernet1",
        "ip": "192.168.240.201",
        "netmask": "24",
        "state": "down"
    }, {
        "ifname": "Management1",
        "ip": "192.168.239.201",
        "netmask": "24",
        "state": "up"
    }]
}

with open("templates/{}/baseConfig.j2".format(device["vendor"])) as f_out:
    template = Template(f_out.read(), trim_blocks=True, lstrip_blocks=True)

template.stream(device=device).dump("outputs/{}/{}.conf".format(
    device["vendor"], device["hostname"]))
