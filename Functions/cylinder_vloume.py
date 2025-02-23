def find_cylinder_volume(radius, height = 7):
    print("radius", radius)
    print("height", height)
    volume = 3.14*(radius**2)*height
    return volume

r = 10
h = 55
v = find_cylinder_volume(radius=r,height=h)
print(v)