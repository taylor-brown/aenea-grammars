# This is a command module for Dragonfly. It provides bindings for the Linux
# window manager always. Only active when running via proxy and the server
# reports Linux.

# You may find this useful to disable the Windows key in windows stealing focus
# from the client.
# http://support.microsoft.com/kb/216893#LetMeFixItMyselfAlways

import aenea
import aenea.misc
import aenea.configuration

import dragonfly

always_context = aenea.ProxyPlatformContext('linux')

grammar = dragonfly.Grammar('always', context=always_context)


from aenea.lax import Key, Text

always_mapping = aenea.configuration.make_grammar_commands('always', {
    'up': Key('up'),
    'down': Key('down'),
    'left': Key('left'),
    'right': Key('right'),
    'pad': Key('down:25'),
    'pug': Key('up:25'),
    'home': Key('home'),
    'end': Key('end'),
    'up <n>': Key('up:%(n)d'),
    'down <n>': Key('down:%(n)d'),
    'left <n>': Key('left:%(n)d'),
    'right <n>': Key('right:%(n)d'),
    'whoops': Key('c-z'),
    'reoops': Key('cs-z'),
    'copy': Key('c-c'),
    'paste': Key('c-v'),

    #navigation
    'lope [<n>]': Key('c-left:%(n)d'),
    'rope [<n>]': Key('c-right:%(n)d'),

    'srope [<n>]': Key('cs-right:%(n)d'),
    'slope [<n>]': Key('cs-left:%(n)d'),

    'file top': Key('c-home'),
    'file toe': Key('c-end'),

    # ### Various keys
    'ace [<n>]': Key('space:%(n)d'),
    'act': Key('escape'),
    'chuck [<n>]': Key('del:%(n)d'),
    'scratch [<n>]': Key('backspace:%(n)d'),
    'slap [<n>]': Key('enter:%(n)d'),
    'tab [<n>]': Key('tab:%(n)d'),

    #### Lines
    'nab [<n>]': Key('home:2, shift:down, down:%(n)d, up, end:2, shift:up, c-c, end:2'),
    'wipe [<n>]': Key('home:2, shift:down, down:%(n)d,  del, shift:up'),
    "see down [<n>]": Key("shift:down, down:%(n)d,shift:up"),
    "see up [<n>]": Key("shift:down, up:%(n)d,shift:up"),
    'comment [<n>]': Key('shift:down, down:%(n)d, shift:up, control:down, slash, control:up'),


    #### Words
    'bump [<n>]': Key('c-del:%(n)d'),
    'whack [<n>]': Key('c-backspace:%(n)d'),

})


class always(dragonfly.MappingRule):
    mapping = always_mapping
    extras = [aenea.misc.DigitalInteger('n', 1, None)]

grammar.add_rule(always())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
