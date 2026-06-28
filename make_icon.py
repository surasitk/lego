from PIL import Image, ImageDraw
S=1024
# supersample canvas
img=Image.new("RGBA",(S,S),(0,0,0,0))
d=ImageDraw.Draw(img)
# background: vertical navy gradient, full-bleed (iOS rounds corners itself)
top=(14,20,33); bot=(28,38,58)
for y in range(S):
    t=y/S
    c=tuple(int(top[i]+(bot[i]-top[i])*t) for i in range(3))
    d.line([(0,y),(S,y)],fill=c+(255,))
# subtle stud dots
for gx in range(0,S,150):
    for gy in range(0,S,150):
        d.ellipse([gx-6,gy-6,gx+6,gy+6],fill=(255,255,255,10))

YEL=(255,206,26,255); RED=(225,29,42,255); CAP=(29,111,224,255); LEG=(24,98,198,255); BLK=(20,20,24,255)
cx=512
def rr(box,r,fill): d.rounded_rectangle(box,radius=r,fill=fill)

# CAP dome + brim
d.pieslice([402,250,622,470],180,360,fill=CAP)       # dome
d.ellipse([497,236,527,266],fill=CAP)                 # top knob
rr([388,360,636,408],18,CAP)                          # brim
# HEAD (yellow cylinder)
rr([410,372,614,566],52,YEL)
# NECK
rr([474,556,550,586],10,YEL)
# FACE
d.ellipse([470,452,500,482],fill=BLK)                 # left eye
d.ellipse([524,452,554,482],fill=BLK)                 # right eye
d.arc([468,470,556,536],20,160,fill=BLK,width=11)     # smile
# TORSO (red trapezoid)
d.polygon([(444,582),(580,582),(620,748),(404,748)],fill=RED)
rr([470,566,554,592],10,RED)                          # collar peg
# ARMS
d.polygon([(452,600),(486,600),(404,742),(356,742)],fill=RED)   # left arm
d.polygon([(572,600),(538,600),(620,742),(668,742)],fill=RED)   # right arm
# HANDS (yellow C)
d.ellipse([336,724,392,780],fill=YEL); d.ellipse([352,740,376,764],fill=(28,38,58,255))
d.ellipse([632,724,688,780],fill=YEL); d.ellipse([648,740,672,764],fill=(28,38,58,255))
# HIPS + LEGS (blue)
rr([404,742,620,800],16,LEG)
rr([410,796,506,866],10,LEG)
rr([518,796,614,866],10,LEG)
d.rectangle([504,800,520,866],fill=(28,38,58,255))    # leg gap

def save(sz,name):
    img.resize((sz,sz),Image.LANCZOS).save(name)
save(180,"apple-touch-icon.png")
save(512,"icon-512.png")
save(192,"icon-192.png")
save(48,"favicon.png")
save(32,"favicon-32.png")
print("icons written")
