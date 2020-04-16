from base64 import b64encode
import random, time, os
from collections import namedtuple

Lyric = namedtuple("Lyric", "time offset text")

srcdata = open('d2d.jpg', 'rb').read()
b64data = b64encode(srcdata).decode('ascii')
dots = ""
while len(dots) < 100:
    dots += ".........."

random.seed("CRAZY")


lyrics = [
    Lyric( 1.1, 5, " this world is going crazy "),
    Lyric( 7.2, 2, " footsteps pass your door "),
    Lyric(13.2, 7, " whatever you believed would be "),
    Lyric(19.0, 6, " well, now you can't be sure "),
    Lyric(25.3, 4, " everything flipped "),
    Lyric(26.6, 20, " upside down "),
    Lyric(31.0, 7, " postponed or left behind "),
    Lyric(37.1, 3, " what love is there to "),
    Lyric(38.5, 16, " find right now ? "),
    Lyric(42.5, 8, " in my sleep i dream of "),
    Lyric(44.6, 15, " another time "),
    Lyric(51.0, 0, "                                        "),
    Lyric( 0.0, 0, "               mandelbro1               "),
    Lyric( 0.0, 0, "                                        "),
    Lyric(1000, 5, " end ")
]

def rand_length(p):
    length = 1
    while random.random() < p:
        length += 1
    return length

current_str = ""
b64data_i = 0
def rand_line(size):
    global current_str, b64data_i
    while len(current_str) < size:
        n = rand_length(0.8)
        current_str += b64data[b64data_i:b64data_i + n]
        b64data_i += n
        n = rand_length(0.95)
        current_str += dots[0:n]
    out = current_str[0:size]
    current_str = current_str[size:]
    return out

os.system("clear")
time.sleep(1.0)
print("Last login: Wed Apr 15 5:21:16 on ttys01")
time.sleep(0.1)
input("MBP:~ mandelbro$ ")
time.sleep(1.0)

lines_per_second = 6.0
line_num = 0
next_lyric_i = 0
line_size = 40

start_t = time.time()

while True:
    current_time = time.time() - start_t
    next_lyric = lyrics[next_lyric_i]
    if current_time >= next_lyric.time:
        line_str = (
            dots[0:next_lyric.offset] +
            "\033[32m" +
            next_lyric.text +
            "\033[0m" +
            dots[0:line_size - next_lyric.offset - len(next_lyric.text)]
        )
        next_lyric_i += 1
        print(line_str)
    else:
        print(rand_line(line_size))
    line_num += 1
    time.sleep(1.0 / lines_per_second)
