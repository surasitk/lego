from PIL import Image, ImageDraw
S=1024
img=Image.new("RGBA",(S,S),(255,255,255,255))   # white background
d=ImageDraw.Draw(img)
BGHOLE=(255,255,255,255)                          # holes/gaps = white
YEL=(255,206,26,255); RED=(225,29,42,255); CAP=(29,111,224,255); LEG=(24,98,198,255); BLK=(20,20,24,255)
def rr(box,r,fill): d.rounded_rectangle(box,radius=r,fill=fill)
# CAP dome + brim
d.pieslice([402,250,622,470],180,360,fill=CAP)
d.ellipse([497,236,527,266],fill=CAP)
rr([388,360,636,408],18,CAP)
# HEAD
rr([410,372,614,566],52,YEL)
# NECK
rr([474,556,550,586],10,YEL)
# FACE
d.ellipse([470,452,500,482],fill=BLK)
d.ellipse([524,452,554,482],fill=BLK)
d.arc([468,470,556,536],20,160,fill=BLK,width=11)
# TORSO
d.polygon([(444,582),(580,582),(620,748),(404,748)],fill=RED)
rr([470,566,554,592],10,RED)
# ARMS
d.polygon([(452,600),(486,600),(404,742),(356,742)],fill=RED)
d.polygon([(572,600),(538,600),(620,742),(668,742)],fill=RED)
# HANDS
d.ellipse([336,724,392,780],fill=YEL); d.ellipse([352,740,376,764],fill=BGHOLE)
d.ellipse([632,724,688,780],fill=YEL); d.ellipse([648,740,672,764],fill=BGHOLE)
# HIPS + LEGS
rr([404,742,620,800],16,LEG)
rr([410,796,506,866],10,LEG)
rr([518,796,614,866],10,LEG)
d.rectangle([504,800,520,866],fill=BGHOLE)
def save(sz,name): img.resize((sz,sz),Image.LANCZOS).save(name)
save(180,"apple-touch-icon.png"); save(512,"icon-512.png"); save(192,"icon-192.png")
save(48,"favicon.png"); save(32,"favicon-32.png")
print("white-bg icons written")
