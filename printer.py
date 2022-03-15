def dynamic_display_dict(input_dict:dict)->None:
    """Dynamically print a dictionary and refresh it
    Inspired by https://stackoverflow.com/questions/39455022/python-3-print-update-on-multiple-lines
    Parameters
    ----------
    input_dict : dict
        The dict you want to print, every element will be printed
    """    
    size=len(input_dict)
    UP = "\x1B["+str(size+1)+"A"
    CLR = "\x1B[0K"
    res=f"{UP}"
    for k,v in input_dict.items():
        res+=f"{k}: {v}{CLR}\n"
    print(res)
