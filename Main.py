""" Main function for Particle Simulation """


import simulationclass
import particleclass

Xmax = 1
Ymax = 1
NoofParticles = 1000
timestep = 0.1
tfinal = 1;
simone = simulationclass.Simulation(Xmax, Ymax, NoofParticles, timestep, tfinal)

#simone.DisplayParticlesTable()

simone.Visualize()
simone.RunSimulation()

#simone.DisplayParticlesTable()
