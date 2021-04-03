December 18 2011

Dear Animator,

Here is a new .blend file that allows creation of BVH animation files, compatible with SecondLife and similar, perfectly working with Blender 2.5x
series and later, using only the native Blender exporter scripts. However,at the time of this writing, Blender doesn't provide the latest version 
of these BVH export scripts, that you will find along with this package. These scripts just need to be replaced in the right folder of your Blender 
installation, which generally is:

[your system path here]/Blender Foundation/Blender/[version #]/scripts/addons/io_anim_bvh

Once you substitute 2 of the 3 scripts in this folder, you're ready to go. You would be able to import, edit and export any BVH file, but the purpose 
of this pre-made scene is to make you able to create animations using a professional set-up on top of the basic skeleton. Inverse Kinematics and animation constraints are already set to ease out your creation process, including a stride object to easily move your character around with the least fuss possible.

This .blend file is provided free of charge for your use, you're free to modify it to better suit your needs, redistribute or rip apart. HOWEVER, 
i won't provide any support on this product alone.

The content provided consists in one SL skeleton, related constrainers and an avatar from LL, split in pieces, without materials and UV layouts in order
to get the lightest file possible. Avatar parts are not selectable in the 3D viewport to avoid selection mistakes. The scene also provides a camera and a basic lighting set up to allow character rendering for textures and videos creation for your products. Either camera either the lights are made invisible in the scene to avoid interferences with your workflow while you animate.


BASIC INSTRUCTIONS TO CORRECTLY EXPORT ANIMATIONS:

1)Pay attention to not overwrite the frame #0, which contains information about the T stance. This is important to not mess up the bones hierarchy and to export an animation that contains said stance. Even without this stance, SecondLife animation uploader and engine recognizes the motion correctly, but there might be some unwanted misalignment.

2)File menu --->export --->motion capture (bvh) is enabled only when you have the skeleton selected. Otherwise it would be grayed out.

3)Export and save screen: on the bottom left side you have the basic parameters. Make sure to export the animation with frame #0 included, since by default it is set to #1. As said above, it would work but there might be some misalignments between the animation you designed and what you actually get inworld. MOST IMPORTANT: check "root transformation only" checkbox to ensure SL compatibility.

4)IF you forgot to add the frame #0 while exporting,or even worse you have overwritten it, you get 2 choices: re-do it again from blender, or you can use BVHacker to add it afterwards. This software is free and can be found here: http://www.bvhacker.com


Happy Animating!

OptimoMaximo (SL name)