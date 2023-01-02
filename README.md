# fbx-to-wtf
convert .fbx 3D model files to .wtf files via Blender

An FBX file dragged onto the .bat file will run Blenders python script "fbxtowtf.py" and produce a .wtf file that works in igame3d!

ChatGPT crappped out before I we could figure out the part where unjoined models in the scene would make it into the WTF file.

If you do coding with ChatGPT and it stops writing code you just tell it 'continue' and it will finish up writing code.

This script doesn't really parse the blender materials to igame3d materials, just uses the default material I taught chatGPT with (our cube.wtf)

be sure to point the .bat file to your installed location of blender
