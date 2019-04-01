from PIL import Image,  ImageDraw

file=open('guests.txt')
content=file.readlines()
flowerImage=Image.open('flower.jpg')
cardSizeFlower=flowerImage.resize((288,360))
cardSizeFlower.save('flowerCardSize.jpg')

for line in content:
    customCard=Image.open('flowerCardSize.jpg')
    draw=ImageDraw.Draw(customCard)
    draw.line([(1, 1), (287, 1), (287, 359), (1, 359), (1, 1)], fill='black')
    draw.text((150, 20), line, fill='purple')
    customCard.save(line+'INVITE.jpg')
print('\n\nAll invites created!!!\n\n')
