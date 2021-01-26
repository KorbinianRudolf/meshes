import gmsh
import sys

# rectangle with quadratic hole

gmsh.initialize()
gmsh.model.add('t1')

x = 50
y = 15
sizeWQ = 3
sizeHQ = 4
startQX = 4
startQY = y / 2 - sizeHQ / 2
lc = 5e-1

gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(x, 0, 0, lc, 2)
gmsh.model.geo.addPoint(x, y, 0, lc, 3)
gmsh.model.geo.addPoint(0, y, 0, lc, 4)

# point for hole
gmsh.model.geo.addPoint(startQX, startQY, 0, lc, 5)
gmsh.model.geo.addPoint(startQX + sizeWQ, startQY, 0, lc, 6)
gmsh.model.geo.addPoint(startQX + sizeWQ, startQY + sizeHQ, 0, lc, 7)
gmsh.model.geo.addPoint(startQX, startQY + sizeHQ, 0, lc, 8)

gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(3, 2, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)

# curves for hole
gmsh.model.geo.addLine(5, 6, 5)
gmsh.model.geo.addLine(7, 6, 6)
gmsh.model.geo.addLine(7, 8, 7)
gmsh.model.geo.addLine(8, 5, 8)

gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1)
gmsh.model.geo.addCurveLoop([8, 5, -6, 7], 2)

gmsh.model.geo.addPlaneSurface([1, 2], 1)

gmsh.model.geo.synchronize()

# gmsh.model.addPhysicalGroup(1, [1, 2, 4], 5)
# ps = gmsh.model.addPhysicalGroup(2, [1])
# gmsh.model.addPhysicalGroup(1, [1, 3], 1)  #wände [1,3]
# gmsh.model.addPhysicalGroup(1, [2], 2)     #outlet      # { müsste, check das nochmal [2]
# gmsh.model.addPhysicalGroup(1, [4], 3)     #inlet[4]
# gmsh.model.addPhysicalGroup(1, [5, 6, 7, 8], 4)     #sind eine einheit, nur wand [5,6,7,8]


# gmsh.model.setPhysicalName(1, 1, "Wall")
# gmsh.model.setPhysicalName(1, 2, "Outlet")
# gmsh.model.setPhysicalName(1, 3, "Inlet")
# gmsh.model.setPhysicalName(1, 4, "Object")


gmsh.model.mesh.generate(2)

gmsh.write("t1.msh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
