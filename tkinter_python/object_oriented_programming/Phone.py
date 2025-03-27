class Phone:
    def __init__(self, area_code, prefix, four_digits):
        self._area_code = area_code
        self._prefix = prefix
        self._four_digits = four_digits

    @property
    def area_code(self):
        """Getter for area code."""
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        """Setter for area code."""
        if len(value) == 3:
            self._area_code = value

    @property
    def prefix(self):
        """Getter for prefix."""
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        """Setter for prefix."""
        self._prefix = value

    @property
    def four_digits(self):
        """Getter for four digits."""
        return self._four_digits

    @four_digits.setter
    def four_digits(self, value):
        """Setter for four digits."""
        self._four_digits = value

    def __str__(self):
        """Returns a formatted string representation of the phone number."""
        return f"({self.area_code}) {self.prefix}-{self.four_digits}"

# Example Usage
phone = Phone("260", "555", "1234")

# Accessing attributes
print(phone.area_code)   # Output: 260
print(phone.prefix)      # Output: 555
print(phone.four_digits) # Output: 1234

# Modifying attributes using setters
phone.area_code = "317"
phone.prefix = "222"
phone.four_digits = "5678"

# Printing the object
print(phone)  # Output: (317) 222-5678

phone.area_code = "666"
print( phone )

phone.area_code = "88888"
print( phone )

