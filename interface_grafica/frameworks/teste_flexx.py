from flexx import flx
class Exemplo(flx.Widget):
    
    def init(self):
        flx.Button(text='Olá')
        flx.Button(text='Mundo!')

if __name__ == '__main__':
    a = flx.App(Exemplo, title='Flexx demonstration')
    m = a.launch()
    flx.run()