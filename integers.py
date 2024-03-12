import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def sine_curve():
    Fs=8000
    f=5
    sample=8000
    x=np.arange(sample)
    y=np.sin(2*np.pi*f*x/Fs)
    plt.plot(x,y)
    plt.xlabel('V(voltage)')
    plt.ylabel('S(sample)')
    plt.show()

def cosine_curve():
    Fs=8000
    f=5
    sample=8000
    x=np.arange(sample)
    y=np.cos(2*np.pi*f*x/Fs)
    plt.plot(x,y)
    plt.xlabel('V(voltage)')
    plt.ylabel('S(sample)')
    plt.show()
def polynomial_curve():
    x=np.arange(-5,5,0.25)
    y=np.arange(-5,5,0.25)
    x,y=np.meshgrid(x,y)
    F=3+2*x+4*x*y+5*x*x
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    ax.plot_surface(x,y,F)
    plt.show()

def exponential_curve(func,x_range):
    x=np.arange(*x_range)
    y=func(x)
    plt.plot(x,y)
    plt.show()

def menu():
    print('1. Sine')
    print('2. Cosine')
    print('3. Polynomial_curve')
    print('4. Exponential_curve')
ch='y'
while(ch=='y'):
    menu()
    choice=int(input("Enter choice..."))
    if(choice==1):
        sine_curve()
    elif(choice==2):
        cosine_curve()
    elif(choice==3):
        polynomial_curve()
    elif(choice==4):
        polynomial_curve()
    else:
        print('Wrong Choice')
    ch=input('Do you wish to continue(y/n)..')