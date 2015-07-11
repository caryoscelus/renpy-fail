label main_menu:
    return

screen normal_screen(s, trans):
    default n = False
    frame at trans:
        has vbox
        label s
        label str(n)
        if n:
            label "You clicked button"
        else:
            textbutton "Click me!" action ToggleScreenVariable('n')

screen nesting_screen(s, trans):
    use normal_screen(s, trans)

transform right:
    xalign 1.0

transform left:
    xalign 0.0

label start:
    show screen nesting_screen('i am inside nested screen', left)
    show screen normal_screen('i am inside normal screen', right)
    "Inside nested screen, actions doesn't work with screen variables.."
    return
