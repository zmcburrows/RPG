from page_471 import time_passes

def you_occupy():
    print('''
    
You occupy yourself on the last bit of activity you can do: taking tiny sips of water, burying yourself in your sleeping bag, and your book, \033[34mHouse\033[0m of Leaves

You burn the page for light as you read. However, it doesn’t take long for you to fall behind, the flames catching the words before you can read them. 

“Maybe I’m a slow reader, or the pages are burning unevenly or messed up burning it." you say. Or the words in the book have been arranged in such a way as to make them practically impossible to read.
  
''')
    last_moments = input('''
    
You resort to lighting the cover and spin of the book. You always end up losing words and burning your fingertips.

You are down to one match and one page. You wait, you want to postpone this last bit of illumination as long as you can.
    
''')
    if last_moments == "":
        end = input('''
        
Eventually, you strike the match. You read as much as you can by match light alone, and as the flames and heat bite your fingertips, you put it against the page.

You read as fast as you can, the flames eating at the paper hungrily. A final act of consumption.

Your eyes beat the last bit of flames, reading the last few words as they get the last bit of paper, ash falling away into emptiness as your last bit of light dims and finally is spent. The book is now invisible traces dismantled in the dark.        
        
''')
        if end == "":
            time_passes()