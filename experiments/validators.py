def int_check(num,mn,mx):
    error = [
        "Enter a valid Integer",
        "Value should be between {} and {}".format(mn,mx)
    ]
    try:
        num = int(num)
    except:
        return 1,error[0],1
    
    if num >=mn and num <=mx:
        return num,"",0
    else:
        return 1,error[1],1
    
def float_check(num,mn,mx):
    error = [
        "Enter a valid Number",
        "Value should be between {} and {}".format(mn,mx)
    ]
    try:
        num = float(num)
    except:
        return 1,error[0],1
    num = round(num,1)
    if num >=mn and num <=mx:
        return num,"",0
    else:
        return 1,error[1],1
    
def choice_check(choice ,all_choices):
     error = "Enter a Valid Choice"
     if choice in all_choices:
         return choice,"",0
     else:
         return choice,error,1