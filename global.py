global_var = 10

def not_change_gloval_var():
    global_var = 20

not_change_gloval_var()
print("response when not using global: ", global_var)


def change_gloval_var():
    global global_var
    global_var = 20

change_gloval_var()
print("response when using global: ", global_var)