print("hello world") 
def main():
 c = int(input("Me diga um número em °C:"))
 try:
  print(f"sua temperatura em °C é {c}", end=', ')
  k = 273
  f = 1.8 * c
  print(f"sua temperatura em °K é {c+k}", end=', ')
  print(f"sua temperatura em F é {c+f}.")
 except (ValueError): print("Por favor, insira apenas números!")

main()
