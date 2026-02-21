def calculate_clock_interval(face1, face2):
    x = abs(face1 - face2)
    if x <= 6 :
        return x
    else :
        return 12 - x
