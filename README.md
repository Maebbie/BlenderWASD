## **Latest release: https://github.com/Maebbie/Blender-Mapping-Config-WASD-Movement-and-more/releases**

Aimed to make Blender easily usable for building Worlds/Mapping similar to how Hammer and
ProBuilder work. For Blender 2.8 and up. Used to make Atoll of Ether, Eventide, HomeBox and the ChilloutVR Hub World.
See this video for a video guide and showcase:
https://www.youtube.com/watch?v=1sPXOYgrZdE&list=PLHPl0SFKkUjNIZs5K9BV4pgXiLrQpEu2D

First released on 2019-09-25 - https://twitter.com/Maebbie/status/1176907912050106374
and since then refined regularly. (Previously called "ProbuilderInBlender")

![b00](https://github.com/user-attachments/assets/ab323208-942b-4afb-af3b-933ced171055)

Setup:
- Throw everything into the same folder,
- Start the BlenderWASD_By_Maebbie.blend file,
- Import the keybinds from BlenderWASDKeybinds_By_Maebbie.blend.py
  Edit -> Preferences -> Keymap -> Import -> Select the Keybinds imported on the center top.
- From 2.83 and 3.0 onwards: Put the gridoverlay.py 
  C:\Users\(your username)\AppData\Roaming\Blender Foundation\Blender\2.90\scripts\startup
  This will show your current Gridscale like you would in ProGrids when pressing N
  on the top right. 

Controls:
- Hold Right Mouse and use WASD to fly around like in Unity, use the scroll wheel to make it go
  faster/slower while flying.
  You may adjust the speed in Edit -> Preferences -> Navigation -> Walk
- + and - (or Numpad + and -) adjust the Grid scale
  (press the magnet in the top center to turn off)
  Rebind these at 3D View - 3D View (Global) - Context Scale Float if desired.
- Middle Mouse button for the context menu in the Scene window (was Right Mouse before)
- The other Controls are just like default Blender
- Please copy using Shift+D and not ctrl+c ctrl+v or else you also duplicate materials
- Generally in Blender you can execute a shortcut and press right Mouse to cancle movement
  Meaning instead of duplicating and moving it, you can duplicate, press the right mouse
  button and then move it with the arrows as it works in ProBuilder.

Available Tabs:
  At the top of your window you will find a few tabs:
  - Layout: Default editing window, at its top right you will have another window,
            that could be used for a general overview or a timelapse ofc.
  - UV Edit: A 1:1 split of a UV window and your 3D view, please note there is also
             a small UV window at the bottom left of the Layout tab
  - Material Edit: Hack into the node mainframe and create or edit Materials
  - GeoNode Edit: Manage Geometry Nodes and dive even deeper
  - Animation: Create Animations, this is very useful for calculating physics,
               which you then convert into a static mesh, like bedsheets.
  - Preview: A large 3D view to help Preview your scene at a 90° Field of View
  - PreviewVR: Similar to the Preview tab, however the FOV is set very low,
               in order to replicate how it would feel in VR while cropped in to a screen.
               I have tested it to be accurate with around 1 Meter away from a monitor.

Common issues:
  If you do not see the Gridtexture, go to the Material menu on the left center and add a
  Image Texture where it says Color on the first of the 2 Diffuse BSDF shaders.
  Then select the Tile_Light or Tile_Dark texture for each material.
  
  You can change the color of the Background by going into the Material Edit Layout,
  selecting "World" in the Node setup where it says Object by default and then going to
  that one frame to change the Hue value from 0.5 to something else.
  To use a Background image/Skybox go to the Context.World Menu (red globe on the bottom
  right in the center of that menu, not the bottom one) and switch the Color option to
  "Environment Texture"
  
  As you progress into very large projects, you may delete some of the Nodes in the "World" section of the Node setup and wire it up as needed to gain a bit of performance.

Files:
- gridoverlay.py
- BlenderWASD_By_Maebbie.blend
- BlenderWASD_Setup.txt
- BlenderWASDKeybinds_By_Maebbie.blend.py
- Tile_Dark.png - from the "Better Tiles Measurements" pack by Toykitty (@ImToykitty)
- Tile_Light.png - from the "Better Tiles Measurements" pack by Toykitty (@ImToykitty)

If you got questions or run into any kind of issue, please share those!

~ @Maebbie
