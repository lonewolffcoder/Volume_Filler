import bpy
import bmesh
from mathutils.bvhtree import BVHTree

Scene = bpy.context.scene
Objects = bpy.context.scene.objects
Active_object = bpy.context.active_object

Intersections = []

def get_start_positon:
    
    world_position = Active_object.matrix_world
    
    ao_mesh = bmesh.new()
    ao_mesh.from_mesh(Active_object.data)
    ao_mesh.transform(Active_object.matrix_world)
    
    vertex_positions = []
    for vert in ao_mesh.verts:
        vertex_positons.append(vert.co)
        
        
    # Start from cursor
    
    # Start from -X
    
    # Start from +X
    
    # Start from -Y
    
    # Start from +Y
    
    # Start from -Z
    
    # Start from +Z
    
def get_end_position:
    # End cursor
    
    # End at -X
    
    # End at +X
    
    # End at -Y
    
    # End at +Y
    
    # End at -Z
    
    # End at +Z
    
def generate_fill_objects:
    
    

def get_active_object_intersections():
    
    # Check every object in the scene for intersections with the active_object
    for obj in Objects:
        if Active_object == obj:
            continue
        
        # Create bmesh objects
        bm_ao = bmesh.new()
        bm_next = bmesh.new()
        
        # Fill bmesh data from scene objects
        bm_ao.from_mesh(Active_object.data)
        bm_next.from_mesh(obj.data)
        
        # Apply world transform
        bm_ao.transform(Active_object.matrix_world)
        bm_next.transform(obj.matrix_world)
        
        # Make BVH tree from BMesh objects
        obj_ao_BVH = BVHTree.FromBMesh(bm_ao)
        obj_next_BVH = BVHTree.FromBMesh(bm_next)
        
        # Get overlapping objects
        overlap = obj_ao_BVH.overlap(obj_next_BVH)
        
        # If 'overlap' list is empty, no objects are touching
        if overlap != []:
            print(Active_object.name + " and " + obj.name + " are overlapping")
        else:
            print(Active_object.name + " and " + obj.name + " are NOT overlapping")
        

def get_global_intersections():
    for obj_now in Objects:
        
        # Check every object in the scene for intersections with all the other objects
        for obj_next in Objects:
            #print(obj_now.name + " :: " + obj_next.name)
            
            if obj_now == obj_next:
                continue
            
            # Create bmesh objects
            bm_now = bmesh.new()
            bm_next = bmesh.new()
            
            # Fill bmesh data from scene objects
            bm_now.from_mesh(obj_now.data)
            bm_next.from_mesh(obj_next.data)
            
            # Apply world transform
            bm_now.transform(obj_now.matrix_world)
            bm_next.transform(obj_next.matrix_world)
            
            # Make BVH tree from BMesh objects
            obj_now_BVH = BVHTree.FromBMesh(bm_now)
            obj_next_BVH = BVHTree.FromBMesh(bm_next)
            
            # Get overlapping objects
            overlap = obj_now_BVH.overlap(obj_next_BVH)
            
            # If 'overlap' list is empty, no objects are touching
            if overlap != []:
                print(obj_now.name + " and " + obj_next.name + " are overlapping!")
                for item in overlap:
                    Intersections.append(item)
            else:
                print(obj_now.name + " and " + obj_next.name + " are NOT overlapping!")
                
        
get_active_object_intersections()