# This is a command module for Dragonfly. It provides bindings for the Linux
# window manager gnome. Only active when running via proxy and the server
# reports Linux.

# You may find this useful to disable the Windows key in windows stealing focus
# from the client.
# http://support.microsoft.com/kb/216893#LetMeFixItMyselfAlways

import aenea
import aenea.misc
import aenea.configuration

import dragonfly

gnome_context = aenea.ProxyPlatformContext('linux')

grammar = dragonfly.Grammar('gnome', context=gnome_context)

gnome = ''

from aenea.lax import Key, Text

basics_mapping = aenea.configuration.make_grammar_commands('gnome', {
    'whim <n>': Key('a-%(n)d'),
    'whim over [<text>]': Key('win') + Text('%(text)s'),
    'whim tab': Key('a-tab'),
    'whim move <n>': Key('as-%(n)d'),
    'whim close': Key('as-c'),
    # '(whim | notion | ion) up': Key(gnome + '-k'),
    # '(whim | notion | ion) down': Key(gnome + '-j'),
    # '(whim | notion | ion) left': Key(gnome + 's-k'),
    # '(whim | notion | ion) right': Key(gnome + 's-j'),
    # '(whim | notion | ion) change screen [<n>]': Key(gnome + '-o:%(n)d'),
    # '(whim | notion | ion) close client': Key(gnome + 's-c'),
    # '(whim | notion | ion) snap': Key(gnome + 'c-enter'),
    # '(whim | notion | ion) full': Key(gnome + '-m'),
    # '(whim | notion | ion) [work] <n>': Key(gnome + '-%(n)d'),
    # '(whim | notion | ion) tag <n>': Key(gnome + 'sc-%(n)d'),
    # '(whim | notion | ion) tag marked <n>': Key(gnome + 's-%(n)d'),
    # '(whim | notion | ion) move marked <n>': Key(gnome + 's-%(n)d')
    })


class Basics(dragonfly.MappingRule):
    mapping = basics_mapping
    extras = [aenea.misc.DigitalInteger('n', 1, None), aenea.Dictation('text')]
    defaults = {
        'n': 1,
        'text': ''
    }


grammar.add_rule(Basics())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
