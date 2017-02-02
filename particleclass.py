class Particle():
	def __init__(self, radius, density, position, velocity, Xmax, Ymax):
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
