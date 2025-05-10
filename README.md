# 🚀 Conversor de Unidades em Python

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

## 📚 Sobre o Projeto

O **Conversor de Unidades** é um projeto simples em Python que permite converter valores entre diferentes unidades de medida diretamente pelo terminal. Ele suporta conversão entre:

- Quilômetros ↔️ Milhas
- Celsius ↔️ Fahrenheit
- Quilogramas ↔️ Libras

Ideal para quem está começando a programar e quer praticar entrada de dados, condicionais e funções!

---

## 🛠️ Como Usar

1. **Clone o repositório:**
git clone https://github.com/rafaelmoreirax/conversor-unidades.git
cd conversor-unidades

2. **Execute o script:**
python conversor_unidades.py


3. **Siga as instruções no terminal para escolher o tipo de conversão e inserir os valores.**

---

## 💻 Exemplo de Uso
Escolha o tipo de conversão:
1 - Quilômetros para Milhas
2 - Milhas para Quilômetros
3 - Celsius para Fahrenheit
4 - Fahrenheit para Celsius
5 - Quilogramas para Libras
6 - Libras para Quilogramas
Opção: 1
Digite o valor em quilômetros: 10
10.0 quilômetros equivalem a 6.21 milhas.

---

## 🧩 Código Fonte

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


---

## 📦 Requisitos

- Python 3.8 ou superior

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## 📝 Licença

Este projeto está sob a licença MIT.

---

## 📫 Contato

Dúvidas ou sugestões? Abra uma issue!

---

