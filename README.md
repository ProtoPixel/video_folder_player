# Video Folder Player for ProtoPixel

Example of a simple video folder player, that will load videos from a folder and play them.

This script exposes the following parameter:

* _video folder_ : folder with videos to play

The content will start playing the videos of the folder alphabetically, once the last video has been
played, it will start again.

## Instructions

* [Add the video_folder_player.py script](https://protopixel.net/doc/create/operational_guide.html#adding-content) into your ProtoPixel Create Project.
* Select the content, this will show the content's parameters in the inspector panel.
* Change the _video folder_ parameter to the path of your videos folder.

## Exporting

When exporting the project, the videos will be packed with it. This may result in a very big file. To prevent that, reset the _video folder_ parameter before exporting the project.

### Default path

There is a variable in the script that can be set to define a default path, in case of permanently preventing packing and unpacking videos on export. Just change the `DEFAULT_VIDEO_PATH` variable to use it.