import os

while True:
    readfile=open('/home/worrall/Downloads/UDC-CS-L05-SW01','r')
    writefile='/home/worrall/Downloads/test'
    select=input('What interface number you want: ')
    smash=readfile.readlines()
    tag=0
    if os.path.exists(writefile):
        destFile=open(writefile, 'a')
    else:
        destFile=open(writefile, 'w') 

    for line in smash:
        if select in line:
            destFile.write(line)
            print(line)
            tag=1
            continue
        if tag==1:
            if 'interface' in line or line == '\n':
                tag=0
                destFile.write('\n')
                print('Done!')
                break
            else:
                destFile.write(line)
                print(line)
    if input('Continue: ') == 'y':
        continue
    else:
        destFile.close()
        break
print('Did that work??')

        
