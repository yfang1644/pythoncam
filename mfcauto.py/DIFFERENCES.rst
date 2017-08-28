=============================================================
Differences between the Python and NodeJS versions of MFCAuto
=============================================================

As of April 22, 2017:

- Many function names are different in an attempt to be more Pythonic. In some cases names have simply been converted to lowercase, in other cases camel casing as been converted to underscore separated names
- Model.when is not yet implemented
- Client.sendChat and Client.sendPM do not support encoding emotes
- To work with events for all models, use Model.All.on(...) instead of Model.on(...)
- Model.bestsession and Packet.smessage are Python dict objects and not expando classes
    - This means that instead of 'model.bestsession.vs' you must do 'model.bestsession["vs"]'
    - Additionally, since they are Python dicts, accessing a non-existent property will result in a KeyError rather than simply returning undefined
- Client emits events based on FCTYPE enum values, not strings.  So use client.on(FCTYPE.USERNAMELOOKUP,...) for instance, instead of client.on("USERNAMELOOKUP",...) as you would do for NodeJS
- Client doesn't contain a 'connectAndWaitForModels' function. Instead it emits a new FCTYPE.CLIENT_MODELSLOADED event.
- Client also emits a FCTYPE.CLIENT_CONNECTED event on first connecting the underlying socket
