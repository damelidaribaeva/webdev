def combo_string(a, b):
    if len(a) < len(b):
        short, long = a, b
    else:
        short, long = b, a
    
    return short + long + short

#combo_string('hi', 'Hello') → 'hiHellohi'