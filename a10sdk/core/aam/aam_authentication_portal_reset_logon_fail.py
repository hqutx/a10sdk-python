from a10sdk.common.A10BaseClass import A10BaseClass


class ResetLogonFail(A10BaseClass):
    
    """Class Description::
    Reset default portal logon fail page configuration.

    Class reset-logon-fail supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param reset: {"default": 0, "optional": true, "type": "number", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/portal/{name}/reset-logon-fail`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "reset-logon-fail"
        self.a10_url="/axapi/v3/aam/authentication/portal/{name}/reset-logon-fail"
        self.DeviceProxy = ""
        self.reset = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


