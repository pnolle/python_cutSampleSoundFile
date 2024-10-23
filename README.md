# Cut sample sound file

Assuming you have an AIF file that contains sample sound with silence in between each sample. This script 
* iterates through the ``file_names`` array in the ``config.json`` file and looks for them in a subfolder called ``input_files``
* cuts the file in chunks and stores them according to the ``sample_names`` in the ``config.json`` file in a subfolder called ``output_chunks``

## How to use

* run Docker daemon
* ``docker build -t cuts_img .``, while ``cuts_img`` is my chosen image name
* ``docker run --rm -v ./:/usr/src/app cuts_img``, which
  * starts the image as a container
  * with the ``--rm`` option to remove the container after the job is done
  * and the ``-v`` option to map the local folder to the ``/usr/src/app`` folder within the container, where the script is working

## Disclaimer

I discussed the development of this script with AI tools.