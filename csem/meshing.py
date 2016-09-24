
import pyvtk
import numpy as np
from scipy.spatial import Delaunay

def generate_spherical_shell():

    vertices = np.array([[0,0,0],
                        [2,0,0],
                        [2,2,0],
                        [0,2,0],
                        [0,0,12],
                        [2,0,12],
                        [2,2,12],
                        [0,2,12]])
    tets = Delaunay(vertices)
    print tets.simplices

    vtk_elements = pyvtk.VtkData(
        pyvtk.UnstructuredGrid(vertices, tetra=tets.simplices))
    vtk_elements.tofile('./test.vtk')
