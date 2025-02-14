def greet(lang):
  if lang == 'es':
    return'Hola'
  elif lang == 'fr':
    return'Bonjour'
  elif lang == 'GS':
    return '⍑ᒷꖎꖎ𝙹'
  else:
    return'Hello'

def main():
    print(greet('en'),'Glenn')
    print(greet('fr'),'Sabine')
    print(greet('es'),'Carlos')
    print(greet('GS'),'Anakin')
    
main()
