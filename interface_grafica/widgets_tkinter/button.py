import tkinter as tk
contador = 0
def contador_label(lblRotulo):
    def funcao_contar():
        global contador
        contador = contador + 1
        lblRotulo.config(text=str(contador))
        lblRotulo.after(1000, funcao_contar)
        
    funcao_contar() # Inicia a contagem

# Criando a janela principal
janela = tk.Tk()
janela.title("Contagem dos Segundos")

# Criando o rótulo para exibir o contador
lblRotulo = tk.Label(janela, fg="green")
lblRotulo.pack()

# iniciando a contagem 
contador_label(lblRotulo)

# Botão e interromper a contagem e fechar a janela
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
btnAcao.pack()

# Iniciando o loop da interface gráfica
janela.mainloop()