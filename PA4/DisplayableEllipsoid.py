from Displayable import Displayable
from GLBuffer import VAO, VBO, EBO
from Point import Point
import numpy as np
import ColorType
import math
try:
    import OpenGL

    try:
        import OpenGL.GL as gl
        import OpenGL.GLU as glu
    except ImportError:
        from ctypes import util

        orig_util_find_library = util.find_library


        def new_util_find_library(name):
            res = orig_util_find_library(name)
            if res:
                return res
            return '/System/Library/Frameworks/' + name + '.framework/' + name


        util.find_library = new_util_find_library
        import OpenGL.GL as gl
        import OpenGL.GLU as glu
except ImportError:
    raise ImportError("Required dependency PyOpenGL not present")


class DisplayableEllipsoid:
    def __init__(self, shaderProgram, radius=(1.0, 1.0, 1.0), num_segments=30, color=ColorType.BLUE):
        super(DisplayableEllipsoid, self).__init__()
        self.shaderProg = shaderProg
        self.shaderProg.use()

        self.vao = VAO()
        self.vbo = VBO()  # vbo can only be initiate with glProgram activated
        self.ebo = EBO()

        self.generate(radius, num_segments, color)


    def generate(self, radius, num_segments, color):
        self.radius = np.array(radius, dtype=np.float32)
        self.num_segments = num_segments
        self.vertices = []
        self.indices = []
        utility = GLUtility()

        for i in range(self.num_segments):
            theta = 2.0 * np.pi * i / self.num_segments
            phi = np.pi * (i + 0.5) / self.num_segments

            x = self.radius[0] * np.cos(theta) * np.sin(phi)
            y = self.radius[1] * np.sin(theta) * np.sin(phi)
            z = self.radius[2] * np.cos(phi)

            vertices.extend([x, y, z])

        for i in range(self.num_segments - 1):
            indices.extend([i, i + 1])

        indices.extend([self.num_segments - 1, 0])  # Closing the loop

        return np.array(vertices, dtype=np.float32), np.array(indices, dtype=np.uint32)
        
    def draw(self):
        self.vao.bind()
        # TODO 1.1 is at here, switch from vbo to ebo
        self.ebo.draw() #switched to ebo
        self.vao.unbind()

    def initialize(self):
        self.vao.bind()
        self.vbo.setBuffer(self.vertices, 11)
        self.ebo.setBuffer(self.indices)

        self.vbo.setAttribPointer(self.shaderProg.getAttribLocation("vertexPos"),
                                  stride=11, offset=0, attribSize=3)
        self.vbo.setAttribPointer(self.shaderProg.getAttribLocation("vertexNormal"),
                                  stride=11, offset=3, attribSize=3)
        self.vbo.setAttribPointer(self.shaderProg.getAttribLocation("vertexColor"),
                                  stride=11, offset=6, attribSize=3)
        # TODO/BONUS 6.1 is at here, you need to set attribPointer for texture coordinates
        # you should check the corresponding variable name in GLProgram and set the pointer
        self.vao.unbind()