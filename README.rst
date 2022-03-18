.. image:: https://github.com/Kejax/Hypixel-Lib/blob/main/doc/Main.png
	:target: https://hypixel.net
	:alt: Hypixel Lib


The Lib to request Hypixel API
===============================

With this API you're able to get much more info from the public Hypixel API
as from hypixelaPY

Big update is coming soon!
--------------------------

I'm working on a big update to offer more functions regarding information from the API, such as leaderboards, guilds, friends and else. Also I'm working on the `documentation <https://hypixel-lib.readthedocs.io>`_ to offer a documentation to explain most of the library.
If you got code or ideas for the library, please open a pull request


Why I should use it?
---------------------

You should use it, because it's a friendly Lib, wich is able to be added by functions


What is included in this Lib?
-----------------------------

This Lib includes nearly all features from the Hypixel API
some features of the Mojang API and the Mojang SessionServer
returns pictures from the `plancke.io <https://plancke.io>`__ picture generator

(Mojang SessionServer, Mojang API & plancke features not build in yet) 

Import Hypixel-Lib in Python
-----------------------------

.. code:: sh
    
    pip install hypixellib

.. code:: python

    import HypixelLib
    
Code Examples
^^^^^^^^^^^^^

.. code:: python
    
    import HypixelLib
    
    hypixel = HypixelLib.Hypixel("<APIKEY>")
    
    player = hypixel.player.get(name="name", uuid="uuid")
    print(player.name)
    print(player.rank.name)
    print(player.uuid)
