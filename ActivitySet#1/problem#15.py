# Object Oriented Programming
# https://www.py4e.com/lessons/Objects
import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lsted = re.findall('\S+@\S+', s)
print(lsted)