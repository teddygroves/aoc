
def fuel(mass):
    """Fuel required to launch a given module is based on its mass.  

    Specifically, to find the fuel required for a module, take its mass, divide
    by three, round down, and subtract 2.  

    """
    return mass // 3 - 2

def main():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    masses = map(float, data)
    fuels = map(fuel, masses)
    total_fuel = sum(fuels)
    print('Total fuel: ' + str(total_fuel))
        

if __name__ == '__main__':
    main()
