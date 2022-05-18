import win32gui
import win32api
import random
from win32api import GetSystemMetrics
from time import sleep

def main():
    # Screen testing stuf
    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)

    dc = win32gui.GetDC(0)

    # Box draw by size, x and y
    def draw_cuadrado(tamaño, x_pos, y_pos):
        for x in range(x_pos, x_pos+tamaño):
            for y in range(y_pos, y_pos+tamaño):
                win32gui.SetPixel(dc, x, y, win32api.RGB(random.randrange(0,200), random.randrange(0,200), random.randrange(0,200)))

    # Draw lines with boxes previous function
    def linea(orientacion, largo, tamaño, x, y):
        if orientacion == 0:
            for iter in range(0,largo + 2):
                draw_cuadrado(tamaño, x+iter*tamaño, y)
        else:
            for iter in range(0, largo + 2):
                draw_cuadrado(tamaño, x, y+iter*tamaño)

    while True: 
        try:
            # Extremo superior e inferior
            for x in range(0,2):
                linea(0, 8+x*6, 12, 900+x*-36, 140+x*8)
                linea(0, 6+x*6, 12, 864+43-x*36, 885-x*8)

            # Eyes
            for b in range(0,2):
                linea(0, 3, 12, 842+b*170, 440)  
                linea(0, 8, 12, 795+b*205, 452)
                for y in range(0,4):                   
                    linea(0, 10, 12, 777+b*220, 460+y*12)
                linea(0, 10+b*-1, 12, 777+b*234, 460+4*12)
                linea(0, 10-b*1, 12, 777+b*235, 460+5*12)
                for a in range(0,2): 
                    linea(0, 6+a*-1, 12, 777+12+x*12+b*230, 532+a*12)
                linea(0, 5, 12, 777+24+b*230, 460+8*12)
                linea(0, 1, 12, 777+36+b*240, 460+9*12)

            # Nariz
            for p in range(0, 7):
                if p <= 1:
                    # lados
                    linea(1, 6, 15, 928+p*54, 554)
                    linea(1, 2, 15, 914+p*82, 590)
                # puente
                linea(0, 1, 14, 940, 540+p*14)
    
            # Contorno
            for u in range(0,2):
                linea(0, 2, 12, 1055+u*-240, 160)
                linea(0, 1, 12, 1100+u*-320, 172)
                linea(0, 1, 12, 1130+u*-386, 184)
                linea(0, 1, 12, 1130+u*-386, 196)
                linea(0, 1, 12, 1145+u*-415, 208)
                linea(0, 1, 12, 1160+u*-440, 212)

                linea(1, 2, 12, 1188+u*-468, 222)
                linea(1, 2 , 12, 1200+u*-490, 250)
                linea(1, 8 , 15, 1210+u*-515, 285)
                linea(1, 4 , 15, 1222+u*-540, 310)
                linea(1, 2, 15, 1200+u*-490, 405)

                linea(1, 18, 15, 1167+u*-428, 310)
                linea(1, 2, 15, 1180+u*-455, 327)
                linea(1, 2, 16, 1180+u*-455, 460)
                linea(1, 5, 16, 1155+u*-405, 405)

                linea(0, 1, 12, 1145+u*-405, 600)
                linea(1, 2, 12, 1145+u*-382, 600)
                
                linea(1, 1, 12, 1095+u*-285, 780)
                linea(1, 1, 12, 1083+u*-261, 795)
                linea(1, 1, 12, 1071+u*-237, 805)
                linea(1, 1, 12, 1059+u*-213, 815)
                linea(1, 1, 12, 1047+u*-194, 825)
                linea(1, 2, 12, 1035+u*-170, 835)

                
                
                for x in range(0,2):
                    linea(0, 2, 17, 1080+u*-308, 620+x*17)

                linea(0, 5, 12, 1055+u*-275, 650)
                
                linea(1, 5, 19, 1105+u*-313, 650)

                linea(1, 5, 15, 1050+u*-198, 650)

                for x in range(0,2):
                    linea(0, 12, 15+x*2, 852+x*-8, 715+x*30)
                    
                linea(0, 3, 12, 1050+u*-250, 680)

                for x in range(0, 3):
                    #dientes
                    linea(1, 5, 13, 906+x*48, 720)

                    linea(0, 12, 12, 877, 800)
                    
                linea(1, 2, 12, 870+u*170, 750)

        except:
            pass


if __name__ == '__main__':
   main()


# # Experimenal function to draw diagonals lines
# def draw_diagonal(orientacion, tamaño, largo, x, y):

#         if orientacion == 1:

#             iter = largo

#             while iter >= 0:
#                 if iter == largo - 1:
#                     # Extremos
#                     draw_cuadrado(tamaño*2, x-2, y)
#                     draw_cuadrado(tamaño*2, x-10, y-10)

#                     draw_cuadrado(tamaño*2, x+iter-2, y-iter)
#                     draw_cuadrado(tamaño*2, x+iter-10, y-iter-10)                    
#                 else:
#                     draw_cuadrado(tamaño, x+iter, y-iter)
#                 iter = iter - 1
#         else:
#             for iter in range(0, largo):
#                 # Extremos
#                 if iter == largo - 1:
#                     draw_cuadrado(tamaño*2, x-10, y)
#                     draw_cuadrado(tamaño*2, x+2, y-10)

#                     draw_cuadrado(tamaño*2, x-iter-10, y-iter)
#                     draw_cuadrado(tamaño*2, x-iter+2, y-iter-10)               
#                 else:
#                     draw_cuadrado(tamaño, x-iter, y-iter)