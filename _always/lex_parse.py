import generate_lexer

t_ACE = r"ace"
t_ACT = r"act"
t_ALPHA = r"alpha"
t_AMP = r"amp"
t_ASH = r"ash"
t_AT_SIGN = r"atsign"
t_BACK_ASH = r"backash"
t_BACKTICK = r"backtick"
t_BANG = r"bang"
t_BAR = r"bar"
t_BIT_AND = r"bitand"
t_BIT_EX_OR = r"bitexor"
t_BIT_ORE = r"bitore"
t_BOXCO = r"boxco"
t_BOXSO = r"boxso"
t_BRAVO = r"bravo"
t_BUMP = r"bump"
t_CHARLIE = r"charlie"
t_CHUCK = r"chuck"
t_COPY = r"copy"
t_COMMENT = r"comment"
t_DELTA = r"delta"
t_DIVIDED = r"divided"
t_DOLLAR = r"dollar"
t_DOT = r"dot"
t_DOWN = r"down"
t_DRIP = r"drip"
t_ECHO = r"echo"
t_EEK = r"eek"
t_EIGHT = r"eight"
t_END = r"end"
t_FILETOE = r"filetoe"
t_FILETOP = r"filetop"
t_FIVE = r"five"
t_FOUR = r"four"
t_FOXTROT = r"foxtrot"
t_GOLF = r"golf"
t_HAT = r"hat"
t_HOME = r"home"
t_HOTEL = r"hotel"
t_HYPH = r"hyph"
t_ITEM = r"item"
t_JOHNNY = r"johnny"
t_KILO = r"kilo"
t_LEFT = r"left"
t_LOPE = r"lope"
t_LOVE = r"love"
t_MIKE = r"mike"
t_MINUS = r"minus"
t_NINER = r"niner"
t_NUTS = r"nuts"
t_ONE = r"one"
t_OSCAR = r"oscar"
t_PAD = r"pad"
t_PASTE = r"paste"
t_PERCENT = r"percent"
t_PLUS = r"plus"
t_POP = r"pop"
t_POPPA = r"poppa"
t_POUND = r"pound"
t_PUG = r"pug"
t_PUSH = r"push"
t_QUEST = r"quest"
t_QUICHE = r"quiche"
t_QUOTE = r"quote"
t_RAIL = r"rail"
t_REOOPS = r"reoops"
t_RIGHT = r"right"
t_ROGER = r"roger"
t_ROPE = r"rope"
t_SCRATCH = r"scratch"
t_SEMI = r"semi"
t_SEVEN = r"seven"
t_SEEUP = r'seeup'
t_SEEDOWN = r'seedown'
t_SIX = r"six"
t_SLAP = r"slap"
t_SLOPE = r"slope"
t_SMOTE = r"smote"
t_SQUARECO = r"squareco"
t_SQUARESO = r"squareso"
t_SROPE = r"srope"
t_STAR = r"star"
t_SUGAR = r"sugar"
t_TAB = r"tab"
t_TANGO = r"tango"
t_THREE = r"three"
t_TILDE = r"tilde"
t_TWO = r"two"
t_UNCLE = r"uncle"
t_UP = r"up"
t_CAP_ALPHA = r"capalpha"
t_CAP_BRAVO = r"capbravo"
t_CAP_CHARLIE = r"capcharlie"
t_CAP_DELTA = r"capdelta"
t_CAP_ECHO = r"capecho"
t_CAP_FOXTROT = r"capfoxtrot"
t_CAP_GOLF = r"capgolf"
t_CAP_HOTEL = r"caphotel"
t_CAP_ITEM = r"capitem"
t_CAP_JOHNNY = r"capjohnny"
t_CAP_KILO = r"capkilo"
t_CAP_LOVE = r"caplove"
t_CAP_MIKE = r"capmike"
t_CAP_NUTS = r"capnuts"
t_CAP_OSCAR = r"caposcar"
t_CAP_POPPA = r"cappoppa"
t_CAP_QUICHE = r"capquiche"
t_CAP_ROGER = r"caproger"
t_CAP_SUGAR = r"capsugar"
t_CAP_TANGO = r"captango"
t_CAP_UNCLE = r"capuncle"
t_CAP_VICTOR = r"capvictor"
t_CAP_WHISKEY = r"capwhiskey"
t_CAP_XRAY = r"capxray"
t_CAP_YANKEE = r"capyankee"
t_CAP_ZULU = r"capzulu"
t_VICTOR = r"victor"
t_WHACK = r"whack"
t_WHISKEY = r"whiskey"
t_WHOOPS = r"whoops"
t_XRAY = r"xray"
t_YANKEE = r"yankee"
t_YEAH = r"yeah"
t_ZERO = r"zero"
t_ZULU = r"zulu"
tokens =  ['ACE', 'ACT', 'ALPHA', 'AMP', 'ASH', 'AT_SIGN', 'BACK_ASH', 'BACKTICK', 'BANG', 'BAR', 'BIT_AND', 'BIT_EX_OR', 'BIT_ORE', 'BOXCO', 'BOXSO', 'BRAVO', 'BUMP', 'CHARLIE', 'CHUCK', 'COPY', 'DELTA', 'DIVIDED', 'DOLLAR', 'DOT', 'DOWN', 'DRIP', 'ECHO', 'EEK', 'EIGHT', 'END', 'FILETOE', 'FILETOP', 'FIVE', 'FOUR', 'FOXTROT', 'GOLF', 'HAT', 'HOME', 'HOTEL', 'HYPH', 'ITEM', 'JOHNNY', 'KILO', 'LEFT', 'LOPE', 'LOVE', 'MIKE', 'MINUS', 'NINER', 'NUTS', 'ONE', 'OSCAR', 'PAD', 'PASTE', 'PERCENT', 'PLUS', 'POP', 'POPPA', 'POUND', 'PUG', 'PUSH', 'QUEST', 'QUICHE', 'QUOTE', 'RAIL', 'REOOPS', 'RIGHT', 'ROGER', 'ROPE', 'SCRATCH', 'SEMI', 'SEVEN', 'SIX', 'SLAP', 'SLOPE', 'SMOTE', 'SQUARECO', 'SQUARESO', 'SROPE', 'STAR', 'SUGAR', 'TAB', 'TANGO', 'THREE', 'TILDE', 'TWO', 'UNCLE', 'UP', 'CAP_ALPHA', 'CAP_BRAVO', 'CAP_CHARLIE', 'CAP_DELTA', 'CAP_ECHO', 'CAP_FOXTROT', 'CAP_GOLF', 'CAP_HOTEL', 'CAP_ITEM', 'CAP_JOHNNY', 'CAP_KILO', 'CAP_LOVE', 'CAP_MIKE', 'CAP_NUTS', 'CAP_OSCAR', 'CAP_POPPA', 'CAP_QUICHE', 'CAP_ROGER', 'CAP_SUGAR', 'CAP_TANGO', 'CAP_UNCLE', 'CAP_VICTOR', 'CAP_WHISKEY', 'CAP_XRAY', 'CAP_YANKEE', 'CAP_ZULU', 'VICTOR', 'WHACK', 'WHISKEY', 'WHOOPS', 'XRAY', 'YANKEE', 'YEAH', 'ZERO', 'ZULU', 'SENTENCE', 'PROPER', 'CAMEL', 'PATH', 'SCORE', 'JUMBLE', 'DOTWORD', 'NATWORD', 'SEEUP', 'SEEDOWN', 'COMMENT']


