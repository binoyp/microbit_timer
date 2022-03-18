from microbit import display, running_time, sleep
from microbit import button_a, button_b, Image

w_min = [1, 10, 15, 30, 45, 60] # Timer intervals

w_times = [(v * 60) for v in w_min]
i = -1 # Time Selection index
t0 = 0
tval = 0

display.scroll("Press A to start", wait=False)
timer_started = False

imgs = [Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, 
    Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, 
    Image.CLOCK5, Image.CLOCK4, Image.CLOCK3, Image.CLOCK2,
    Image.CLOCK1]

N_IMGS = len(imgs) - 1
im = 0 

timer_over = False

def anim():
    while 1:
        with open('anim0.txt', 'r') as _f:
            for _ in range(60):
                content = _f.readline()
                display.show(Image(content.strip()))
                sleep(100)
                if button_a.was_pressed() or button_b.was_pressed():
                    
                    return 

while 1:
    if timer_over is True:
        display.clear()
        timer_started = False
        anim()
        timer_over = False
    if timer_started:
        curtime = round((running_time() - t0)/(1000), 2)
                    
        if curtime > w_times[i]:
            timer_started = False
            timer_over = True
            show_img = False
        if show_img:
            display.show(imgs[N_IMGS - im], wait=False)
            sleep(100)
            if im == len(imgs) - 1:
                im = 0
            else:
                im += 1
 
    if button_a.was_pressed():

        if not timer_started:
            if i == len(w_min) - 1: #increment index
                i = 0
            else:
                i += 1 
            
            display.scroll(w_min[i], delay=80)
        else:  # timer is running
            display.scroll(w_min[i])
    
    if button_b.was_pressed():
        if i < 0:
             i = 0
        if timer_started is False:
            display.scroll("St.. : %i m"%w_min[i], delay=60)
            t0 = running_time()
            timer_started = True
            show_img = True
        else:
            
            cur_min = round(curtime,2)//60
            cur_sec = round(curtime,2)-(cur_min*60)
            display.scroll("%im %is"%(cur_min, cur_sec), delay=80, wait=True)
            show_img= True
