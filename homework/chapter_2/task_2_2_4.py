def debug_control(*args, **kwargs):
  st = 0
  ir = 0
  fl = 0 
  for i in range(len(args)):
    if type(args[i]) == type(''):
      st += 1
    if type(args[i]) == type(1):
      ir += 1
    if type(args[i]) == type(1.1):
      fl += 1
  for _, value in kwargs.items():
    if type(value) == type(''):
      st += 1
    if type(value) == type(1):
      ir += 1
    if type(value) == type(1.1):
      fl += 1  
  return('str:', st,',', 'int:',ir,',','float:',fl)
