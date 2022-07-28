import re


print('insert new central value for adjustment\n')
replace_text_mid = input()
print("insert old maximum value for adjustment\n")
replace_text_min = input()
print('insert new maximum value for adjustment\n')
replace_text_max = input()

#adjustment files

file_1 = 'zxc1.ini'
file_2 = 'zxc2.ini'
file_3 = 'zxc3.ini'
file_4 = 'zxc4.ini'
file_5 = 'zxc5.ini'
file_6 = 'zxc6.ini'
file_7 = 'zxc7.ini'
file_8 = 'zxc8.ini'
file_9 = 'zxc9.ini'

#free files
free_1 = 'xyz1.ini'
free_2 = 'xyz2.ini'
free_3 = 'xyz3.ini'
free_4 = 'xyz4.ini'
free_5 = 'xyz5.ini'
free_6 = 'xyz7.ini'
free_7 = 'xyz7.ini'
free_8 = 'xyz8.ini'
free_9 = 'xyz9.ini'
free_10 = 'xyz10.ini'

minimum = "FreqMinFcCtrlEnergie = "+ '*'
middle = "FreqFcibleCtrlEnergie = "+ '*'
maximal = "FreqMaxFcCtrlEnergie = "+ '*'

print(minimum,middle,maximal)

minimum_new = "FreqMinFcCtrlEnergie = "+replace_text_min
middle_new = "FreqFcibleCtrlEnergie = "+replace_text_mid
maximal_new = "FreqMaxFcCtrlEnergie = "+replace_text_max


adjustments = [file_1, file_2, file_3, file_4, file_5, file_6, file_7, file_8, file_9]
free = [free_1, free_2, free_3, free_4, free_5, free_6, free_7, free_8, free_9, free_10]
old_values = [minimum, middle, maximal]
new_values = [minimum_new, middle_new, maximal_new]

for i in range (0,8):
    
    for b in range(0,3):
        
        with open(adjustments[i], 'r') as file:
            
            data = file.read()
            data = data.replace(old_values[b],new_values[b])
            
        with open(adjustments[i],'w') as file:
            file.write(data)
    print("changed in file:" , adjustments[i])
    


print('insert new minimal value for free\n')
replace_text_min_free = input()
print('insert new central value for free\n')
replace_text_mid_free = input()
print('insert new maximum value for free\n')
replace_text_max_free = input()

minimum_free = "FreqMinFcCtrlEnergie = "+ "..,..."
middle_free = "FreqFcibleCtrlEnergie = "+ "..,..."
maximal_free = "FreqMaxFcCtrlEnergie = "+ "..,..."

minimum_new_free = "FreqMinFcCtrlEnergie = "+replace_text_min_free
middle_new_free = "FreqFcibleCtrlEnergie = "+replace_text_mid_free
maximal_new_free = "FreqMaxFcCtrlEnergie = "+replace_text_max_free

old_values_free = [minimum_free, middle_free, maximal_free]
new_values_free = [minimum_new_free, middle_new_free, maximal_new_free]


for i in range (0,9):
    
    for b in range(0,3):
        
        with open(free[i], 'r') as file:
            
            data = file.read()
            data = data.replace(old_values_free[b],new_values_free[b])
            
        with open(free[i],'w') as file:
            file.write(data)
    print("changed in file:", free[i])


print('data relaced')