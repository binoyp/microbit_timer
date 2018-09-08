from microbit import display, running_time, sleep
from microbit import button_a, button_b, Image
sel0 = True
sel1 = False
cursel = "W"
w_min = [1, 10, 15, 30, 45, 60] # Timer intervals
bool_timer = False
w_times = [(v * 60) for v in w_min]
i = 0
t0 = 0
tval = 0
if sel0:
    display.scroll("Press A to start", wait=False)
timer_started = False
show_img = True
imgs = [Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, 
    Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, 
    Image.CLOCK5, Image.CLOCK4, Image.CLOCK3, Image.CLOCK2,
    Image.CLOCK1]
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
    if timer_started is True:
        curtime = round((running_time() - t0)/(1000), 2)
        if i == 0:
            _i = 0
        else:
            _i = i - 1
            
        if curtime > w_times[_i]:
            t0 = 0
            timer_started = False
            timer_over = True
        if show_img is True:
            display.show(imgs[len(imgs) - 1 - im], wait=False)
            sleep(100)
            if im == len(imgs) - 1:
                im = 0
            else:
                im += 1
 
    if button_a.was_pressed():
        if timer_started is False:
            display.scroll(w_min[i])
            if i == len(w_min) - 1:
                i = 0
            else:
                i += 1 
        else:  # timer is running
            if i == 0:
                _i = 0
            else:
                _i = i-1
            display.scroll(w_times[_i])
    
    if button_b.was_pressed():
        if timer_started is False:
            t0 = running_time()
            timer_started = True
        else:
            
            display.scroll(str(curtime), wait=True)
            show_img= True