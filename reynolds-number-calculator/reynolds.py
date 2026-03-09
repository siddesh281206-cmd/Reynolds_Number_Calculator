def calculate_reynolds(rho, velocity, diameter, viscosity):
    """
    Calculate Reynolds number
    """
    Re = (rho * velocity * diameter) / viscosity
    return Re


def flow_type(Re):
    if Re < 2300:
        return "Laminar Flow"
    elif Re <= 4000:
        return "Transitional Flow"
    else:
        return "Turbulent Flow"


def main():
    print("Reynolds Number Calculator")

    rho = float(input("Enter fluid density (kg/m^3): "))
    velocity = float(input("Enter fluid velocity (m/s): "))
    diameter = float(input("Enter pipe diameter (m): "))
    viscosity = float(input("Enter dynamic viscosity (Pa.s): "))

    Re = calculate_reynolds(rho, velocity, diameter, viscosity)

    print("Reynolds Number =", round(Re, 2))
    print("Flow Type:", flow_type(Re))


if __name__ == "__main__":
    main()