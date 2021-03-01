# Shannon-for-Dummies

Educational application

Exploration from Claude's Shannon initial theory to its practical application to satellite communications.

The application is using PysimpleGUI / PySimpleGUIWeb and runs either in local windows or in web pages.

The Web version via localhost is fully functional although not as convenient as the windowed version (only 1 plot open).
The look of the web version differs significantly from the local version (PySimpleGUIWeb is still beta). 

The Web version in remote does work for a single user (all users connected can send commands but see the same page). 
This mode is experimental and doesnt behave as a web server : users are not managed, the app closes when the user closes the window ...

The value of the application is essentially in the background information accessed by clicking labels of all inputs / outputs.

A Knowedge DB is coupled to the application for collaborative contributions on the subject opening technical discussions. 
At this stage the DB is local.

Athough the scripts are small, pyinstaller generates 70M of files for sandalone distribution.
