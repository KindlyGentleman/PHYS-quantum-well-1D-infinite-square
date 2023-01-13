# Quantum Mechanics Solver
This program solves the time-independent Schrodinger equation for an infinite one-dimensional potential well using the Runge-Kutta method of order 4 and the secant method to determine the energy levels. The program also visualizes the wave function and probability density function.

## Getting Started
To use this program, you will need to have the following dependencies installed:

1. numpy
2. matplotlib

You can install these packages by running:
`pip install numpy matplotlib`

## Running the Program
The program can be run by executing the script in a python environment. Upon running the program, the user will be presented with a menu of options:

1. Show the wave function and probability density function graph
2. Show energy levels
3. Exit

The user can select an option by inputting the corresponding number.

## Constants
The following constants are used in the program:

`m`: electron mass (9.1094e-31 kg) <br>
`hbar`: reduced Planck constant (1.0546e-34 Js) <br>
`e`: electron charge (1.6022e-19 C) <br>
`L`: length of the potential well (5.2918e-11 m) <br>
`N`: number of iterations desired (1000) <br>
`h`: step size (determined by L and N) <br>

Function Descriptions
`V(x)`: The potential energy function of the system. In this case, it is set to a constant value of 0.0.

`f(r,x,E)`: The right-hand side of the time-independent Schrödinger equation.

`rungeKutta4Orde2(Epred)`: The Runge-Kutta method of order 4 for solving the time-independent Schrödinger equation.

`secantEnergi(Epred)`: The Secant method for determining the energy levels of the system.

`pilihan1(Ehasilmain)`: The first menu option for displaying the wave function and probability density graph.

`pilihan2()`: The second menu option for displaying the energy levels of the system.

`printMenu()` : function to display the menu

## Potential Function
The potential function used in the program is a infinite one-dimensional potential well. The potential function is defined as:

`def V(x):
    return 0.0`


This function can be modified to implement other potentials.

## Note
The physical constants and parameters used in the program (mass of the electron, reduced Planck constant, electron charge, and length of the potential well) are set to approximate values for the hydrogen atom. The values can be modified to suit the desired system.

## Acknowledgments
The program uses the Runge-Kutta method of order 4 and the secant method to solve the time-independent Schrodinger equation and determine energy levels.
The program uses matplotlib to visualize the wave function and probability density function.
