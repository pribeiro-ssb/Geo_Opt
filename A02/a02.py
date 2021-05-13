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

1.remap angleList
remaped=[]
for i in angleList:
    remaped_value=(((i - min(angleList)) * (max_off - min_off)) / (max(angleList) - min(angleList))) + min_off
    remaped.append(remaped_value)
#2. Get the Faces outlines
outlines=[]
for i in exploded:
    outline=rg.Mesh.GetNakedEdges(i)
    outlines.append(outline)


# join outlines
joined_outlines=[]
for i in outlines:
    curves=[]
    for j in i:
        curve=rg.Polyline.ToNurbsCurve(j)
        curves.append(curve)
    joined=rg.Curve.JoinCurves(curves)[0]
    joined_outlines.append(joined)
# Offset outlines
mesh_points=[]
for i in exploded:
    points=rg.Mesh.Vertices.GetValue(i)
    mesh_points.append(points)
mesh_points_3d=[]
for i in mesh_points:
    sub=[]
    for j in i:
        pt=rg.Point3d(j)
        sub.append(pt)
    mesh_points_3d.append(sub)


offset_outlines=[]
for i in range(len(joined_outlines)):
    surface=rg.NurbsSurface.CreateFromPoints(mesh_points_3d[i],2,2,2,2)
    off=rg.Curve.OffsetOnSurface(joined_outlines[i],surface,remaped[i],.001)[0]
    offset_outlines.append(off)
    
# Loft 
lofted_breps=[]
for i in range(len(offset_outlines)):
    list_curves=[offset_outlines[i],joined_outlines[i]]
    lofted=rg.Brep.CreateFromLoft(list_curves,rg.Point3d.Unset,rg.Point3d.Unset,rg.LoftType.Normal,False)[0]
    lofted_breps.append(lofted)