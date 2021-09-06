# Create by Bender

try:
    x = 1 / 0
except Exception as err:
    raise ValueError() from err
