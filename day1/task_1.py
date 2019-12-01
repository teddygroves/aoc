
def fuel(mass):
    """Fuel required to launch a given module is based on its mass.  

    Specifically, to find the fuel required for a module, take its mass, divide
    by three, round down, and subtract 2.  

    """
    return mass // 3 - 2

def main():
    masses = []
    with open('input.txt', 'r') as f:
        data = f.readlines()
    for mass_str in data:
        masses.append(float(mass_str))
    fuels = map(fuel, masses)
    total_fuel = sum(fuels)
    print('Total fuel: ' + str(total_fuel))
        

if __name__ == '__main__':
    main()
