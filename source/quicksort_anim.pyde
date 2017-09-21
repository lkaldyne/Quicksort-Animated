from random import randint

def switcheroni(numlist,pivot,smallernum):
  templist = [0 for i in range(len(numlist))]
  extraslist = [0 for i in range(len(numlist)-(pivot+2))]
  j = pivot + 1
  counter = 0
  while j < len(numlist):
      if j != smallernum:
          extraslist[counter] = numlist[j]
          counter += 1
      j += 1

  counter = 0

  for n in range(len(templist)):
      if n < pivot:
          templist[n] = numlist[n]
      elif n == pivot:
          templist[n] = numlist[smallernum]
      elif n == (pivot+1):
          templist[n] = numlist[pivot]
      else:
          templist[n] = extraslist[counter]
          counter += 1
  return templist
def setup():
  global numlist,listcopy,counter,pivot,solved,nums,multiplier,colour
  size(1100,600)
  rectMode(CORNERS)
  nums = 200
  multiplier = 1/((float(nums) - (nums * 0.999))) 
  numlist = [randint(0,1000) for i in range(nums)]
  listcopy = numlist[:]
  solved = False
  counter = 0
  pivot = 0
  solved = False
  colour = 255
  if nums > 300:
    noStroke()

def draw():
  global numlist,listcopy,counter,pivot,solved,nums,multiplier,colour
  background(100)
  #delay(100)
  incr = 1
  if pivot >= len(listcopy):
      solved = True
  if solved == False:
      while True:
          pivotspot = pivot
          if (pivotspot + incr) >= len(numlist):
              break
          if numlist[pivotspot] > numlist[pivotspot+incr]:
              numlist = switcheroni(numlist,pivotspot,pivotspot+incr)
              counter += 1
              incr -= 1
          incr += 1
      pivot += 1
  else:
      colour = 1000
  for i in range(len(numlist)):
      fill(colour)
      rect(50 + (multiplier*i), 550, 50 +(multiplier) + (multiplier*i), 550 - (numlist[i]/2))
      fill(0)
      textSize(15)
      text(numlist[i], 50 + (multiplier*i), 550)
      
              
    
    
  textSize(20)
  text("Processes: %s" %(counter),50,580)