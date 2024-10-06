def rgb(r, g, b):
    return ''.join(['{:02X}'.format(min(255, max(x, 0))) for x in [r, g, b]])

if __name__ == '__main__':
    assert rgb(255, 255, 0) == "FFFF00"
    assert rgb(300, 0, -55) == "FF0000"
