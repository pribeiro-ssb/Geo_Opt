"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""
        
import Rhino.Geometry as rg

#1.
#compute face normals using rg.Mesh.FaceNormals.ComputeFaceNormals()
#output the vectors to a


m.FaceNormals.ComputeFaceNormals()      # m = input meshin GH
m.Flip(m.FaceNormals, True, True, True) 
a = m.FaceNormals

#2.
#get the centers of each faces using rg.Mesh.Faces.GetFaceCenter()
#store the centers into a list called centers 
#output that list to b

face_centers = [m.Faces.GetFaceCenter(i) for i in xrange(m.Faces.Count)]
b = face_centers

#3.
#calculate the angle between the sun and each FaceNormal using rg.Vector3d.VectorAngle()
#store the angles in a list called angleList and output it to c

angleList = []
for i in a:
    angle = rg.Vector3d.VectorAngle(s,i) 
    angleList.append(angle)

c = angleList

#4. explode the mesh - convert each face of the mesh into a mesh
#for this, you have to first copy the mesh using rg.Mesh.Duplicate()
#then iterate through each face of the copy, extract it using rg.Mesh.ExtractFaces
#and store the result into a list called exploded in output d

meshDup = rg.Mesh.Duplicate(m)
meshDup_faces = meshDup.Faces.Count

exploded = []
for i in range (meshDup_faces):
    extMesh = meshDup.Faces.ExtractFaces([0])
    exploded.append(extMesh)

d = exploded

##after here, your task is to apply a transformation to each face of the mesh
#the transformation should correspond to the angle value that corresponds that face to it... 
#the result should be a mesh that responds to the sun position... its up to you!

""" Not completed

Questions : 
- Extract edges from a mesh/surface?
- Define plane by mesh orientation?


meshSquares = []

for i in range (len(face_centers)):
    squares = rg
    meshSquares.append(squares)
    
e = meshSquares
    
"""