
In the simulation, as the planets revolve around the sun, the x position, y position, x velocity, 
and y velocity, radius between the planets and the sun, Force, and acceleration are calculated into 
small code snippets, making it easier to debug and check the appropriate outcome.

The values of earth, mars, mercury, sun, and venus are stored in a list (planets_val) containing 
an object of lists. In other words, it is a list of lists. This approach condenses the program 
code significantly compared to other approaches where the x position, y position, etc., had to be 
entered manually or a combination of manual entry and loop to populate the values in a list.

The program loops several times, and it keeps a running total of the time step. 
The program loop ends when the time step running total exceeds the simulation time where 't' equals 157788000. 
As planets revolve around the sun in our solar system, the physics calculation only applies to planets, 
and there is no calculation for the sun.

I see a small improvement in the program. As the list of lists contains all the planets and the sun, 
there is no need to specify a variable 'N'.  The 'for' loops can be created by taking the range of the 
length of the list of lists. For example, range(len(planets_val)) instead of range(N). 
The trivial improvement will reduce two lines of code from the program. 
However, I have not removed it from this program.

As there are two loops in the program, the program's run-time complexity is O(n^2).

Known Bugs:
NA