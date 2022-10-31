def interpret(command):
    newStr = ''
    deleteStr = ''
    
    for item in command:
        deleteStr += item
        if deleteStr.endswith('()'):
            newStr += 'o'
        elif item == '(' or item ==')':
            pass
        
        else:
            newStr += item
        
    return newStr

print(interpret('G()()()(al)'))