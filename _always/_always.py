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

import lex_parse

import generate_lexer

always_context = aenea.ProxyPlatformContext('linux')

grammar = dragonfly.Grammar('always', context=always_context)
from aenea import (
    AeneaContext,
    AppContext,
    Alternative,
    CompoundRule,
    Dictation,
    DictList,
    DictListRef,
    Grammar,
    IntegerRef,
    Literal,
    ProxyAppContext,
    MappingRule,
    NeverContext,
    Repetition,
    RuleRef,
    Sequence
)

from aenea.lax import Key, Text


def textify(input):
    for x in input:
        input[x] = Text(input[x])


class Compound(CompoundRule):
    inner_keys = '( ' + '|'.join(generate_lexer.all_keys.keys()) + ')'
    spec = inner_keys + ('[' + inner_keys + ']') * 10
    extras = [aenea.misc.DigitalInteger('n', 1, None), Dictation(name='text')]
    defaults = {
        'n': 1,
        }

    def _process_recognition(self, value, extras):
        words = ' '.join(value.words())
        print 'process recognition node:', words
        [i.execute() for i in lex_parse.ext_yacc.parse(words)]


grammar.add_rule(Compound())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
