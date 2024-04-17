r = int(input("enter the red value: "))
g = int(input("enter the green value: "))
b = int(input("enter the blue value: "))
if r > 255 or r < 0:
    print("the red value is not in the acceptable range")
if g > 255 or g < 0:
    print("the green value is not in the acceptable range")
if b > 255 or b < 0:
    print("the blue value is not in the acceptable range")
if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
    print("no problems found")