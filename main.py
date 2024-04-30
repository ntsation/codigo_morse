   # Dicionário que mapeia caracteres para código Morse
   morse_dict = {
      'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
      'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
      'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
      'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
      '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
      '8': '---..', '9': '----.', '0': '-----', ' ': '/'
   }

   def morse_texto(morse_code):
      texto_dict = {v: k for k, v in morse_dict.items()}
      palavras = morse_code.split(' / ')
      texto_traduzido = ''

      for palavra in palavras:
         letras_morse = palavra.split()
         palavra_traduzida = ''.join([texto_dict.get(letra, '') for letra in letras_morse])
         texto_traduzido += palavra_traduzida + ' '

      return texto_traduzido.strip()

   codigo_morse = "... --- ..."
   texto_traduzido = morse_texto(codigo_morse)
   print(f"Tradução do código Morse '{codigo_morse}': '{texto_traduzido}'")