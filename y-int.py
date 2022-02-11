from multiprocessing.spawn import import_main_path


import run
def yint_multiply(slope_final, x1):
    return slope_final * x1

def yint_final(y1, yint_multiply):
    return y1 - yint_multiply


