"""
.. moduleauthor:: Siddesh Pachkawade <your.address@yourdomain.at>
"""

from math import pi
radius = float(input("Enter a radius: "))   
area = 4 * radius**2 * pi
volume = (4/3) * radius**3 * pi
print("The sphere has a volume of", round(volume, 2));
print("The surface area of this sphere is", round(area, 2));


## from math import PI
## radius = input("Enter a radius: ")
## area = 2 * r**2 ** pi
## volume = (4 div 3) * r^3 * PI
## print("The sphere has a volume of", round(volume, 2));
## print("The surface area of this sphere is", round(Area, 2));