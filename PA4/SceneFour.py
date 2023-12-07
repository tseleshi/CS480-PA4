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

class SceneFour(Component):
    shaderProg = None
    glutility = None

    lights = None
    lightToruses = None

    def __init__(self, shaderProg):
        super().__init__(Point((0, 0, 0)))
        self.shaderProg = shaderProg
        self.glutility = GLUtility.GLUtility()

        # DisplayableTorus
        torus = Component(Point((1, 0, 0)), DisplayableTorus(shaderProg, 0.25, 0.5, 36, 36, ColorType.BLUE))
        m2 = Material(np.array((0.1, 0.1, 0.1, 0.1)), np.array((0.2, 0.2, 0.2, 1)),
                      np.array((0, 0, 0, 1.0)), 64)
        torus.setMaterial(m2)
        torus.renderingRouting = "lighting"
        torus.rotate(90, torus.uAxis)
        self.addChild(torus)

        # DisplayableEllipsoid
        ellipsoid = Component(Point((-1, 0, 0)), DisplayableEllipsoid(shaderProg, (0.5, 0.3, 0.2), 30))
        m3 = Material(np.array((0.1, 0.1, 0.1, 0.1)), np.array((0.2, 0.2, 0.2, 1)),
                      np.array((0, 0, 0, 1.0)), 64)
        ellipsoid.setMaterial(m3)
        ellipsoid.renderingRouting = "lighting"
        self.addChild(ellipsoid)

        # DisplayableCylinder
        cylinder = Component(Point((0, -1, 0)), DisplayableCylinder(shaderProg, 0.3, 1.0, 30))
        m4 = Material(np.array((0.1, 0.1, 0.1, 0.1)), np.array((0.2, 0.2, 0.2, 1)),
                      np.array((0, 0, 0, 1.0)), 64)
        cylinder.setMaterial(m4)
        cylinder.renderingRouting = "lighting"
        self.addChild(cylinder)

        l0 = Light(Point([0.0, 1.5, 0.0]),
                   np.array((*ColorType.WHITE, 1.0)))
        lightTorus0 = Component(Point((0.0, 1.5, 0.0)), DisplayableTorus(shaderProg, 0.1, 0.03, ColorType.WHITE))
        lightTorus0.renderingRouting = "vertex"

        self.addChild(lightTorus0)
        self.lights = [l0, ]
        self.lightToruses = [lightTorus0, ]

    def initialize(self):
        self.shaderProg.clearAllLights()
        for i, v in enumerate(self.lights):
            self.shaderProg.setLight(i, v)
        super().initialize()
