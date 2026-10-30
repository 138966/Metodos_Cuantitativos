x=[2, 8, 5]
y=[7, 9, 6]

def media(X):
  n = len(X)
  sumatoria = 0
  media = 0;
  for i in x:
     sumatoria = sumatoria + i 
  print(f"La sumatoria es:{sumatoria}")
  print(f"Elementos:{n}")

  media = sumatoria / n 
  print(f"La media es:{media}")

media(x)

