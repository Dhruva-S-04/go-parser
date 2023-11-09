import ply.lex as lex
import ply.yacc as yacc

# Define Go keywords
go_keywords = {
    'var': 'VAR',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'case': 'CASE',
    'default': 'DEFAULT',
    'switch' : 'SWITCH'
}

tokens = ['ID', 'SEMICOLON', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'ASSIGN', 'NUMBER', 'STRING', 'GT', 'LT', 'GE', 'LE', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE','COLON'] + list(go_keywords.values())

t_SEMICOLON = r';'
t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = go_keywords.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_statements(p):
    '''statements : declaration
                   | if_statement
                   | for_statement
                   | switch_statement
                   | expression SEMICOLON
                   | arithmetic_counter SEMICOLON
                   | expression ASSIGN expression SEMICOLON
                   | if_statement statements
                   | for_statement statements
                   | switch_statement statements
                   | expression SEMICOLON statements
                   | arithmetic_counter SEMICOLON statements
                   | expression ASSIGN expression SEMICOLON statements
                   | empty'''

def p_declaration(p):
    '''declaration : VAR ID ASSIGN expression SEMICOLON'''
    print("Valid Declaration:", p[2])

def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN block
                    | IF LPAREN expression RPAREN block ELSE block
                    | IF LPAREN expression RPAREN block ELSE if_statement'''

def p_for_statement(p):
    '''for_statement : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN block
                     | FOR LPAREN expression SEMICOLON expression SEMICOLON arithmetic_counter RPAREN block
                     | FOR LPAREN initialization SEMICOLON expression SEMICOLON expression RPAREN block
                     | FOR LPAREN initialization SEMICOLON expression SEMICOLON arithmetic_counter RPAREN block
                     | FOR expression SEMICOLON expression SEMICOLON expression block
    '''

def p_initialization(p):
    '''
        initialization : ID COLON ASSIGN expression
    '''
def p_expression(p):
    '''expression : ID
                  | literal
                  | comparison
                  | arithmetic_expression
                  | LPAREN expression RPAREN
                  | expression ASSIGN expression 
                  '''

def p_switch_statement(p):
    '''switch_statement : SWITCH expression LBRACE case_statement RBRACE
    '''

def p_case_statement(p):
    '''case_statement : CASE expression COLON expression SEMICOLON
                      | CASE expression COLON expression SEMICOLON case_statement
                      | DEFAULT COLON expression SEMICOLON 
                      | DEFAULT COLON expression SEMICOLON case_statement
                      | empty
    '''

def p_literal(p):
    '''literal : NUMBER
               | STRING'''

def p_comparison(p):
    '''comparison : expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression'''
    p[0] = True

def p_arithmetic_expression(p):
    '''arithmetic_expression : expression PLUS expression
                            | expression MINUS expression
                            | expression TIMES expression
                            | expression DIVIDE expression'''
    p[0] = True

def p_arithmetic_counter(p):
    '''
      arithmetic_counter  : ID PLUS ASSIGN expression
                          | ID MINUS ASSIGN expression
    '''
def p_block(p):
    '''block : LBRACE statements RBRACE'''

def p_empty(p):
    '''empty :'''
    pass

# Error handling for syntax errors
def p_error(p):
    global syntax_error
    syntax_error = True
    print("Syntax error")

parser = yacc.yacc()

syntax_error = False

while True:
    try:
        s = input("Enter: ")
    except EOFError:
        break
    if not s:
        continue
    
    lexer.input(s)
    for tok in lexer:
        print(tok)
    
    syntax_error = False
    
    result = parser.parse(s)
    
    if not syntax_error:
        print("Valid statement")
