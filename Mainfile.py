import matrix_multiply as mm
import Bresenham1 as bresen
import mcda as midcirc
import meda as midellip
import translate as tr
import rotation as rot
import scaling as sc
import reflection as ref
import shearing as sh
from matplotlib import pyplot as plt

x_list, y_list = [], []
shape = int(input("\nEnter the number of shapes you want to create: "))
while(shape != 0):
    ch = int(input("\nEnter 1 for drawing a line\nEnter 2 for drawing a circle\nEnter 3 for drawing an ellipse\n\nINPUT : "))
    if(ch == 1):
        line = int(input("\nEnter the number of lines you want to draw: "))
        while(line != 0):
            x1 = float(input("\nEnter x coordinate of starting point: "))
            y1 = float(input("Enter y coordinate of starting point: "))
            x2 = float(input("Enter x coordinate of ending point: "))
            y2 = float(input("Enter y coordinate of ending point: "))
            returned_list1 = bresen.drawBresenham(x1, y1, x2, y2)
            for i in returned_list1[0]:
                x_list.extend(i)
            for i in returned_list1[1]:
                y_list.extend(i)
            line = line - 1
        shape = shape - 1
    elif(ch == 2):
        circ = int(input("\nEnter the number of circles you want to draw: "))
        temp = circ
        while (circ != 0):
            cx = float(input("\nEnter x coordinate of centre point: "))
            cy = float(input("Enter y coordinate of centre point: "))
            r = float(input("Enter radius: "))
            returned_list2 = midcirc.midpoint_circle(cx, cy, r)
            for i in returned_list2[0]:
                x_list.extend(i)
            for i in returned_list2[1]:
                y_list.extend(i)
            circ = circ - 1
        shape = shape - temp
    elif(ch == 3):
        elip = int(input("\nEnter the number of ellipse you want to draw: "))
        temp = elip
        while (elip != 0):
            xe = float(input("\nEnter x center coordinate : "))
            ye = float(input("Enter y center coordinate : "))
            rxe_1 = float(input("Enter major axis of the ellipse : "))
            rye_1 = float(input("Enter minor axis of the ellipse : "))
            returned_list3 = midellip.midpoint_ellipse(xe, ye, rxe_1, rye_1)
            for i in returned_list3[0]:
                x_list.extend(i)
            for i in returned_list3[1]:
                y_list.extend(i)
            elip = elip - 1
        shape = shape - temp
    else:
        print("\nWrong choice. Please enter correct details.")

plt.rc('grid', linestyle="-", color='black')
plt.scatter(x_list, y_list, c='r')
plt.xlabel(" X axis --->")
plt.ylabel(" Y axis --->")
plt.title('Plotting Shapes For Transformations')
plt.grid()
plt.show()
            


