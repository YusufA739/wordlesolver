# string = "oajnsd,asd,ad,a,sd,a,sd,a,sd"
# lstring = []
# for carrier in string:
#     lstring.append(carrier)
#
# lstring.remove(",")
# value = list(string)
# value.remove(",")
# print(lstring)
# print(value)
#
# string = "2345,123"
# string = string.split(",")
# pos = []
# for carrier in string:
#     pos.append(list(carrier))
# print(pos)
#
# string = "2345,123"
# temp_list = list(string)
# indexPointer = 0
# for letter in temp_list:
#     try:
#         temp = int(letter)
#         temp -= 1
#         temp_list[indexPointer] = temp
#     except:
#         pass
#     indexPointer += 1
# print(temp_list)
from wordlesolver.wordlehelper import yellow_letter_positions_anti_input_MODIFIED

#works
yellow_letter_positions_anti_input = "2345,123"
if yellow_letter_positions_anti_input != "":
    # #disassemble, subtract 1 from all numbers
    # temp_list = list(yellow_letter_positions_anti_input)
    # indexPointer = 0
    # for letter in temp_list:
    #     try:
    #         temp = int(letter)
    #         temp -= 1
    #         temp_list[indexPointer] = str(temp)#cast back to string after modifications
    #     except:
    #         pass
    #     indexPointer += 1
    # #reassemble input
    # yellow_letter_positions_anti_input_MODIFIED = ""
    # for letter in temp_list:
    #     yellow_letter_positions_anti_input_MODIFIED += letter
    # print(yellow_letter_positions_anti_input_MODIFIED)
    yellow_letter_positions_anti_input_MODIFIED = yellow_letter_positions_anti_input
#NOW continue operations on input as normal, ON MODIFIED DATA, OTHERWISE THE EFFORT AND LENGTHS TAKEN TO MODIFY ARE USELESS IF WE DON'T USE THIS NEW DATA
    list1 = yellow_letter_positions_anti_input_MODIFIED.split(",")
    print(list1)
    list2 = []
    for entry in list1:
        list2.append(list(entry))
    print(list2)

    outerIndex = 0
    innerIndex = 0
    for current_list in list2:
        for element in current_list:
            print(element)
            list2[outerIndex][innerIndex] = int(element) - 1
            innerIndex += 1
        outerIndex += 1
        innerIndex = 0
    print(list2)
#end of finished prototype code that works