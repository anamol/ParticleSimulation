class Particle():
	""" Defines the particle. Stores the radius, density, position vector, velocity vector of particle. """
	
	def __init__(self, radius, density, position, velocity, Xmax, Ymax):
		""" Initializes particle with given radius, density, position and velocity. Xmax and Ymax are maximum
			bounds of simulation domain. """
		self.radius = radius
		self.density = density
		self.position = position
		self. velocity = velocity
		self.Xleft = self.position[0] - self.radius
		if (self.Xleft < 0):
			self.Xleft = self.Xleft + Xmax
		self.Xright = self.position[0] + self.radius
		if (self.Xright > Xmax):
			self.Xright = self.Xright - Xmax
		self.Ybot = self.position[1] - self.radius
		if (self.Ybot < 0):
			self.Ybot = self.Ybot + Ymax
		self.Ytop = self.position[1] + self.radius
		if (self.Ytop > Ymax):
			self.Ytop = self.Ytop - Ymax
