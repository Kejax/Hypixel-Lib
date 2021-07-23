Hypixel-Lib Documentation
=======================================


.. toctree::
   :caption: Player
   :glob:
   :hidden:
   
   player/*

   

Hypixel-Lib installieren:
^^^^^^^^^^^^^^^^^^^^^^^^^^

Hypixel-Lib via pip installieren:

.. code-block:: sh
   
   pip install hypixellib

Und im Skript importieren:

.. code-block:: python

    import HypixelLib

How to: Hypixel-Lib benutzen:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import HypixelLib
    
    hypixel = HypixelLib.hypixel(<APIKEY>)
    player = hypixel.Player.get(name=<Your Name>)
    print(player.name)

Dieser Code gibt den Namen des Spielers aus, wenn er jemals auf Hypixel gejoint ist.


Wie bekomme ich den API Schlüssel?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Du bekommst den API Schlüssel, indem du ``/api new`` auf dem Hypixel Server(``play.hypixel.net``)
eingibst.



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
