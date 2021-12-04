"""
Created on Thu Feb 18, 2021
@author: Ashish Singh

"""
import math

# Universal gravitational constant.
g_constant = 6.67E-11

# Number of celestial bodies.
N = 5

# In order; x position, y position, x velocity, y velocity, and mass
# of planets and sun in our solar system.
earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
mars = [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23]
mercury = [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23]
sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
venus = [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24]

# List contains an object of lists. In other words, planets_val
# stores all the values of the planets and sun aforementioned
# on line 16 through line 20.
planets_val = [earth, mars, mercury, sun, venus]

px = []     # x position is stored in px for planets and sun.
py = []     # y position is stored in py for planets and sun.
vx = []     # x velocity is stored in vx for planets and sun.
vy = []     # y velocity is stored in vy for planets and sun.
mass = []   # mass value is stored in p_mass for planets and sun.
# Parses out the x position, y position, x velocity, y velocity
# and mass separately in their respective lists.
for index in range(N):
    px.append(planets_val[index][0])    # x position.
    py.append(planets_val[index][1])    # y position.
    vx.append(planets_val[index][2])    # x velocity.
    vy.append(planets_val[index][3])    # y velocity.
    mass.append(planets_val[index][4])  # mass.
        

t = 157788000   # Total time of simulation.
dt = 25000      # Length of the timestep.
t_total = 0.00  # Running total of timestep.

while t_total < t:
    for index in range(N):
        # For sun, we skip the physics calculation.
        if index == 3:      # index 3 is sun in planets_val list.
            continue
        else:
            # Radius calculation between sun and the planets. 
            delta_x = sun[0] - px[index]                # delta x
            delta_y = sun[1] - py[index]                # delta y
            r = math.sqrt(delta_x**2 + delta_y**2)      # r = square root of delta x^2 + delta y^2

            # Force between celestial bodies. 
            f_numerator = g_constant * sun[-1] * mass[index]    # G X (m1 X m2)
            f_denominator = r**2                                # r^2
            F = f_numerator/f_denominator                       # Force (F).
            
            # Simulation will be in two-dimensional plane, so the total force needs to be
            # decomposed into x and y components. 
            Fx = F * (delta_x/r)     
            Fy = F * (delta_y/r)     

            # Newton's second law states the acceleration of a body is the total force 
            # exerted on it divided by its mass. And because the simulation is in 
            # two-dimensional plane, the acceleration needs to be broken into in x and y 
            # components.
            ax = Fx/mass[index]
            ay = Fy/mass[index]

            # New x velocity and y velocity.
            vx[index] = vx[index] + (ax*dt)
            vy[index] = vy[index] + (ay*dt)

            # New x position and y position.
            px[index] = px[index] + vx[index]*dt
            py[index] = py[index] + vy[index]*dt    

    t_total = t_total + dt      # Running total of the time step.

# Prints the output of the Physics Calculations.
for index in range(N):
    print(f"{px[index]:.4e} {py[index]:.4e} {vx[index]:.4e} {vy[index]:.4e} {mass[index]:.4e}")