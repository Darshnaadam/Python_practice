# In a function, how do you create a global variable?

global_var = 0
def setting_global_var():
    global global_var # setting global_var as global variable
    global_var = 10

def print_global_var():
    print(global_var) # no need to declare global_var

setting_global_var()
print_global_var() # will print the value in global_var which is 10