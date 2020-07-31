# face-recognition
Face detection and recognition on static images in pyhton using face_recognition, dlib and opencv.

### Setting known images
Every image in a "known_faces" subdirectory *must contain exactly one face*, images without faces will throw an exception. Needless to say, images with more that one face 
are clearly problematic.

It is not mandatory for each folder to have an inmense amount of pictures. Furthermore, these images do not have to be of great size. Although both these aspects will increase the
accuracy, they *will* make the program considerably slower.

What *is* important is for the pictures to represent the subject cleary. The persons's face should be at least the 25% of the image. Ideally, facing the camera. Including bad
images will not make the program more accuarate, quite the contrary, as you will probably need to lower the database tolerance if you dou so.

Here is an example of a good reference picture:

![OBAMA_GOOD_PIC](https://canalhistoria.es/wp-content/uploads/2018/07/president_official_portrait_hires-1.jpg)


Here is an example of a bad reference picture

![OBAMA_BAD_PIC](https://phantom-elmundo.unidadeditorial.es/1a42e937bde54601bd22cdc7dc208769/resize/746/f/jpg/assets/multimedia/imagenes/2020/02/12/15815150736995.jpg)

*Small face and looking at the side. Worst of all, there are multiple subjects*
