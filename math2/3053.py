import sys
import math

r = int(sys.stdin.readline())
p = float("%0.100f"%math.pi)

print("%0.6f"%(p*(r**2)))
print("%0.6f"%(2*(r**2)))