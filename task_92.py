lesson = int(input("Enter № lesson: "))

lessons_start = 540
lessons_start += lesson * 45

for lessons_over in range (1, lesson):
    if lessons_over % 2 == 1:
        lessons_start += 5
    else:
        lessons_start += 15

hours = lessons_start // 60
minutes = lessons_start % 60

print(str(hours) + " " + str(minutes))
