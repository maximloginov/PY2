from typing import Union
import doctest

# 3 класса с документацией и аннотацией типов
class Computer:
    '''
    Class for computer description
    '''
    def __init__(self, name: str, ip: Union[str, None] = None):
        '''
        Computer initialization

        :param name: hostname (required)
        :param ip: IP-address (can be obtained from hostname)

        Examples:
        >>> c1 = Computer('work')  # initialize without IP-address
        >>> c2 = Computer('home', '127.0.0.1')  # with valid IP-address
        >>> c3 = Computer('home', '127.0.0')  # with invalid IP-address
        Traceback (most recent call last):
        ...
        ValueError: address/netmask is invalid: 127.0.0
        '''
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Hostname should be a string, not {type(name)}')
        self.ip = ip
        self.ip_init()

    def ip_init(self) -> bool:
        '''
        Initialize and validate IP-address

        Examples:
        >>> c1 = Computer('home')
        >>> c1.ip_init()
        '''

        if self.ip is None:
            self.ip = self.get_ip()

        # validate IP address
        return self.ip_is_valid()

    def get_ip(self) -> str:
        '''
        Obtain IP-address from computer name
        :return: IP-address

        Examples:
        >>> c1 = Computer('home')
        >>> c1.get_ip()
        '0.0.0.0'
        '''
        # TODO: get IP-address from known self.name
        ip = '0.0.0.0'
        return ip


    def ip_is_valid(self) -> bool:
        '''
        Validate IP-address to be a valid IPv4 address
        :return: True if computer's IP-address is valid

        :raise: Val
        '''
        import ipaddress

        try:
            self.ip = str(ipaddress.ip_address(self.ip))
        except ValueError:
            print(f'Address is invalid: %s' % self.ip)


if __name__ == "__main__":
    # работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
