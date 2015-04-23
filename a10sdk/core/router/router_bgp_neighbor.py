from a10sdk.common.A10BaseClass import A10BaseClass


class Neighbor(A10BaseClass):
    
    """Class Description::
    Specify a neighbor router.

    Class neighbor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param peer_group_neighbor_list: {"minItems": 1, "items": {"type": "peer-group-neighbor"}, "uniqueItems": true, "array": [{"required": ["peer-group"], "properties": {"activate": {"default": 1, "optional": true, "type": "number", "description": "Enable the Address Family for this Neighbor", "format": "flag"}, "route-refresh": {"default": 1, "optional": true, "type": "number", "description": "Advertise route-refresh capability to this neighbor", "format": "flag"}, "ve": {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "trunk", "lif"], "type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "optional": true, "format": "interface"}, "weight": {"description": "Set default weight for routes from this neighbor", "format": "number", "default": 0, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "timers-keepalive": {"description": "Keepalive interval", "format": "number", "default": 30, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "dynamic": {"default": 0, "optional": true, "type": "number", "description": "Advertise dynamic capability to this neighbor", "format": "flag"}, "loopback": {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "ve", "trunk", "lif"], "type": "number", "description": "Loopback interface (Port number)", "optional": true, "format": "interface"}, "default-originate": {"default": 0, "optional": true, "type": "number", "description": "Originate default route to this neighbor", "format": "flag"}, "distribute-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distribute-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "distribute-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (IP standard/extended/named access list)", "format": "string"}}}]}, "shutdown": {"default": 0, "optional": true, "type": "number", "description": "Administratively shut down this neighbor", "format": "flag"}, "prefix-list-direction": {"optional": true, "enum": ["both", "receive", "send"], "type": "string", "description": "'both': both; 'receive': receive; 'send': send; ", "format": "enum"}, "neighbor-route-map-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-rmap-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Apply route map to neighbor (Name of route map)", "format": "string"}}}]}, "advertisement-interval": {"description": "Minimum interval between sending BGP routing updates (time in seconds)", "format": "number", "type": "number", "maximum": 600, "minimum": 1, "optional": true}, "lif": {"description": "Logical interface (Lif interface number)", "format": "number", "optional": true, "not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "ve", "trunk"], "maximum": 128, "minimum": 1, "type": "number"}, "send-community-val": {"description": "'both': Send Standard and Extended Community attributes; 'none': Disable Sending Community attributes; 'standard': Send Standard Community attributes; 'extended': Send Extended Community attributes; ", "format": "enum", "default": "both", "type": "string", "enum": ["both", "none", "standard", "extended"], "optional": true}, "update-source-ip": {"not-list": ["update-source-ipv6", "ethernet", "loopback", "ve", "trunk", "lif"], "type": "string", "description": "IP address", "optional": true, "format": "ipv4-address"}, "collide-established": {"default": 0, "optional": true, "type": "number", "description": "Include Neighbor in Established State for Collision Detection", "format": "flag"}, "next-hop-self": {"default": 0, "optional": true, "type": "number", "description": "Disable the next hop calculation for this neighbor", "format": "flag"}, "pass-encrypted": {"optional": true, "type": "encrypted", "format": "encrypted"}, "peer-group": {"description": "Neighbor tag", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}, "dont-capability-negotiate": {"default": 0, "optional": true, "type": "number", "description": "Do not perform capability negotiation", "format": "flag"}, "unsuppress-map": {"description": "Route-map to selectively unsuppress suppressed routes (Name of route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "passive": {"default": 0, "optional": true, "type": "number", "description": "Don't send open messages to this neighbor", "format": "flag"}, "ebgp-multihop-hop-count": {"description": "maximum hop count", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "allowas-in": {"default": 0, "optional": true, "type": "number", "description": "Accept as-path with my AS present in it", "format": "flag"}, "pass-value": {"description": "Key String", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "timers-holdtime": {"description": "Holdtime", "format": "number", "default": 90, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "description": {"description": "Neighbor specific description (Up to 80 characters describing this neighbor)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 80, "type": "string"}, "inbound": {"default": 0, "optional": true, "type": "number", "description": "Allow inbound soft reconfiguration for this neighbor", "format": "flag"}, "maximum-prefix-thres": {"description": "threshold-value, 1 to 100 percent", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "neighbor-prefix-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-prefix-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-prefix-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (Name of a prefix list)", "format": "string"}}}]}, "peer-group-remote-as": {"description": "Specify AS number of BGP neighbor", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 1, "optional": true}, "disallow-infinite-holdtime": {"default": 0, "optional": true, "type": "number", "description": "BGP per neighbor disallow-infinite-holdtime", "format": "flag"}, "route-map": {"description": "Route-map to specify criteria to originate default (route-map name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "trunk": {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "ve", "lif"], "type": "number", "description": "Trunk interface (Trunk interface number)", "optional": true, "format": "interface"}, "remove-private-as": {"default": 0, "optional": true, "type": "number", "description": "Remove private AS number from outbound updates", "format": "flag"}, "neighbor-filter-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"filter-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Establish BGP filters (AS path access-list name)", "format": "string"}, "filter-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true}}]}, "update-source-ipv6": {"not-list": ["update-source-ip", "ethernet", "loopback", "ve", "trunk", "lif"], "type": "string", "description": "IPv6 address", "optional": true, "format": "ipv6-address"}, "maximum-prefix": {"description": "Maximum number of prefix accept from this peer (maximum no. of prefix limit (various depends on model))", "format": "number", "type": "number", "maximum": 65536, "minimum": 1, "optional": true}, "peer-group-key": {"default": 0, "optional": true, "type": "number", "description": "Configure peer-group", "format": "flag"}, "allowas-in-count": {"description": "Number of occurrences of AS number", "format": "number", "default": 3, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}, "as-origination-interval": {"description": "Minimum interval between sending AS-origination routing updates (time in seconds)", "format": "number", "type": "number", "maximum": 600, "minimum": 1, "optional": true}, "override-capability": {"default": 0, "optional": true, "type": "number", "description": "Override capability negotiation result", "format": "flag"}, "enforce-multihop": {"default": 0, "optional": true, "type": "number", "description": "Enforce EBGP neighbors to perform multihop", "format": "flag"}, "strict-capability-match": {"default": 0, "optional": true, "type": "number", "description": "Strict capability negotiation match", "format": "flag"}, "ebgp-multihop": {"default": 0, "optional": true, "type": "number", "description": "Allow EBGP neighbors not on directly connected networks", "format": "flag"}, "ethernet": {"not-list": ["update-source-ip", "update-source-ipv6", "loopback", "ve", "trunk", "lif"], "type": "number", "description": "Ethernet interface (Port number)", "optional": true, "format": "interface"}, "connect": {"description": "BGP connect timer", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/router/bgp/{as-number}/neighbor/peer-group-neighbor/{peer-group}"}
    :param ipv6_neighbor_list: {"minItems": 1, "items": {"type": "ipv6-neighbor"}, "uniqueItems": true, "array": [{"required": ["neighbor-ipv6"], "properties": {"activate": {"default": 1, "optional": true, "type": "number", "description": "Enable the Address Family for this Neighbor", "format": "flag"}, "route-refresh": {"default": 1, "optional": true, "type": "number", "description": "Advertise route-refresh capability to this neighbor", "format": "flag"}, "ve": {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "trunk", "lif"], "type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "optional": true, "format": "interface"}, "weight": {"description": "Set default weight for routes from this neighbor", "format": "number", "default": 0, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "timers-keepalive": {"description": "Keepalive interval", "format": "number", "default": 30, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "bfd-value": {"description": "Key String", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "key-type": {"optional": true, "enum": ["md5", "meticulous-md5", "meticulous-sha1", "sha1", "simple"], "type": "string", "description": "'md5': md5; 'meticulous-md5': meticulous-md5; 'meticulous-sha1': meticulous-sha1; 'sha1': sha1; 'simple': simple;  (Keyed MD5/Meticulous Keyed MD5/Meticulous Keyed SHA1/Keyed SHA1/Simple Password)", "format": "enum"}, "dynamic": {"default": 0, "optional": true, "type": "number", "description": "Advertise dynamic capability to this neighbor", "format": "flag"}, "loopback": {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "ve", "trunk", "lif"], "type": "number", "description": "Loopback interface (Port number)", "optional": true, "format": "interface"}, "multihop": {"default": 0, "optional": true, "type": "number", "description": "Enable multihop", "format": "flag"}, "default-originate": {"description": "Originate default route to this neighbor", "format": "flag", "default": 0, "optional": true, "not": "peer-group-name", "type": "number"}, "distribute-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distribute-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "distribute-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (IP standard/extended/named access list)", "format": "string"}}}]}, "shutdown": {"default": 0, "optional": true, "type": "number", "description": "Administratively shut down this neighbor", "format": "flag"}, "prefix-list-direction": {"optional": true, "enum": ["both", "receive", "send"], "type": "string", "description": "'both': both; 'receive': receive; 'send': send; ", "format": "enum"}, "nbr-remote-as": {"description": "Specify AS number of BGP neighbor", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 1, "optional": true}, "description": {"description": "Neighbor specific description (Up to 80 characters describing this neighbor)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 80, "type": "string"}, "advertisement-interval": {"description": "Minimum interval between sending BGP routing updates (time in seconds)", "format": "number", "optional": true, "maximum": 600, "minimum": 1, "not": "peer-group-name", "type": "number"}, "lif": {"description": "Logical interface (Lif interface number)", "format": "number", "optional": true, "not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "ve", "trunk"], "maximum": 128, "minimum": 1, "type": "number"}, "neighbor-route-map-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-rmap-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Apply route map to neighbor (Name of route map)", "format": "string"}}}]}, "send-community-val": {"description": "'both': Send Standard and Extended Community attributes; 'none': Disable Sending Community attributes; 'standard': Send Standard Community attributes; 'extended': Send Extended Community attributes; ", "format": "enum", "default": "both", "type": "string", "enum": ["both", "none", "standard", "extended"], "optional": true}, "bfd": {"default": 0, "optional": true, "type": "number", "description": "Bidirectional Forwarding Detection (BFD)", "format": "flag"}, "collide-established": {"default": 0, "optional": true, "type": "number", "description": "Include Neighbor in Established State for Collision Detection", "format": "flag"}, "next-hop-self": {"description": "Disable the next hop calculation for this neighbor", "format": "flag", "default": 0, "optional": true, "not": "peer-group-name", "type": "number"}, "pass-encrypted": {"optional": true, "type": "encrypted", "format": "encrypted"}, "dont-capability-negotiate": {"default": 0, "optional": true, "type": "number", "description": "Do not perform capability negotiation", "format": "flag"}, "unsuppress-map": {"description": "Route-map to selectively unsuppress suppressed routes (Name of route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "not": "peer-group-name", "type": "string"}, "passive": {"default": 0, "optional": true, "type": "number", "description": "Don't send open messages to this neighbor", "format": "flag"}, "ebgp-multihop-hop-count": {"description": "maximum hop count", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "allowas-in": {"default": 0, "optional": true, "type": "number", "description": "Accept as-path with my AS present in it", "format": "flag"}, "pass-value": {"description": "Key String", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "key-id": {"description": "Key ID", "format": "number", "type": "number", "maximum": 255, "minimum": 0, "optional": true}, "timers-holdtime": {"description": "Holdtime", "format": "number", "default": 90, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "update-source-ip": {"not-list": ["update-source-ipv6", "ethernet", "loopback", "ve", "trunk", "lif"], "type": "string", "description": "IP address", "optional": true, "format": "ipv4-address"}, "neighbor-ipv6": {"optional": false, "type": "string", "description": "Neighbor IPv6 address", "format": "ipv6-address"}, "inbound": {"default": 0, "optional": true, "type": "number", "description": "Allow inbound soft reconfiguration for this neighbor", "format": "flag"}, "maximum-prefix-thres": {"description": "threshold-value, 1 to 100 percent", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "bfd-encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}, "disallow-infinite-holdtime": {"description": "BGP per neighbor disallow-infinite-holdtime", "format": "flag", "default": 0, "optional": true, "not": "peer-group-name", "type": "number"}, "route-map": {"description": "Route-map to specify criteria to originate default (route-map name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "trunk": {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "ve", "lif"], "type": "number", "description": "Trunk interface (Trunk interface number)", "optional": true, "format": "interface"}, "remove-private-as": {"default": 0, "optional": true, "type": "number", "description": "Remove private AS number from outbound updates", "format": "flag"}, "neighbor-filter-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"filter-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Establish BGP filters (AS path access-list name)", "format": "string"}, "filter-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true}}]}, "update-source-ipv6": {"not-list": ["update-source-ip", "ethernet", "loopback", "ve", "trunk", "lif"], "type": "string", "description": "IPv6 address", "optional": true, "format": "ipv6-address"}, "maximum-prefix": {"description": "Maximum number of prefix accept from this peer (maximum no. of prefix limit (various depends on model))", "format": "number", "type": "number", "maximum": 65536, "minimum": 1, "optional": true}, "neighbor-prefix-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-prefix-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-prefix-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (Name of a prefix list)", "format": "string"}}}]}, "allowas-in-count": {"description": "Number of occurrences of AS number", "format": "number", "default": 3, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}, "peer-group-name": {"description": "Configure peer-group (peer-group name)", "format": "string", "minLength": 1, "not-list": ["advertisement-interval", "as-origination-interval", "default-originate", "disallow-infinite-holdtime", "next-hop-self", "timers", "unsuppress-map"], "optional": true, "maxLength": 128, "type": "string"}, "as-origination-interval": {"description": "Minimum interval between sending AS-origination routing updates (time in seconds)", "format": "number", "optional": true, "maximum": 600, "minimum": 1, "not": "peer-group-name", "type": "number"}, "override-capability": {"default": 0, "optional": true, "type": "number", "description": "Override capability negotiation result", "format": "flag"}, "enforce-multihop": {"default": 0, "optional": true, "type": "number", "description": "Enforce EBGP neighbors to perform multihop", "format": "flag"}, "strict-capability-match": {"default": 0, "optional": true, "type": "number", "description": "Strict capability negotiation match", "format": "flag"}, "ebgp-multihop": {"default": 0, "optional": true, "type": "number", "description": "Allow EBGP neighbors not on directly connected networks", "format": "flag"}, "ethernet": {"not-list": ["update-source-ip", "update-source-ipv6", "loopback", "ve", "trunk", "lif"], "type": "number", "description": "Ethernet interface (Port number)", "optional": true, "format": "interface"}, "connect": {"description": "BGP connect timer", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/router/bgp/{as-number}/neighbor/ipv6-neighbor/{neighbor-ipv6}"}
    :param ipv4_neighbor_list: {"minItems": 1, "items": {"type": "ipv4-neighbor"}, "uniqueItems": true, "array": [{"required": ["neighbor-ipv4"], "properties": {"activate": {"default": 1, "optional": true, "type": "number", "description": "Enable the Address Family for this Neighbor", "format": "flag"}, "route-refresh": {"default": 1, "optional": true, "type": "number", "description": "Advertise route-refresh capability to this neighbor", "format": "flag"}, "ve": {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "trunk", "lif"], "type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "optional": true, "format": "interface"}, "weight": {"description": "Set default weight for routes from this neighbor", "format": "number", "default": 0, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "timers-keepalive": {"description": "Keepalive interval", "format": "number", "default": 30, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "bfd-value": {"description": "Key String", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "key-type": {"optional": true, "enum": ["md5", "meticulous-md5", "meticulous-sha1", "sha1", "simple"], "type": "string", "description": "'md5': md5; 'meticulous-md5': meticulous-md5; 'meticulous-sha1': meticulous-sha1; 'sha1': sha1; 'simple': simple;  (Keyed MD5/Meticulous Keyed MD5/Meticulous Keyed SHA1/Keyed SHA1/Simple Password)", "format": "enum"}, "dynamic": {"default": 0, "optional": true, "type": "number", "description": "Advertise dynamic capability to this neighbor", "format": "flag"}, "loopback": {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "ve", "trunk", "lif"], "type": "number", "description": "Loopback interface (Port number)", "optional": true, "format": "interface"}, "multihop": {"default": 0, "optional": true, "type": "number", "description": "Enable multihop", "format": "flag"}, "default-originate": {"description": "Originate default route to this neighbor", "format": "flag", "default": 0, "optional": true, "not": "peer-group-name", "type": "number"}, "distribute-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distribute-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "distribute-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (IP standard/extended/named access list)", "format": "string"}}}]}, "shutdown": {"default": 0, "optional": true, "type": "number", "description": "Administratively shut down this neighbor", "format": "flag"}, "prefix-list-direction": {"optional": true, "enum": ["both", "receive", "send"], "type": "string", "description": "'both': both; 'receive': receive; 'send': send; ", "format": "enum"}, "as-origination-interval": {"description": "Minimum interval between sending AS-origination routing updates (time in seconds)", "format": "number", "optional": true, "maximum": 600, "minimum": 1, "not": "peer-group-name", "type": "number"}, "nbr-remote-as": {"description": "Specify AS number of BGP neighbor", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 1, "optional": true}, "advertisement-interval": {"description": "Minimum interval between sending BGP routing updates (time in seconds)", "format": "number", "optional": true, "maximum": 600, "minimum": 1, "not": "peer-group-name", "type": "number"}, "lif": {"description": "Logical interface (Lif interface number)", "format": "number", "optional": true, "not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "ve", "trunk"], "maximum": 128, "minimum": 1, "type": "number"}, "neighbor-route-map-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-rmap-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Apply route map to neighbor (Name of route map)", "format": "string"}}}]}, "send-community-val": {"description": "'both': Send Standard and Extended Community attributes; 'none': Disable Sending Community attributes; 'standard': Send Standard Community attributes; 'extended': Send Extended Community attributes; ", "format": "enum", "default": "both", "type": "string", "enum": ["both", "none", "standard", "extended"], "optional": true}, "bfd": {"default": 0, "optional": true, "type": "number", "description": "Bidirectional Forwarding Detection (BFD)", "format": "flag"}, "collide-established": {"default": 0, "optional": true, "type": "number", "description": "Include Neighbor in Established State for Collision Detection", "format": "flag"}, "next-hop-self": {"description": "Disable the next hop calculation for this neighbor", "format": "flag", "default": 0, "optional": true, "not": "peer-group-name", "type": "number"}, "pass-encrypted": {"optional": true, "type": "encrypted", "format": "encrypted"}, "dont-capability-negotiate": {"default": 0, "optional": true, "type": "number", "description": "Do not perform capability negotiation", "format": "flag"}, "unsuppress-map": {"description": "Route-map to selectively unsuppress suppressed routes (Name of route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "not": "peer-group-name", "type": "string"}, "passive": {"default": 0, "optional": true, "type": "number", "description": "Don't send open messages to this neighbor", "format": "flag"}, "ebgp-multihop-hop-count": {"description": "maximum hop count", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "allowas-in": {"default": 0, "optional": true, "type": "number", "description": "Accept as-path with my AS present in it", "format": "flag"}, "pass-value": {"description": "Key String", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "key-id": {"description": "Key ID", "format": "number", "type": "number", "maximum": 255, "minimum": 0, "optional": true}, "timers-holdtime": {"description": "Holdtime", "format": "number", "default": 90, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "update-source-ip": {"not-list": ["update-source-ipv6", "ethernet", "loopback", "ve", "trunk", "lif"], "type": "string", "description": "IP address", "optional": true, "format": "ipv4-address"}, "description": {"description": "Neighbor specific description (Up to 80 characters describing this neighbor)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 80, "type": "string"}, "neighbor-ipv4": {"optional": false, "type": "string", "description": "Neighbor address", "format": "ipv4-address"}, "inbound": {"default": 0, "optional": true, "type": "number", "description": "Allow inbound soft reconfiguration for this neighbor", "format": "flag"}, "maximum-prefix-thres": {"description": "threshold-value, 1 to 100 percent", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "bfd-encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}, "disallow-infinite-holdtime": {"description": "BGP per neighbor disallow-infinite-holdtime", "format": "flag", "default": 0, "optional": true, "not": "peer-group-name", "type": "number"}, "trunk": {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "ve", "lif"], "type": "number", "description": "Trunk interface (Trunk interface number)", "optional": true, "format": "interface"}, "remove-private-as": {"default": 0, "optional": true, "type": "number", "description": "Remove private AS number from outbound updates", "format": "flag"}, "neighbor-filter-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"filter-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Establish BGP filters (AS path access-list name)", "format": "string"}, "filter-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true}}]}, "update-source-ipv6": {"not-list": ["update-source-ip", "ethernet", "loopback", "ve", "trunk", "lif"], "type": "string", "description": "IPv6 address", "optional": true, "format": "ipv6-address"}, "maximum-prefix": {"description": "Maximum number of prefix accept from this peer (maximum no. of prefix limit (various depends on model))", "format": "number", "type": "number", "maximum": 65536, "minimum": 1, "optional": true}, "neighbor-prefix-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-prefix-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-prefix-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (Name of a prefix list)", "format": "string"}}}]}, "allowas-in-count": {"description": "Number of occurrences of AS number", "format": "number", "default": 3, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}, "peer-group-name": {"description": "Configure peer-group (peer-group name)", "format": "string", "minLength": 1, "not-list": ["advertisement-interval", "as-origination-interval", "default-originate", "disallow-infinite-holdtime", "next-hop-self", "timers", "unsuppress-map"], "optional": true, "maxLength": 128, "type": "string"}, "enforce-multihop": {"default": 0, "optional": true, "type": "number", "description": "Enforce EBGP neighbors to perform multihop", "format": "flag"}, "override-capability": {"default": 0, "optional": true, "type": "number", "description": "Override capability negotiation result", "format": "flag"}, "route-map": {"description": "Route-map to specify criteria to originate default (route-map name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "strict-capability-match": {"default": 0, "optional": true, "type": "number", "description": "Strict capability negotiation match", "format": "flag"}, "ebgp-multihop": {"default": 0, "optional": true, "type": "number", "description": "Allow EBGP neighbors not on directly connected networks", "format": "flag"}, "ethernet": {"not-list": ["update-source-ip", "update-source-ipv6", "loopback", "ve", "trunk", "lif"], "type": "number", "description": "Ethernet interface (Port number)", "optional": true, "format": "interface"}, "connect": {"description": "BGP connect timer", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/router/bgp/{as-number}/neighbor/ipv4-neighbor/{neighbor-ipv4}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/neighbor`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "neighbor"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/neighbor"
        self.DeviceProxy = ""
        self.peer_group_neighbor_list = []
        self.ipv6_neighbor_list = []
        self.ipv4_neighbor_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