# Ignored characters
t_ignore = " 	"

def t_SENTENCE(t):
    r'sentence .*? feen'
    t.value = t.value[9:-5]
    t.value = t.value.capitalize()
    return t


def t_PROPER(t):
    r'proper .*? feen'
    t.value = t.value[7:-5]
    t.value = ''.join([i.capitalize() for i in t.value.split(' ')])
    return t


def t_CAMEL(t):
    r'camel .*? feen'
    t.value = t.value[4:-5]
    def format_camel(text):
        return text[0] + ''.join([word[0].upper() + word[1:] for word in text[1:]])

    t.value = format_camel(t.value.split(' '))
    return t

def t_PATH(t):
    r'path .*? feen'
    t.value = t.value[5:-5]
    t.value = '/'.join(t.value.split(' '))
    return t

def t_SCORE(t):
    r'score .*? feen'
    t.value = t.value[6:-5]
    t.value = '_'.join(t.value.split(' '))
    return t


def t_JUMBLE(t):
    r'jumble .*? feen'
    t.value = t.value[7:-5]
    t.value = ''.join(t.value.split(' '))
    return t


def t_DOTWORD(t):
    r'dotword .*? feen'
    t.value = t.value[8:-5]
    t.value = '.'.join(t.value.split(' '))
    return t


def t_NATWORD(t):
    r'natword .*? feen'
    t.value = t.value[7:-5]
    return t


def add_to_t(t, app):
    if not isinstance(lst, t[0]):
        t[0] = []
    t[0].append(app)


from aenea.lax import Key, Text
# class Text(object):
#     def __init__(self, txt):
#         self.txt = txt
#         super(Text, self).__init__()
#
#     def __repr__(self):
#         return 'Text' + self.txt
#
#
# class Key(object):
#     def __init__(self, txt):
#         self.txt = txt
#         super(Key, self).__init__()
#
#     def __repr__(self):
#         return "key" + self.txt


