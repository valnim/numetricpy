def convert_to_si(unit):
    offset = 0
    # SI Units with Prefixes
    # Length Units
    if unit == 'mm':    # millimeter
        factor = 0.001
        conv_dict = {'s': 0, 'm': 1, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'cm':  # centimeter
        factor = 0.01
        conv_dict = {'s': 0, 'm': 1, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'dm':  # decimeter
        factor = 0.1
        conv_dict = {'s': 0, 'm': 1, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'km':  # kilometer
        factor = 1000
        conv_dict = {'s': 0, 'm': 1, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    # Mass Units
    elif unit == 'mg':  # milligram
        factor = 0.000001
        conv_dict = {'s': 0, 'm': 0, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'g':   # gram
        factor = 0.001
        conv_dict = {'s': 0, 'm': 0, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}

    # Time Units
    elif unit == 'ms':  # Millisecond
        factor = 0.001
        conv_dict = {'s': 1, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'min':     # Minute
        factor = 60
        conv_dict = {'s': 1, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'h':   # hour
        factor = 3600
        conv_dict = {'s': 1, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}

    # Temperature Units
    elif unit == '°C':  # Degree Celsius
        offset = 273.15
        factor = 1
        conv_dict = {'s': 0, 'm': 0, 'kg': 0, 'A': 0, 'K': 1, 'mol': 0, 'cd': 0}
    elif unit == '°F':  # Degree Fahrenheit
        offset = 255.3722
        factor = 5/9
        conv_dict = {'s': 0, 'm': 0, 'kg': 0, 'A': 0, 'K': 1, 'mol': 0, 'cd': 0}

    # Current Units
    elif unit == 'mA':  # milli Ampere
        factor = 0.001
        conv_dict = {'s': 0, 'm': 0, 'kg': 0, 'A': 1, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'kA':  # kilo Ampere
        factor = 1000
        conv_dict = {'s': 0, 'm': 0, 'kg': 0, 'A': 1, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'MA':  # mega Ampere
        factor = 1000000
        conv_dict = {'s': 0, 'm': 0, 'kg': 0, 'A': 1, 'K': 0, 'mol': 0, 'cd': 0}

    # Luminous Intensity Units

    # Amount of Substance Units
    elif unit == 'kmol':    # kilo mole
        factor = 1000
        conv_dict = {'s': 0, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 1, 'cd': 0}

    # Derived Units
    elif unit == 'Hz':  # Frequency
        factor = 1
        conv_dict = {'s': -1, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'rad':     # radian
        factor = 1
        conv_dict = {'s': 0, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'sr':  # steradian
        factor = 1
        conv_dict = {'s': 0, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'N':   # Newton
        factor = 1
        conv_dict = {'s': -2, 'm': 1, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'kN':  # kilo Newton
        factor = 1000
        conv_dict = {'s': -2, 'm': 1, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'Pa':  # Pascal
        factor = 1
        conv_dict = {'s': -2, 'm': -1, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'bar':     # Bar
        factor = 100000
        conv_dict = {'s': -2, 'm': -1, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'J':   # Joule
        factor = 1
        conv_dict = {'s': -2, 'm': 2, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'eV':  # Electron Volt
        factor = 1.6021766208e-19
        conv_dict = {'s': -2, 'm': 2, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'cal':     # Calorie
        factor = 4.184
        conv_dict = {'s': -2, 'm': 2, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'W':   # Watt
        factor = 1
        conv_dict = {'s': -3, 'm': 2, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'hp':  # Horse Power
        factor = 745.7
        conv_dict = {'s': -3, 'm': 2, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'C':   # Coulomb
        factor = 1
        conv_dict = {'s': 1, 'm': 0, 'kg': 0, 'A': 1, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'V':   # Volt
        factor = 1
        conv_dict = {'s': -3, 'm': 2, 'kg': 1, 'A': -1, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'F':   # Farad
        factor = 1
        conv_dict = {'s': 4, 'm': -2, 'kg': -1, 'A': 2, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'ohm':    # Ohm
        factor = 1
        conv_dict = {'s': -3, 'm': 2, 'kg': 1, 'A': -2, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'S':   # Siemens
        factor = 1
        conv_dict = {'s': 3, 'm': -2, 'kg': -1, 'A': 2, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'Wb':  # Weber
        factor = 1
        conv_dict = {'s': -2, 'm': 2, 'kg': 1, 'A': -1, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'T':   # Tesla
        factor = 1
        conv_dict = {'s': -2, 'm': 0, 'kg': 1, 'A': -1, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'H':   # Henry
        factor = 1
        conv_dict = {'s': -2, 'm': 2, 'kg': 1, 'A': -2, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'lm':  # Lumen
        factor = 1
        conv_dict = {'s': 0, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 1}
    elif unit == 'lx':  # Lux
        factor = 1
        conv_dict = {'s': 0, 'm': -2, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 1}
    elif unit == 'Bq':  # Becquerel
        factor = 1
        conv_dict = {'s': -1, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'Gy':  # Gray
        factor = 1
        conv_dict = {'s': -2, 'm': 2, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'Sv':  # Sievert
        factor = 1
        conv_dict = {'s': -2, 'm': 2, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    elif unit == 'kat':  # Katal
        factor = 1
        conv_dict = {'s': -1, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 1, 'cd': 0}
    elif unit == '':    # dimensionless
        factor = 1
        conv_dict = {'s': 0, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
    else:
        raise ValueError('Unit not found')
    return factor, offset, conv_dict


class UnitValue:
    def __init__(self, value, unit):
        factor = 1
        offset = 0
        self.unit_dict = {'s': 0, 'm': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0}
        # Extracts the unit of the object if the unit parameter is a string
        if isinstance(unit, str):
            unit_list = unit.split('*')
            for k in unit_list:
                if '^' in k:
                    unit_and_exp = k.split('^')
                    if self.is_si_unit(unit_and_exp[0]):
                        self.unit_dict[unit_and_exp[0]] = int(unit_and_exp[1])
                    else:
                        factor, offset, si_unit = convert_to_si(unit_and_exp[0])
                        self.unit_dict = {i: self.unit_dict[i] + si_unit[i] * int(unit_and_exp[1])
                                          for i in self.unit_dict.keys()}
                else:
                    if self.is_si_unit(k):
                        self.unit_dict[k] = 1
                    else:
                        factor, offset, si_unit = convert_to_si(k)
                        self.unit_dict = {i: self.unit_dict[i] + si_unit[i] for i in self.unit_dict.keys()}
        # If the unit parameter is a dictionary, then it is the unit of the object
        elif isinstance(unit, dict):
            self.unit_dict = unit
        self.value = value * factor + offset

    def __add__(self, other):
        if self.unit_dict.keys() != other.unit_dict.keys():
            raise ValueError("Cannot add quantities with different base units")
        if self.unit_dict.keys() != other.unit_dict.keys():
            raise ValueError("Cannot add quantities with different exponents")
        return UnitValue(self.value + other.value, self.unit_dict)

    def __sub__(self, other):
        if self.unit_dict.keys() != other.unit_dict.keys():
            raise ValueError("Cannot add quantities with different base units")
        if self.unit_dict.keys() != other.unit_dict.keys():
            raise ValueError("Cannot add quantities with different exponents")
        return UnitValue(self.value - other.value, self.unit_dict)

    def __mul__(self, other):
        if isinstance(other, UnitValue):
            # For two UnitValue Elements combine the units of self and other by adding the exponents
            combined_unit = {k: self.unit_dict[k] + other.unit_dict[k] for k in self.unit_dict.keys()}
            return UnitValue(self.value * other.value, combined_unit)
        else:
            # For multiplication with numbers without a unit keep unit of self
            return UnitValue(self.value * other, self.unit_dict)

    def __rmul__(self, other):
        if isinstance(other, UnitValue):
            # For two UnitValue Elements combine the units of self and other by adding the exponents
            combined_unit = {k: self.unit_dict[k] + other.unit_dict[k] for k in self.unit_dict.keys()}
            return UnitValue(other.value * self.value, combined_unit)
        else:
            # For multiplication with numbers without a unit keep unit of self
            return UnitValue(other * self.value, self.unit_dict)

    def __truediv__(self, other):
        if isinstance(other, UnitValue):
            # Combine the units of self and other by subtracting the exponents
            combined_unit = {k: self.unit_dict[k] - other.unit_dict[k] for k in self.unit_dict.keys()}
            return UnitValue(self.value / other.value, combined_unit)
        else:
            # For division by numbers without a unit keep unit of self
            return UnitValue(self.value / other, self.unit_dict)

    def __rtruediv__(self, other):
        if isinstance(other, UnitValue):
            # Combine the units of self and other by subtracting the exponents
            combined_unit = {k: other.unit_dict[k] - self.unit_dict[k] for k in self.unit_dict.keys()}
            return UnitValue(other.value / self.value, combined_unit)
        else:
            # For division of numbers without a unit invert unit of self
            combined_unit = {k: -self.unit_dict[k] for k in self.unit_dict.keys()}
            return UnitValue(other / self.value, combined_unit)

    def __pow__(self, power):
        # Raise the value of self to the power and raise the exponents of the unit
        return UnitValue(self.value ** power, {k: power * self.unit_dict[k] for k in self.unit_dict.keys()})

    def __eq__(self, other):
        # If the units are the same, then compare the values
        if self.unit_dict.keys() == other.unit_dict.keys():
            return self.value == other.value
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.unit_dict.keys() != other.unit_dict.keys():
            raise ValueError("Cannot compare quantities with different base units")
        if self.unit_dict.keys() != other.unit_dict.keys():
            raise ValueError("Cannot compare quantities with different exponents")
        return self.value < other.value

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if self.unit_dict.keys() != other.unit_dict.keys():
            raise ValueError("Cannot compare quantities with different base units")
        if self.unit_dict.keys() != other.unit_dict.keys():
            raise ValueError("Cannot compare quantities with different exponents")
        return self.value > other.value

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __hash__(self):
        return hash((self.value, self.unit_dict))

    def __repr__(self):
        return f'ValueWithUnit("{self.value}","{self.unit_dict}")'

    def __str__(self):
        # Create a string of the unit
        unit_str = ''
        for k in self.unit_dict.keys():
            if self.unit_dict[k] == 1:
                unit_str += k + '*'
            elif self.unit_dict[k] > 1:
                unit_str += k + '^' + str(self.unit_dict[k]) + '*'
            elif self.unit_dict[k] < 0:
                unit_str += k + '^' + str(self.unit_dict[k]) + '*'
        # Remove the last '*' from the unit string
        unit_str = unit_str[:-1]
        return str(self.value) + ' ' + unit_str

    def str_as(self, unit):
        print_dict = self.unit_dict
        print_value = self.value
        # Create a string of the unit
        unit_str = unit + '*'
        if unit is not None:
            factor, offset, si_unit = convert_to_si(unit)
            print_value = (print_value - offset) / factor
            print_dict = {k: print_dict[k] - si_unit[k] for k in print_dict.keys()}
        for k in self.unit_dict.keys():
            if print_dict[k] == 1:
                unit_str += k + '*'
            elif print_dict[k] > 1:
                unit_str += k + '^' + str(print_dict[k]) + '*'
            elif print_dict[k] < 0:
                unit_str += k + '^' + str(print_dict[k]) + '*'
        # Remove the last '*' from the unit string
        unit_str = unit_str[:-1]
        return str(print_value) + ' ' + unit_str

    def is_si_unit(self, unit):
        # Check if the unit is a SI unit
        if unit in self.unit_dict.keys():
            return True
        else:
            return False


class UnitConstants:
    def __init__(self):
        self.gravity = UnitValue(9.81, 'm*s^-2')
        self.speed_of_light = UnitValue(299792458, 'm*s^-1')
        self.plank_constant = UnitValue(6.62607004e-34, 'm^2*kg*s^-1')
