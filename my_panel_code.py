'''
version 2.79
'''

import bpy

FloatProperty = bpy.props.FloatProperty
IntProperty = bpy.props.IntProperty
BoolProperty = bpy.props.BoolProperty
CollectionProperty = bpy.props.CollectionProperty
EnumProperty = bpy.props.EnumProperty
FloatVectorProperty = bpy.props.FloatVectorProperty
IntVectorProperty = bpy.props.IntVectorProperty

EnumProperty(attr="lamp_type",
	items = (
		("Area","Area",""),
		("Directional","Directional",""),
		("MeshLight","MeshLight",""),
		("Point","Point",""),
		("Sphere","Sphere",""),
		("Spot","Spot",""),
		("Sun","Sun",""),
),default="Sun")

BoolProperty(attr="infinite")

IntProperty(attr="angle",
		max = 80,
		min = 0)

class YAF_PT_lamp(bpy.types.Panel):

	bl_label = 'Lamp'
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = 'object'
	COMPAT_ENGINES =['YAF_RENDER_ENGINE']

	def draw(self, context):

		layout = self.layout
		split = layout.split()
		col = split.column()

		col.label(text="lamp_type")
		col.prop(context.scene,"lamp_type", text= "")

		if context.scene.lamp_type == 'Area':
			context.lamp.type = 'AREA'
			col.prop(context.lamp,"shadow_ray_samples", text= "Samples")
			
		if context.scene.lamp_type == 'Directional':
			context.lamp.type = 'SUN'
			col.prop(context.scene,"infinite", text= "Infinite")
			col.prop(context.lamp,"shadow_soft_size", text= "Radius")
			
		if context.scene.lamp_type == 'Sphere':
			context.lamp.type = 'POINT'
			col.prop(context.lamp,"shadow_soft_size", text= "Radius")
			col.prop(context.lamp,"shadow_ray_samples", text= "Samples")			

		if context.scene.lamp_type == 'Spot':
			context.lamp.type = 'SPOT'
			col.prop(context.lamp,"spot_blend", text= "Blend")
			col.prop(context.lamp,"spot_size", text= "Cone Angle")		

		if context.scene.lamp_type == 'Sun':
			context.lamp.type = 'SUN'
			col.prop(context.scene,"angle", text= "Angle")
			col.prop(context.lamp,"shadow_ray_samples", text= "Samples")
			
		if context.scene.lamp_type == 'Area':
			context.lamp.type = 'POINT'

		col.prop(context.lamp,"color", text= "Color")
		col.prop(context.lamp,"energy", text= "Power")

def register():
    bpy.utils.register_class(YAF_PT_lamp)

def unregister():
    bpy.utils.unregister_class(YAF_PT_lamp)

if __name__ == "__main__":
    register()