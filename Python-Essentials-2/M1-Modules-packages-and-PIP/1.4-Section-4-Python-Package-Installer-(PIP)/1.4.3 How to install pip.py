""" 
Antes que nada recuerda de que es buena practica usar entornos virtuales para tus proyectos en Python.
El uso de entornos virtuales te permite gestionar dependencias y paquetes de manera aislada para cada proyecto, 
evitando conflictos entre diferentes proyectos y manteniendo tu entorno de desarrollo limpio.

Crear y activar un entorno virtual es sencillo. Aquí te dejo los pasos básicos:
1. Crear un entorno virtual:
    python -m venv nombre_del_entorno
2. Activar el entorno virtual:
    - En Windows:
        nombre_del_entorno\Scripts\activate
    - En macOS y Linux:
        source nombre_del_entorno/bin/activate
Una vez que el entorno virtual esté activado, cualquier paquete que instales usando pip se instalará únicamente en ese entorno,
sin afectar al resto de tu sistema o a otros proyectos.

Ahora recuerda que para trabajar con el entorno virtual en Visual Studio Code,
asegúrate de seleccionar el intérprete de Python correcto asociado con tu entorno virtual.

Use the Python: Select Interpreter command from the Command Palette (Ctrl+Shift+P) and select the python interpreter that belongs to the new virtual environment.

Enlace con mas info:
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments
https://code.visualstudio.com/docs/python/environments
https://stackoverflow.com/questions/54009081/how-can-i-debug-a-python-code-in-a-virtual-environment-using-vscode
"""

""" # 1.4.3 How to install pip """

# The question that should be put now is: how to get a proper cheese knife? In other words, how to ensure that pip is installed and ready to work?

# The most precise answer is “it depends”. Really.

# Some Python installations come with pip, some don't. What’s more, it doesn’t only depend on the OS you use, although this is a very important factor.

# Let's start with MS Windows.

    # """ # pip on MS Windows """
# The MS Windows Python installer already contains pip, and so no other steps need to be taken in order to install it. 
# Unfortunately, if the PATH variable is misconfigured, pip may unavailable.

# To verify that we haven’t misled you, try to do this:

# open the Windows console (CMD or PowerShell, whatever you prefer)
# execute the following command:
# pip --version

# in the most optimistic scenario (and we really want that to happen) you’ll see something like this:
        # pip 19.2.3 from c:\program files\python3\lib\site-packages\pip (python 3.8)

# the absence of this message may mean that the PATH variable either incorrectly points to the location of the Python binaries, or doesn't point to it at all; 
# for example, our PATH variable contains the following substring:
        # C:\Program Files\Python3\Scripts\;C:\Program Files\Python3\;

# the easiest way to reconfigure the PATH variable is to reinstall Python, instructing the installer to set it for you.


    # """ # pip on Linux """
# Different Linux distributions may behave differently when it comes to using pip. 
# Some of them (like Gentoo), which are closely bound to Python and which use it internally, may have pip preinstalled and are instantly ready to work.

# Don't forget that some Linuces may utilize more than one Python version concurrently, 
# e.g., one Python 2 and one Python 3 coexisting side by side. 
# Such systems may launch Python 2 as the default version, and it may be necessary to explicitly specify the program name as python3. 
# In this case there may be two different pips identified as pip (or pip2) and pip3. Check it carefully.

# Open the terminal window and issue the following command:

# pip --version
        # pip 20.0.2 from /usr/lib/python2.7/site-packages/pip (python 2.7)

# An answer similar to the one shown in the previous picture determines that you've launched pip from Python 2, so the next try should look as follows:

# pip3 --version
        # pip 20.0.2 from /usr/lib/python3.8/site-packages/pip (python 3.8)

# As you can see, we’re now sure that we’re using the appropriate version of pip.

# Unfortunately, some Linux distributions don't have pip preinstalled, even if Python itself is installed by default (some versions of Ubuntu may behave this way). 
# In this case, you have two possibilities:

    # install pip as a system package using a dedicated package manager (e.g., apt in Debian-like systems)
    # install pip using internal Python mechanisms.
    
# The former is definitely better. Although there are some smart scripts that are able to download and install pip by ignoring the OS, we discourage you from using them. 
# This method can get you into trouble.
# Look – we've tried to launch pip3 and we’ve failed. Our OS (we used Ubuntu Budgie this time) suggested using apt in order to install the package named python3-pip:

        # """ # Installing pip using the OS package manager """
        # """ sudo apt install python-pip """


# That's good advice, and we're going to follow it, but it has to be stated that we’ll need administrative rights to do it. 
# Don't forget that different Linuces may use different package managers (e.g., it could be pacman if you use Arch Linux, or yum used by distributions derived from Red Hat).

# Anyway, all these methods should get pip (or pip3) installed and working.

# Look what happened when we followed the OS suggestion:


# As you can see, the OS decided to install not only pip itself, but also a couple of additional components needed by pip. This is normal – don't be alarmed.

# When apt finishes its job, we are finally able to utilize pip3:


# If you're a Mac user and you've installed Python 3 using the brew installer, pip is already present in your system and ready to work. 
# Check it by issuing the previously mentioned command:


# pip3 --version
 
# and wait for the response.

# This is what we saw: