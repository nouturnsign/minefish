# Minefish

Automatic fishing script. Uses image comparison.

## Setup
You will need to have an installation of Python 3. Currently, only Python
3.12.4 on OSX has been tested.

First, you need to take a screenshot of the "Fishing Bobber splashes" subtitle.
- The screenshot must only contain the subtitle itself.
- You can crop the image (i.e. not including all of the text) for better
  performance.
- An example is included in `image-example.png` and reproduced below.
![Example of image required for Minefish to work](image-example.png)

Save the screenshot as `image.png`.

Then, I recommend using a virtual environment. Use
```sh
/path/to/python3 -m venv
```

to create a virtual environment. Then, run
```sh
source venv/bin/activate
```
to activate the virtual environment.

Finally, run
```sh
pip install -r requirements.txt
```

This installs all the dependencies.

## Run
If you used a virtual environment, run
```sh
source venv/bin/activate
```
again.

Then, run
```sh
python3 fisher.py
```
to run the script. You can start the script before beginning to fish; you are
given a grace period of sixty seconds before the first fish. If after sixty
seconds no fish have been caught, the program will stop.