new_matrix, old_matrix = [], []
temp_list = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
nt = int(input("\nEnter the number of transformations: "))
while(nt != 0):
    choice = int(input("\nEnter 1 for translation\nEnter 2 for rotation\nEnter 3 for scaling\nEnter 4 for reflection\nEnter 5 for shearing\n\nINPUT : "))
    if(choice == 1):
        c1 = int(input("\nEnter 1 for translating along x-axis\nEnter 2 for translating along y-axis\nEnter 3 for translating along both axes\n\nINPUT : "))
        if (c1 == 1):
            tx = float(input("\nEnter the translating factor along x-axis: "))
            temp_list = mm.matrix_mul(tr.translate_x(tx), temp_list)
        elif (c1 == 2):
            ty = float(input("\nEnter the translating factor along y-axis: "))
            temp_list = mm.matrix_mul(tr.translate_y(ty), temp_list)
        elif (c1 == 3):
            tx = float(input("\nEnter the translating factor along x-axis: "))
            ty = float(input("Enter the translating factor along y-axis: "))
            temp_list = mm.matrix_mul(tr.translate_xy(tx, ty), temp_list)
        else:
            print("\nWrong choice. Please enter correct details.")
        nt = nt - 1

    elif(choice == 2):
        c2 = int(input("\nEnter 1 for clockwise rotation\nEnter 2 for anticlockwise rotation\n\nINPUT : "))
        if (c2 == 1):
            theta = float(input("\nEnter the angle of clockwise rotation: "))
            x_fixed = float(input("Enter the abscissa of the pivot point(Enter 0 in case of origin): "))
            y_fixed = float(input("Enter the ordinate of the pivot point(Enter 0 in case of origin): "))
            temp_list = mm.matrix_mul(rot.rotation(c2, x_fixed, y_fixed, theta), temp_list)
        elif (c2 == 2):
            theta = float(input("\nEnter the angle of anticlockwise rotation: "))
            x_fixed = float(input("Enter the abscissa of the pivot point(Enter 0 in case of origin): "))
            y_fixed = float(input("Enter the ordinate of the pivot point(Enter 0 in case of origin): "))
            temp_list = mm.matrix_mul(rot.rotation(c2, x_fixed, y_fixed, theta), temp_list)
        else:
            print("\nWrong choice. Please enter correct details.")
        nt = nt - 1

    elif(choice == 3):
        c3 = int(input("\nEnter 1 for scaling along x-axis\nEnter 2 for scaling along y-axis\nEnter 3 for scaling along both axes\n\nINPUT : "))
        if (c3 == 1):
            Sx = float(input("\nEnter the scaling factor along x-axis: "))
            temp_list = mm.matrix_mul(sc.scale_x(Sx), temp_list)
        elif (c3 == 2):
            Sy = float(input("\nEnter the scaling factor along y-axis: "))
            temp_list = mm.matrix_mul(sc.scale_y(Sy), temp_list)
        elif (c3 == 3):
            Sx = float(input("\nEnter the scaling factor along x-axis: "))
            Sy = float(input("Enter the scaling factor along y-axis: "))
            temp_list = mm.matrix_mul(sc.scale_xy(Sx, Sy), temp_list)
        else:
            print("\nWrong choice. Please enter correct details.")
        nt = nt - 1

    elif (choice == 4):
        c4 = int(input("Enter 1 for reflection about x-axis\nEnter 2 for reflection about y-axis\nEnter 3 for reflection about a line parallel to x-axis\nEnter 4 for reflection about a line parallel to y-axis\nEnter 5 for reflection about any other line\n\nINPUT : "))
        if (c4 == 1):
            temp_list = mm.matrix_mul(ref.x_axis(), temp_list)
        elif (c4 == 2):
            temp_list = mm.matrix_mul(ref.y_axis(), temp_list)
        elif (c4 == 3):
            constant = float(input("\nEnter the value of constant (as in y = constant): "))
            temp_list = mm.matrix_mul(ref.x_parallel(constant), temp_list)
        elif (c4 == 4):
            constant = float(input("\nEnter the value of constant (as in x = constant): "))
            temp_list = mm.matrix_mul(ref.y_parallel(constant), temp_list)
        elif (c4 == 5):
            slope = float(input("\nEnter the value of slope(m) [as in y = mx + c]: "))
            constant = float(input("Enter the value of constant(c) [as in y = mx + c]: "))
            temp_list = mm.matrix_mul(ref.others(constant, slope), temp_list)
        else:
            print("\nWrong choice. Please enter correct details.")
        nt = nt - 1

    elif(choice == 5):
        c5 = int(input("Enter 1 for shearing along x-axis\nEnter 2 for shearing along y-axis\nEnter 3 for shearing along both axes\n\nINPUT : "))
        if (c5 == 1):
            shx = float(input("\nEnter the shearing factor along x-axis: "))
            temp_list = mm.matrix_mul(sh.shear_x(shx), temp_list)
        elif (c5 == 2):
            shy = float(input("\nEnter the shearing factor along y-axis: "))
            temp_list = mm.matrix_mul(sh.shear_y(shy), temp_list)
        elif (c5 == 3):
            shx = float(input("\nEnter the shearing factor along x-axis: "))
            shy = float(input("Enter the shearing factor along y-axis: "))
            temp_list = mm.matrix_mul(sh.shear_xy(shx, shy), temp_list)
        else:
            print("\nWrong choice. Please enter correct details.")
        nt = nt - 1
    else:
            print("\nWrong choice. Please enter correct details.")

x_list_new,y_list_new = [], []
#print("The corresponding coordinates obtained after transformations are: ")
for i in range(len(x_list)):
    old_matrix = [[x_list[i]], [y_list[i]], [1]]
    new_matrix = mm.matrix_mul(temp_list, old_matrix)
    x_list_new.append(new_matrix[0][0])
    y_list_new.append(new_matrix[1][0])
    #print("x = %s, y = %s" % (new_matrix[0][0], new_matrix[1][0]))

plt.rc('grid', linestyle="-", color='black')
plt.scatter(x_list,y_list, c='r')
plt.scatter(x_list_new,y_list_new, c='green')
plt.xlabel(" X axis --->")
plt.ylabel(" Y axis --->")
plt.grid()
plt.show()