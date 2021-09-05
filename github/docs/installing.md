# Installing SpotDLGUI

### Requirements

- Python 3.9+ (in PATH)
- ffmpeg (in PATH

#### Installing ffmpeg

- [Windows Tutorial](https://windowsloop.com/install-ffmpeg-windows-10/)
- OSX `brew install ffmpeg`
- Linux `sudo snap install ffmpeg`

#### Download the project

You can clone the project with Git using:

```
git clone https://github.com/MrFellox/spotdlgui.git
```

Or downloading it [here](https://github.com/MrFellox/spotdlgui/archive/refs/heads/main.zip).

You can now extract it wherever you like.

#### Creating a Virtual Environment (optional)

You may want to create a virtual environment, to keep the tool's dependencies separated from the other modules you may have installed.

Open up a terminal in the root of the project's folder, and run:

```
python -m venv venv
```

Wait until the venv is created and then activate it with:

```
venv\Scripts\activate
```

**NOTE: If you are using a Virtual Environment to install the dependencies, you have to activate it every time you want to run the tool.**

#### Installing dependencies

Open up a terminal in the root folder of the project and run:

```
python -m pip install -r requirements.txt
```

Wait until everything installs.

#### Running the tool

In the root folder of the project, go to the `spotdlgui` folder, and run a terminal in there.
Now, run the python file with:

```
python main.py
```

And you should be good to go!