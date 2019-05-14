import sys
from imp_parser import *
from imp_lexer import *

def uso():
    sys.stderr.write('Importar archivo\n')
    sys.exit(1)

if nombre == 'main':
    if len(sys.argv) != 2:
        uso()
    nombrearchivo = sys.argv[1]
    texto = open(nombrearchivo).read()
    tokens = imp_lex(texto)
    for t in tokens:
        print t
     resultado_analisis = imp_parse(tokens)
     if not resultado_analisis:
         sys.stderr.write('Error de analisis!\n')
         sys.exit(1)
     ast = resultado_analisis.value
     enviar = {}
     ast.eval(enviar)

     sys.stdout.write('Valor final de las variables:\n')
     for nombre in enviar:
         sys.stdout.write('%s: %s\n' % (nombre, enviar[nombre]))
