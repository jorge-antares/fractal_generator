
import matplotlib.pyplot as plt
import math


class FractalGenerator:
    '''Class to create fractals from regular 2D geometric shapes.'''
    # Generators
    trianGen = [(0,0),(1/3,0),(0.5,math.sqrt(3)/6),(2/3,0),(1,0)]
    squarGer = [(0,0),(1/3,0),(1/3,1/3),(2/3,1/3),(2/3,0),(1,0)]
    
    # Polygons
    line = [(0,0),(1,0)]
    triangle = [(0,0),(0.5,math.sqrt(3)/2),(1,0),(0,0)]
    square = [(0,0),(1,0),(1,-1),(0,-1),(0,0)]
    
    def __init__(self):
        self.generator = [(0,0),(1/3,0),(0.5,1/3),(2/3,0),(1,0)]
        self.polygon  = [(0,0),(1,0)]
        margin = 1.1 * max([ num[1] for num in self.generator])
        xmin,xmax = min([ num[0] for num in self.polygon]), max([ num[0] for num in self.polygon])
        ymin,ymax = min([ num[1] for num in self.polygon]), max([ num[1] for num in self.polygon])
        self.xlims = (xmin - margin,xmax + margin)
        self.ylims = (ymin - margin,ymax + margin)
        self.convertToComplex()
        self.iter = 0
    
    def convertToComplex(self):
        '''Do not call directly: Converts tuples to complex.'''
        self.generator = [complex(num[0],num[1]) for num in self.generator]
        self.polygon   = [complex(num[0],num[1]) for num in self.polygon]
    
    def iterateManyTimes(self,n):
        for i in range(n):
            self.iterateFractal()
    
    def iterateFractal(self):
        '''Do not call directly: Iterates once.'''
        self.iter += 1
        newPoints = [self.polygon[0]]
        for point0,point1 in zip(self.polygon[:-1],self.polygon[1:]):
            for gen in self.generator[1:-1]:
                newPoints.append( gen * (point1 - point0) + point0 )
            newPoints.append( point1 )
        self.polygon = newPoints
    
    def getXandY(self):
        x = [num.real for num in self.polygon]
        y = [num.imag for num in self.polygon]
        return x,y
    
    def plotFractal(self,**kwargs):
        x,y = self.getXandY()
        fig,ax = plt.subplots()
        ax.plot(x,y,**kwargs)
        ax.set_xlim(self.xlims)
        ax.set_ylim(self.ylims)
        ax.axis('off')
        ax.axis('scaled')
        fig.patch.set_facecolor('w')
        fig.tight_layout()
        self.fig = fig
    
    def saveFig(self,**kwargs):
        self.fig.savefig(**kwargs)

if __name__ == '__main__':
    F = FractalGenerator()
    F.iterateManyTimes(5)
    F.plotFractal(color='b',linewidth=0.5)
    F.saveFig(fname='/Users/ja4garci/Documents/PythonFiles/projects2022/fractal.jpg',
              dpi=200)
