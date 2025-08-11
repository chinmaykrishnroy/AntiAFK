import threading,time,random,pyautogui
from pynput import mouse,keyboard
import pystray
from PIL import Image,ImageDraw
a,b,oo=10,0.2,1;c=time.time();d=0;e,f=True,False
def g(*x):global c;c=time.time()
j=mouse.Listener(on_move=g,on_click=g,on_scroll=g);j.start()
L=keyboard.Listener(on_press=g,on_release=g);L.start()
K=keyboard.Controller()
def k():
 i=Image.new("RGB",(64,64),0);ImageDraw.Draw(i).ellipse((16,16,48,48),fill=255);return i
def l():
 global d
 while e:
  if not f:
   m=time.time()
   if m-c>a and m-d>=1/b:
    K.press(keyboard.Key.ctrl);x,y=pyautogui.position();p=random.choice(["up","down","left","right"])
    if p=="up":pyautogui.moveTo(x,y-oo)
    elif p=="down":pyautogui.moveTo(x,y+oo)
    elif p=="left":pyautogui.moveTo(x-oo,y)
    else:pyautogui.moveTo(x+oo,y)
    time.sleep(0.1);pyautogui.moveTo(x,y);K.release(keyboard.Key.ctrl);d=time.time()
  time.sleep(0.05)
def q(_):return"Resume"if f else"Pause"
def s(_,__):global f;f=not f
def v(_,__):global e;e=False;j.stop();L.stop();_.stop()
def y(_):_.visible=True
M=pystray.MenuItem(q,s,default=False);N=pystray.Menu(M,pystray.MenuItem("Quit",v))
O=pystray.Icon("_",k(),"_",N)
threading.Thread(target=l,daemon=True).start();O.run(y)
