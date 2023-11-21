import dungeon_generator

dg = dungeon_generator.DungeonGenerator().generate()
dg.save_image()
dg.save_cost_plot()