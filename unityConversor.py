def km_para_milhas(km):
  return km * 0.621371

def milhas_para_km(milhas):
    return milhas / 0.621371

def celsius_para_fahrenheit(c):
  return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
  return (f - 32) * 5/9

def kg_para_libras(kg):
  return kg * 2.20462

def libras_para_kg(lb):
  return lb / 2.20462

print("Escolha o tipo de conversão:")
print("1 - Quilômetros para Milhas")
print("2 - Milhas para Quilômetros")
print("3 - Celsius para Fahrenheit")
print("4 - Fahrenheit para Celsius")
print("5 - Quilogramas para Libras")
print("6 - Libras para Quilogramas")
opcao = input("Opção: ")

valor = float(input("Digite o valor: "))

if opcao == "1":
  print(f"{valor} quilômetros equivalem a {km_para_milhas(valor):.2f} milhas.")
elif opcao == "2":
  print(f"{valor} milhas equivalem a {milhas_para_km(valor):.2f} quilômetros.")
elif opcao == "3":
  print(f"{valor}°C equivalem a {celsius_para_fahrenheit(valor):.2f}°F.")
elif opcao == "4":
  print(f"{valor}°F equivalem a {fahrenheit_para_celsius(valor):.2f}°C.")
elif opcao == "5":
  print(f"{valor} kg equivalem a {kg_para_libras(valor):.2f} libras.")
elif opcao == "6":
  print(f"{valor} libras equivalem a {libras_para_kg(valor):.2f} kg.")
else:
  print("Opção inválida.")