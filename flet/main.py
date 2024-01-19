from flet import *
import os, importlib.util

_modulelist = {}
for root, dirs, __ in os.walk(r'./'):
    for dir in dirs:
        if dir == 'pages':
            for filename in os.listdir(dir):
                _file = os.path.join(dir, filename)
                if os.path.isfile(_file):
                    filename = filename.strip('.py')
                    _modulelist['/'+filename] = importlib.util.spec_from_file_location(filename,_file)

def main(page: Page):
    page.title = "Stockero"
    
    def route_change(route):    
        page.views.clear()
        for key in _modulelist:
            if page.route == key:
                page.views.append(_modulelist[key].loader.load_module().index())

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.views.append(_modulelist["/index"].loader.load_module().index())
    page.update()


app(target=main)