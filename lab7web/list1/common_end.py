def common_end(a, b):
    if len(a) >= 1 and len(b) >= 1:
        if a[0] == b[0] or a[-1] == b[-1]:
            return True
    return False

#common_end([1, 2, 3], [7, 3, 2]) → False