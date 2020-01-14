import pandas as pd
import cv2 as cv
import sys
cv.namedWindow('image')
path=str(sys.argv[1])
img=cv.imread(path,1)
col_names=['color','col_name','hex_code','r','g','b']
df=pd.read_csv('colors.csv',header=None,names=col_names)
b=g=r=0
clk=False
def color(b,g,r):
      minimum=9999
      for i in range(0,len(df)):
            d = abs(b- int(df.loc[i,'b'])) + abs(g- int(df.loc[i,'g']))+ abs(r- int(df.loc[i,'r']))
            if(d<=minimum):
            	minimum = d
            	cname = df.loc[i,'col_name']
      return cname
def click_event(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDBLCLK:
        global b,g,r,clk
        clk=True
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
cv.setMouseCallback('image', click_event)
while 1:
    cv.imshow('image',img)
    if clk:
        cv.rectangle(img, (10,10), (300,60), (255,255,255),-1)
        text=color(b,g,r)
        cv.putText(img, text, (40,40), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))
        clk=False
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cv.destroyAllWindows()
    