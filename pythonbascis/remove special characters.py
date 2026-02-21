def remove_special_chars(s):
    special_characters=('@','#',"!","*",".","$","%","^","&","_","-",'=',"+",'~','<',">","?",",","(",")","/")
    s = ''.join(char for char in s if char not in special_characters)
    return s