def p_statement_expr(t):
    'statement : expression'
    t[0] = t[1]

def p_expr_expr(t):
    'expression : expression expression'
    t[0] = t[1] + t[2]


def p_number(t):
    """number : EIGHT
             | FIVE
             | FOUR
             | NINER
             | ONE
             | SEVEN
             | SIX
             | THREE
             | TWO
             | ZERO

    """
    ints = {    'zero':'0',
    'one':'1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'niner': '9',}

    t[0] = ints[t[1]]

def p_key(t):
    """expression : COPY
                 | COMMENT
                 | END
                 | FILETOE
                 | FILETOP
                 | HOME
                 | PAD
                 | PASTE
                 | PUG
                 | REOOPS
                 | WHOOPS
                 | AMP
                 | ASH
                 | AT_SIGN
                 | BACK_ASH
                 | BACKTICK
                 | BANG
                 | BAR
                 | BIT_AND
                 | BIT_EX_OR
                 | BIT_ORE
                 | BOXCO
                 | BOXSO
                 | DIVIDED
                 | DOLLAR
                 | DOT
                 | DRIP
                 | EEK
                 | HAT
                 | HYPH
                 | MINUS
                 | PERCENT
                 | PLUS
                 | POP
                 | POUND
                 | PUSH
                 | QUEST
                 | QUOTE
                 | RAIL
                 | SEMI
                 | SMOTE
                 | SQUARECO
                 | SQUARESO
                 | STAR
                 | TILDE
                 | YEAH

 """
    t[0] = [Key(generate_lexer.all_keys[t[1]])]

def p_text_expression(t):
    """expression : SENTENCE
                 | PROPER
                 | CAMEL
                 | PATH
                 | SCORE
                 | JUMBLE
                 | DOTWORD
                 | NATWORD
    """
    t[0] = [Text(t[1])]

def p_keytext_expression(t):
    """expression : ALPHA
                 | BRAVO
                 | CHARLIE
                 | DELTA
                 | ECHO
                 | FOXTROT
                 | GOLF
                 | HOTEL
                 | ITEM
                 | JOHNNY
                 | KILO
                 | LOVE
                 | MIKE
                 | NUTS
                 | OSCAR
                 | POPPA
                 | QUICHE
                 | ROGER
                 | SUGAR
                 | TANGO
                 | UNCLE
                 | CAP_ALPHA
                 | CAP_BRAVO
                 | CAP_CHARLIE
                 | CAP_DELTA
                 | CAP_ECHO
                 | CAP_FOXTROT
                 | CAP_GOLF
                 | CAP_HOTEL
                 | CAP_ITEM
                 | CAP_JOHNNY
                 | CAP_KILO
                 | CAP_LOVE
                 | CAP_MIKE
                 | CAP_NUTS
                 | CAP_OSCAR
                 | CAP_POPPA
                 | CAP_QUICHE
                 | CAP_ROGER
                 | CAP_SUGAR
                 | CAP_TANGO
                 | CAP_UNCLE
                 | CAP_VICTOR
                 | CAP_WHISKEY
                 | CAP_XRAY
                 | CAP_YANKEE
                 | CAP_ZULU
                 | VICTOR
                 | WHISKEY
                 | XRAY
                 | YANKEE
                 | ZULU
    """
    t[0] = [Text(generate_lexer.all_keys[t[1]])]

def p_expression_number(t):
    """expression : number"""
    t[0] = [Text(t[1])]

def p_multiple(t):
    """multiple : ACE
                 | ACT
                 | BUMP
                 | CHUCK
                 | DOWN
                 | LEFT
                 | LOPE
                 | RIGHT
                 | ROPE
                 | SEEUP
                 | SEEDOWN
                 | SCRATCH
                 | SLAP
                 | SLOPE
                 | SROPE
                 | TAB
                 | UP
                 | WHACK"""
    t[0] = Key(generate_lexer.multiples[t[1]])

def p_expression_multiple(t):
    """ expression : multiple
                    | multiple number"""
    p = []
    if len(t) > 2:
        p = [t[1]] * int(t[2])
    else:
        p = [t[1]]
    t[0] = p

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_error(t):
    print("Syntax error at '%s'" % t)

import ply.lex as lex
lex.lex()

import ply.yacc as yacc
yacc.yacc(debugfile=r'\tmp\parser.out', outputdir='\\tmp\\', write_tables=False)
ext_yacc = yacc

print yacc.parse("caposcar ace eight niner bravo dotword woohoo me feen ")