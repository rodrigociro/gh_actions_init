import camelcase

#pip list
#command: pip install camelcase

camel = camelcase.CamelCase()

texto = "mi nombre es rodri"

print(camel.hump(texto))

#desinstalar modulo
#command: pip uninstall camelcase
#comprobar: pip list