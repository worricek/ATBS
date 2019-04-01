#! python3
# hangoutgAutoGUI.py - Automatically sends a message to a select group of contacts. 

import pyautogui, time

# Set these to the correct coordinates for your particular computer.
searchField = (245, 240)
messageButton = (943, 483)
newConvButton = (259, 240)
closeConv = (1338, 219)

contacts=[{'name':'someAddress', 'message':'mr Gummidge wake up and smell the \ 		roses'}, {'name':'someOtherAddress', 'message':'To the Womble \
		it concerns. You test results are in and you are required to \
		lose 250kgs'}]

pyautogui.PAUSE = 5.0

time.sleep(2)

#pyautogui.click(messageButton[0], messageButton[1])

for person in contacts:
    # Start new conversation
    pyautogui.click(newConvButton[0], newConvButton[1])

    print('Entering %s info...' % (person['name']))

    # Fill out the Name field.
    pyautogui.typewrite(person['name']);pyautogui.typewrite('\n')
    #Write the message
    pyautogui.typewrite(person['message']);pyautogui.typewrite('\n')
    pyautogui.click(closeConv[0], closeConv[1])
    
    print('Message sent to ...' + person['name'])
    time.sleep(5)
 
