import tkinter as tk  # Importa Tkinter para GUI

# Dicionário que mapeia caracteres para código Morse
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}


# Função para traduzir Morse para texto
def morse_para_texto(morse_code):
    texto_dict = {v: k for k, v in morse_dict.items()}
    palavras = morse_code.split(' / ')

    texto_traduzido = ''
    for palavra in palavras:
        letras_morse = palavra.split()
        palavra_traduzida = ''.join([texto_dict.get(letra, '') for letra in letras_morse])
        texto_traduzido += palavra_traduzida + ' '

    return texto_traduzido.strip()


# Criação da janela GUI
root = tk.Tk()
root.title("Tradutor de Morse")


# Função que será chamada quando o texto for alterado
def on_text_changed(*args):
    codigo_morse = morse_input.get()
    traducao = morse_para_texto(codigo_morse)
    texto_output.config(text=traducao)


# Entrada para o código Morse
morse_input = tk.StringVar()
morse_input.trace("w", on_text_changed)  # Chama a função quando o texto é modificado

# Elementos da GUI
entrada_label = tk.Label(root, text="Código Morse:")
entrada_label.pack()

entrada = tk.Entry(root, textvariable=morse_input, width=50)
entrada.pack()

resultado_label = tk.Label(root, text="Tradução:")
resultado_label.pack()

texto_output = tk.Label(root, text="", width=50, bg='white', fg='black', anchor='w')
texto_output.pack()

root.mainloop()  # Inicia o loop principal da GUI
