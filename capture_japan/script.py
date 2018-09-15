
import math
N = 27
K = 42

def init():
    probUnique = 1.0
    for k in xrange(1, K):
        probUnique = probUnique * (N - (k - 1)) / N
        print k, 1 - probUnique, 1 - math.exp(-0.5 * k * (k - 1) / N)
        
init()