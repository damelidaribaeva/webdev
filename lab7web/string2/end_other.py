def end_other(a, b):
    a_lower = a.lower()
    b_lower = b.lower()

    if b_lower.endswith(a_lower):
        return True

    if a_lower.endswith(b_lower):
        return True
    
    return False

#end_other('abc', 'abXabc') → True