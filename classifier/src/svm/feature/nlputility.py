
def ngrams(input, n):
  input = input.split(' ')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
    
  return ["-".join(x) for x in output]


# print ngrams("x1 x2 x3 x4 x5", 3)
