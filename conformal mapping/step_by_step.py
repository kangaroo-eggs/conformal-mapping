# This implement the upper half plane mapping to the unit disc step by step
from PIL import Image
# =========================================

def f1(z):
    return 1j*z
def inv_f1(z):
    return -1j*z

def f2(z):
    return z-1/2
def inv_f2(z):
    return z+1/2

def f3(z):
    return 1/z
def inv_f3(z):
    a = z.real;b = z.imag
    return (a-b*1j)/(a*a+b*b)

def f4(z):
    return z+1
def inv_f4(z):
    return z-1

# =========================================
srcf1 = Image.open("./upperplane.png")
srcf2 = Image.open("./f1.png")
srcf3 = Image.open("./f2.png")
srcf4 = Image.open("./f3.png")

sizef = srcf1.size

#=======================
# visualize the mapping f1
# the range of the picture is [-2,2]x[-2,2]
img = Image.new('RGB',(sizef[0],sizef[1]),(0,80,150))
for i in range(sizef[0]):
    for j in range(sizef[1]):
        x = 4*i/(sizef[0]-1)-2
        y = -4*j/(sizef[1]-1)+2
        if(x < 0):   # range of f1 is  x < 0 
            z = complex(x,y)
            zH = inv_f1(z)
            # find the pixel in the src
            src_i = int(((zH.real+2)/4*(sizef[0]-1))%(sizef[0]-1))    
            src_j = int((zH.imag-2)/-4*(sizef[1]-1)%(sizef[1]-1))
            img.putpixel((i,j), srcf1.getpixel((src_i,src_j)))
img.save("./f1.png")
#========================
# visualize the mapping f2
# the range of the picture is [-2,2]x[-2,2]
img = Image.new('RGB',(sizef[0],sizef[1]),(0,80,150))
for i in range(sizef[0]):
    for j in range(sizef[1]):
        x = 4*i/(sizef[0]-1)-2
        y = -4*j/(sizef[1]-1)+2
        if(x < -1/2):   # range of f2 is x < -1/2 
            z = complex(x,y)
            zH = inv_f2(z)
            # find the pixel in the src
            src_i = int(((zH.real+2)/4*(sizef[0]-1))%(sizef[0]-1))    
            src_j = int((zH.imag-2)/-4*(sizef[1]-1)%(sizef[1]-1))
            img.putpixel((i,j), srcf2.getpixel((src_i,src_j)))
img.save("./f2.png")
#========================
# visualize the mapping f3
# the range of the picture is [-2,2]x[-2,2]
img = Image.new('RGB',(sizef[0],sizef[1]),(0,80,150))
for i in range(sizef[0]):
    for j in range(sizef[1]):
        x = 4*i/(sizef[0]-1)-2
        y = -4*j/(sizef[1]-1)+2
        if((x+1)**2+y**2 < 1):   # range of f3 is |z+1| < 1
            z = complex(x,y)
            zH = inv_f3(z)
            # find the pixel in the src
            if(zH.real <= -2):
                src_i = 0
            elif(zH.real >= 2):
                src_i = sizef[0]-1
            else:
                src_i = int((zH.real+2)/4*(sizef[0]-1))    
            src_j = int((zH.imag-2)/-4*(sizef[1]-1)%(sizef[1]-1))
            img.putpixel((i,j), srcf3.getpixel((src_i,src_j)))
img.save("./f3.png")
# ========================
# visualize the mapping f4
# the range of the picture is [-2,2]x[-2,2]
img = Image.new('RGB',(sizef[0],sizef[1]),(0,80,150))
for i in range(sizef[0]):
    for j in range(sizef[1]):
        x = 4*i/(sizef[0]-1)-2
        y = -4*j/(sizef[1]-1)+2
        if(x**2+y**2 < 1):   # range of f4 is |z| < 1 
            z = complex(x,y)
            zH = inv_f4(z)
            # find the pixel in the src
            src_i = int((zH.real+2)/4*(sizef[0]-1))    
            src_j = int((zH.imag-2)/-4*(sizef[1]-1))
            img.putpixel((i,j), srcf4.getpixel((src_i,src_j)))
img.save("./f4.png")