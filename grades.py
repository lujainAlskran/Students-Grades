def Add_STD_Grdaes():
    stdList =[0]*2
    i = 0
    while i < len(stdList):
        stdList[i] = [0]*5
        e = 0
        while e < len(stdList[i]):
            grade = raw_input("Enter the grade of student number " + str(i+1) + ": ")
            stdList[i][e] = grade
            e += 1
        print "________________________________________"
        #stdList[i] = gradeList
        i += 1
#print stdList 
    # _____________Calculate Total___________________
    TotalList = [0]*len(stdList)
    #t = 0
    j = 0
    while j < len(stdList):
        s = 0
        t = 0
        while s < len(stdList[j]):
            v = stdList[j][s]
            t += int(v)
            s += 1
        TotalList[j] = t
        j += 1
    # _____________calculate AVG_____________________
    AVG_list = [0]*len(TotalList)
    f = 0
    for e in TotalList:
        avg = float(e) / 5
        AVG_list[f] = avg
        f += 1
    # ______________AVG in words_______________________
    AVG_in_words = [" "]*len(AVG_list)
    w = 0
    for e in AVG_list:
        if e == 100 and e >= 90:
            AVG_in_words[w] = "Excellent"
        elif e < 90 and e >= 80:
            AVG_in_words[w] = "Very Good"
        elif e < 80 and e >= 70:
            AVG_in_words[w] = "Good"
        elif e < 70 and e >= 60:
            AVG_in_words[w] = "Acceptable"
        elif e < 60:
            AVG_in_words[w] = "Deposit"
        w += 1
    return stdList , TotalList , AVG_list , AVG_in_words

print Add_STD_Grdaes()


