def fuel_basic(mass):
    """Fuel required to launch a given module is based on its mass.  

    Specifically, to find the fuel required for a module, take its mass, divide
    by three, round down, and subtract 2.  

    """
    return mass // 3 - 2


def fuel_advanced(mass):
    """For each module mass, calculate its fuel and add it to the total. 
    
    Then, treat the fuel amount you just calculated as the input mass and
    repeat the process, continuing until a fuel requirement is zero or
    negative.

    """
    fuel_mass = fuel_basic(mass)
    additional_fuel = fuel_basic(fuel_mass)
    while additional_fuel > 0:
        fuel_mass += additional_fuel
        additional_fuel = fuel_basic(additional_fuel)
    return fuel_mass



def main():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    masses = map(float, data)
    fuels = map(fuel_advanced, masses)
    total_fuel = sum(fuels)
    print('Total fuel: ' + str(total_fuel))
        

if __name__ == '__main__':
    main()

