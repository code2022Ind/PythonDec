import os
import sys

test = os.path.abspath(os.pth.join(os.path.dirname(__file__)))
Day3_path = os.path.join(test,"Day3")
print(Day3_path)
sys.path.append(Day3_path)
from Day3 import Function

m1()