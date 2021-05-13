import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th                    #this one is to import nested lists to grasshopper trees
import math


# 2.CREATE POINTS ////////////////////////

list_a = []
list_b = []

for i in range (int(x)):
   px = rg.Point3d(i, 0, 0)
   py = rg.Point3d(i, y, 0)
   list_a.append (px)
   list_b.append (py)

    
a = list_a
b = list_b

# 3.CREATE LINES ////////////////////////

line_list = []


for i in range(x):
        l = rg.LineCurve (list_a[i], list_b[i])
        line_list.append(l)

c = line_list


# 4.DIVIDE CURVE ////////////////////////

allDivPts = []                                          # List of lists

for i in line_list:
    linePts = []                                        # create an empty list to fill each iteration
    n_crv = i.ToNurbsCurve()
    div_crv = n_crv.DivideByCount (z,True)
    linePts.append(div_crv)
    
    divPts = []
    for p in  div_crv :
        divPts.append(n_crv.PointAt(p))
    allDivPts.append(divPts)
    
d = th.list_to_tree(allDivPts)


# 5.SIN FUNCTION //////////////////////////            

Sin_Vec=[]                                              # list of moved points
for i in allDivPts:
    pt_vec= []
    for j in i:
        sub_v = rg.Vector3d(j)                          # create vectors from points
        vec_len = (sub_v).Length                        # Vector length
        sin = math.sin (vec_len)                        # Sin function
        z_vec = rg.Vector3d(0,0,sin*u)
        sin_z = j - z_vec
        pt_vec.append(sin_z)
    Sin_Vec.append(pt_vec)


e = th.list_to_tree(Sin_Vec)                            # list of new points (sin points)


# 6.CREATE CURVES //////////////////////////

Sin_Crv_list = []

for i in Sin_Vec:
    sin_crv = rg.Curve.CreateInterpolatedCurve(i, 3)    # Create interpolate curve 
    Sin_Crv_list.append(sin_crv)

f = Sin_Crv_list


# 7.CREATE SURFACE //////////////////////////

for i in Sin_Crv_list:
    sin_srf = rg.Brep.CreateFromLoft(Sin_Crv_list, rg.Point3d.Unset, rg.Point3d.Unset, 0, False)

g = sin_srf

# 8. SRF TO MESH ////////////////////////////

Sin_Mesh = rg.Mesh.CreateFromBrep(sin_srf[v], rg.MeshingParameters(w)) 
#keep in mind that CreateFromBrep needs one Brep and CreateFromLoft() returns a list (even if only of one element)

h = Sin_Mesh

# MISSING : Control mesh U / V from (question for support)