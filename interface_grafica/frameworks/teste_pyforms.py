
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText 
from pyforms.controls import ControlButton
from pyforms import start_app


class ExemploSimples(BaseWidget):
    
    def __init__(self):
        super().__init__('ExemploSimples')
        
        # Definição dos elementos do formulário
        self._nome = ControlText('Nome', default='Default value')
        self._sobrenome = ControlText('Sobrenome')
        self._nomeCompleto = ControlText('Nome completo')
        self._button = ControlButton('Pressione o Botão')
        
        # Definindo evento do botão
        self._button.value = self.gerar_nome_completo
        
        # Organizando o Layout
        self.formset = [
            '_nome',
            '_sobrenome',
            '_button',
            '_nomeCompleto'
        ]
    
    def gerar_nome_completo(self):
        # Concatena nome e sobrenome e exibe no campo Nome Completo 
        self._nomeCompleto.value = f"{self._nome.value} {self._sobrenome.value}"
        
# Execução da aplicação
if __name__ == "__main__":
    start_app(ExemploSimples)