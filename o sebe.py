import pygame



pygame.init()
pygame.mixer.init()

win=pygame.display.set_mode((1100,600))

white=(255,255,255)
black=(0,0,0)

meow_sound=pygame.mixer.Sound('o sebe1/meow.mp3')
ochki_sound=pygame.mixer.Sound('o sebe1/ochki.mp3')
straniti_sound=pygame.mixer.Sound('o sebe1/straniti.mp3')

meow_sound.set_volume(0.5)
ochki_sound.set_volume(0.7)
straniti_sound.set_volume(0.7)

pygame.mixer.music.load('o sebe1/music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)


fon=pygame.image.load("o sebe1/fon.png").convert()
fon=pygame.transform.scale(fon,((1100,600)))
background=fon

happy_cat=pygame.image.load('o sebe1/happycat.png').convert()
happy_cat.set_colorkey((0,0,0))
happy_cat=pygame.transform.scale(happy_cat,((550,500)))
h_cat=happy_cat

sad_cat=pygame.image.load('o sebe1/sadcat.png').convert()
sad_cat.set_colorkey((0,0,0))
sad_cat=pygame.transform.scale(sad_cat,((550,500)))
s_cat=sad_cat

normal_cat=pygame.image.load('o sebe1/normalcat.png').convert()
normal_cat.set_colorkey((0,0,0))
normal_cat=pygame.transform.scale(normal_cat,((550,500)))
norm_cat=normal_cat

question_cat=pygame.image.load('o sebe1/qustioncat.png').convert()
question_cat.set_colorkey((0,0,0))
question_cat=pygame.transform.scale(question_cat,((550,500)))
q_cat=question_cat

nachalo=pygame.image.load('o sebe1/nachalo.png')
nachalo=pygame.transform.scale(nachalo,((1100,600)))
na=nachalo

comic1=pygame.image.load('o sebe1/comic1.png')
comic1=pygame.transform.scale(comic1,((1100,600)))
co1=comic1

comic2=pygame.image.load('o sebe1/comic2.png')
comic2=pygame.transform.scale(comic2,((1100,600)))
co2=comic2

comic3=pygame.image.load('o sebe1/comic3.png')
comic3=pygame.transform.scale(comic3,((1100,600)))
co3=comic3

comic4=pygame.image.load('o sebe1/comic4.png')
comic4=pygame.transform.scale(comic4,((1100,600)))
co4=comic4

comic5=pygame.image.load('o sebe1/comic5.png')
comic5=pygame.transform.scale(comic5,((1100,600)))
co5=comic5

comic6=pygame.image.load('o sebe1/comic6.png')
comic6=pygame.transform.scale(comic6,((1100,600)))
co6=comic6

book=pygame.image.load('o sebe1/book.png').convert()
book.set_colorkey((0,0,0))
book=pygame.transform.scale(book,((500,500)))
b=book

book1=pygame.image.load('o sebe1/book1.png').convert()
book1.set_colorkey((0,0,0))
book1=pygame.transform.scale(book1,((800,500)))
b1=book1

myth1=pygame.image.load('o sebe1/appalondaphna.png').convert()
myth1.set_colorkey((0,0,0))
myth1=pygame.transform.scale(myth1,((600,400)))
m1=myth1

myth2=pygame.image.load('o sebe1/ariadna.png').convert()
myth2.set_colorkey((0,0,0))
myth2=pygame.transform.scale(myth2,((400,500)))
m2=myth2

myth3=pygame.image.load('o sebe1/meduse.png').convert()
myth3.set_colorkey((0,0,0))
myth3=pygame.transform.scale(myth3,((600,400)))
m3=myth3

myth4=pygame.image.load('o sebe1/achillies.png').convert()
myth4.set_colorkey((0,0,0))
myth4=pygame.transform.scale(myth4,((600,400)))
m4=myth4

bust=pygame.image.load('o sebe1/bust.png').convert()
bust.set_colorkey((0,0,0))
bust=pygame.transform.scale(bust,((500,500)))
b=bust

bust1=pygame.image.load('o sebe1/brokenbust.png').convert()
bust1.set_colorkey((0,0,0))
bust1=pygame.transform.scale(bust1,((500,500)))
b1=bust1

spasibo_za_igru=pygame.image.load('o sebe1/spasibo_za_igru.png')
spasibo_za_igru=pygame.transform.scale(spasibo_za_igru,((1100,600)))
spa=spasibo_za_igru

konfetka=pygame.image.load('o sebe1/konfetka.png')
konfetka=pygame.transform.scale(konfetka,((1100,600)))
kon=konfetka

font=pygame.font.SysFont('Trebuchet MS',35)

clock=pygame.time.Clock()
fps=30

def start_screen():
    waiting = True

    while waiting:
        win.blit(na,(0,0))


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False


def comics():
    comics_list=[co1,co2,co3,co4,co5,co6]
    
    for comic in comics_list:
        win.blit(comic,(0,0))
        pygame.display.update()

        start=pygame.time.get_ticks()
        waiting=True

        while waiting:
            for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if pygame.time.get_ticks()-start>2000:
                waiting=False

start_screen()
comics()

rrr = [
    ["...",s_cat],
    ["Что тебе нужно?",s_cat],
    ["Ты поможешь?",h_cat],
    ["Как здорово!Так давай же не медлить!",norm_cat],
    ["Я правда еще не знаю,как вернуть мой бюст...",s_cat],
    ["Я уверен,что вместе мы сможем восстоновить бюст!",norm_cat],
    ["Смотри!Книга открылась!",h_cat,book1],
    ["Похоже,нужно угадать греский миф?",q_cat,book1]
    ]

bbb=[
    ["Смотри!Книга открылась!",h_cat,book1],
    ["Похоже,нужно угадать греский миф?",q_cat,book1]
    ]

current = 0

user_text = ""
typing = False
result=''
fragment=0

answers = [
    "аполон и дафна",
    "ариадна",
    "медуза",
    "ахиллес"
]

myths = [m1, m2, m3, m4]
myth_index = 0

pet_time=0
happy_time=0

show_bust = False
bust_time = 0

game=True
while game:
    win.blit(background,(0,0))
    
    if current < len(rrr):  
     text = rrr[current][0]
     cat = rrr[current][1]

    now = pygame.time.get_ticks()

    if now < pet_time + 1000:
     cat = h_cat

    elif now < happy_time:
     cat = h_cat

    elif typing:
     cat = norm_cat

    current_book = book

    if current >= 6:
     current_book = book1
    else:
     current_book = book

    typing = current > 7

    win.blit(current_book,(0,0))
    win.blit(cat,(650,100))

    if not typing:
     txt = font.render(text, True, (255,255,255))
     win.blit(txt,(100,430))
    

    for event in pygame.event.get():

     if event.type == pygame.QUIT:
        game = False

     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RSHIFT:
         pet_time = pygame.time.get_ticks()
         meow_sound.play()

        if typing:

            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

            elif event.key == pygame.K_RETURN:

                if user_text.lower() == answers[myth_index]:

                    result = "Фрагмент получен!"
                    fragment += 1

                    if fragment == 4:
                     show_bust = True
                     bust_time = pygame.time.get_ticks()
                     ochki_sound.play()

                    happy_time=pygame.time.get_ticks() + 2000
                    
                    straniti_sound.play()

                    if myth_index < 3:
                        myth_index += 1


                else:
                    result = "Неверно"

                user_text = ""

            else:
                user_text += event.unicode

        else:

            if event.key == pygame.K_SPACE and not typing:

             current += 1
        
        typing = current >= len(rrr)

    if not typing:
     txt = font.render(text, True, (255,255,255))
     win.blit(txt,(100,430))
    
    
    if typing:

     win.blit(myths[myth_index], (110,30))

     input_box = font.render(
        "Ответ: " + user_text,
        True,
        white
     )

     res = font.render(
        result,
        True,
        white
     )

     fr = font.render(
        f"Фрагменты: {fragment}/4",
        True,
        white
     )

     win.blit(input_box,(100,520))
     win.blit(res,(100,550))
     win.blit(fr,(700,40))


    if show_bust:

     if pygame.time.get_ticks() - bust_time < 2500:
        win.fill(black)
        win.blit(b1,(350,50))

     else:
        win.fill(black)
        win.blit(b,(400,50))
     
     if show_bust:

      passed = pygame.time.get_ticks() - bust_time

     win.fill(black)

     if passed < 2000:
        win.blit(b1,(300,50))

     elif passed < 4000:

        if passed < 2050:
            ochki_sound.play(1)

        win.blit(b,(300,50))

     elif passed < 6000:
        win.blit(kon,(0,0))
        meow_sound.play(1)

     else:
        win.blit(spa,(0,0))

        

    pygame.display.update()
pygame.quit()