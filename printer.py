def dynamic_display_dict(input_dict:dict)->None:
    """Dynamically print a dictionary and refresh it

    Parameters
    ----------
    input_dict : dict
        The dict you want to print, every element will be printed
    """    
    size=len(input_dict)
    UP = "\x1B["+str(size)+"A"
    CLR = "\x1B[0K"
    res=f"{UP}"
    for k,v in input_dict.items():
        res+=f"{k}: {v}{CLR}\n"
    print(res)
