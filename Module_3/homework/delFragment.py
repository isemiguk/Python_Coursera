str = input()

firstH = str.find('h')
endH = str.rfind('h')

finishStr = str[:firstH] + str[endH + 1:]
print(finishStr)
