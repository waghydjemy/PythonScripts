from pkgutil import iter_modules

def module_exists(module_name):
    return module_name in (name for loader, name, ispkg in iter_modules())

print(module_exists('numpy'))
#print(module_exists(yourModuleHere))