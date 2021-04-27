import sys, pygame
import random
pygame.init()

def isInList(list1, num):
    for x in list1:
        if x == num:
            return True
    return False

def checkLists(list1, list2, length):
    for i in range(length):
        if list1[i] != list2[i]:
            return False
    return True

def translator(image_num):
    if image_num == image_2x2_1 or image_num == image_2x3_1:
        return 1
    elif image_num == image_2x2_2 or image_num == image_2x3_2:
        return 2
    elif image_num == image_2x2_3 or image_num == image_2x3_3:
        return 3
    elif image_num == image_2x2_4 or image_num == image_2x3_4:
        return 4
    elif image_num == image_2x3_5:
        return 5
    elif image_num == image_2x3_6:
        return 6

large_font = pygame.font.SysFont("Times New Roman", 60)
font = pygame.font.SysFont("Times New Roman", 35)
smallfont = pygame.font.SysFont("Times New Roman", 28)

color_dark = (0, 150, 100)
color_light = (170, 170, 170)
color_clicked = (0, 200, 200)

width = 600
height = 600
screen = pygame.display.set_mode((width, height))

image = pygame.image.load("pictures/sunflower.jpg")
image = pygame.transform.scale(image, (400, 400))

color = (0, 0, 0)
color_red = (255, 0, 0)

text = font.render("Choose complexity:", True, color)
fours = font.render("2x2", True, color)
sixes = font.render("2x3", True, color)
eights = font.render("2x4", True, color)

states = ['home', 'full_img_disp', 'img_split_2x2', 'img_split_2x3', 'img_split_2x4', 'log_in']
curr_state = states[0]

img_states = ['on', 'off']
img1 = img_states[0]
img2 = img_states[0]
img3 = img_states[0]
img4 = img_states[0]
img5 = img_states[0]
img6 = img_states[0]
error_state = img_states[1]
next_button_state = img_states[1]
logged_in_state = img_states[1]
try_again_state = img_states[1]

ATTEMPTS = 4
bottom_words = "Try again! "+str(ATTEMPTS)

password_seq = []
check_password_seq = []

#images
image_2x2_1 = pygame.image.load("2x2/sunflower_01_01.png")
image_2x2_1 = pygame.transform.scale(image_2x2_1, (200,200))
image_2x2_2 = pygame.image.load("2x2/sunflower_01_02.png")
image_2x2_2 = pygame.transform.scale(image_2x2_2, (200,200))
image_2x2_3 = pygame.image.load("2x2/sunflower_02_01.png")
image_2x2_3 = pygame.transform.scale(image_2x2_3, (200,200))
image_2x2_4 = pygame.image.load("2x2/sunflower_02_02.png")
image_2x2_4 = pygame.transform.scale(image_2x2_4, (200,200))

image_2x3_1 = pygame.image.load("2x3/sunflower_01_01.png")
image_2x3_1 = pygame.transform.scale(image_2x3_1, (133,200))
image_2x3_2 = pygame.image.load("2x3/sunflower_01_02.png")
image_2x3_2 = pygame.transform.scale(image_2x3_2, (133,200))
image_2x3_3 = pygame.image.load("2x3/sunflower_01_03.png")
image_2x3_3 = pygame.transform.scale(image_2x3_3, (133,200))
image_2x3_4 = pygame.image.load("2x3/sunflower_02_01.png")
image_2x3_4 = pygame.transform.scale(image_2x3_4, (133,200))
image_2x3_5 = pygame.image.load("2x3/sunflower_02_02.png")
image_2x3_5 = pygame.transform.scale(image_2x3_5, (133,200))
image_2x3_6 = pygame.image.load("2x3/sunflower_02_03.png")
image_2x3_6 = pygame.transform.scale(image_2x3_6, (133,200))

image_order_2x2 = [image_2x2_1, image_2x2_2, image_2x2_3, image_2x2_4]
image_order_2x3 = [image_2x3_1, image_2x3_2, image_2x3_3, image_2x3_4, image_2x3_5, image_2x3_6]
random.shuffle(image_order_2x2)
random.shuffle(image_order_2x3)

