'''
TODO:
Write the faulty line numbers and explanations in line1-4 and explanation_line1-4.
line1-4 must be ints. explanation_line1-4 must be strings.
'''

line1 = 12
line2 = 17
line3 = 20
line4 = 23

explanation_line1 = "The bug occured due to a KeyError. The key does not exist in memory dictionary: Instead of memory[ptr+1] = 0, the line should be memory[ptr] = 0"
explanation_line2 = "The bug occured due to a KeyError. The key does not exist in memory dictionary: Instead of memory[ptr-1] = 0, the line should be memory[ptr] = 0"
explanation_line3 = "The bug occured due to a ValueError. The parameter for chr() is not in range: Instead of memory[ptr] = (memory[ptr]+1), the line should be memory[ptr] = (memory[ptr]+1) % 256"
explanation_line4 = "The bug occured due to a ValueError. The parameter for chr() is not in range: Instead of memory[ptr] = (memory[ptr]-1), the line should be memory[ptr] = (memory[ptr]-1) % 256"