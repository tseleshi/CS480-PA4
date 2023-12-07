import math
import numpy as np
import ColorType
from Animation import Animation
from Component import Component
from Light import Light
from Material import Material
from Point import Point
import GLUtility
from DisplayableCube import DisplayableCube
from DisplayableSphere import DisplayableSphere
from DisplayableTorus import DisplayableTorus
from DisplayableEllipsoid import DisplayableEllipsoid
from DisplayableCylinder import DisplayableCylinder

class SceneThree(Component):
    shaderProg = None
    glutility = None
    lights = None
    lightSpheres = None

    def __init__(self, shaderProg):
        super().__init__(Point((0, 0, 0)))
        self.shaderProg = shaderProg
        self.glutility = GLUtility.GLUtility()

        sphere = Component(Point((0, 0, 0)), DisplayableSphere(shaderProg, 0.5, ColorType.BLUE))
        m1 = Material(np.array((0.1, 0.1, 0.1, 0.1)), np.array((0.2, 0.2, 0.2, 1)),
                      np.array((0.4, 0.4, 0.4, 0.1)), 64)
        sphere.setMaterial(m1)
        sphere.renderingRouting = "lighting"
        self.addChild(sphere)

        l0 = Light(Point([0.0, 1.5, 0.0]),
                   np.array((*ColorType.WHITE, 1.0)))
        lightSphere0 = Component(Point((0.0, 1.5, 0.0)), DisplayableSphere(shaderProg, 0.1, ColorType.WHITE))
        lightSphere0.renderingRouting = "vertex"

        self.addChild(lightSphere0)
        self.lights = [l0, ]
        self.lightSpheres = [lightSphere0, ]

    def initialize(self):
        self.shaderProg.clearAllLights()
        for i, v in enumerate(self.lights):
            self.shaderProg.setLight(i, v)
        super().initialize()
