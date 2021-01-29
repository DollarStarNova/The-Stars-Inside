import pygame


def wrap_and_render_text(text, myfont, dimensions):
    final_image = pygame.Surface(dimensions, pygame.SRCALPHA, 32)
    # dimensions = (int(dimensions[0]*0.9), int(dimensions[1]*0.9))
    end_of_text = False
    words = text.split(" ")
    counter = 0
    textline = ""
    too_long = False
    blitposition = 0
    first_word = True
    while not end_of_text:
        while not too_long and not end_of_text:
            if len(words) <= counter:
                end_of_text = True
                # print("end of text")
            else:
                newtextline = textline + words[counter] + " "
                print(newtextline)
                new_render_size = myfont.size(newtextline)
                if new_render_size[0] <= dimensions[0]:
                    textline = newtextline
                    counter += 1
                    first_word = False
                else:
                    # This is an ugly way to handle too-long words but its better than crashing!
                    if first_word == True:
                        word1 = words[counter][int(len(words[counter])/2):]
                        word2 = words[counter][:int(len(words[counter])/2)]
                        words[counter] = word1
                        words.insert(counter, word2)
                    else:
                        too_long = True
        final_image.blit(myfont.render(
            textline, True, pygame.Color(150, 150, 150)), (0, blitposition))
        blitposition += myfont.size(textline)[1]
        textline = ""
        render_size = (0, 0)
        too_long = False
        first_word = True
    return final_image
