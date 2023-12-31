
#TPRG 2131 Fall 2023 Assignment 1 (A_V_calc)

# Jhyg Castillejos (100882960)
# TPRG1131 Section 2131
# October 15, 2023
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).
# The program calculates the areas of a rectangle, a triangle 
# and a circle as well as the volume of both a cube and a sphere.
# It also gives the user  the option of quitting or choosing
# between a calculated or default view.
# area of triangle formula - https://byjus.com/maths/area-of-a-triangle/
# area of circle formula - https://www.omnicalculator.com/math/area-of-a-circle
# volume of a sphere formula - https://byjus.com/maths/volume-of-sphere/
# volume of a cube formula - https://byjus.com/maths/volume-of-a-cube/
# area of rectange formula- https://byjus.com/maths/area-of-rectangle/

#READY FOR MARKING

import math

def main():
    #------------------------------------------------------------- view options
    print("A/V Calculator")
    print("(Level 0)")
    print("Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.")
    print("Enter V/v to change the calculated view or D/d for default view.")

    view= "default view"
    state = True

#keeps asking the user for a valid input if inputted value is invalid.
    while state:  
        menu_view= input("Enter your choice: ")
        #turns input into lowercase
        menu_view = menu_view.lower()
        if menu_view == "q":
            print("Exiting the A/V Calculator.")
            break
        elif menu_view == "v":
            view = "calculated view"
            state= False
        elif menu_view == "d":
            view = "default view"
            state= False
        else:
            print ("invalid input.")
            state= True
            
    print("\n")
    print("View selected:", view)
            
    #------------------------------------------------------------- area/volume calculations
    
    #turns number into interger
    def inter(n):
        return int(n)
    
    #calculates area of rectangle
    def option1(l,w):
        return inter(l*w)

    #calculates area of triangle
    def option2(b,h):
        return inter((1/2)*b*h)
    
    #calculates area of circle
    def option3(r):
        return inter(math.pi * math.pow(r, 2))

    #calculates volume of cube
    def option4(s):
        return inter(math.pow(s, 3))

    #calculates volume of sphere
    def option5(ra):
        return inter(4/3*math.pi*(math.pow(ra, 3)))



    while True:
        #------------------------------------------------------------- level options
        print("\n")
        print("A/V calculator Menu")
        print("\n", "1. Area of Rectangle. \n", "2. Area of a Triangle. \n", "3. Area of a circle. \n",
              "4. Volume of a cube. \n", "5. Volume of a sphere. \n") 
        level = 1
        state1= True
        while state1:
            level= inter(input("select level(1~5): "))
            if level in (1, 2, 3, 4, 5):
                level = level
                state1= False
            else:
                print("invalid inpput:" )
        #-------------------------------------------------------------
    
    #------------------------------------------------------------- user input for calulations
        
    # asks user the required variables to calulate the chosen option.
    # calulates area/volume by using the define functions

        if level == 1:
            l=inter(input("enter lenght:" ))
            w=inter(input("enter width:" ))
            #prints either the default or calulated view depending on what user wants.
            if view == "default view":
                print ( l, "*", w, "=", option1(l,w))
            else:
                print ( l, "*", w, "=", option1(l,w), "(l * w = a)")
                
        elif level == 2:
            b=inter(input("enter base:" ))
            h=inter(input("enter height:" ))
            if view == "default view":
                print ( b, "*", h, "*","(1/2)", "=", option2(b,h))
            else:
                print ( b, "*", h, "*","(1/2)", "=", option2(b,h), "(1/2) * b * h = a)")
            
        elif level == 3:
            r=inter(input("enter radius:" ))
            if view == "default view":
                print ( "pi", "*", r, "^2", "=", option3(r))
            else:
                print ( "pi", "*", r, "^2", "=", option3(r), "(pi * r^2 = a)")
                
        elif level == 4:
            s=inter(input("enter side:" ))
            if view == "default view":
                print ( s, "^2", "=", option4(s))
            else:
                print (  s, "^2", "=", option4(s), "(s^2 = v)")
        else:
            ra=inter(input("enter radius:" ))
            if view == "default view":
                print ( "4/3","*","pi","*", "r^3", "=", option5(ra))
            else:
                print ( "4/3","*","pi","*", "r^3", "=", option5(ra), "((4/3)*pi*r^3 = v)")
                
if __name__ == "__main__":
    main()
    
        
        

        

        
        
        
    

    