while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if curr_state == 'home':
                #log in
                if 100-5 <= mouse[0] <= 100+130-5 and 300-5 <= mouse[1] <= 300+50-5:
                    if not password_seq:
                        error_state = img_states[0]
                    else:
                        curr_state = states[5]
                #create new password
                if 100-5 <= mouse[0] <= 100+350-5 and 400-5 <= mouse[1] <= 400+50-5:
                    ATTEMPTS = 4
                    try_again_state = img_states[1]
                    curr_state = states[1]
                    error_state = img_states[1]
                    password_seq.clear()
                    check_password_seq.clear()
                    logged_in_state = img_states[1]
                    img1 = img_states[0]
                    img2 = img_states[0]
                    img3 = img_states[0]
                    img4 = img_states[0]
                    img5 = img_states[0]
                    img6 = img_states[0]

            elif curr_state == 'log_in':
                #back button
                if 10-5 <= mouse[0] <= 10-5+90 and 500-5 <= mouse[1] <= 500-5+50:
                    curr_state = states[0]
                #img sections
                if complexity_chosen == '2x2':
                    if 100 <= mouse[0] <= 100+200 and 150 <= mouse[1] <= 150+200:
                        img1 = img_states[1]
                        if isInList(check_password_seq, translator(image_order_2x2[0])) != True:
                            check_password_seq.append(translator(image_order_2x2[0]))
                    if 100+200+5 <= mouse[0] <= 100+200+200 and 150 <= mouse[1] <= 150+200:
                        img2 = img_states[1]
                        if isInList(check_password_seq, translator(image_order_2x2[1])) != True:
                            check_password_seq.append(translator(image_order_2x2[1]))
                    if 100 <= mouse[0] <= 100+200 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                        img3 = img_states[1]
                        if isInList(check_password_seq, translator(image_order_2x2[2])) != True:
                            check_password_seq.append(translator(image_order_2x2[2]))
                    if 100+200+5 <= mouse[0] <= 100+200+5+200 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                        img4 = img_states[1]  
                        if isInList(check_password_seq, translator(image_order_2x2[3])) != True:
                            check_password_seq.append(translator(image_order_2x2[3]))
                    if len(check_password_seq) == 4:
                        if checkLists(password_seq, check_password_seq, 4):
                            logged_in_state = img_states[0]
                            try_again_state = img_states[1]
                        elif ATTEMPTS == 0:
                            bottom_words = "LOCKED OUT"
                        else:
                            img1 = img_states[0]
                            img2 = img_states[0]
                            img3 = img_states[0]
                            img4 = img_states[0]
                            check_password_seq.clear()
                            try_again_state = img_states[0]
                            bottom_words = "Try again! ("+str(ATTEMPTS)+")"
                            ATTEMPTS = ATTEMPTS - 1
                elif complexity_chosen == '2x3':
                    if 100 <= mouse[0] <= 100+133 and 150 <= mouse[1] <= 150+200:
                        img1 = img_states[1]
                        if isInList(check_password_seq, translator(image_order_2x3[0])) != True:
                            check_password_seq.append(translator(image_order_2x3[0]))
                    if 100+133+5 <= mouse[0] <= 100+133+133+5 and 150 <= mouse[1] <= 150+200:
                        img2 = img_states[1]
                        if isInList(check_password_seq, translator(image_order_2x3[1])) != True:
                            check_password_seq.append(translator(image_order_2x3[1]))
                    if 100+133+133+5+5 <= mouse[0] <= 100+133+133+133+5+5 and 150 <= mouse[1] <= 150+200:
                        img3 = img_states[1]
                        if isInList(check_password_seq, translator(image_order_2x3[2])) != True:
                            check_password_seq.append(translator(image_order_2x3[2]))
                    if 100 <= mouse[0] <= 100+133 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                        img4 = img_states[1]  
                        if isInList(check_password_seq, translator(image_order_2x3[3])) != True:
                            check_password_seq.append(translator(image_order_2x3[3]))
                    if 100+133+5 <= mouse[0] <= 100+133+133+5 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                        img5 = img_states[1]  
                        if isInList(check_password_seq, translator(image_order_2x3[4])) != True:
                            check_password_seq.append(translator(image_order_2x3[4]))
                    if 100+133+133+5+5 <= mouse[0] <= 100+133+133+133+5+5 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                        img6 = img_states[1]  
                        if isInList(check_password_seq, translator(image_order_2x3[5])) != True:
                            check_password_seq.append(translator(image_order_2x3[5]))
                    if len(check_password_seq) == 6:
                        if checkLists(password_seq, check_password_seq, 6):
                            logged_in_state = img_states[0]
                            try_again_state = img_states[1]
                        elif ATTEMPTS == 0:
                            bottom_words = "LOCKED OUT"
                        else:
                            img1 = img_states[0]
                            img2 = img_states[0]
                            img3 = img_states[0]
                            img4 = img_states[0]
                            img5 = img_states[0]
                            img6 = img_states[0]
                            check_password_seq.clear()
                            try_again_state = img_states[0]
                            bottom_words = "Try again! ("+str(ATTEMPTS)+")"
                            ATTEMPTS = ATTEMPTS - 1
            elif curr_state == 'full_img_disp':
                #2x2
                if 5 <= mouse [0] <= 5+65 and 50 <= mouse[1] <= 50+40:
                    curr_state = states[2]
                    complexity_chosen = '2x2'
                #2x3
                if 10+100 <= mouse [0] <= 10+100+65 and 50 <= mouse[1] <= 50+40:
                    curr_state = states[3]
                    complexity_chosen = '2x3'
                #back
                if 10-5 <= mouse[0] <= 10-5+90 and 500-5 <= mouse[1] <= 500-5+50:
                    curr_state = states[0]
            elif curr_state == 'img_split_2x2':
                #img sections
                if 100 <= mouse[0] <= 100+200 and 150 <= mouse[1] <= 150+200:
                    img1 = img_states[1]
                    if isInList(password_seq, 1) != True:
                        password_seq.append(1)
                if 100+200+5 <= mouse[0] <= 100+200+200 and 150 <= mouse[1] <= 150+200:
                    img2 = img_states[1]
                    if isInList(password_seq, 2) != True:
                        password_seq.append(2)
                if 100 <= mouse[0] <= 100+200 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                    img3 = img_states[1]
                    if isInList(password_seq, 3) != True:
                        password_seq.append(3)
                if 100+200+5 <= mouse[0] <= 100+200+5+200 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                    img4 = img_states[1]  
                    if isInList(password_seq, 4) != True:
                        password_seq.append(4)  
                #check if password is done
                if len(password_seq) == 4:
                    next_button_state = img_states[0]  
                #next button
                if 500-5 <= mouse[0] <= 500-5+90 and 500-5 <= mouse[1] <= 500-5+50:
                    next_button_state = img_states[1]
                    curr_state = states[0]
                    img1 = img_states[0]
                    img2 = img_states[0]
                    img3 = img_states[0]
                    img4 = img_states[0]
            elif curr_state == 'img_split_2x3':
                #img sections
                if 100 <= mouse[0] <= 100+133 and 150 <= mouse[1] <= 150+200:
                    img1 = img_states[1]
                    if isInList(password_seq, 1) != True:
                        password_seq.append(1)
                if 100+133+5 <= mouse[0] <= 100+133+133+5 and 150 <= mouse[1] <= 150+200:
                    img2 = img_states[1]
                    if isInList(password_seq, 2) != True:
                        password_seq.append(2)
                if 100+133+133+5+5 <= mouse[0] <= 100+133+133+133+5+5 and 150 <= mouse[1] <= 150+200:
                    img3 = img_states[1]
                    if isInList(password_seq, 3) != True:
                        password_seq.append(3)
                if 100 <= mouse[0] <= 100+133 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                    img4 = img_states[1]  
                    if isInList(password_seq, 4) != True:
                        password_seq.append(4)  
                if 100+133+5 <= mouse[0] <= 100+133+133+5 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                    img5 = img_states[1]
                    if isInList(password_seq, 5) != True:
                        password_seq.append(5)
                if 100+133+133+5+5 <= mouse[0] <= 100+133+133+133+5+5 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                    img6 = img_states[1]
                    if isInList(password_seq, 6) != True:
                        password_seq.append(6)
                #check if password is done
                if len(password_seq) == 6:
                    next_button_state = img_states[0]  
                #next button
                if 500-5 <= mouse[0] <= 500-5+90 and 500-5 <= mouse[1] <= 500-5+50:
                    next_button_state = img_states[1]
                    curr_state = states[0]
                    img1 = img_states[0]
                    img2 = img_states[0]
                    img3 = img_states[0]
                    img4 = img_states[0]
                    img5 = img_states[0]
                    img6 = img_states[0]

    mouse = pygame.mouse.get_pos()

    if curr_state == 'home':
        if 100-5 <= mouse[0] <= 100+130-5 and 300-5 <= mouse[1] <= 300+50-5:
            pygame.draw.rect(screen, color_light, [100-5, 300-5, 130, 50])
        else:
            pygame.draw.rect(screen, color_dark, [100-5, 300-5, 130, 50])
        if 100-5 <= mouse[0] <= 100+350-5 and 400-5 <= mouse[1] <= 400+50-5:
            pygame.draw.rect(screen, color_light, [100-5, 400-5, 350, 50])
        else:
            pygame.draw.rect(screen, color_dark, [100-5, 400-5, 350, 50])
        welcome_text = large_font.render("Welcome!", True, color)
        inst_text = font.render("Log In", True, color)
        create_text = font.render("Create new password", True, color)
        error_text = font.render("Please create a password first!!", True, color)
        screen.blit(welcome_text, (100, 100))
        screen.blit(inst_text, (100, 300))
        screen.blit(create_text, (100, 400))
        if error_state == 'on':
            screen.blit(error_text, (100, 500))
    
    elif curr_state == 'log_in':
        #top text
        enter_text = font.render("Enter password", True, color)
        screen.blit(enter_text, (20, 50))
        #image pieces
        if complexity_chosen == '2x2':
            if img1 == 'on':
                screen.blit(image_order_2x2[0], (100, 150))
            if img2 == 'on':
                screen.blit(image_order_2x2[1], (100+200+5, 150))
            if img3 == 'on':
                screen.blit(image_order_2x2[2], (100, 150+200+5))
            if img4 == 'on':
                screen.blit(image_order_2x2[3], (100+200+5, 150+200+5))
        elif complexity_chosen == '2x3':
            if img1 == 'on':
                screen.blit(image_order_2x3[0], (100, 150))
            if img2 == 'on':
                screen.blit(image_order_2x3[1], (100+133+5, 150))
            if img3 == 'on':
                screen.blit(image_order_2x3[2], (100+133+133+5+5, 150))
            if img4 == 'on':
                screen.blit(image_order_2x3[3], (100, 150+200+5))
            if img5 == 'on':
                screen.blit(image_order_2x3[4], (100+133+5, 150+200+5))
            if img6 == 'on':
                screen.blit(image_order_2x3[5], (100+133+133+5+5, 150+200+5))
        #text
        if logged_in_state == 'on':
            logged_in_text = large_font.render("Logged in!", True, color)
            screen.blit(logged_in_text, (175, 275))
        if try_again_state == 'on':
            try_again_text = font.render(bottom_words, True, color)
            screen.blit(try_again_text, (225, 557))
        #back button
        if 10-5 <= mouse[0] <= 10-5+90 and 500-5 <= mouse[1] <= 500-5+50:
            pygame.draw.rect(screen, color_light, [10-5, 500-5, 90, 50])
        else:
            pygame.draw.rect(screen, color_dark, [10-5, 500-5, 90, 50])
        back_text = font.render("Back", True, color)
        screen.blit(back_text, (10, 500))

    elif curr_state == 'full_img_disp':
        #main image
        screen.blit(image, (100,150))
        #buttons and highlights
        if 10 <= mouse [0] <= 10+65 and 50 <= mouse[1] <= 50+40:
            pygame.draw.rect(screen, color_light, [10, 50, 65, 40])
        else:
            pygame.draw.rect(screen, color_dark, [10, 50, 65, 40])
        if 10+100 <= mouse [0] <= 10+100+65 and 50 <= mouse[1] <= 50+40:
            pygame.draw.rect(screen, color_light, [10+100, 50, 65, 40])
        else:
            pygame.draw.rect(screen, color_dark, [10+100, 50, 65, 40])
        if 10+100+100 <= mouse [0] <= 10+100+65+100 and 50 <= mouse[1] <= 50+40:
            pygame.draw.rect(screen, color_light, [10+100+100, 50, 65, 40])
        else:
            pygame.draw.rect(screen, color_dark, [10+100+100, 50, 65, 40])
        #text and complexities
        screen.blit(text, (15, 0))
        screen.blit(fours, (15, 50))
        screen.blit(sixes, (15+100, 50))
        screen.blit(eights, (15+100+100, 50))
        #back button
        if 10-5 <= mouse[0] <= 10-5+90 and 500-5 <= mouse[1] <= 500-5+50:
            pygame.draw.rect(screen, color_light, [10-5, 500-5, 90, 50])
        else:
            pygame.draw.rect(screen, color_dark, [10-5, 500-5, 90, 50])
        back_text = font.render("Back", True, color)
        screen.blit(back_text, (10, 500))

    elif curr_state == 'img_split_2x2':
        #selected button
        pygame.draw.rect(screen, color_clicked, [5, 50, 65, 40])
        if img1 == 'on':
            screen.blit(image_2x2_1, (100, 150))
            if 100 <= mouse[0] <= 100+200 and 150 <= mouse[1] <= 150+200:
                one = font.render("1", True, color_red)
            else:
                one = font.render("1", True, color)
            screen.blit(one, (100, 150))
        if img2 == 'on':
            screen.blit(image_2x2_2, (100+200+5, 150))
            if 100+200+5 <= mouse[0] <= 100+200+200 and 150 <= mouse[1] <= 150+200:
                two = font.render("2", True, color_red)
            else:
                two = font.render("2", True, color)
            screen.blit(two, (100+200+5, 150))
        if img3 == 'on':
            screen.blit(image_2x2_3, (100, 150+200+5))
            if 100 <= mouse[0] <= 100+200 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                three = font.render("3", True, color_red)
            else:
                three = font.render("3", True, color)
            screen.blit(three, (100, 150+200+5))
        if img4 == 'on':
            screen.blit(image_2x2_4, (100+200+5, 150+200+5))
            if 100+200+5 <= mouse[0] <= 100+200+5+200 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                four = font.render("4", True, color_red)
            else:
                four = font.render("4", True, color)  
            screen.blit(four, (100+200+5, 150+200+5))
        #text and complexities
        text = smallfont.render("Click the images to choose your new password", True, color)
        screen.blit(text, (15, 0))
        screen.blit(fours, (15, 50))
        screen.blit(sixes, (15+100, 50))
        screen.blit(eights, (15+100+100, 50))
        #next button
        if next_button_state == 'on':
            if 500-5 <= mouse[0] <= 500-5+90 and 500-5 <= mouse[1] <= 500-5+50:
                pygame.draw.rect(screen, color_light, [500-5, 500-5, 90, 50])
            else:
                pygame.draw.rect(screen, color_dark, [500-5, 500-5, 90, 50])
            back_text = font.render("Next", True, color)
            screen.blit(back_text, (500, 500))

    elif curr_state == 'img_split_2x3':
        #selected button
        pygame.draw.rect(screen, color_clicked, [10+100, 50, 65, 40])
        if img1 == 'on':
            screen.blit(image_2x3_1, (100, 150))
            if 100 <= mouse[0] <= 100+133 and 150 <= mouse[1] <= 150+200:
                one = font.render("1", True, color_red)
            else:
                one = font.render("1", True, color)
            screen.blit(one, (100, 150))
        if img2 == 'on':
            screen.blit(image_2x3_2, (100+133+5, 150))
            if 100+133+5 <= mouse[0] <= 100+133+133+5 and 150 <= mouse[1] <= 150+200:
                two = font.render("2", True, color_red)
            else:
                two = font.render("2", True, color)
            screen.blit(two, (100+133+5, 150))
        if img3 == 'on':
            screen.blit(image_2x3_3, (100+133+133+5+5, 150))
            if 100+133+133+5+5 <= mouse[0] <= 100+133+133+133+5+5 and 150 <= mouse[1] <= 150+200:
                three = font.render("3", True, color_red)
            else:
                three = font.render("3", True, color)
            screen.blit(three, (100+133+133+5+5, 150))
        if img4 == 'on':
            screen.blit(image_2x3_4, (100, 150+200+5))
            if 100 <= mouse[0] <= 100+133 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                four = font.render("4", True, color_red)
            else:
                four = font.render("4", True, color)
            screen.blit(four, (100, 150+200+5))
        if img5 == 'on':
            screen.blit(image_2x3_5, (100+133+5, 150+200+5))
            if 100+133+5 <= mouse[0] <= 100+133+133+5 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                five = font.render("5", True, color_red)
            else:
                five = font.render("5", True, color)
            screen.blit(five, (100+133+5, 150+200+5))
        if img6 == 'on':
            screen.blit(image_2x3_6, (100+133+133+5+5, 150+200+5))
            if 100+133+133+5+5 <= mouse[0] <= 100+133+133+133+5+5 and 150+200+5 <= mouse[1] <= 150+200+5+200:
                six = font.render("6", True, color_red)
            else:
                six = font.render("6", True, color)
            screen.blit(six, (100+133+133+5+5, 150+200+5))
        #text and complexities
        text = smallfont.render("Click the images to choose your new password", True, color)
        screen.blit(text, (15, 0))
        screen.blit(fours, (15, 50))
        screen.blit(sixes, (15+100, 50))
        screen.blit(eights, (15+100+100, 50))
        #next button
        if next_button_state == 'on':
            if 500-5 <= mouse[0] <= 500-5+90 and 500-5 <= mouse[1] <= 500-5+50:
                pygame.draw.rect(screen, color_light, [500-5, 500-5, 90, 50])
            else:
                pygame.draw.rect(screen, color_dark, [500-5, 500-5, 90, 50])
            back_text = font.render("Next", True, color)
            screen.blit(back_text, (500, 500))

    else:
        text = font.render("error", True, color)
        screen.blit(text, (300,300))

    pygame.display.update()

pygame.quit()
quit()