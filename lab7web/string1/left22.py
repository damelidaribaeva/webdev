def left2(s):
    if len(s) >= 2:
        return s[2:] + s[:2]
    else:
        return s
    
    #left2('java') → 'vaja'