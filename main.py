print("hello world") 
def main():
 x = input("Me diga um número em °C:")
 try:
  xx = int( x )
  print("sua temperatura em °C é {}" .format(x), end=', ')
  y = 273
  yy = int( y )
  z = 1.8 * xx
  zz = float( z )
  print("sua temperatura em °K é {}" .format(xx+yy), end=', ')
  print("sua temperatura em F é {}." .format(zz+32))
 except (ValueError): print("Por favor, insira apenas números!")

main()
