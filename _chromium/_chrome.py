import aenea.config
import aenea.configuration

from aenea import (
    AeneaContext,
    AppContext,
    Dictation,
    Grammar,
    IntegerRef,
    Key,
    MappingRule,
    ProxyAppContext,
    Text
    )

chrome_context = aenea.AeneaContext(
    ProxyAppContext(cls_name='chrome', cls='chrome'),
    (AppContext(executable='chrome'))
    )

chrome_grammar = Grammar('chrome', context=chrome_context)


class chromeRule(MappingRule):
    mapping = aenea.configuration.make_grammar_commands('chrome', {
        'close [<n>] ( frame | frames )':    Key('c-w:%(n)d'),
        'open frame':                        Key('c-t'),
        'open window':                       Key('c-n'),
        'reopen [<n>] ( frame | frames )':   Key('cs-t:%(n)d'),
        '[ go to ] frame [<n>]':             Key('c-%(n)d'),
        'frame left [<n>]':                  Key('cs-tab:%(n)d'),
        'frame right [<n>]':                 Key('c-tab:%(n)d'),
        'search [<text>]':                   Key('c-k') + Text('%(text)s'),
        'find [<text>]':                     Key('c-f') + Text('%(text)s'),
        'history':                           Key('c-h'),
        'reload':                            Key('c-r'),
        'next [<n>]':                        Key('c-g:%(n)d'),
        'previous [<n>]':                    Key('cs-g:%(n)d'),
        'back [<n>]':                        Key('a-left:%(n)d'),
        'forward [<n>]':                     Key('a-right:%(n)d'),
        'enter': Key('enter'),
        'escape': Key('escape'),
        })

    extras = [IntegerRef('n', 1, 10), Dictation('text')]
    defaults = {
        'n': 1,
        'text': ''
        }

chrome_grammar.add_rule(chromeRule())

chrome_grammar.load()


def unload():
    global chrome_grammar
    if chrome_grammar:
        chrome_grammar.unload()
    chrome_grammar = None
