# N-body Simulations of Globular Cluster Evolution Using Monte-Carlo Methods  
## Aim of the Project  
Globular clusters are spherical clusters of stars born from the same parent gas cloud. The study of these can tell us a lot about the properties and statistics of stellar evolution and dynamics.  
This project aims to study the dynamics of such a system, specifically studyng the average radius evolution of the cluster.  
## Monte Carlo Simulations  
A Monte-Carlo simulation is a model to predict the probabilities of an experiment when various random variables are present. An example of this being used in Physics is in the study of ferromagnetic behaviour of materials in the Ising Model.  

## Initialization  
Stars of random mass (uniformly random) were distributed along a Plummer distribution:  
$ f(r) = \fra{3M}{4\pi a^3} (1 + (\frac{r}{a})^2)^{-2.5} $  
Their velocities were also taken as uniform random variables in the polar coordinates  
Radial distribution of the stars:  
![image](https://github.com/Srishti-Goel/N-body-Simulations-of-Globular-Cluster-Evolution-Using-Monte-Carlo-Methods/assets/43054441/d5d218fb-577f-4a7a-a36c-f55361bd1bab)

Total energy as a function of radius:  
![image](https://github.com/Srishti-Goel/N-body-Simulations-of-Globular-Cluster-Evolution-Using-Monte-Carlo-Methods/assets/43054441/f55df039-e59f-49c0-8b90-47f65f802e0a)


 
  
## Process Considered  
![image](https://github.com/Srishti-Goel/N-body-Simulations-of-Globular-Cluster-Evolution-Using-Monte-Carlo-Methods/assets/43054441/0e0f029c-b133-4d53-974f-bf787d953382)  

### Formation of multiple-star systems (Collision Dynamics)
When stars orbitting the common center of mass become gravitationally bound to each other, we consider them to have "inelastically collided" and are treated as a single star system with a larger mass.  
### Stellar Evolution  
As stars lose mass to the nuclear fusion inside their cores, this affects their dynamics. We assume that the rate of mass loss is :  
$$ \frac{dM}{dt} = k M^{3.5} $$  
### New Orbit Calculation  
The new orbits after collision are calculated based on the Newton's Laws of Motion  

## Results  
### Collisionless Evolution  
![image](https://github.com/Srishti-Goel/N-body-Simulations-of-Globular-Cluster-Evolution-Using-Monte-Carlo-Methods/assets/43054441/68e8b9ae-012d-4505-a1a9-4d8ba5ac70f9)  
As there is no gravitational collapse of multiple-star systems, all the stars eventually fall in towards the center, reducing the average radius  
### Collisioned Evolution  
![image](https://github.com/Srishti-Goel/N-body-Simulations-of-Globular-Cluster-Evolution-Using-Monte-Carlo-Methods/assets/43054441/84cd4b28-76c2-4b58-b99d-75cf68b0650f)  
The stars furthest away from the center fall into the gravitational well of the cluster, and the ones inside are flung out till they all settle at a intermediate position. The top graph traces the positions of the stars that start in the inner parts of the cluster, and the one below it traces the positions of the start in the outer parts.  
![image](https://github.com/Srishti-Goel/N-body-Simulations-of-Globular-Cluster-Evolution-Using-Monte-Carlo-Methods/assets/43054441/ece45006-8d21-42bb-8fc5-f9a3ffb6b383)  
The average radius of the system remains fairly more constant.


