# import Lesson_5_1
# from Lesson_5_1 import *
import Lesson_5_1 as bien
a = [1, 2, 4, 5, 6]
b = [-1, 2, 3, 4]
c = [0, 1, 4]

max_a = bien.tim_max(a)
print(max_a)
max_b = bien.tim_max(b)
print(max_b)
max_c = bien.tim_max(c)
print(max_c)

chu_vi_tam_giac = bien.chu_vi(max_a, max_b, max_c)
print(chu_vi_tam_giac)

