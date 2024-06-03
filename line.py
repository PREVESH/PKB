from easygraphics import *
import time
def main():
    init_graph(640, 480)
    set_color("#ff0000")
    for i in range(1,10000,10):
        set_color(to_alpha("red",i))
        line(0, 0, 640, 480)
        time.sleep(2)
    pause()
    close_graph()

easy_run(main)