class ValueWithUnit:
    def __init__(self, value, unit):
        self.value = value
        self.unitDict = {'s': 0, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
        # Extracts the unit of the object if the unit parameter is a string
        if isinstance(unit, str):
            unit_list = unit.split('*')
            for k in unit_list:
                if '^' in k:
                    unit_and_exp = k.split('^')
                    self.unitDict[unit_and_exp[0]] = int(unit_and_exp[1])
                else:
                    self.unitDict[k] = 1
        # If the unit parameter is a dictionary, then it is the unit of the object
        elif isinstance(unit, dict):
            self.unitDict = unit

    def __add__(self, other):
        if self.unitDict.keys() != other.unitDict.keys():
            raise ValueError("Cannot add quantities with different base units")
        if self.unitDict.keys() != other.unitDict.keys():
            raise ValueError("Cannot add quantities with different exponents")
        return ValueWithUnit(self.value + other.value, self.unitDict)

    def __sub__(self, other):
        if self.unitDict.keys() != other.unitDict.keys():
            raise ValueError("Cannot add quantities with different base units")
        if self.unitDict.keys() != other.unitDict.keys():
            raise ValueError("Cannot add quantities with different exponents")
        return ValueWithUnit(self.value - other.value, self.unitDict)

    def __mul__(self, other):
        # Combine the units of self and other by adding the exponents
        combined_unit = {k: self.unitDict[k] + other.unitDict[k] for k in self.unitDict.keys()}
        return ValueWithUnit(self.value * other.value, combined_unit)

    def __truediv__(self, other):
        # Combine the units of self and other by subtracting the exponents
        combined_unit = {k: self.unitDict[k] - other.unitDict[k] for k in self.unitDict.keys()}
        return ValueWithUnit(self.value / other.value, combined_unit)

    def __pow__(self, power):
        # Raise the value of self to the power and raise the exponents of the unit
        return ValueWithUnit(self.value ** power, {k: power * self.unitDict[k] for k in self.unitDict.keys()})

    def __eq__(self, other):
        # If the units are the same, then compare the values
        if self.unitDict.keys() == other.unitDict.keys():
            return self.value == other.value
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.unitDict.keys() != other.unitDict.keys():
            raise ValueError("Cannot compare quantities with different base units")
        if self.unitDict.keys() != other.unitDict.keys():
            raise ValueError("Cannot compare quantities with different exponents")
        return self.value < other.value

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if self.unitDict.keys() != other.unitDict.keys():
            raise ValueError("Cannot compare quantities with different base units")
        if self.unitDict.keys() != other.unitDict.keys():
            raise ValueError("Cannot compare quantities with different exponents")
        return self.value > other.value

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __hash__(self):
        return hash((self.value, self.unitDict))

    def __repr__(self):
        return f'ValueWithUnit("{self.value}","{self.unitDict}")'

    def __str__(self):
        # Create a string of the unit
        unit_str = ''
        for k in self.unitDict.keys():
            if self.unitDict[k] == 1:
                unit_str += k + '*'
            elif self.unitDict[k] > 1:
                unit_str += k + '^' + str(self.unitDict[k]) + '*'
        # Remove the last '*' from the unit string
        unit_str = unit_str[:-1]
        return str(self.value) + ' ' + unit_str


class ConstantsWithUnits:
    def __init__(self):
        self.gravity = ValueWithUnit(9.81, 'm*s^-2')
        self.speed_of_light = ValueWithUnit(299792458, 'm*s^-1')
        self.plank_constant = ValueWithUnit(6.62607004e-34, 'm^2*kg*s^-1')


