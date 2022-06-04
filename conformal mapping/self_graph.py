# This implement the upper half plane mapping to the unit disc
from PIL import Image
from copy import deepcopy   
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
src = Image.open("./jojo.png")
size = max(src.size)

img = Image.new('RGB',(size,size),(0,80,150)) # 用成正方形
Frame_num = 20
Frames = []
#================================================
# the range of the picture is [-1,1]x[-1,1]
for frame in range(Frame_num):
    print(frame)
    shift = size*frame/(Frame_num-1)  # 平移距離 in coordinate (i, j)
    for i in range(size):
        for j in range(size):
            x = 2*i/(size-1)-1
            y = -2*j/(size-1)+1
            if(x**2 + y**2 < 1):   # for each pixel Z in U，so we need to find the pixel ZH in H+ (by inverse function g) s.t. f(ZH) = Z => ZH = g(Z) 
                z = complex(x,y)
                zH = g(z)
                # find the pixel in the src
                src_i = int((shift + (zH.real+1)/2*(src.size[0]-1))%src.size[0])
                src_j = int((zH.imag-1)/-2*(src.size[1]-1)%src.size[1])
                img.putpixel((i,j), src.getpixel((src_i,src_j)))
    Frames.append(deepcopy(img))
img.save("./Udisc_jojo.png")
Frames[0].save("./Udisc_jojo.gif",save_all=True,append_images=Frames[1:],opimize=False,duration=40,loop=0)