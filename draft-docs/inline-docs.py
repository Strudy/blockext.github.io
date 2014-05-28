# __init__.py

"""

Helper class
============

The helper class passed to run_extension should look like this:

    class Helper:
        def __init__(self):
            ...

        def _problem(self):
            # Return a string describing the problem with the extension, if
            # any. The problem report should help users troubleshoot.
            #
            # Returns None if everything is working correctly.
            #
            # Example:
            #
            #    def _problem():
            #        if not self.is_connected():
            #            return "The spaceship is not connected."

        def _on_reset(self):
            # Reset the extension to its initial state.
            #
            # Triggered by clicking the red stop button in Scratch 2.0.
            #
            # Example:
            #
            #    def _on_reset():
            #        self.stop_all_motors()

There is also an optional _connect interface:

        def _is_connected():
            # Optional.
            #
            # Called before running any of the helper class's methods.
            # If it returns False, abort

             try:
                 # ping the brick to check it's still connected
                 brick.get_battery_level()
             except USBError:
                 self.brick = None

             if not self.brick:
                 try:
                     self.block = nxt.find_one_brick()
                     ...
                 except:
                     pass # Couldn't connect :(

             return bool(self.brick)
             # ^ True if we're connected, False otherwise

        ...


"""


# helper.py

"""
Usage
=====

- define a helper class
- create an Interface
- construct a thing
- call run_forever, passing the helper class and the extension.

The Extension object defines the interface between Scratch and the extension.

The helper app uses the Extension object to get information about the available
blocks. Its only concern is with interfacing with Scratch (except in debug
mode)

Except in debug mode

run_forever sets up an HTTP server 


Helper class
============

The helper class passed to run_extension should look like this:

    class Helper:
        def __init__(self):
            ...

        def _problem(self):
            # Return a string describing the problem with the extension, if
            # any. The problem report should help users troubleshoot.
            #
            # Returns None if everything is working correctly.
            #
            # Example:
            #
            #    def _problem():
            #        if not self.is_connected():
            #            return "The spaceship is not connected."

        def _on_reset(self):
            # Reset the extension to its initial state.
            #
            # Triggered by clicking the red stop button in Scratch 2.0.
            #
            # Example:
            #
            #    def _on_reset():
            #        self.stop_all_motors()

There is also an optional _connect interface:

    class Helper:
    
        def _is_connected():
            # Optional.
            #
            # Called before running any of the helper class's methods.
            # If it returns False, abort

             try:
                 # ping the brick to check it's still connected
                 brick.get_battery_level()
             except USBError:
                 self.brick = None

             if not self.brick:
                 try:
                     self.block = nxt.find_one_brick()
                     ...
                 except:
                     pass # Couldn't connect :(

             return bool(self.brick)
             # ^ True if we're connected, False otherwise

        ...
"""
