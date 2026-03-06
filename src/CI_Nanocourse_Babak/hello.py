import os


def main():
    print("Hello!")

def hello(name):
    a = name
    print(a)

def p(s,n=0,f=False):
  if s is None or s=="":
    return ""  # empty
  t = s.split(",")
  o = []
  i = 0
  for x in t:
    x = x.strip()
    if x == "":
      continue
    if f:
      x = x.lower()
    if len(x) < 2:
      continue
    if x in o:
      continue
    o.append(x)
    i += 1
    if n and i >= n:
      break
  return "|".join(o)