# keymap control setting
init python:
    config.keymap['dismiss'].append('mousedown_5')
    config.keymap['dismiss'].append('K_DOWN')
    config.keymap['rollback'] = ('K_UP')

define config.mouse = { }
define config.mouse['default'] = [ ( "gui/cc.png", 0, 0) ]

# save setting
init python:
    config.has_autosave = False
    config.has_quicksave = False
    config.autosave_on_quit = False
    config.autosave_on_choice = False