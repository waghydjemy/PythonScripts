import win32gui

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ) and len(win32gui.GetWindowText( hwnd )) > 0 :
        print (win32gui.GetWindowText( hwnd ))

win32gui.EnumWindows( winEnumHandler, None )
