# numetricpy

The numetricpy library provides a UnitValue class for representing physical quantities that have both a value and an associated unit. 
The UnitValue class overloads arithmetic operators such as +, -, *, and / to allow for easy manipulation and calculation of quantities with units. 
The class also overloads comparison operators such as ==, !=, <, <=, >, and >= to allow for comparison of quantities with the same units.

With the UnitValue class, it is easy to perform calculations involving physical quantities while keeping track of the units involved. 
This can help reduce the likelihood of errors in calculations and improve the clarity and readability of code.

This library also contains the class UnitConstants. 
This class contains a number of physical constants that are useful in calculations involving physical quantities.

## Supported SI based Units
### Length:
* millimeter (mm);
* centimeter (cm)
* decimeter (dm)
* kilometer (km)
### Mass:
* milligram (mg)
* gram (g)
### Time:
* millisecond (ms)
* minute (min)
* hour (h)
### Temperature:
* degree Celsius (°C)
* degree Fahrenheit (°F)
### Current:
* milliampere (mA)
* kiloampere (kA)
* megaampere (MA)

### Amount of Substance:
* kilomole (kmol)

## Supported Derived Units
### Frequency:
* hertz (Hz)
### Angle:
* radian (rad)
### Solid angle:
* steradian (sr)
### Force:
* newton (N)
* kilonewton (kN)
### Pressure:
* pascal (Pa)
* bar (bar)
### Energy:
* joule (J)
* electronvolt (eV)
* calorie (cal)
### Power:
* watt (W)
* horsepower (hp)
### Charge:
* coulomb (C)
### Voltage:
* volt (V)
### Capacitance:
* farad (F)
### Electrical resistance:
* ohm (ohm)
### Electrical conductance:
* siemens (S)
### Magnetic flux:
* weber (Wb)
### Magnetic field strength:
* tesla (T)
### Inductance:
* henry (H)
### Luminous flux:
* lumen (lm)
### Illuminance:
* lux (lx)
### Activity (of a radionuclide):
* becquerel (Bq)
### Absorbed dose:
* gray (Gy)
### Dose equivalent:
* sievert (Sv)

## Implemented Constants
### Mathematical constants:
* pi (pi)
* Euler's number (e)
### Space and Time constants:
* speed of light in vacuum (c)
### Electromagnetic constants:
* electron charge (e)
* vacuum permeability (mu_0)
* vacuum electric permittivity (eps_0)
* Coulomb's constant (k_c)
* characteristic impedance of vacuum (Z_0)
### Quantum mechanics constants:
* Planck's constant (h)
* reduced Planck's constant (h_bar)
* magnetic flux quantum (Phi_0)
* conductance quantum (G_0)
* von Klitzing constant (R_k)
* Josephson constant (K_j)
* fine structure constant (alpha)
### Thermodynamic constants:
* Boltzmann's constant (k_b, k)
* Stefan-Boltzmann constant (sigma)
* first radiation constant (c_1)
* second radiation constant (c_2)
* Wien's wavelength displacement law constant (b)
### Gravity and Cosmology constants:
* Newtonian constant of gravitation (G)
* Earth gravity acceleration (g_earth)
* Planck mass (m_planck)
* Planck length (l_planck)
* Planck time (t_planck)
* Planck temperature (T_planck)
### Atomic and nuclear constants:
* Bohr radius (a_0)
* Rydberg constant (R_inf)
* Rydberg frequency constant (R_inf_c)
* Rydberg energy constant (R_inf_hc)
* Hartree energy (E_h)
### Amount of substance constants:
* Avogadro constant (N_A)
* Faraday constant (F)
* molar gas constant (Rm)
