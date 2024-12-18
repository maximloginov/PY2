from typing import Union, Optional
import doctest


# 3 класса с документацией и аннотацией типов
class Computer:
    """
    Class for computer description
    """
    def __init__(self, name: str, ip: Union[str, None] = None):
        """
        Computer initialization

        :param name: hostname (required)
        :param ip: IP-address (can be obtained from hostname)

        Examples:
        >>> c1 = Computer('work')  # initialize without IP-address
        >>> c2 = Computer('home', '127.0.0.1')  # with valid IP-address
        >>> c3 = Computer('home', '127.0.0')  # with invalid IP-address
        Address is invalid: 127.0.0
        """
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Hostname should be a string, not {type(name)}')
        self.ip = ip
        self.ip_init()

    def ip_init(self) -> None:
        """
        Initialize and validate IP-address

        Examples:
        >>> c1 = Computer('home')
        >>> c1.ip_init()
        """

        if self.ip is None or not self.ip_is_valid():
            self.ip = self.get_ip()

    def get_ip(self) -> str:
        """
        Obtain IP-address from computer name

        :return: valid IP-address

        Examples:
        >>> c1 = Computer('home')
        >>> c1.get_ip()
        '0.0.0.0'
        """
        # TODO: get IP-address from known self.name
        ip = '0.0.0.0'
        return ip

    def ip_is_valid(self) -> bool:
        """
        Validate IP-address to be a valid IPv4 address

        :return: True if computer's IP-address is valid

        :raise: Val
        """
        import ipaddress

        try:
            self.ip = str(ipaddress.ip_address(self.ip))
        except ValueError:
            print(f'Address is invalid: %s' % self.ip)


class Room:
    """
    Class for computer room description
    """
    def __init__(self, number: str, address: str = '', computers: list = []):
        """
        Room initialization

        :param number: room number within building, can contain letters
        :param address: address of the building
        :param computers: list of computers in the room

        Examples:
        >>> r1 = Room('404', 'Molodezhnaya 7')
        >>> r2 = Room(404, 'Molodezhnaya 7')
        Traceback (most recent call last):
        ...
        TypeError: Room number should be a string, not <class 'int'>
        """
        if not isinstance(number, str):
            raise TypeError(f'Room number should be a string, not {type(number)}')
        self.number = number
        self.address = address
        self.computers = computers
        if self.computers:
            print(f'Room {self.number} at {self.address} has {len(self.computers)} initially')

    def add_computer(self, computer) -> None:
        """
        Adds a computer to the room.

        :param computer: ID of the computer to add.
        :type computer: str
        """
        self.computers.append(computer)

    def remove_computer(self, computer: str) -> None:
        """
        Removes a computer from the room.

        :param computer: ID of the computer to remove.
        :type computer: str
        """
        self.computers.remove(computer)

    def update_room_number(self, new_number: str) -> None:
        """
        Updates the room number.

        :param new_number: New unique identifier for the room.
        :type new_number: str

        :raises ValueError: If new_number is empty or None.
        """
        if not new_number:
            raise ValueError('Room number cannot be empty')
        self.number = new_number


class Student:
    """
    Represents a student with attributes for name and grade.

    :param name: Name of the student.
    :param grade: Grade of the student.

    Example usage:

    >>> student = Student('Ivan', initial_grade=85)
    >>> student.update_grade(90)
    >>> student.get_info()
    'Ivan: 90'

    :raises ValueError: If name is empty or None, or if new_grade is negative or None.
    """

    def __init__(self, name: str, initial_grade: Optional[float] = None):
        """
        Initializes a Student instance.

        :param name: Name of the student.
        :param initial_grade: Initial grade (default is None).

        :raises ValueError: If name is empty or None.
        """
        if not name:
            raise ValueError('Name cannot be empty')
        self.name = name
        self.grade = initial_grade or 0

    def update_grade(self, new_grade: float) -> None:
        """
        Updates the student's grade.

        :param new_grade: New grade value.
        :type new_grade: float

        :raises ValueError: If new_grade is negative or None.
        """
        if new_grade is None or new_grade < 0:
            raise ValueError('Grade cannot be negative or None')
        self.grade = new_grade

    def get_info(self) -> str:
        """
        Returns student information as a string.

        :return: Student name and grade.
        :rtype: str

        Example:

        >>> student = Student('Ivan', initial_grade=85)
        >>> student.get_info()
        'Ivan: 85'
        """
        return f'{self.name}: {self.grade}'


if __name__ == "__main__":
    # работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
