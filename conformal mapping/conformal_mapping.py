# This implement the upper half plane mapping to the unit disc
from PIL import Image
# =========================================
# f:H+ -> U
def f(z):
    return (1j*z+0.5)/(1j*z-0.5)

# g is inverse function of f
# g:U -> H+
def g(z):
    A = z+1; B = z-1
    a = A.real; b = A.imag; c = B.real; d = B.imag
    return -1j/2*((a*c+b*d)-(a*d-b*c)*1j)/(c*c+d*d) # -i/2*(z+1)/(z-1) will cause 數值 error
# =========================================
srcf = Image.open("./upperplane.png")
sizef = srcf.size

img = Image.new('RGB',(sizef[0],sizef[1]),(0,80,150))
# =======================
# visualize the conformal mapping f
# the range of the picture is [-2,2]x[-2,2]
for i in range(sizef[0]):
    for j in range(sizef[1]):
        x = 4*i/(sizef[0]-1)-2
        y = -4*j/(sizef[1]-1)+2
        if(x**2 + y**2 < 1):   # for each pixel Z in U，so we need to find the pixel ZH in H+ (by inverse function g) s.t. f(ZH) = Z => ZH = g(Z) 
            z = complex(x,y)
            zH = g(z)
            # find the pixel in the src
            src_i = int(((zH.real+2)/4*(sizef[0]-1))%(sizef[0]-1))
            if(zH.imag > 2):
                src_j = 0
            else:      
                src_j = int((zH.imag-2)/-4*(sizef[1]-1))
            img.putpixel((i,j), srcf.getpixel((src_i,src_j)))
img.save("./f.png")