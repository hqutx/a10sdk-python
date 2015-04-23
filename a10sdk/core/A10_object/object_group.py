from a10sdk.common.A10BaseClass import A10BaseClass


class ObjectGroup(A10BaseClass):
    
    """Class Description::
    Configure Object Group.

    Class object-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param network_list: {"minItems": 1, "items": {"type": "network"}, "uniqueItems": true, "array": [{"required": ["net-name"], "properties": {"rules": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"host-v6": {"type": "string", "description": "IPv6 Host Address", "format": "ipv6-address"}, "subnet": {"type": "string", "description": "IPv4 Network Address", "format": "ipv4-address"}, "host-v4": {"type": "string", "description": "IPv4 Host Address", "format": "ipv4-address"}, "ipv6-subnet": {"type": "string", "description": "IPv6 Network Address", "format": "ipv6-address-plen"}, "seq-num": {"description": "Sequence number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}, "rev-subnet-mask": {"type": "string", "description": "Network Mask. 0=apply, 255=ignore", "format": "ipv4-rev-netmask"}, "optional": true, "any": {"default": 0, "type": "number", "description": "Any host", "format": "flag"}}}]}, "net-name": {"description": "Network Object Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "description": {"description": "Description of the object-group instance", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/object-group/network/{net-name}"}
    :param service_list: {"minItems": 1, "items": {"type": "service"}, "uniqueItems": true, "array": [{"required": ["svc-name"], "properties": {"rules": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"icmp-type": {"description": "ICMP type number", "format": "number", "not-list": ["any-type", "special-type"], "maximum": 254, "minimum": 0, "type": "number"}, "icmpv6-code": {"description": "ICMPv6 code number", "format": "number", "not-list": ["v6-any-code", "special-v6-code"], "maximum": 254, "minimum": 0, "type": "number"}, "lt-src": {"description": "Match only packets with a lower port number", "minimum": 2, "type": "number", "maximum": 65535, "format": "number"}, "eq-dst": {"description": "Match only packets on a given destination port (port number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "range-dst": {"description": "Match only packets in the range of port numbers (Starting Destination Port Number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "seq-num": {"description": "Sequence number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}, "source": {"default": 0, "type": "number", "description": "Source Port Information", "format": "flag"}, "eq-src": {"description": "Match only packets on a given source port (port number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "v6-any-code": {"default": 0, "not-list": ["icmpv6-code", "special-v6-code"], "type": "number", "description": "Any ICMPv6 code", "format": "flag"}, "icmpv6-type": {"description": "ICMPv6 type number", "format": "number", "not-list": ["v6-any-type", "special-v6-type"], "maximum": 254, "minimum": 0, "type": "number"}, "icmp-code": {"description": "ICMP code number", "format": "number", "not-list": ["any-code", "special-code"], "maximum": 254, "minimum": 0, "type": "number"}, "special-code": {"not-list": ["any-code", "icmp-code"], "enum": ["frag-required", "host-unreachable", "network-unreachable", "port-unreachable", "proto-unreachable", "route-failed"], "type": "string", "description": "'frag-required': Code 4, fragmentation required; 'host-unreachable': Code 1, destination host unreachable; 'network-unreachable': Code 0, destination network unreachable; 'port-unreachable': Code 3, destination port unreachable; 'proto-unreachable': Code 2, destination protocol unreachable; 'route-failed': Code 5, source route failed; ", "format": "enum"}, "tcp-udp": {"enum": ["tcp", "udp"], "type": "string", "description": "'tcp': Protocol TCP; 'udp': Protocol UDP; ", "format": "enum"}, "gt-dst": {"description": "Match only packets with a greater port number", "minimum": 1, "type": "number", "maximum": 65534, "format": "number"}, "icmp": {"default": 0, "type": "number", "description": "Internet Control Message Protocol", "format": "flag"}, "optional": true, "port-num-end-src": {"description": "Ending Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "special-v6-type": {"not-list": ["icmpv6-type", "v6-any-type"], "enum": ["dest-unreachable", "echo-reply", "echo-request", "packet-too-big", "param-prob", "time-exceeded"], "type": "string", "description": "'dest-unreachable': Type 1, destination unreachable; 'echo-reply': Type 129, echo reply; 'echo-request': Type 128, echo request; 'packet-too-big': Type 2, packet too big; 'param-prob': Type 4, parameter problem; 'time-exceeded': Type 3, time exceeded; ", "format": "enum"}, "any-type": {"default": 0, "not-list": ["icmp-type", "special-type"], "type": "number", "description": "Any ICMP type", "format": "flag"}, "lt-dst": {"description": "Match only packets with a lesser port number", "minimum": 2, "type": "number", "maximum": 65535, "format": "number"}, "gt-src": {"description": "Match only packets with a greater port number", "minimum": 1, "type": "number", "maximum": 65534, "format": "number"}, "special-v6-code": {"not-list": ["v6-any-code", "icmpv6-code"], "enum": ["addr-unreachable", "admin-prohibited", "no-route", "not-neighbour", "port-unreachable"], "type": "string", "description": "'addr-unreachable': Code 3, address unreachable; 'admin-prohibited': Code 1, admin prohibited; 'no-route': Code 0, no route to destination; 'not-neighbour': Code 2, not neighbor; 'port-unreachable': Code 4, destination port unreachable; ", "format": "enum"}, "icmpv6": {"default": 0, "type": "number", "description": "Internet Control Message Protocol version 6", "format": "flag"}, "range-src": {"description": "match only packets in the range of port numbers (Starting Port Number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "port-num-end-dst": {"description": "Ending Destination Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "v6-any-type": {"default": 0, "not-list": ["icmpv6-type", "special-v6-type"], "type": "number", "description": "Any ICMP type", "format": "flag"}, "any-code": {"default": 0, "not-list": ["icmp-code", "special-code"], "type": "number", "description": "Any ICMP code", "format": "flag"}, "special-type": {"not-list": ["icmp-type", "any-type"], "enum": ["echo-reply", "echo-request", "info-reply", "info-request", "mask-reply", "mask-request", "parameter-problem", "redirect", "source-quench", "time-exceeded", "timestamp", "timestamp-reply", "dest-unreachable"], "type": "string", "description": "'echo-reply': Type 0, echo reply; 'echo-request': Type 8, echo request; 'info-reply': Type 16, information reply; 'info-request': Type 15, information request; 'mask-reply': Type 18, address mask reply; 'mask-request': Type 17, address mask request; 'parameter-problem': Type 12, parameter problem; 'redirect': Type 5, redirect message; 'source-quench': Type 4, source quench; 'time-exceeded': Type 11, time exceeded; 'timestamp': Type 13, timestamp; 'timestamp-reply': Type 14, timestamp reply; 'dest-unreachable': Type 3, destination unreachable; ", "format": "enum"}}}]}, "svc-name": {"description": "Service Object Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "description": {"description": "Description of the object-group instance", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/object-group/service/{svc-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/object-group`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "object-group"
        self.a10_url="/axapi/v3/object-group"
        self.DeviceProxy = ""
        self.network_list = []
        self.service_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


