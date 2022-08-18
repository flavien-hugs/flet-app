import flet

from main import main

port = 8550
target = main
view = flet.WEB_BROWSER

flet.app(port=port, target=target, view=view)
