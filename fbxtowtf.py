import bpy
import sys
import os

# Set the input and output filenames
input_filename = sys.argv[-1]
output_filename = input_filename.replace('.fbx', '.wtf')

# Normalize the input filename
input_filename = os.path.normpath(input_filename)

# Import the .fbx file
bpy.ops.import_scene.fbx(filepath=input_filename)

# Define the .wtf export function
def export_wtf(filename, objects):
    # Open the output file
    with open(filename, 'w') as f:
        # Write the header information
        f.write("iGame3D Mdl\n")
        f.write("0\n")
        f.write("#Author:\n")
        f.write("#Date:\n")
        f.write("#Notes:\n")
        f.write("#PNG: 0\n")
        
        # Write the bone information
        f.write("#Bones:\n")
        f.write("0\n")
        
        # Write the vertex information
        f.write("#Vertices:\n")
        f.write(str(len(objects[0].data.vertices)) + "\n")
        for vertex in objects[0].data.vertices:
            f.write("{:.6f},{:.6f},{:.6f},0\n".format(vertex.co[0] * 400, vertex.co[1] * 400, vertex.co[2] * 400))
        # Write the path information
        f.write("#Paths:\n")
        f.write("0\n")
    
        # Write the group information
        f.write("#Groups:\n")
        f.write("0\n")
    
        # Write the edge information
        f.write("#Edges:\n")
        f.write(str(len(objects[0].data.edges)) + "\n")
        for edge in objects[0].data.edges:
            f.write(str(edge.vertices[0]) + "," + str(edge.vertices[1]) + "\n")
    
        # Write the material information
        f.write("#Materials:\n")
        #f.write("{}\n".format(str(len(bpy.data.objects.data.meshes.keys()))))
        #f.write("acmat_0\n")
    
        # Write the triangle information
        f.write("{}\n".format(len(objects)))
        for obj in objects:
            f.write("{}\n".format(obj.name.title()))
            f.write("11\n")
            f.write("smooth=0\n")
            f.write("color=1.000000,1.000000,1.000000,1.000000\n")
            f.write("ambient=0.200000,0.200000,0.200000,1.000000\n")
            f.write("diffuse=0.800000,0.800000,0.800000,1.000000\n")
            f.write("specular=0.000000,0.000000,0.000000,1.000000\n")
            f.write("shininess=0.000000\n")
            f.write("emission=0.000000,0.000000,0.000000,1.000000\n")
            f.write("blend=0\n")
            f.write("texture=1,Data/Images/normalWalls/wall280.png\n")
            f.write("wire=0.000000\n")
            f.write("depth=1\n")
    
            f.write("{}\n".format(len(obj.data.polygons)))
            for face in obj.data.polygons:
                f.write("{},{},{},0.000000,1.000000,1.000000,1.000000,1.000000,0.000000\n".format(face.vertices[0], face.vertices[1], face.vertices[2]))

        # Write the animation information
        f.write("#Animations\n")
        f.write("0\n")


#Export the .wtf file
export_wtf(output_filename, bpy.context.selected_objects)

#Convert the line endings from Windows style to Unix style
with open(output_filename, 'rb') as f:
    contents = f.read()

with open(output_filename, 'wb') as f:
    f.write(contents.replace(os.fsencode("\r\n"), os.fsencode("\n")))

#Quit Blender
bpy.ops.wm.quit_blender()