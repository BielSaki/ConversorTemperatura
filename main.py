print("hello world") 
def main():
 x = input("Me diga um número em °C:")
 try:
  xx = int( x )
  print("sua temperatura em °C é", x)
  y = 273
  yy = int( y )
  z = 1.8 * xx
  zz = float( z )
  print("sua temperatura em °K é", xx + yy)
  print("sua temperatura em F é", zz + 32)
 except (ValueError): print("Por favor, insira apenas números!")

main()
