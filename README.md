# Reynolds Number Calculator

## Aim
To determine the flow regime of a fluid in a pipe using the Reynolds number.

## Objective
This program calculates the Reynolds number and classifies the flow as laminar, transitional, or turbulent.

## Theory
Reynolds number is a dimensionless parameter used to predict the flow pattern in fluid systems.

Re = (ρ × v × D) / μ

Where:

- ρ = Fluid density
- v = Velocity of fluid
- D = Pipe diameter
- μ = Dynamic viscosity

Flow classification:

- Re < 2300 → Laminar flow
- 2300 ≤ Re ≤ 4000 → Transitional flow
- Re > 4000 → Turbulent flow

## Requirements

Python 3.x

## How to Run

python reynolds.py

## Example Input

Density = 1000  
Velocity = 2  
Diameter = 0.05  
Viscosity = 0.001

## Example Output

Reynolds Number = 100000  
Flow Type: Turbulent Flow

## Applications

- Fluid transport systems
- Pipeline design
- Chemical process engineering
