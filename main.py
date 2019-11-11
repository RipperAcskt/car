import pygame
import random
import cars

pygame.init()

win = pygame.display.set_mode((800, 1000))

x = 260
y = 790
height = 100
width = 50

height_line = 200
width_line = 20
speed_line = 1
run = True

lines = [
    [200, 0],
    [200, 400],
    [200, 800],
    [400, 0],
    [400, 400],
    [400, 800],
    [600, 0],
    [600, 400],
    [600, 800]
]

speed_car_blue = 5
speed_car = 7
n = 0
cars_list = []


def draw_lines():
    x_line = 0
    y_line = 0

    for i in range(9):
        for j in range(2):
            if j == 0:
                x_line = lines[i][j]

            else:
                y_line = lines[i][j]
                lines[i][j] += speed_line
                if lines[i][j] > 1000:
                    lines[i][j] = -200

        pygame.draw.rect(win, (255, 255, 255), (x_line, y_line, width_line, height_line))


def cars_draw():
    for i in range(len(cars_list)):
        cars_list[i].move(speed_car_blue)
        if cars_list[i].y < 1030:
            pygame.draw.rect(win, (0, 0, 255), (cars_list[i].x, cars_list[i].y, width, height))
        else:
            del cars_list[i]
            pygame.draw.rect(win, (0, 0, 255), (cars_list[i].x, cars_list[i].y, width, height))
            break


def cars_logic():
    x_car = 60
    y_car = -200

    if len(cars_list) < 5:
        if len(cars_list) != 0:
            if cars_list[len(cars_list) - 1].y > 400:
                line = random.randint(0, 3)
                cars_list.append(cars.car(x_car + line * 200, y_car))
                cars_draw()
            else:
                cars_draw()
        else:
            line = random.randint(0, 3)
            cars_list.append(cars.car(x_car + line * 200, y_car))

    else:
        cars_draw()


def control(xn, yn):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and xn > 0:
        xn -= speed_car
    if keys[pygame.K_RIGHT] and xn < 800 - width:
        xn += speed_car
    if keys[pygame.K_UP] and yn > 0:
        yn -= speed_car
    if keys[pygame.K_DOWN] and yn < 1000 - height:
        yn += speed_car

    return xn, yn


def crash():
    for i in range(len(cars_list)):
        if y > cars_list[i].y:
            if abs(x - cars_list[i].x) <= 40 and abs(y - (cars_list[i].y)) <= 90:
                return False
        else:
            if abs(x - (cars_list[i].x - 10)) <= 50 and abs(y - (cars_list[i].y - 10)) <= 100:
                return False
    return True


while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    if crash():
        win.fill((0, 0, 0))
        draw_lines()
        cars_logic()
        x, y = control(x, y)
        pygame.draw.rect(win, (145, 255, 195), (x, y, width, height))
        pygame.display.update()
    else:
        run = False

pygame.quit()
