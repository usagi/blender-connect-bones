### The code for add-on ecosystem ###

bl_info = {
 'name'    : 'connect-bones',
 'blender' : ( 2, 80, 0 ),
 'category': 'Armature',
 'author'  : 'USAGI.NETWORK / Usagi Ito',
 'version' : ( 0, 1, 0 ),
 'support' : 'TESTING',
}

addon_keymaps = []

import bpy
from itertools import chain
from re import compile
import numpy

class ConnectBones( bpy.types.Operator ):
 '''Connect bones if it find a bone pair that has a same position of a head and a tail'''
 bl_idname  = 'armature.connect_bones'
 bl_label   = 'Connect bones'
 bl_options = { 'REGISTER', 'UNDO' }
 
 name_regex: bpy.props.StringProperty( name = 'name_regex', default = '.*' )
 tolerance: bpy.props.FloatProperty( name = 'tolerance', default = 0.0 )
 
 def execute( self, context ):
  return connect_bones( self.name_regex, self.tolerance )

def register():
 bpy.utils.register_class( ConnectBones )
 bpy.types.VIEW3D_MT_object.append( menu )
 wm = bpy.context.window_manager
 kc = wm.keyconfigs.addon
 if kc:
  km = wm.keyconfigs.addon.keymaps.new( name = '3D View', space_type = 'VIEW_3D' )
  kmi = km.keymap_items.new( idname = ConnectBones.bl_idname, type = 'C', value = 'PRESS', ctrl = True, shift = True, alt = True )
  kmi.properties.name_regex = '(?!)'
  addon_keymaps.append( ( km, kmi ) )

def unregister():
 bpy.utils.unregister_class( ConnectBones )
 for km, kmi in addon_keymaps:
  km.keymap_items.remove(kmi)

def menu( self, context ):
 self.layout.separator()
 self.layout.operator( ConnectBones.bl_idname )
 addon_keymaps.clear()

if __name__ == '__main__':
 register()

### The main code of the add-on ###

def connect_bones( name_regex = '.*', tolerance = 0.0 ):
 bpy.ops.object.mode_set(mode='EDIT')
 
 armatures = bpy.data.armatures
 bones     = list( chain( *[ a.edit_bones for a in armatures ] ) )
 
 regex = compile( name_regex )
 
 filtered_bones = [ b for b in bones if regex.match( b.name ) ]
 
 is_close = ( lambda a, b: a == b ) if tolerance == 0.0 else ( lambda a, b: numpy.isclose( numpy.linalg.norm( a - b ), 0.0, atol = tolerance ) )
 
 def find_connectable_pair( parent ):
  for candidate in filtered_bones:
   if is_close( parent.tail, candidate.head ):
    return ( parent, candidate )
 
 connectable_pairs = [ p for p in map( find_connectable_pair, filtered_bones ) if p != None ]
 
 for p in connectable_pairs:
  print( 'connect-bones:', p[0].name, '<-', p[1].name )
  p[1].select = True
  p[0].select = True
  armatures[0].edit_bones.active = p[0]
  bpy.ops.armature.parent_set()
  p[0].select = False
  p[1].select = False
 
 for p in connectable_pairs:
  p[0].select = True
  p[1].select = True
 
 return {'FINISHED'}
