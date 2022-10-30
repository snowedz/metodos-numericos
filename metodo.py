def main():
  y0 = 2
  ylinha = 2
  h = 0.1
  x1 = h
  x = []
  y = []

  for n in range(1,1001):
    y1 = y0 + h *(x1-y0+ylinha)
    # print(f'Resultado {n}: {y1}')
    x1 = h + x1
    y0 = y1
    x.append(x1)
    y.append(y1)

main()