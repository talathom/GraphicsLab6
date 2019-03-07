# Luxo.py

import viz
import vizshape

class Luxo(viz.EventClass):

	# Constructor 
	def __init__(self):
		# must call constructor of EventClass first!!
		viz.EventClass.__init__(self)
		
		#Luxo instance variables that describe configuration
		self.x = 0    # location of base in world
		self.y = 0
		self.z = 0
		self.a = 30   # rotation angle of lower arm 
		self.b = 20   # spin angle of lower arm 
		self.c = -30  # rotation angle of upper arm 
		self.d = 0    # rotation angle of shade 
		self.e = 0    # spin angle of shade 
		
		self.base = vizshape.addCylinder(5, 20)
		mat = viz.Matrix()
		mat.postTrans(0, 2.5, 0)
		self.base.setMatrix(mat)
		
		#World Group
		self.group = viz.addGroup()
		self.base.setParent(self.group)
		
		# Create Lower Arm and its socket
		self.lowerArmBall = vizshape.addSphere(3)
		self.lowerArm = vizshape.addCylinder(20, 2)
		# Lower Arm Standard Position
		mat = viz.Matrix()
		mat.postTrans(0, 10, 0)
		self.lowerArm.setMatrix(mat)
		
		# Create Upper Arm and Socket
		self.upperArmBall = vizshape.addSphere(3)
		self.upperArm = vizshape.addCylinder(20, 2)
		
		# Upper Arm Standard Position
		mat = viz.Matrix()
		mat.postTrans(0, 10, 0)
		self.upperArm.setMatrix(mat)
		
		# Create Shade and socket
		self.shadeBall = vizshape.addSphere(3)
		self.shade = vizshape.addCone(15, 20)
		
		# Shade Standard Position
		mat = viz.Matrix()
		mat.postAxisAngle(0, 0, 1, 90)
		mat.postTrans(10, 0, 0)
		self.shade.setMatrix(mat)
		
		# Lower Arm Group
		self.lowerArmGroup = viz.addGroup()
		self.lowerArmGroup.setParent(self.group)
		self.lowerArmBall.setParent(self.lowerArmGroup)
		self.lowerArm.setParent(self.lowerArmGroup)
		
		# Upper Arm Group
		self.upperArmGroup = viz.addGroup()
		self.upperArmGroup.setParent(self.lowerArmGroup)
		self.upperArmBall.setParent(self.upperArmGroup)
		self.upperArm.setParent(self.upperArmGroup)
		
		# Shade Group
		self.shadeGroup = viz.addGroup()
		self.shadeGroup.setParent(self.upperArmGroup)
		self.shadeBall.setParent(self.shadeGroup)
		self.shade.setParent(self.shadeGroup)
		
		
		
		# set transformation group matrices of nodes to give 
		# desired configuration
		self.transform()
		
		# setup callback methods
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		self.callback(viz.TIMER_EVENT,self.onTimer)
	
	# Sets the transformation matrices of the Luxo group 
	# nodes to achieve desired configuration
	def transform(self):
		baseM = viz.Matrix()
		baseM.postTrans(self.x, self.y)
		self.group.setMatrix(baseM)		
		
		mat = viz.Matrix()
		mat.postAxisAngle(0, 0, 1, self.a)
		mat.postAxisAngle(0, 1, 0, self.b)
		mat.postTrans(0, 4.5)
		self.lowerArmGroup.setMatrix(mat)
		
		mat = viz.Matrix()
		mat.postAxisAngle(0, 0, 1, self.c)
		mat.postAxisAngle(0, 1, 0, self.d)
		mat.postTrans(0, 20)
		self.upperArmGroup.setMatrix(mat)
		
		mat = viz.Matrix()
		mat.postTrans(0, 20)
		mat.postAxisAngle(0, 0, 1, self.e)
		self.shadeGroup.setMatrix(mat)
		
		
		
	# This gets executed whenever a key is pressed down.
	def onKeyDown(self,key):
		if (key == viz.KEY_RIGHT):
			self.x = self.x + 5
		if (key == viz.KEY_LEFT):
			self.x = self.x - 5	
		if (key == viz.KEY_DOWN):
			self.y = self.y - 5
		if (key == viz.KEY_UP):
			self.y = self.y + 5
		if (key == '1'):
			self.a = self.a + 5
		if (key == '2'):
			self.a = self.a - 5
		if (key == '3'):
			self.b = self.b + 5
		if (key == '4'):
			self.b = self.b - 5
		if (key == '5'):
			self.c = self.c + 5
		if (key == '6'):
			self.c = self.c - 5
		if (key == '7'):
			self.d = self.d + 5
		if (key == '8'):
			self.d = self.d - 5
		if (key == '9'):
			self.e = self.e + 5
		if (key == '0'):
			self.e = self.e - 5
		self.transform()
		
		if ( key == 'g' ):
			self.starttimer(1, 1/20.0, viz.FOREVER)

	# This gets executed whenever a timer event occurs.
	def onTimer(self,num):
		if num == 1:
			self.y += 2
			self.transform()
			if(self.y >= 30):
				self.killtimer(1)
				self.starttimer(2, 1/20.0, viz.FOREVER)
		else:
			self.y -= 2
			self.transform()
			if(self.y == 0):
				self.killtimer(2)
		
		
# Luxo Driver Code
# set size (in pixels) and title of application window
viz.window.setSize( 500, 500 )
viz.window.setName( "Luxo" )

# get graphics window
window = viz.MainWindow
# setup viewing volume
window.ortho(-100,100,-100,100,-100,100)
# set background color of window to very light gray 
viz.MainWindow.clearcolor( [150,150,150] ) 
# center viewpoint 
viz.eyeheight(0)

c = Luxo()

# render the scene in the window
viz.go()
