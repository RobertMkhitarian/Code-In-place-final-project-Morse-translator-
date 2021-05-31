import pygame

#Importing PyGame

from pygame import mixer
pygame.mixer.pre_init()
pygame.init()
pygame.mixer.init()


sound_dot = pygame.mixer.Sound("morse_dot.wav")
sound_dash = pygame.mixer.Sound("morse_dash.wav")



def main():
    #Default speed
    speed = 225
    space_speed = 335
    stop = ""
    #Creating dictionary 
    letters = {
        'a': '._' ,
        'b': '_...',
        'c': '_._.',
        'd': '_..',
        'e': '.',
        'f': '.._.',
        'g': '__.',
        'h': '....',
        'i': '..',
        'j': '.___',
        'k': '_._',
        'l': '._..',
        'm': '__',
        'n': '_.',
        'o': '___',
        'p': '.__.',
        'q': '__._',
        'r': '._.',
        's': '...',
        't': '_',
        'u': '.._',
        'v': '..._',
        'w': '.__',
        'x': '_.._',
        'y': '_.__',
        'z': '__..',
        '1': '.____',
        '2': '..___',
        '3': '...__',
        '4': '...._',
        '5': '.....',
        '6': '_....',
        '7': '__...',
        '8': '___..',
        '9': '____.',
        '0': '_____',
        ' ': ''
        }

    #Programm will work until user write 'stop'
    while stop!= "stop":
        answer = " "
        morse_list = []
        list_part = ""
        print("In this programm you can translate Morse code to English, or from English to Morse code \n////////////////////WARNING//////////////////// \nYou can only translate from English to Morse or From Morse to English!\nWhen translating from Morse code to English put spaces between letters, and two spaces between words!\nYou can also use numbers.\n If you have inputed something wrong program will return empty line, so please run it again.\n///////////////////////////////////////////////")
        final_text = input("Enter English text or Morse code, to translate: ")
        final_text = final_text.lower()

        

        for x in final_text:
            for key in letters:
                if x == key:
                    answer+=letters[key]
                    answer+=" "

        
        final_text = final_text + " "
        
        #Add all letters in list
        for x in final_text:
            if x != " ":
                list_part += x
            elif x == " ":
                #Removing all unnecessary spaces
                list_part = list_part.strip()
                
                morse_list.append(list_part)
                list_part = " "


        for i in morse_list:
            for key in letters:
                if i == letters[key]:                
                    answer+=key

        print(answer)

        
        #Playing appropriate souund
        for j in answer:
            if j == ".":
               sound_dot.play()
               pygame.time.wait(speed)
            elif j == "_":
                sound_dash.play()
                pygame.time.wait(speed)
            elif j == " ":
                pygame.time.wait(space_speed)

        stop = " "     
        stop = input("///////\n If you ended your translation type 'stop', if not type anything, if you want to change speed of sounds Morse code type 'change' : ")
        #User can can change speed of Morse code  
        if stop == "change":
            speed = int(input("Eter value from 2 to 10: "))
            speed = speed * 100
            space_speed = speed +110
        stop = stop.lower()
        if stop == "stop": 
            print("Goodbye!")            


if __name__ == '__main__':
    main()

