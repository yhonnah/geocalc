# main code for calculator (commit nyo sa vscode para maka push and pull tayo ng code ng madali)

from math import pi, sqrt

# sphere when radius is given

def sphereRadius(r):
    sphereDiameter = 2 * r
    circumference = pi * diameter

    sphereArea = 4 * pi * (r ** 2)
    sphereVolume = (4/3) * pi * (r ** 3)

    return sphereArea, sphereVolume, sphereDiameter, circumference
# sphere when diameter is given

def sphere_diameter(d):
    sphereRadius = d/2
    radius = sphereRadius
    circumference = d * pi 

    sphereArea = 4 * pi * (radius ** 2)
    sphereVolume = (4/3) * pi * (radius ** 3)

    return sphereArea, sphereVolume, sphereRadius, circumference

# sphere when circumference is given

def sphere_circumference(c):
    radius = c / (2 * pi)
    sphereRadius = radius
    sphereDiameter = radius / 2

    sphereArea = 4 * pi * (radius ** 2)
    sphereVolume = (4/3) * pi * (radius ** 3)

    return sphereArea, sphereVolume, radius, sphereDiameter

# area and volume of a cube

def cube(s):
    sphereArea = 6 * (s ** 2)
    sphereVolume = s ** 3

    return sphereArea, sphereVolume

# cuboid

def cuboid(length, width, height):
    cuboidArea = 2 ((length * width) + (width * height) + (length * height))
    cuboidVolume = length * width * height

    return cuboidArea, cuboidVolume

# triangular prism given sides

def triangularPrismSides(a, b, c, height, length, width):
    triangularPrismSidesPerimeter = a + b + c
    perimeter = triangularPrismPerimeter
    triangularPrismArea = (length * perimeter) + (height * width)
    triangularPrismVolume = (width * height * length) / 2

# triangular prism given perimeter

def triangularPrismPerimeter(perimeter, height, length, width):
    triangularPrismArea = (length * perimeter) + (height * width)
    triangularPrismLateralArea = perimeter + height
    triangularPrismVolume = (height * length * width) / 2

# cylinder given radius

def cylinderRadius(base, height, radius):
    cylinderDiameter = radius * 2
    cylinderLateralArea = 2 * pi * radius * height
    cylinderSurfaceArea = (2 * pi * radius * height) + (2 * pi * (radius ** 2))
    cylinderVolume = pi * (radius ** 2) * height

    return cylinderLateralArea, cylinderSurfaceArea, cylinderVolume, cylinderDiameter

# cylinder given diameter

def cylinderDiameter(base, height, diameter):
    radius = diameter / 2
    cylinderRadius = radius
    cylinderLateralArea = 2 * pi * radius * height
    cylinderSurfaceArea = (2 * pi * radius * height) + (2 * pi * (radius ** 2))
    cylinderVolume = pi * (radius ** 2) * height

    return cylinderLateralArea, cylinderSurfaceArea, cylinderVolume, cylinderRadius

# cone given radius

def coneRadius(base, height, radius):
    coneDiameter = radius * 2
    coneArea = (pi * radius) * (radius + sqrt((height ** 2) + (radius ** 2)))
    coneVolume = (pi * (radius ** 2) * height) / 3

    return coneArea, coneVolume, coneDiameter

def coneDiameter(base, height, diameter):
    coneRadius = diameter / 2
    radius = coneRadius
    coneArea = (pi * radius) * (radius + sqrt((height ** 2) + (radius ** 2)))
    coneVolume = (pi * (radius ** 2) * height) / 3

    return coneArea, coneVolume, coneRadius