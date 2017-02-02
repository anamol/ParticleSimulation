import particleclass
import random
import matplotlib.pyplot as plp
import math

class Simulation():

	AllParticles = []
	ParticlesPresent = False

	def __init__(self, Xmax, Ymax, NoofParticles, timestep, tfinal):
		""" Initializes an object of the class, given length X and width Y of the domain, number of particles, the required 
		timestep and final time. """
		self.Xmax = Xmax
		self.Ymax = Ymax
		self.NoofParticles = NoofParticles
		self.timestep = timestep
		self.__Initialize(0.001, 1800)
		self.tfinal = tfinal
		self.Noofsteps = int(tfinal/timestep)


	def __Initialize(self, radius, density):
		for ctr in range(self.NoofParticles):
			if (self.ParticlesPresent == False):
				Xposition = random.random() * self.Xmax
				Yposition = random.random() * self.Ymax
				position = [Xposition, Yposition]
				Xvel = random.uniform(-1.0, 1.0) * 10
				Yvel = random.uniform(-1.0, 1.0) * 10
				velocity = [Xvel, Yvel]
				particle = particleclass.Particle(radius, density, position, velocity, self.Xmax, self.Ymax)
				self.AllParticles.append(particle)
				self.ParticlesPresent = True
			elif (self.ParticlesPresent):
				overlap = True
				check = False
				while (overlap):
					Xposition = random.random() * self.Xmax
					Yposition = random.random() * self.Ymax
					position = [Xposition, Yposition]
					Xvel = random.uniform(-1.0, 1.0) * 10
					Yvel = random.uniform(-1.0, 1.0) * 10
					velocity = [Xvel, Yvel]
					particle = particleclass.Particle(radius, density, position, velocity, self.Xmax, self.Ymax)
					for ctr2 in range(ctr):
						check = self.__CheckIntersection(particle, self.AllParticles[ctr2])
						if (check):
							break
					if (check == False):
						overlap = False
					else :
						overlap = True
				self.AllParticles.append(particle)


	def RunSimulation(self):

		for ctr2 in range(self.Noofsteps):
			self.Visualize(

			for ctr in range(self.NoofParticles):
				changeinXpos = self.AllParticles[ctr].velocity[0] * self.timestep
				changeinYpos = self.AllParticles[ctr].velocity[1] * self.timestep
				self.AllParticles[ctr].position[0] = self.AllParticles[ctr].position[0] + changeinXpos
				self.AllParticles[ctr].position[1] = self.AllParticles[ctr].position[1] + changeinYpos
				if (self.AllParticles[ctr].position[0] > self.Xmax):
					self.AllParticles[ctr].position[0] = self.AllParticles[ctr].position[0] - self.Xmax
				elif (self.AllParticles[ctr].position[0] < 0):
					self.AllParticles[ctr].position[0] = self.AllParticles[ctr].position[0] + self.Xmax

				if (self.AllParticles[ctr].position[1] > self.Ymax):
					self.AllParticles[ctr].position[1] = self.AllParticles[ctr].position[1] - self.Ymax
				elif (self.AllParticles[ctr].position[1] < 0):
					self.AllParticles[ctr].position[1] = self.AllParticles[ctr].position[1] + self.Ymax

			
			

	def __CheckIntersection(self, particle1, particle2):
		
		intersection = False
		dist = math.sqrt((particle1.position[0] - particle2.position[0])**2 + (particle1.position[1] - particle2.position[1])**2)
		if (dist <= particle1.radius + particle2.radius):
			intersection = True

		if ((particle1.position[0] > self.Xmax - 2*particle1.radius) and (particle2.position[0] < 2*particle2.radius)):
			newXcentre = self.Xmax + particle2.position[0]
			dist = math.sqrt((particle1.position[0] - newXcentre)**2 + (particle1.position[1] - particle2.position[1])**2)
			if (dist <= particle2.radius + particle1.radius):
				intersection = True

		if ((particle2.position[0] > self.Xmax - 2*particle2.radius) and (particle1.position[0] < 2*particle1.radius)):
			newXcentre = self.Xmax + particle1.position[0]
			dist = math.sqrt((particle2.position[0] - newXcentre)**2 + (particle1.position[1] - particle1.position[1])**2)
			if (dist <= particle2.radius + particle1.radius):
				intersection = True

		if ((particle1.position[1] > self.Ymax - 2*particle1.radius) and (particle2.position[1] < 2*particle2.radius)):
			newYcentre = self.Ymax + particle2.position[1]
			dist = math.sqrt((particle1.position[1] - newYcentre)**2 + (particle1.position[0] - particle2.position[0])**2)
			if (dist <= particle2.radius + particle1.radius):
				intersection = True

		if ((particle2.position[1] > self.Ymax - 2*particle2.radius) and (particle1.position[1] < 2*particle1.radius)):
			newYcentre = self.Ymax + particle1.position[1]
			dist = math.sqrt((particle2.position[1] - newYcentre)**2 + (particle1.position[0] - particle2.position[0])**2)
			if (dist <= particle2.radius + particle1.radius):
				intersection = True

		if ((particle1.position[0] > self.Xmax - 2*particle1.radius) and (particle2.position[0] < 2*particle2.radius) and \
			(particle1.position[1] > self.Ymax - 2*particle1.radius) and (particle2.position[1] < 2*particle2.radius)):
			newXcentre = self.Xmax + particle2.position[0]
			newYcentre = self.Ymax + particle2.position[1]
			dist = math.sqrt((particle1.position[0] - newXcentre)**2 + (particle1.position[1] - newYcentre)**2)
			if (dist <= particle2.radius + particle1.radius):
				intersection = True

		if ((particle2.position[0] > self.Xmax - 2*particle2.radius) and (particle1.position[0] < 2*particle1.radius) and \
			(particle2.position[1] > self.Ymax - 2*particle2.radius) and (particle1.position[1] < 2*particle1.radius)):
			newXcentre = self.Xmax + particle1.position[0]
			newYcentre = self.Ymax + particle1.position[1]
			dist = math.sqrt((particle2.position[0] - newXcentre)**2 + (particle2.position[1] - newYcentre)**2)
			if (dist <= particle2.radius + particle1.radius):
				intersection = True

		if ((particle1.position[0] > self.Xmax - 2*particle1.radius) and (particle2.position[0] < 2*particle2.radius) and \
			(particle1.position[1] < 2*particle1.radius) and (particle2.position[1] < self.Ymax - 2*particle2.radius)):
			newXcentre = self.Xmax + particle2.position[0]
			newYcentre = particle2.position[1] - self.Ymax
			dist = math.sqrt((particle1.position[0] - newXcentre)**2 + (particle1.position[1] - newYcentre)**2)
			if (dist <= particle2.radius + particle1.radius):
				intersection = True

		if ((particle2.position[0] > self.Xmax - 2*particle2.radius) and (particle1.position[0] < 2*particle1.radius) and \
			(particle2.position[1] < 2*particle2.radius) and (particle1.position[1] < self.Ymax - 2*particle1.radius)):
			newXcentre = self.Xmax + particle1.position[0]
			newYcentre = particle1.position[1] - self.Ymax
			dist = math.sqrt((particle2.position[0] - newXcentre)**2 + (particle2.position[1] - newYcentre)**2)
			if (dist <= particle2.radius + particle1.radius):
				intersection = True

		return intersection


	def __Collision(self):
		""" Checks whether or not two particles are colliding. Returns True if collision occurs, False if not"""



	
	def Visualize(self):
		x = [particle.position[0] for particle in self.AllParticles]
		y = [particle.position[1] for particle in self.AllParticles]
		plp.plot(x, y, 'bo')#, ms = 3.141*self.AllParticles[0].radius*self.AllParticles[0].radius)
		plp.axis([0,self.Xmax,0,self.Ymax])
		plp.show()

	def DisplayParticlesTable(self):
		for ctr in range(self.NoofParticles):
			print str(self.AllParticles[ctr].position) + " " + str(self.AllParticles[ctr].Xleft) + " " \
			+ str(self.AllParticles[ctr].Xright)  + " " + str(self.AllParticles[ctr].Ybot) + " " \
			+ str(self.AllParticles[ctr].Ytop)



