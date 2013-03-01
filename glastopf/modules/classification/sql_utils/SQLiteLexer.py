# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SQLite.g 2012-04-18 19:31:20

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

#package org.tmatesoft.sqljet.core.internal.lang;



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
ROW = 183
BLOB_LITERAL = 7
TYPE_PARAMS = 35
NOT = 43
EXCEPT = 120
FOREIGN = 163
EOF = -1
STATEMENT = 32
TYPE = 34
RPAREN = 50
CREATE = 151
STRING_LITERAL = 31
IS_NULL = 25
USING = 133
BIND = 5
CREATE_TRIGGER = 15
BEGIN = 141
REGEXP = 62
ANALYZE = 108
FUNCTION_LITERAL = 19
CONFLICT = 150
APOSTROPHE = 188
LESS_OR_EQ = 65
ATTACH = 105
VIRTUAL = 152
D = 195
E = 196
F = 197
ID_QUOTED = 233
G = 198
BLOB = 92
A = 192
B = 193
C = 194
ASC = 112
L = 203
M = 204
N = 205
O = 206
TRANSACTION = 145
KEY = 159
H = 199
BIND_NAME = 6
I = 200
ELSE = 85
J = 201
K = 202
U = 212
T = 211
IN_VALUES = 22
W = 214
UNDERSCORE = 191
V = 213
Q = 208
P = 207
S = 210
R = 209
ROLLBACK = 101
FAIL = 103
RESTRICT = 166
Y = 216
X = 215
Z = 217
GROUP = 124
INTERSECT = 119
DROP_INDEX = 16
WS = 237
PLAN = 39
ALIAS = 4
END = 86
RPAREN_SQUARE = 190
CONSTRAINT = 157
RENAME = 171
ALTER = 170
ID_PLAIN = 227
STRING_CORE_DOUBLE = 222
ISNULL = 52
TABLE = 153
FLOAT = 90
STRING_CORE_SINGLE = 221
ID_QUOTED_CORE_SQUARE = 229
NOTNULL = 53
NOT_EQUALS = 58
NOT_NULL = 27
LPAREN = 48
ASTERISK = 74
GREATER_OR_EQ = 67
AT = 98
DOUBLE_PIPE = 77
AS = 83
SLASH = 75
IS_NOT = 26
THEN = 88
ID_QUOTED_CORE = 228
OFFSET = 116
REPLACE = 111
LEFT = 127
COLUMN = 173
PLUS = 72
PIPE = 71
EXISTS = 156
LIKE = 60
COLLATE = 79
ADD = 172
INTEGER = 89
OUTER = 128
BY = 42
DEFERRABLE = 167
TO = 147
ID_CORE = 226
AMPERSAND = 70
SET = 139
HAVING = 125
MINUS = 73
IGNORE = 100
SEMI = 36
UNION = 117
COLUMN_CONSTRAINT = 8
COLON = 97
FLOAT_EXP = 234
COLUMNS = 10
COMMIT = 146
IN_TABLE = 23
DATABASE = 106
VACUUM = 110
DROP = 169
DETACH = 107
WHEN = 87
ID_QUOTED_APOSTROPHE = 232
STRING_DOUBLE = 224
STRING_SINGLE = 223
NATURAL = 126
BETWEEN = 56
OPTIONS = 28
STRING = 91
CAST = 82
STRING_CORE = 220
TABLE_CONSTRAINT = 33
ID_LITERAL = 21
CURRENT_TIME = 93
TRIGGER = 176
CASE = 84
EQUALS = 51
CASCADE = 165
RELEASE = 149
EXPLAIN = 37
GREATER = 66
ESCAPE = 46
INSERT = 134
SAVEPOINT = 148
LESS = 64
RAISE = 99
LPAREN_SQUARE = 189
EACH = 182
COMMENT = 235
ABORT = 102
SELECT = 121
INTO = 135
UNIQUE = 161
GLOB = 61
VIEW = 174
LINE_COMMENT = 236
NULL = 55
QUOTE_DOUBLE = 186
ON = 132
MATCH = 63
PRIMARY = 158
DELETE = 140
OF = 180
SHIFT_LEFT = 68
SHIFT_RIGHT = 69
INTEGER_LITERAL = 24
FUNCTION_EXPRESSION = 20
OR = 44
QUERY = 38
CHECK = 162
QUOTE_SINGLE = 187
STRING_ESCAPE_DOUBLE = 219
FROM = 122
DISTINCT = 81
TEMPORARY = 154
CURRENT_DATE = 94
BACKSLASH = 184
DOLLAR = 185
WHERE = 123
CONSTRAINTS = 11
COLUMN_EXPRESSION = 9
INNER = 129
STRING_ESCAPE_SINGLE = 218
ORDER = 114
LIMIT = 115
PRAGMA = 104
UPDATE = 138
FOR = 181
DEFERRED = 142
SELECT_CORE = 30
EXCLUSIVE = 144
AND = 45
ID = 80
CROSS = 130
IF = 155
INDEX = 175
TILDA = 78
IN = 47
REFERENCES = 164
CREATE_TABLE = 13
COMMA = 49
IS = 54
ALL = 118
DOT = 40
CURRENT_TIMESTAMP = 95
CREATE_VIEW = 14
INITIALLY = 168
REINDEX = 109
EQUALS2 = 57
PERCENT = 76
AUTOINCREMENT = 160
NOT_EQUALS2 = 59
DEFAULT = 137
VALUES = 136
BEFORE = 177
AFTER = 178
INSTEAD = 179
JOIN = 131
ID_QUOTED_CORE_APOSTROPHE = 230
ID_QUOTED_SQUARE = 231
INDEXED = 41
FLOAT_LITERAL = 18
CREATE_INDEX = 12
QUESTION = 96
ORDERING = 29
IMMEDIATE = 143
DESC = 113
DROP_TABLE = 17
ID_START = 225


class SQLiteLexer(Lexer):
    grammarFileName = "SQLite.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(SQLiteLexer, self).__init__(input, state)

        self.dfa19 = self.DFA19(
            self, 19,
            eot=self.DFA19_eot,
            eof=self.DFA19_eof,
            min=self.DFA19_min,
            max=self.DFA19_max,
            accept=self.DFA19_accept,
            special=self.DFA19_special,
            transition=self.DFA19_transition
        )

        self.dfa26 = self.DFA26(
            self, 26,
            eot=self.DFA26_eot,
            eof=self.DFA26_eof,
            min=self.DFA26_min,
            max=self.DFA26_max,
            accept=self.DFA26_accept,
            special=self.DFA26_special,
            transition=self.DFA26_transition
        )


    """public void displayRecognitionError(String[] tokenNames, RecognitionException e) {
         final StringBuilder buffer = new StringBuilder();
         buffer.append("[").append(getErrorHeader(e)).append("] ");
         buffer.append(getErrorMessage(e, tokenNames));
         if(e.input!=null && e.input instanceof CharStream) {
            final CharStream stream = (CharStream) e.input;
              int size = stream.size();
              if(size>0) {
                 buffer.append("\n").append(stream.substring(0, size-1));
              }
           }
         throw new SqlJetParserException(buffer.toString(), e);
    }"""




    # $ANTLR start "EQUALS"
    def mEQUALS(self, ):

        try:
            _type = EQUALS
            _channel = DEFAULT_CHANNEL

            # SQLite.g:759:7: ( '=' )
            # SQLite.g:759:16: '='
            pass
            self.match(61)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUALS"



    # $ANTLR start "EQUALS2"
    def mEQUALS2(self, ):

        try:
            _type = EQUALS2
            _channel = DEFAULT_CHANNEL

            # SQLite.g:760:8: ( '==' )
            # SQLite.g:760:16: '=='
            pass
            self.match("==")

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUALS2"



    # $ANTLR start "NOT_EQUALS"
    def mNOT_EQUALS(self, ):

        try:
            _type = NOT_EQUALS
            _channel = DEFAULT_CHANNEL

            # SQLite.g:761:11: ( '!=' )
            # SQLite.g:761:16: '!='
            pass
            self.match("!=")

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT_EQUALS"



    # $ANTLR start "NOT_EQUALS2"
    def mNOT_EQUALS2(self, ):

        try:
            _type = NOT_EQUALS2
            _channel = DEFAULT_CHANNEL

            # SQLite.g:762:12: ( '<>' )
            # SQLite.g:762:16: '<>'
            pass
            self.match("<>")

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT_EQUALS2"



    # $ANTLR start "LESS"
    def mLESS(self, ):

        try:
            _type = LESS
            _channel = DEFAULT_CHANNEL

            # SQLite.g:763:5: ( '<' )
            # SQLite.g:763:16: '<'
            pass
            self.match(60)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LESS"



    # $ANTLR start "LESS_OR_EQ"
    def mLESS_OR_EQ(self, ):

        try:
            _type = LESS_OR_EQ
            _channel = DEFAULT_CHANNEL

            # SQLite.g:764:11: ( '<=' )
            # SQLite.g:764:16: '<='
            pass
            self.match("<=")

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LESS_OR_EQ"



    # $ANTLR start "GREATER"
    def mGREATER(self, ):

        try:
            _type = GREATER
            _channel = DEFAULT_CHANNEL

            # SQLite.g:765:8: ( '>' )
            # SQLite.g:765:16: '>'
            pass
            self.match(62)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GREATER"



    # $ANTLR start "GREATER_OR_EQ"
    def mGREATER_OR_EQ(self, ):

        try:
            _type = GREATER_OR_EQ
            _channel = DEFAULT_CHANNEL

            # SQLite.g:766:14: ( '>=' )
            # SQLite.g:766:16: '>='
            pass
            self.match(">=")

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GREATER_OR_EQ"



    # $ANTLR start "SHIFT_LEFT"
    def mSHIFT_LEFT(self, ):

        try:
            _type = SHIFT_LEFT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:767:11: ( '<<' )
            # SQLite.g:767:16: '<<'
            pass
            self.match("<<")

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SHIFT_LEFT"



    # $ANTLR start "SHIFT_RIGHT"
    def mSHIFT_RIGHT(self, ):

        try:
            _type = SHIFT_RIGHT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:768:12: ( '>>' )
            # SQLite.g:768:16: '>>'
            pass
            self.match(">>")

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SHIFT_RIGHT"



    # $ANTLR start "AMPERSAND"
    def mAMPERSAND(self, ):

        try:
            _type = AMPERSAND
            _channel = DEFAULT_CHANNEL

            # SQLite.g:769:10: ( '&' )
            # SQLite.g:769:16: '&'
            pass
            self.match(38)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AMPERSAND"



    # $ANTLR start "PIPE"
    def mPIPE(self, ):

        try:
            _type = PIPE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:770:5: ( '|' )
            # SQLite.g:770:16: '|'
            pass
            self.match(124)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PIPE"



    # $ANTLR start "DOUBLE_PIPE"
    def mDOUBLE_PIPE(self, ):

        try:
            _type = DOUBLE_PIPE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:771:12: ( '||' )
            # SQLite.g:771:16: '||'
            pass
            self.match("||")

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLE_PIPE"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # SQLite.g:772:5: ( '+' )
            # SQLite.g:772:16: '+'
            pass
            self.match(43)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # SQLite.g:773:6: ( '-' )
            # SQLite.g:773:16: '-'
            pass
            self.match(45)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "TILDA"
    def mTILDA(self, ):

        try:
            _type = TILDA
            _channel = DEFAULT_CHANNEL

            # SQLite.g:774:6: ( '~' )
            # SQLite.g:774:16: '~'
            pass
            self.match(126)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TILDA"



    # $ANTLR start "ASTERISK"
    def mASTERISK(self, ):

        try:
            _type = ASTERISK
            _channel = DEFAULT_CHANNEL

            # SQLite.g:775:9: ( '*' )
            # SQLite.g:775:16: '*'
            pass
            self.match(42)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASTERISK"



    # $ANTLR start "SLASH"
    def mSLASH(self, ):

        try:
            _type = SLASH
            _channel = DEFAULT_CHANNEL

            # SQLite.g:776:6: ( '/' )
            # SQLite.g:776:16: '/'
            pass
            self.match(47)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SLASH"



    # $ANTLR start "BACKSLASH"
    def mBACKSLASH(self, ):

        try:
            _type = BACKSLASH
            _channel = DEFAULT_CHANNEL

            # SQLite.g:777:10: ( '\\\\' )
            # SQLite.g:777:16: '\\\\'
            pass
            self.match(92)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BACKSLASH"



    # $ANTLR start "PERCENT"
    def mPERCENT(self, ):

        try:
            _type = PERCENT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:778:8: ( '%' )
            # SQLite.g:778:16: '%'
            pass
            self.match(37)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PERCENT"



    # $ANTLR start "SEMI"
    def mSEMI(self, ):

        try:
            _type = SEMI
            _channel = DEFAULT_CHANNEL

            # SQLite.g:779:5: ( ';' )
            # SQLite.g:779:16: ';'
            pass
            self.match(59)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEMI"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:780:4: ( '.' )
            # SQLite.g:780:16: '.'
            pass
            self.match(46)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # SQLite.g:781:6: ( ',' )
            # SQLite.g:781:16: ','
            pass
            self.match(44)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):

        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:782:7: ( '(' )
            # SQLite.g:782:16: '('
            pass
            self.match(40)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):

        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:783:7: ( ')' )
            # SQLite.g:783:16: ')'
            pass
            self.match(41)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "QUESTION"
    def mQUESTION(self, ):

        try:
            _type = QUESTION
            _channel = DEFAULT_CHANNEL

            # SQLite.g:784:9: ( '?' )
            # SQLite.g:784:16: '?'
            pass
            self.match(63)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "QUESTION"



    # $ANTLR start "COLON"
    def mCOLON(self, ):

        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # SQLite.g:785:6: ( ':' )
            # SQLite.g:785:16: ':'
            pass
            self.match(58)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "AT"
    def mAT(self, ):

        try:
            _type = AT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:786:3: ( '@' )
            # SQLite.g:786:16: '@'
            pass
            self.match(64)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AT"



    # $ANTLR start "DOLLAR"
    def mDOLLAR(self, ):

        try:
            _type = DOLLAR
            _channel = DEFAULT_CHANNEL

            # SQLite.g:787:7: ( '$' )
            # SQLite.g:787:16: '$'
            pass
            self.match(36)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOLLAR"



    # $ANTLR start "QUOTE_DOUBLE"
    def mQUOTE_DOUBLE(self, ):

        try:
            _type = QUOTE_DOUBLE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:788:13: ( '\"' )
            # SQLite.g:788:16: '\"'
            pass
            self.match(34)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "QUOTE_DOUBLE"



    # $ANTLR start "QUOTE_SINGLE"
    def mQUOTE_SINGLE(self, ):

        try:
            _type = QUOTE_SINGLE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:789:13: ( '\\'' )
            # SQLite.g:789:16: '\\''
            pass
            self.match(39)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "QUOTE_SINGLE"



    # $ANTLR start "APOSTROPHE"
    def mAPOSTROPHE(self, ):

        try:
            _type = APOSTROPHE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:790:11: ( '`' )
            # SQLite.g:790:16: '`'
            pass
            self.match(96)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "APOSTROPHE"



    # $ANTLR start "LPAREN_SQUARE"
    def mLPAREN_SQUARE(self, ):

        try:
            _type = LPAREN_SQUARE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:791:14: ( '[' )
            # SQLite.g:791:16: '['
            pass
            self.match(91)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LPAREN_SQUARE"



    # $ANTLR start "RPAREN_SQUARE"
    def mRPAREN_SQUARE(self, ):

        try:
            _type = RPAREN_SQUARE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:792:14: ( ']' )
            # SQLite.g:792:16: ']'
            pass
            self.match(93)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RPAREN_SQUARE"



    # $ANTLR start "UNDERSCORE"
    def mUNDERSCORE(self, ):

        try:
            _type = UNDERSCORE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:793:11: ( '_' )
            # SQLite.g:793:16: '_'
            pass
            self.match(95)

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNDERSCORE"



    # $ANTLR start "A"
    def mA(self, ):

        try:
            # SQLite.g:796:11: ( ( 'a' | 'A' ) )
            # SQLite.g:796:12: ( 'a' | 'A' )
            pass
            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "A"



    # $ANTLR start "B"
    def mB(self, ):

        try:
            # SQLite.g:797:11: ( ( 'b' | 'B' ) )
            # SQLite.g:797:12: ( 'b' | 'B' )
            pass
            if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "B"



    # $ANTLR start "C"
    def mC(self, ):

        try:
            # SQLite.g:798:11: ( ( 'c' | 'C' ) )
            # SQLite.g:798:12: ( 'c' | 'C' )
            pass
            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "C"



    # $ANTLR start "D"
    def mD(self, ):

        try:
            # SQLite.g:799:11: ( ( 'd' | 'D' ) )
            # SQLite.g:799:12: ( 'd' | 'D' )
            pass
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "D"



    # $ANTLR start "E"
    def mE(self, ):

        try:
            # SQLite.g:800:11: ( ( 'e' | 'E' ) )
            # SQLite.g:800:12: ( 'e' | 'E' )
            pass
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "E"



    # $ANTLR start "F"
    def mF(self, ):

        try:
            # SQLite.g:801:11: ( ( 'f' | 'F' ) )
            # SQLite.g:801:12: ( 'f' | 'F' )
            pass
            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "F"



    # $ANTLR start "G"
    def mG(self, ):

        try:
            # SQLite.g:802:11: ( ( 'g' | 'G' ) )
            # SQLite.g:802:12: ( 'g' | 'G' )
            pass
            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "G"



    # $ANTLR start "H"
    def mH(self, ):

        try:
            # SQLite.g:803:11: ( ( 'h' | 'H' ) )
            # SQLite.g:803:12: ( 'h' | 'H' )
            pass
            if self.input.LA(1) == 72 or self.input.LA(1) == 104:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "H"



    # $ANTLR start "I"
    def mI(self, ):

        try:
            # SQLite.g:804:11: ( ( 'i' | 'I' ) )
            # SQLite.g:804:12: ( 'i' | 'I' )
            pass
            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "I"



    # $ANTLR start "J"
    def mJ(self, ):

        try:
            # SQLite.g:805:11: ( ( 'j' | 'J' ) )
            # SQLite.g:805:12: ( 'j' | 'J' )
            pass
            if self.input.LA(1) == 74 or self.input.LA(1) == 106:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "J"



    # $ANTLR start "K"
    def mK(self, ):

        try:
            # SQLite.g:806:11: ( ( 'k' | 'K' ) )
            # SQLite.g:806:12: ( 'k' | 'K' )
            pass
            if self.input.LA(1) == 75 or self.input.LA(1) == 107:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "K"



    # $ANTLR start "L"
    def mL(self, ):

        try:
            # SQLite.g:807:11: ( ( 'l' | 'L' ) )
            # SQLite.g:807:12: ( 'l' | 'L' )
            pass
            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "L"



    # $ANTLR start "M"
    def mM(self, ):

        try:
            # SQLite.g:808:11: ( ( 'm' | 'M' ) )
            # SQLite.g:808:12: ( 'm' | 'M' )
            pass
            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "M"



    # $ANTLR start "N"
    def mN(self, ):

        try:
            # SQLite.g:809:11: ( ( 'n' | 'N' ) )
            # SQLite.g:809:12: ( 'n' | 'N' )
            pass
            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "N"



    # $ANTLR start "O"
    def mO(self, ):

        try:
            # SQLite.g:810:11: ( ( 'o' | 'O' ) )
            # SQLite.g:810:12: ( 'o' | 'O' )
            pass
            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "O"



    # $ANTLR start "P"
    def mP(self, ):

        try:
            # SQLite.g:811:11: ( ( 'p' | 'P' ) )
            # SQLite.g:811:12: ( 'p' | 'P' )
            pass
            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "P"



    # $ANTLR start "Q"
    def mQ(self, ):

        try:
            # SQLite.g:812:11: ( ( 'q' | 'Q' ) )
            # SQLite.g:812:12: ( 'q' | 'Q' )
            pass
            if self.input.LA(1) == 81 or self.input.LA(1) == 113:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "Q"



    # $ANTLR start "R"
    def mR(self, ):

        try:
            # SQLite.g:813:11: ( ( 'r' | 'R' ) )
            # SQLite.g:813:12: ( 'r' | 'R' )
            pass
            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "R"



    # $ANTLR start "S"
    def mS(self, ):

        try:
            # SQLite.g:814:11: ( ( 's' | 'S' ) )
            # SQLite.g:814:12: ( 's' | 'S' )
            pass
            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "S"



    # $ANTLR start "T"
    def mT(self, ):

        try:
            # SQLite.g:815:11: ( ( 't' | 'T' ) )
            # SQLite.g:815:12: ( 't' | 'T' )
            pass
            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "T"



    # $ANTLR start "U"
    def mU(self, ):

        try:
            # SQLite.g:816:11: ( ( 'u' | 'U' ) )
            # SQLite.g:816:12: ( 'u' | 'U' )
            pass
            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "U"



    # $ANTLR start "V"
    def mV(self, ):

        try:
            # SQLite.g:817:11: ( ( 'v' | 'V' ) )
            # SQLite.g:817:12: ( 'v' | 'V' )
            pass
            if self.input.LA(1) == 86 or self.input.LA(1) == 118:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "V"



    # $ANTLR start "W"
    def mW(self, ):

        try:
            # SQLite.g:818:11: ( ( 'w' | 'W' ) )
            # SQLite.g:818:12: ( 'w' | 'W' )
            pass
            if self.input.LA(1) == 87 or self.input.LA(1) == 119:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "W"



    # $ANTLR start "X"
    def mX(self, ):

        try:
            # SQLite.g:819:11: ( ( 'x' | 'X' ) )
            # SQLite.g:819:12: ( 'x' | 'X' )
            pass
            if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "X"



    # $ANTLR start "Y"
    def mY(self, ):

        try:
            # SQLite.g:820:11: ( ( 'y' | 'Y' ) )
            # SQLite.g:820:12: ( 'y' | 'Y' )
            pass
            if self.input.LA(1) == 89 or self.input.LA(1) == 121:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "Y"



    # $ANTLR start "Z"
    def mZ(self, ):

        try:
            # SQLite.g:821:11: ( ( 'z' | 'Z' ) )
            # SQLite.g:821:12: ( 'z' | 'Z' )
            pass
            if self.input.LA(1) == 90 or self.input.LA(1) == 122:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "Z"



    # $ANTLR start "ABORT"
    def mABORT(self, ):

        try:
            _type = ABORT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:823:6: ( A B O R T )
            # SQLite.g:823:8: A B O R T
            pass
            self.mA()
            self.mB()
            self.mO()
            self.mR()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ABORT"



    # $ANTLR start "ADD"
    def mADD(self, ):

        try:
            _type = ADD
            _channel = DEFAULT_CHANNEL

            # SQLite.g:824:4: ( A D D )
            # SQLite.g:824:6: A D D
            pass
            self.mA()
            self.mD()
            self.mD()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ADD"



    # $ANTLR start "AFTER"
    def mAFTER(self, ):

        try:
            _type = AFTER
            _channel = DEFAULT_CHANNEL

            # SQLite.g:825:6: ( A F T E R )
            # SQLite.g:825:8: A F T E R
            pass
            self.mA()
            self.mF()
            self.mT()
            self.mE()
            self.mR()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AFTER"



    # $ANTLR start "ALL"
    def mALL(self, ):

        try:
            _type = ALL
            _channel = DEFAULT_CHANNEL

            # SQLite.g:826:4: ( A L L )
            # SQLite.g:826:6: A L L
            pass
            self.mA()
            self.mL()
            self.mL()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ALL"



    # $ANTLR start "ALTER"
    def mALTER(self, ):

        try:
            _type = ALTER
            _channel = DEFAULT_CHANNEL

            # SQLite.g:827:6: ( A L T E R )
            # SQLite.g:827:8: A L T E R
            pass
            self.mA()
            self.mL()
            self.mT()
            self.mE()
            self.mR()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ALTER"



    # $ANTLR start "ANALYZE"
    def mANALYZE(self, ):

        try:
            _type = ANALYZE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:828:8: ( A N A L Y Z E )
            # SQLite.g:828:10: A N A L Y Z E
            pass
            self.mA()
            self.mN()
            self.mA()
            self.mL()
            self.mY()
            self.mZ()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ANALYZE"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # SQLite.g:829:4: ( A N D )
            # SQLite.g:829:6: A N D
            pass
            self.mA()
            self.mN()
            self.mD()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "AS"
    def mAS(self, ):

        try:
            _type = AS
            _channel = DEFAULT_CHANNEL

            # SQLite.g:830:3: ( A S )
            # SQLite.g:830:5: A S
            pass
            self.mA()
            self.mS()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AS"



    # $ANTLR start "ASC"
    def mASC(self, ):

        try:
            _type = ASC
            _channel = DEFAULT_CHANNEL

            # SQLite.g:831:4: ( A S C )
            # SQLite.g:831:6: A S C
            pass
            self.mA()
            self.mS()
            self.mC()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASC"



    # $ANTLR start "ATTACH"
    def mATTACH(self, ):

        try:
            _type = ATTACH
            _channel = DEFAULT_CHANNEL

            # SQLite.g:832:7: ( A T T A C H )
            # SQLite.g:832:9: A T T A C H
            pass
            self.mA()
            self.mT()
            self.mT()
            self.mA()
            self.mC()
            self.mH()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ATTACH"



    # $ANTLR start "AUTOINCREMENT"
    def mAUTOINCREMENT(self, ):

        try:
            _type = AUTOINCREMENT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:833:14: ( A U T O I N C R E M E N T )
            # SQLite.g:833:16: A U T O I N C R E M E N T
            pass
            self.mA()
            self.mU()
            self.mT()
            self.mO()
            self.mI()
            self.mN()
            self.mC()
            self.mR()
            self.mE()
            self.mM()
            self.mE()
            self.mN()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AUTOINCREMENT"



    # $ANTLR start "BEFORE"
    def mBEFORE(self, ):

        try:
            _type = BEFORE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:834:7: ( B E F O R E )
            # SQLite.g:834:9: B E F O R E
            pass
            self.mB()
            self.mE()
            self.mF()
            self.mO()
            self.mR()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BEFORE"



    # $ANTLR start "BEGIN"
    def mBEGIN(self, ):

        try:
            _type = BEGIN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:835:6: ( B E G I N )
            # SQLite.g:835:8: B E G I N
            pass
            self.mB()
            self.mE()
            self.mG()
            self.mI()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BEGIN"



    # $ANTLR start "BETWEEN"
    def mBETWEEN(self, ):

        try:
            _type = BETWEEN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:836:8: ( B E T W E E N )
            # SQLite.g:836:10: B E T W E E N
            pass
            self.mB()
            self.mE()
            self.mT()
            self.mW()
            self.mE()
            self.mE()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BETWEEN"



    # $ANTLR start "BY"
    def mBY(self, ):

        try:
            _type = BY
            _channel = DEFAULT_CHANNEL

            # SQLite.g:837:3: ( B Y )
            # SQLite.g:837:5: B Y
            pass
            self.mB()
            self.mY()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BY"



    # $ANTLR start "CASCADE"
    def mCASCADE(self, ):

        try:
            _type = CASCADE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:838:8: ( C A S C A D E )
            # SQLite.g:838:10: C A S C A D E
            pass
            self.mC()
            self.mA()
            self.mS()
            self.mC()
            self.mA()
            self.mD()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CASCADE"



    # $ANTLR start "CASE"
    def mCASE(self, ):

        try:
            _type = CASE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:839:5: ( C A S E )
            # SQLite.g:839:7: C A S E
            pass
            self.mC()
            self.mA()
            self.mS()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CASE"



    # $ANTLR start "CAST"
    def mCAST(self, ):

        try:
            _type = CAST
            _channel = DEFAULT_CHANNEL

            # SQLite.g:840:5: ( C A S T )
            # SQLite.g:840:7: C A S T
            pass
            self.mC()
            self.mA()
            self.mS()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CAST"



    # $ANTLR start "CHECK"
    def mCHECK(self, ):

        try:
            _type = CHECK
            _channel = DEFAULT_CHANNEL

            # SQLite.g:841:6: ( C H E C K )
            # SQLite.g:841:8: C H E C K
            pass
            self.mC()
            self.mH()
            self.mE()
            self.mC()
            self.mK()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CHECK"



    # $ANTLR start "COLLATE"
    def mCOLLATE(self, ):

        try:
            _type = COLLATE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:842:8: ( C O L L A T E )
            # SQLite.g:842:10: C O L L A T E
            pass
            self.mC()
            self.mO()
            self.mL()
            self.mL()
            self.mA()
            self.mT()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLLATE"



    # $ANTLR start "COLUMN"
    def mCOLUMN(self, ):

        try:
            _type = COLUMN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:843:7: ( C O L U M N )
            # SQLite.g:843:9: C O L U M N
            pass
            self.mC()
            self.mO()
            self.mL()
            self.mU()
            self.mM()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLUMN"



    # $ANTLR start "COMMIT"
    def mCOMMIT(self, ):

        try:
            _type = COMMIT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:844:7: ( C O M M I T )
            # SQLite.g:844:9: C O M M I T
            pass
            self.mC()
            self.mO()
            self.mM()
            self.mM()
            self.mI()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMIT"



    # $ANTLR start "CONFLICT"
    def mCONFLICT(self, ):

        try:
            _type = CONFLICT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:845:9: ( C O N F L I C T )
            # SQLite.g:845:11: C O N F L I C T
            pass
            self.mC()
            self.mO()
            self.mN()
            self.mF()
            self.mL()
            self.mI()
            self.mC()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CONFLICT"



    # $ANTLR start "CONSTRAINT"
    def mCONSTRAINT(self, ):

        try:
            _type = CONSTRAINT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:846:11: ( C O N S T R A I N T )
            # SQLite.g:846:13: C O N S T R A I N T
            pass
            self.mC()
            self.mO()
            self.mN()
            self.mS()
            self.mT()
            self.mR()
            self.mA()
            self.mI()
            self.mN()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CONSTRAINT"



    # $ANTLR start "CREATE"
    def mCREATE(self, ):

        try:
            _type = CREATE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:847:7: ( C R E A T E )
            # SQLite.g:847:9: C R E A T E
            pass
            self.mC()
            self.mR()
            self.mE()
            self.mA()
            self.mT()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CREATE"



    # $ANTLR start "CROSS"
    def mCROSS(self, ):

        try:
            _type = CROSS
            _channel = DEFAULT_CHANNEL

            # SQLite.g:848:6: ( C R O S S )
            # SQLite.g:848:8: C R O S S
            pass
            self.mC()
            self.mR()
            self.mO()
            self.mS()
            self.mS()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CROSS"



    # $ANTLR start "CURRENT_TIME"
    def mCURRENT_TIME(self, ):

        try:
            _type = CURRENT_TIME
            _channel = DEFAULT_CHANNEL

            # SQLite.g:849:13: ( C U R R E N T '_' T I M E )
            # SQLite.g:849:15: C U R R E N T '_' T I M E
            pass
            self.mC()
            self.mU()
            self.mR()
            self.mR()
            self.mE()
            self.mN()
            self.mT()
            self.match(95)
            self.mT()
            self.mI()
            self.mM()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CURRENT_TIME"



    # $ANTLR start "CURRENT_DATE"
    def mCURRENT_DATE(self, ):

        try:
            _type = CURRENT_DATE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:850:13: ( C U R R E N T '_' D A T E )
            # SQLite.g:850:15: C U R R E N T '_' D A T E
            pass
            self.mC()
            self.mU()
            self.mR()
            self.mR()
            self.mE()
            self.mN()
            self.mT()
            self.match(95)
            self.mD()
            self.mA()
            self.mT()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CURRENT_DATE"



    # $ANTLR start "CURRENT_TIMESTAMP"
    def mCURRENT_TIMESTAMP(self, ):

        try:
            _type = CURRENT_TIMESTAMP
            _channel = DEFAULT_CHANNEL

            # SQLite.g:851:18: ( C U R R E N T '_' T I M E S T A M P )
            # SQLite.g:851:20: C U R R E N T '_' T I M E S T A M P
            pass
            self.mC()
            self.mU()
            self.mR()
            self.mR()
            self.mE()
            self.mN()
            self.mT()
            self.match(95)
            self.mT()
            self.mI()
            self.mM()
            self.mE()
            self.mS()
            self.mT()
            self.mA()
            self.mM()
            self.mP()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CURRENT_TIMESTAMP"



    # $ANTLR start "DATABASE"
    def mDATABASE(self, ):

        try:
            _type = DATABASE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:852:9: ( D A T A B A S E )
            # SQLite.g:852:11: D A T A B A S E
            pass
            self.mD()
            self.mA()
            self.mT()
            self.mA()
            self.mB()
            self.mA()
            self.mS()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DATABASE"



    # $ANTLR start "DEFAULT"
    def mDEFAULT(self, ):

        try:
            _type = DEFAULT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:853:8: ( D E F A U L T )
            # SQLite.g:853:10: D E F A U L T
            pass
            self.mD()
            self.mE()
            self.mF()
            self.mA()
            self.mU()
            self.mL()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DEFAULT"



    # $ANTLR start "DEFERRABLE"
    def mDEFERRABLE(self, ):

        try:
            _type = DEFERRABLE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:854:11: ( D E F E R R A B L E )
            # SQLite.g:854:13: D E F E R R A B L E
            pass
            self.mD()
            self.mE()
            self.mF()
            self.mE()
            self.mR()
            self.mR()
            self.mA()
            self.mB()
            self.mL()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DEFERRABLE"



    # $ANTLR start "DEFERRED"
    def mDEFERRED(self, ):

        try:
            _type = DEFERRED
            _channel = DEFAULT_CHANNEL

            # SQLite.g:855:9: ( D E F E R R E D )
            # SQLite.g:855:11: D E F E R R E D
            pass
            self.mD()
            self.mE()
            self.mF()
            self.mE()
            self.mR()
            self.mR()
            self.mE()
            self.mD()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DEFERRED"



    # $ANTLR start "DELETE"
    def mDELETE(self, ):

        try:
            _type = DELETE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:856:7: ( D E L E T E )
            # SQLite.g:856:9: D E L E T E
            pass
            self.mD()
            self.mE()
            self.mL()
            self.mE()
            self.mT()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DELETE"



    # $ANTLR start "DESC"
    def mDESC(self, ):

        try:
            _type = DESC
            _channel = DEFAULT_CHANNEL

            # SQLite.g:857:5: ( D E S C )
            # SQLite.g:857:7: D E S C
            pass
            self.mD()
            self.mE()
            self.mS()
            self.mC()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DESC"



    # $ANTLR start "DETACH"
    def mDETACH(self, ):

        try:
            _type = DETACH
            _channel = DEFAULT_CHANNEL

            # SQLite.g:858:7: ( D E T A C H )
            # SQLite.g:858:9: D E T A C H
            pass
            self.mD()
            self.mE()
            self.mT()
            self.mA()
            self.mC()
            self.mH()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DETACH"



    # $ANTLR start "DISTINCT"
    def mDISTINCT(self, ):

        try:
            _type = DISTINCT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:859:9: ( D I S T I N C T )
            # SQLite.g:859:11: D I S T I N C T
            pass
            self.mD()
            self.mI()
            self.mS()
            self.mT()
            self.mI()
            self.mN()
            self.mC()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DISTINCT"



    # $ANTLR start "DROP"
    def mDROP(self, ):

        try:
            _type = DROP
            _channel = DEFAULT_CHANNEL

            # SQLite.g:860:5: ( D R O P )
            # SQLite.g:860:7: D R O P
            pass
            self.mD()
            self.mR()
            self.mO()
            self.mP()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DROP"



    # $ANTLR start "EACH"
    def mEACH(self, ):

        try:
            _type = EACH
            _channel = DEFAULT_CHANNEL

            # SQLite.g:861:5: ( E A C H )
            # SQLite.g:861:7: E A C H
            pass
            self.mE()
            self.mA()
            self.mC()
            self.mH()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EACH"



    # $ANTLR start "ELSE"
    def mELSE(self, ):

        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:862:5: ( E L S E )
            # SQLite.g:862:7: E L S E
            pass
            self.mE()
            self.mL()
            self.mS()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "END"
    def mEND(self, ):

        try:
            _type = END
            _channel = DEFAULT_CHANNEL

            # SQLite.g:863:4: ( E N D )
            # SQLite.g:863:6: E N D
            pass
            self.mE()
            self.mN()
            self.mD()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "END"



    # $ANTLR start "ESCAPE"
    def mESCAPE(self, ):

        try:
            _type = ESCAPE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:864:7: ( E S C A P E )
            # SQLite.g:864:9: E S C A P E
            pass
            self.mE()
            self.mS()
            self.mC()
            self.mA()
            self.mP()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ESCAPE"



    # $ANTLR start "EXCEPT"
    def mEXCEPT(self, ):

        try:
            _type = EXCEPT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:865:7: ( E X C E P T )
            # SQLite.g:865:9: E X C E P T
            pass
            self.mE()
            self.mX()
            self.mC()
            self.mE()
            self.mP()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXCEPT"



    # $ANTLR start "EXCLUSIVE"
    def mEXCLUSIVE(self, ):

        try:
            _type = EXCLUSIVE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:866:10: ( E X C L U S I V E )
            # SQLite.g:866:12: E X C L U S I V E
            pass
            self.mE()
            self.mX()
            self.mC()
            self.mL()
            self.mU()
            self.mS()
            self.mI()
            self.mV()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXCLUSIVE"



    # $ANTLR start "EXISTS"
    def mEXISTS(self, ):

        try:
            _type = EXISTS
            _channel = DEFAULT_CHANNEL

            # SQLite.g:867:7: ( E X I S T S )
            # SQLite.g:867:9: E X I S T S
            pass
            self.mE()
            self.mX()
            self.mI()
            self.mS()
            self.mT()
            self.mS()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXISTS"



    # $ANTLR start "EXPLAIN"
    def mEXPLAIN(self, ):

        try:
            _type = EXPLAIN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:868:8: ( E X P L A I N )
            # SQLite.g:868:10: E X P L A I N
            pass
            self.mE()
            self.mX()
            self.mP()
            self.mL()
            self.mA()
            self.mI()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXPLAIN"



    # $ANTLR start "FAIL"
    def mFAIL(self, ):

        try:
            _type = FAIL
            _channel = DEFAULT_CHANNEL

            # SQLite.g:869:5: ( F A I L )
            # SQLite.g:869:7: F A I L
            pass
            self.mF()
            self.mA()
            self.mI()
            self.mL()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FAIL"



    # $ANTLR start "FOR"
    def mFOR(self, ):

        try:
            _type = FOR
            _channel = DEFAULT_CHANNEL

            # SQLite.g:870:4: ( F O R )
            # SQLite.g:870:6: F O R
            pass
            self.mF()
            self.mO()
            self.mR()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FOR"



    # $ANTLR start "FOREIGN"
    def mFOREIGN(self, ):

        try:
            _type = FOREIGN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:871:8: ( F O R E I G N )
            # SQLite.g:871:10: F O R E I G N
            pass
            self.mF()
            self.mO()
            self.mR()
            self.mE()
            self.mI()
            self.mG()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FOREIGN"



    # $ANTLR start "FROM"
    def mFROM(self, ):

        try:
            _type = FROM
            _channel = DEFAULT_CHANNEL

            # SQLite.g:872:5: ( F R O M )
            # SQLite.g:872:7: F R O M
            pass
            self.mF()
            self.mR()
            self.mO()
            self.mM()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FROM"



    # $ANTLR start "GLOB"
    def mGLOB(self, ):

        try:
            _type = GLOB
            _channel = DEFAULT_CHANNEL

            # SQLite.g:873:5: ( G L O B )
            # SQLite.g:873:7: G L O B
            pass
            self.mG()
            self.mL()
            self.mO()
            self.mB()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOB"



    # $ANTLR start "GROUP"
    def mGROUP(self, ):

        try:
            _type = GROUP
            _channel = DEFAULT_CHANNEL

            # SQLite.g:874:6: ( G R O U P )
            # SQLite.g:874:8: G R O U P
            pass
            self.mG()
            self.mR()
            self.mO()
            self.mU()
            self.mP()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GROUP"



    # $ANTLR start "HAVING"
    def mHAVING(self, ):

        try:
            _type = HAVING
            _channel = DEFAULT_CHANNEL

            # SQLite.g:875:7: ( H A V I N G )
            # SQLite.g:875:9: H A V I N G
            pass
            self.mH()
            self.mA()
            self.mV()
            self.mI()
            self.mN()
            self.mG()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HAVING"



    # $ANTLR start "IF"
    def mIF(self, ):

        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # SQLite.g:876:3: ( I F )
            # SQLite.g:876:5: I F
            pass
            self.mI()
            self.mF()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IF"



    # $ANTLR start "IGNORE"
    def mIGNORE(self, ):

        try:
            _type = IGNORE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:877:7: ( I G N O R E )
            # SQLite.g:877:9: I G N O R E
            pass
            self.mI()
            self.mG()
            self.mN()
            self.mO()
            self.mR()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IGNORE"



    # $ANTLR start "IMMEDIATE"
    def mIMMEDIATE(self, ):

        try:
            _type = IMMEDIATE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:878:10: ( I M M E D I A T E )
            # SQLite.g:878:12: I M M E D I A T E
            pass
            self.mI()
            self.mM()
            self.mM()
            self.mE()
            self.mD()
            self.mI()
            self.mA()
            self.mT()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IMMEDIATE"



    # $ANTLR start "IN"
    def mIN(self, ):

        try:
            _type = IN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:879:3: ( I N )
            # SQLite.g:879:5: I N
            pass
            self.mI()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IN"



    # $ANTLR start "INDEX"
    def mINDEX(self, ):

        try:
            _type = INDEX
            _channel = DEFAULT_CHANNEL

            # SQLite.g:880:6: ( I N D E X )
            # SQLite.g:880:8: I N D E X
            pass
            self.mI()
            self.mN()
            self.mD()
            self.mE()
            self.mX()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INDEX"



    # $ANTLR start "INDEXED"
    def mINDEXED(self, ):

        try:
            _type = INDEXED
            _channel = DEFAULT_CHANNEL

            # SQLite.g:881:8: ( I N D E X E D )
            # SQLite.g:881:10: I N D E X E D
            pass
            self.mI()
            self.mN()
            self.mD()
            self.mE()
            self.mX()
            self.mE()
            self.mD()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INDEXED"



    # $ANTLR start "INITIALLY"
    def mINITIALLY(self, ):

        try:
            _type = INITIALLY
            _channel = DEFAULT_CHANNEL

            # SQLite.g:882:10: ( I N I T I A L L Y )
            # SQLite.g:882:12: I N I T I A L L Y
            pass
            self.mI()
            self.mN()
            self.mI()
            self.mT()
            self.mI()
            self.mA()
            self.mL()
            self.mL()
            self.mY()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INITIALLY"



    # $ANTLR start "INNER"
    def mINNER(self, ):

        try:
            _type = INNER
            _channel = DEFAULT_CHANNEL

            # SQLite.g:883:6: ( I N N E R )
            # SQLite.g:883:8: I N N E R
            pass
            self.mI()
            self.mN()
            self.mN()
            self.mE()
            self.mR()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INNER"



    # $ANTLR start "INSERT"
    def mINSERT(self, ):

        try:
            _type = INSERT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:884:7: ( I N S E R T )
            # SQLite.g:884:9: I N S E R T
            pass
            self.mI()
            self.mN()
            self.mS()
            self.mE()
            self.mR()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INSERT"



    # $ANTLR start "INSTEAD"
    def mINSTEAD(self, ):

        try:
            _type = INSTEAD
            _channel = DEFAULT_CHANNEL

            # SQLite.g:885:8: ( I N S T E A D )
            # SQLite.g:885:10: I N S T E A D
            pass
            self.mI()
            self.mN()
            self.mS()
            self.mT()
            self.mE()
            self.mA()
            self.mD()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INSTEAD"



    # $ANTLR start "INTERSECT"
    def mINTERSECT(self, ):

        try:
            _type = INTERSECT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:886:10: ( I N T E R S E C T )
            # SQLite.g:886:12: I N T E R S E C T
            pass
            self.mI()
            self.mN()
            self.mT()
            self.mE()
            self.mR()
            self.mS()
            self.mE()
            self.mC()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTERSECT"



    # $ANTLR start "INTO"
    def mINTO(self, ):

        try:
            _type = INTO
            _channel = DEFAULT_CHANNEL

            # SQLite.g:887:5: ( I N T O )
            # SQLite.g:887:7: I N T O
            pass
            self.mI()
            self.mN()
            self.mT()
            self.mO()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTO"



    # $ANTLR start "IS"
    def mIS(self, ):

        try:
            _type = IS
            _channel = DEFAULT_CHANNEL

            # SQLite.g:888:3: ( I S )
            # SQLite.g:888:5: I S
            pass
            self.mI()
            self.mS()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IS"



    # $ANTLR start "ISNULL"
    def mISNULL(self, ):

        try:
            _type = ISNULL
            _channel = DEFAULT_CHANNEL

            # SQLite.g:889:7: ( I S N U L L )
            # SQLite.g:889:9: I S N U L L
            pass
            self.mI()
            self.mS()
            self.mN()
            self.mU()
            self.mL()
            self.mL()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ISNULL"



    # $ANTLR start "JOIN"
    def mJOIN(self, ):

        try:
            _type = JOIN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:890:5: ( J O I N )
            # SQLite.g:890:7: J O I N
            pass
            self.mJ()
            self.mO()
            self.mI()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "JOIN"



    # $ANTLR start "KEY"
    def mKEY(self, ):

        try:
            _type = KEY
            _channel = DEFAULT_CHANNEL

            # SQLite.g:891:4: ( K E Y )
            # SQLite.g:891:6: K E Y
            pass
            self.mK()
            self.mE()
            self.mY()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "KEY"



    # $ANTLR start "LEFT"
    def mLEFT(self, ):

        try:
            _type = LEFT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:892:5: ( L E F T )
            # SQLite.g:892:7: L E F T
            pass
            self.mL()
            self.mE()
            self.mF()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEFT"



    # $ANTLR start "LIKE"
    def mLIKE(self, ):

        try:
            _type = LIKE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:893:5: ( L I K E )
            # SQLite.g:893:7: L I K E
            pass
            self.mL()
            self.mI()
            self.mK()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LIKE"



    # $ANTLR start "LIMIT"
    def mLIMIT(self, ):

        try:
            _type = LIMIT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:894:6: ( L I M I T )
            # SQLite.g:894:8: L I M I T
            pass
            self.mL()
            self.mI()
            self.mM()
            self.mI()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LIMIT"



    # $ANTLR start "MATCH"
    def mMATCH(self, ):

        try:
            _type = MATCH
            _channel = DEFAULT_CHANNEL

            # SQLite.g:895:6: ( M A T C H )
            # SQLite.g:895:8: M A T C H
            pass
            self.mM()
            self.mA()
            self.mT()
            self.mC()
            self.mH()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MATCH"



    # $ANTLR start "NATURAL"
    def mNATURAL(self, ):

        try:
            _type = NATURAL
            _channel = DEFAULT_CHANNEL

            # SQLite.g:896:8: ( N A T U R A L )
            # SQLite.g:896:10: N A T U R A L
            pass
            self.mN()
            self.mA()
            self.mT()
            self.mU()
            self.mR()
            self.mA()
            self.mL()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NATURAL"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:897:4: ( N O T )
            # SQLite.g:897:6: N O T
            pass
            self.mN()
            self.mO()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "NOTNULL"
    def mNOTNULL(self, ):

        try:
            _type = NOTNULL
            _channel = DEFAULT_CHANNEL

            # SQLite.g:898:8: ( N O T N U L L )
            # SQLite.g:898:10: N O T N U L L
            pass
            self.mN()
            self.mO()
            self.mT()
            self.mN()
            self.mU()
            self.mL()
            self.mL()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOTNULL"



    # $ANTLR start "NULL"
    def mNULL(self, ):

        try:
            _type = NULL
            _channel = DEFAULT_CHANNEL

            # SQLite.g:899:5: ( N U L L )
            # SQLite.g:899:7: N U L L
            pass
            self.mN()
            self.mU()
            self.mL()
            self.mL()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NULL"



    # $ANTLR start "OF"
    def mOF(self, ):

        try:
            _type = OF
            _channel = DEFAULT_CHANNEL

            # SQLite.g:900:3: ( O F )
            # SQLite.g:900:5: O F
            pass
            self.mO()
            self.mF()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OF"



    # $ANTLR start "OFFSET"
    def mOFFSET(self, ):

        try:
            _type = OFFSET
            _channel = DEFAULT_CHANNEL

            # SQLite.g:901:7: ( O F F S E T )
            # SQLite.g:901:9: O F F S E T
            pass
            self.mO()
            self.mF()
            self.mF()
            self.mS()
            self.mE()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OFFSET"



    # $ANTLR start "ON"
    def mON(self, ):

        try:
            _type = ON
            _channel = DEFAULT_CHANNEL

            # SQLite.g:902:3: ( O N )
            # SQLite.g:902:5: O N
            pass
            self.mO()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ON"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # SQLite.g:903:3: ( O R )
            # SQLite.g:903:5: O R
            pass
            self.mO()
            self.mR()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "ORDER"
    def mORDER(self, ):

        try:
            _type = ORDER
            _channel = DEFAULT_CHANNEL

            # SQLite.g:904:6: ( O R D E R )
            # SQLite.g:904:8: O R D E R
            pass
            self.mO()
            self.mR()
            self.mD()
            self.mE()
            self.mR()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ORDER"



    # $ANTLR start "OUTER"
    def mOUTER(self, ):

        try:
            _type = OUTER
            _channel = DEFAULT_CHANNEL

            # SQLite.g:905:6: ( O U T E R )
            # SQLite.g:905:8: O U T E R
            pass
            self.mO()
            self.mU()
            self.mT()
            self.mE()
            self.mR()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OUTER"



    # $ANTLR start "PLAN"
    def mPLAN(self, ):

        try:
            _type = PLAN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:906:5: ( P L A N )
            # SQLite.g:906:7: P L A N
            pass
            self.mP()
            self.mL()
            self.mA()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLAN"



    # $ANTLR start "PRAGMA"
    def mPRAGMA(self, ):

        try:
            _type = PRAGMA
            _channel = DEFAULT_CHANNEL

            # SQLite.g:907:7: ( P R A G M A )
            # SQLite.g:907:9: P R A G M A
            pass
            self.mP()
            self.mR()
            self.mA()
            self.mG()
            self.mM()
            self.mA()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PRAGMA"



    # $ANTLR start "PRIMARY"
    def mPRIMARY(self, ):

        try:
            _type = PRIMARY
            _channel = DEFAULT_CHANNEL

            # SQLite.g:908:8: ( P R I M A R Y )
            # SQLite.g:908:10: P R I M A R Y
            pass
            self.mP()
            self.mR()
            self.mI()
            self.mM()
            self.mA()
            self.mR()
            self.mY()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PRIMARY"



    # $ANTLR start "QUERY"
    def mQUERY(self, ):

        try:
            _type = QUERY
            _channel = DEFAULT_CHANNEL

            # SQLite.g:909:6: ( Q U E R Y )
            # SQLite.g:909:8: Q U E R Y
            pass
            self.mQ()
            self.mU()
            self.mE()
            self.mR()
            self.mY()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "QUERY"



    # $ANTLR start "RAISE"
    def mRAISE(self, ):

        try:
            _type = RAISE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:910:6: ( R A I S E )
            # SQLite.g:910:8: R A I S E
            pass
            self.mR()
            self.mA()
            self.mI()
            self.mS()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RAISE"



    # $ANTLR start "REFERENCES"
    def mREFERENCES(self, ):

        try:
            _type = REFERENCES
            _channel = DEFAULT_CHANNEL

            # SQLite.g:911:11: ( R E F E R E N C E S )
            # SQLite.g:911:13: R E F E R E N C E S
            pass
            self.mR()
            self.mE()
            self.mF()
            self.mE()
            self.mR()
            self.mE()
            self.mN()
            self.mC()
            self.mE()
            self.mS()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REFERENCES"



    # $ANTLR start "REGEXP"
    def mREGEXP(self, ):

        try:
            _type = REGEXP
            _channel = DEFAULT_CHANNEL

            # SQLite.g:912:7: ( R E G E X P )
            # SQLite.g:912:9: R E G E X P
            pass
            self.mR()
            self.mE()
            self.mG()
            self.mE()
            self.mX()
            self.mP()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REGEXP"



    # $ANTLR start "REINDEX"
    def mREINDEX(self, ):

        try:
            _type = REINDEX
            _channel = DEFAULT_CHANNEL

            # SQLite.g:913:8: ( R E I N D E X )
            # SQLite.g:913:10: R E I N D E X
            pass
            self.mR()
            self.mE()
            self.mI()
            self.mN()
            self.mD()
            self.mE()
            self.mX()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REINDEX"



    # $ANTLR start "RELEASE"
    def mRELEASE(self, ):

        try:
            _type = RELEASE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:914:8: ( R E L E A S E )
            # SQLite.g:914:10: R E L E A S E
            pass
            self.mR()
            self.mE()
            self.mL()
            self.mE()
            self.mA()
            self.mS()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RELEASE"



    # $ANTLR start "RENAME"
    def mRENAME(self, ):

        try:
            _type = RENAME
            _channel = DEFAULT_CHANNEL

            # SQLite.g:915:7: ( R E N A M E )
            # SQLite.g:915:9: R E N A M E
            pass
            self.mR()
            self.mE()
            self.mN()
            self.mA()
            self.mM()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RENAME"



    # $ANTLR start "REPLACE"
    def mREPLACE(self, ):

        try:
            _type = REPLACE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:916:8: ( R E P L A C E )
            # SQLite.g:916:10: R E P L A C E
            pass
            self.mR()
            self.mE()
            self.mP()
            self.mL()
            self.mA()
            self.mC()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REPLACE"



    # $ANTLR start "RESTRICT"
    def mRESTRICT(self, ):

        try:
            _type = RESTRICT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:917:9: ( R E S T R I C T )
            # SQLite.g:917:11: R E S T R I C T
            pass
            self.mR()
            self.mE()
            self.mS()
            self.mT()
            self.mR()
            self.mI()
            self.mC()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RESTRICT"



    # $ANTLR start "ROLLBACK"
    def mROLLBACK(self, ):

        try:
            _type = ROLLBACK
            _channel = DEFAULT_CHANNEL

            # SQLite.g:918:9: ( R O L L B A C K )
            # SQLite.g:918:11: R O L L B A C K
            pass
            self.mR()
            self.mO()
            self.mL()
            self.mL()
            self.mB()
            self.mA()
            self.mC()
            self.mK()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROLLBACK"



    # $ANTLR start "ROW"
    def mROW(self, ):

        try:
            _type = ROW
            _channel = DEFAULT_CHANNEL

            # SQLite.g:919:4: ( R O W )
            # SQLite.g:919:6: R O W
            pass
            self.mR()
            self.mO()
            self.mW()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROW"



    # $ANTLR start "SAVEPOINT"
    def mSAVEPOINT(self, ):

        try:
            _type = SAVEPOINT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:920:10: ( S A V E P O I N T )
            # SQLite.g:920:12: S A V E P O I N T
            pass
            self.mS()
            self.mA()
            self.mV()
            self.mE()
            self.mP()
            self.mO()
            self.mI()
            self.mN()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SAVEPOINT"



    # $ANTLR start "SELECT"
    def mSELECT(self, ):

        try:
            _type = SELECT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:921:7: ( S E L E C T )
            # SQLite.g:921:9: S E L E C T
            pass
            self.mS()
            self.mE()
            self.mL()
            self.mE()
            self.mC()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SELECT"



    # $ANTLR start "SET"
    def mSET(self, ):

        try:
            _type = SET
            _channel = DEFAULT_CHANNEL

            # SQLite.g:922:4: ( S E T )
            # SQLite.g:922:6: S E T
            pass
            self.mS()
            self.mE()
            self.mT()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SET"



    # $ANTLR start "TABLE"
    def mTABLE(self, ):

        try:
            _type = TABLE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:923:6: ( T A B L E )
            # SQLite.g:923:8: T A B L E
            pass
            self.mT()
            self.mA()
            self.mB()
            self.mL()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TABLE"



    # $ANTLR start "TEMPORARY"
    def mTEMPORARY(self, ):

        try:
            _type = TEMPORARY
            _channel = DEFAULT_CHANNEL

            # SQLite.g:924:10: ( T E M P ( O R A R Y )? )
            # SQLite.g:924:12: T E M P ( O R A R Y )?
            pass
            self.mT()
            self.mE()
            self.mM()
            self.mP()
            # SQLite.g:924:20: ( O R A R Y )?
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 79 or LA1_0 == 111):
                alt1 = 1
            if alt1 == 1:
                # SQLite.g:924:22: O R A R Y
                pass
                self.mO()
                self.mR()
                self.mA()
                self.mR()
                self.mY()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TEMPORARY"



    # $ANTLR start "THEN"
    def mTHEN(self, ):

        try:
            _type = THEN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:925:5: ( T H E N )
            # SQLite.g:925:7: T H E N
            pass
            self.mT()
            self.mH()
            self.mE()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THEN"



    # $ANTLR start "TO"
    def mTO(self, ):

        try:
            _type = TO
            _channel = DEFAULT_CHANNEL

            # SQLite.g:926:3: ( T O )
            # SQLite.g:926:5: T O
            pass
            self.mT()
            self.mO()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TO"



    # $ANTLR start "TRANSACTION"
    def mTRANSACTION(self, ):

        try:
            _type = TRANSACTION
            _channel = DEFAULT_CHANNEL

            # SQLite.g:927:12: ( T R A N S A C T I O N )
            # SQLite.g:927:14: T R A N S A C T I O N
            pass
            self.mT()
            self.mR()
            self.mA()
            self.mN()
            self.mS()
            self.mA()
            self.mC()
            self.mT()
            self.mI()
            self.mO()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TRANSACTION"



    # $ANTLR start "TRIGGER"
    def mTRIGGER(self, ):

        try:
            _type = TRIGGER
            _channel = DEFAULT_CHANNEL

            # SQLite.g:928:8: ( T R I G G E R )
            # SQLite.g:928:10: T R I G G E R
            pass
            self.mT()
            self.mR()
            self.mI()
            self.mG()
            self.mG()
            self.mE()
            self.mR()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TRIGGER"



    # $ANTLR start "UNION"
    def mUNION(self, ):

        try:
            _type = UNION
            _channel = DEFAULT_CHANNEL

            # SQLite.g:929:6: ( U N I O N )
            # SQLite.g:929:8: U N I O N
            pass
            self.mU()
            self.mN()
            self.mI()
            self.mO()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNION"



    # $ANTLR start "UNIQUE"
    def mUNIQUE(self, ):

        try:
            _type = UNIQUE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:930:7: ( U N I Q U E )
            # SQLite.g:930:9: U N I Q U E
            pass
            self.mU()
            self.mN()
            self.mI()
            self.mQ()
            self.mU()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNIQUE"



    # $ANTLR start "UPDATE"
    def mUPDATE(self, ):

        try:
            _type = UPDATE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:931:7: ( U P D A T E )
            # SQLite.g:931:9: U P D A T E
            pass
            self.mU()
            self.mP()
            self.mD()
            self.mA()
            self.mT()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UPDATE"



    # $ANTLR start "USING"
    def mUSING(self, ):

        try:
            _type = USING
            _channel = DEFAULT_CHANNEL

            # SQLite.g:932:6: ( U S I N G )
            # SQLite.g:932:8: U S I N G
            pass
            self.mU()
            self.mS()
            self.mI()
            self.mN()
            self.mG()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "USING"



    # $ANTLR start "VACUUM"
    def mVACUUM(self, ):

        try:
            _type = VACUUM
            _channel = DEFAULT_CHANNEL

            # SQLite.g:933:7: ( V A C U U M )
            # SQLite.g:933:9: V A C U U M
            pass
            self.mV()
            self.mA()
            self.mC()
            self.mU()
            self.mU()
            self.mM()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VACUUM"



    # $ANTLR start "VALUES"
    def mVALUES(self, ):

        try:
            _type = VALUES
            _channel = DEFAULT_CHANNEL

            # SQLite.g:934:7: ( V A L U E S )
            # SQLite.g:934:9: V A L U E S
            pass
            self.mV()
            self.mA()
            self.mL()
            self.mU()
            self.mE()
            self.mS()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VALUES"



    # $ANTLR start "VIEW"
    def mVIEW(self, ):

        try:
            _type = VIEW
            _channel = DEFAULT_CHANNEL

            # SQLite.g:935:5: ( V I E W )
            # SQLite.g:935:7: V I E W
            pass
            self.mV()
            self.mI()
            self.mE()
            self.mW()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VIEW"



    # $ANTLR start "VIRTUAL"
    def mVIRTUAL(self, ):

        try:
            _type = VIRTUAL
            _channel = DEFAULT_CHANNEL

            # SQLite.g:936:8: ( V I R T U A L )
            # SQLite.g:936:10: V I R T U A L
            pass
            self.mV()
            self.mI()
            self.mR()
            self.mT()
            self.mU()
            self.mA()
            self.mL()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VIRTUAL"



    # $ANTLR start "WHEN"
    def mWHEN(self, ):

        try:
            _type = WHEN
            _channel = DEFAULT_CHANNEL

            # SQLite.g:937:5: ( W H E N )
            # SQLite.g:937:7: W H E N
            pass
            self.mW()
            self.mH()
            self.mE()
            self.mN()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHEN"



    # $ANTLR start "WHERE"
    def mWHERE(self, ):

        try:
            _type = WHERE
            _channel = DEFAULT_CHANNEL

            # SQLite.g:938:6: ( W H E R E )
            # SQLite.g:938:8: W H E R E
            pass
            self.mW()
            self.mH()
            self.mE()
            self.mR()
            self.mE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHERE"



    # $ANTLR start "STRING_ESCAPE_SINGLE"
    def mSTRING_ESCAPE_SINGLE(self, ):

        try:
            # SQLite.g:940:30: ( ( BACKSLASH QUOTE_SINGLE ) )
            # SQLite.g:940:32: ( BACKSLASH QUOTE_SINGLE )
            pass
            # SQLite.g:940:32: ( BACKSLASH QUOTE_SINGLE )
            # SQLite.g:940:33: BACKSLASH QUOTE_SINGLE
            pass
            self.mBACKSLASH()
            self.mQUOTE_SINGLE()







        finally:

            pass

    # $ANTLR end "STRING_ESCAPE_SINGLE"



    # $ANTLR start "STRING_ESCAPE_DOUBLE"
    def mSTRING_ESCAPE_DOUBLE(self, ):

        try:
            # SQLite.g:941:30: ( ( BACKSLASH QUOTE_DOUBLE ) )
            # SQLite.g:941:32: ( BACKSLASH QUOTE_DOUBLE )
            pass
            # SQLite.g:941:32: ( BACKSLASH QUOTE_DOUBLE )
            # SQLite.g:941:33: BACKSLASH QUOTE_DOUBLE
            pass
            self.mBACKSLASH()
            self.mQUOTE_DOUBLE()







        finally:

            pass

    # $ANTLR end "STRING_ESCAPE_DOUBLE"



    # $ANTLR start "STRING_CORE"
    def mSTRING_CORE(self, ):

        try:
            # SQLite.g:942:21: (~ ( QUOTE_SINGLE | QUOTE_DOUBLE ) )
            # SQLite.g:942:23: ~ ( QUOTE_SINGLE | QUOTE_DOUBLE )
            pass
            if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 65535):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "STRING_CORE"



    # $ANTLR start "STRING_CORE_SINGLE"
    def mSTRING_CORE_SINGLE(self, ):

        try:
            # SQLite.g:943:28: ( ( STRING_CORE | QUOTE_DOUBLE | STRING_ESCAPE_SINGLE )* )
            # SQLite.g:943:30: ( STRING_CORE | QUOTE_DOUBLE | STRING_ESCAPE_SINGLE )*
            pass
            # SQLite.g:943:30: ( STRING_CORE | QUOTE_DOUBLE | STRING_ESCAPE_SINGLE )*
            while True: #loop2
                alt2 = 4
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 92):
                    LA2_2 = self.input.LA(2)

                    if (LA2_2 == 39):
                        alt2 = 3

                    else:
                        alt2 = 1


                elif (LA2_0 == 34):
                    alt2 = 2
                elif ((0 <= LA2_0 <= 33) or (35 <= LA2_0 <= 38) or (40 <= LA2_0 <= 91) or (93 <= LA2_0 <= 65535)):
                    alt2 = 1

                if alt2 == 1:
                    # SQLite.g:943:32: STRING_CORE
                    pass
                    self.mSTRING_CORE()


                elif alt2 == 2:
                    # SQLite.g:943:46: QUOTE_DOUBLE
                    pass
                    self.mQUOTE_DOUBLE()


                elif alt2 == 3:
                    # SQLite.g:943:61: STRING_ESCAPE_SINGLE
                    pass
                    self.mSTRING_ESCAPE_SINGLE()


                else:
                    break #loop2




        finally:

            pass

    # $ANTLR end "STRING_CORE_SINGLE"



    # $ANTLR start "STRING_CORE_DOUBLE"
    def mSTRING_CORE_DOUBLE(self, ):

        try:
            # SQLite.g:944:28: ( ( STRING_CORE | QUOTE_SINGLE | STRING_ESCAPE_DOUBLE )* )
            # SQLite.g:944:30: ( STRING_CORE | QUOTE_SINGLE | STRING_ESCAPE_DOUBLE )*
            pass
            # SQLite.g:944:30: ( STRING_CORE | QUOTE_SINGLE | STRING_ESCAPE_DOUBLE )*
            while True: #loop3
                alt3 = 4
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 92):
                    LA3_2 = self.input.LA(2)

                    if (LA3_2 == 34):
                        alt3 = 3

                    else:
                        alt3 = 1


                elif (LA3_0 == 39):
                    alt3 = 2
                elif ((0 <= LA3_0 <= 33) or (35 <= LA3_0 <= 38) or (40 <= LA3_0 <= 91) or (93 <= LA3_0 <= 65535)):
                    alt3 = 1

                if alt3 == 1:
                    # SQLite.g:944:32: STRING_CORE
                    pass
                    self.mSTRING_CORE()


                elif alt3 == 2:
                    # SQLite.g:944:46: QUOTE_SINGLE
                    pass
                    self.mQUOTE_SINGLE()


                elif alt3 == 3:
                    # SQLite.g:944:61: STRING_ESCAPE_DOUBLE
                    pass
                    self.mSTRING_ESCAPE_DOUBLE()


                else:
                    break #loop3




        finally:

            pass

    # $ANTLR end "STRING_CORE_DOUBLE"



    # $ANTLR start "STRING_SINGLE"
    def mSTRING_SINGLE(self, ):

        try:
            # SQLite.g:945:23: ( ( QUOTE_SINGLE STRING_CORE_SINGLE QUOTE_SINGLE ) )
            # SQLite.g:945:25: ( QUOTE_SINGLE STRING_CORE_SINGLE QUOTE_SINGLE )
            pass
            # SQLite.g:945:25: ( QUOTE_SINGLE STRING_CORE_SINGLE QUOTE_SINGLE )
            # SQLite.g:945:26: QUOTE_SINGLE STRING_CORE_SINGLE QUOTE_SINGLE
            pass
            self.mQUOTE_SINGLE()
            self.mSTRING_CORE_SINGLE()
            self.mQUOTE_SINGLE()







        finally:

            pass

    # $ANTLR end "STRING_SINGLE"



    # $ANTLR start "STRING_DOUBLE"
    def mSTRING_DOUBLE(self, ):

        try:
            # SQLite.g:946:23: ( ( QUOTE_DOUBLE STRING_CORE_DOUBLE QUOTE_DOUBLE ) )
            # SQLite.g:946:25: ( QUOTE_DOUBLE STRING_CORE_DOUBLE QUOTE_DOUBLE )
            pass
            # SQLite.g:946:25: ( QUOTE_DOUBLE STRING_CORE_DOUBLE QUOTE_DOUBLE )
            # SQLite.g:946:26: QUOTE_DOUBLE STRING_CORE_DOUBLE QUOTE_DOUBLE
            pass
            self.mQUOTE_DOUBLE()
            self.mSTRING_CORE_DOUBLE()
            self.mQUOTE_DOUBLE()







        finally:

            pass

    # $ANTLR end "STRING_DOUBLE"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # SQLite.g:947:7: ( ( STRING_SINGLE | STRING_DOUBLE ) )
            # SQLite.g:947:9: ( STRING_SINGLE | STRING_DOUBLE )
            pass
            # SQLite.g:947:9: ( STRING_SINGLE | STRING_DOUBLE )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 39):
                alt4 = 1
            elif (LA4_0 == 34):
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae

            if alt4 == 1:
                # SQLite.g:947:10: STRING_SINGLE
                pass
                self.mSTRING_SINGLE()


            elif alt4 == 2:
                # SQLite.g:947:26: STRING_DOUBLE
                pass
                self.mSTRING_DOUBLE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "ID_START"
    def mID_START(self, ):

        try:
            # SQLite.g:949:18: ( ( 'a' .. 'z' | 'A' .. 'Z' | UNDERSCORE ) )
            # SQLite.g:949:20: ( 'a' .. 'z' | 'A' .. 'Z' | UNDERSCORE )
            pass
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ID_START"



    # $ANTLR start "ID_CORE"
    def mID_CORE(self, ):

        try:
            # SQLite.g:950:17: ( ( ID_START | '0' .. '9' | DOLLAR ) )
            # SQLite.g:950:19: ( ID_START | '0' .. '9' | DOLLAR )
            pass
            if self.input.LA(1) == 36 or (48 <= self.input.LA(1) <= 57) or (
                    65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ID_CORE"



    # $ANTLR start "ID_PLAIN"
    def mID_PLAIN(self, ):

        try:
            # SQLite.g:951:18: ( ID_START ( ID_CORE )* )
            # SQLite.g:951:20: ID_START ( ID_CORE )*
            pass
            self.mID_START()
            # SQLite.g:951:29: ( ID_CORE )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 36 or (48 <= LA5_0 <= 57) or (65 <= LA5_0 <= 90) or LA5_0 == 95 or (97 <= LA5_0 <= 122)):
                    alt5 = 1

                if alt5 == 1:
                    # SQLite.g:951:30: ID_CORE
                    pass
                    self.mID_CORE()


                else:
                    break #loop5




        finally:

            pass

    # $ANTLR end "ID_PLAIN"



    # $ANTLR start "ID_QUOTED_CORE"
    def mID_QUOTED_CORE(self, ):

        try:
            # SQLite.g:953:24: (~ ( APOSTROPHE | LPAREN_SQUARE | RPAREN_SQUARE ) )
            # SQLite.g:953:26: ~ ( APOSTROPHE | LPAREN_SQUARE | RPAREN_SQUARE )
            pass
            if (0 <= self.input.LA(1) <= 90) or self.input.LA(1) == 92 or (94 <= self.input.LA(1) <= 95) or (
                    97 <= self.input.LA(1) <= 65535):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ID_QUOTED_CORE"



    # $ANTLR start "ID_QUOTED_CORE_SQUARE"
    def mID_QUOTED_CORE_SQUARE(self, ):

        try:
            # SQLite.g:954:31: ( ( ID_QUOTED_CORE | APOSTROPHE )* )
            # SQLite.g:954:33: ( ID_QUOTED_CORE | APOSTROPHE )*
            pass
            # SQLite.g:954:33: ( ID_QUOTED_CORE | APOSTROPHE )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((0 <= LA6_0 <= 90) or LA6_0 == 92 or (94 <= LA6_0 <= 65535)):
                    alt6 = 1

                if alt6 == 1:
                    # SQLite.g:
                    pass
                    if (0 <= self.input.LA(1) <= 90) or self.input.LA(1) == 92 or (94 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop6




        finally:

            pass

    # $ANTLR end "ID_QUOTED_CORE_SQUARE"



    # $ANTLR start "ID_QUOTED_CORE_APOSTROPHE"
    def mID_QUOTED_CORE_APOSTROPHE(self, ):

        try:
            # SQLite.g:955:35: ( ( ID_QUOTED_CORE | LPAREN_SQUARE | RPAREN_SQUARE )* )
            # SQLite.g:955:37: ( ID_QUOTED_CORE | LPAREN_SQUARE | RPAREN_SQUARE )*
            pass
            # SQLite.g:955:37: ( ID_QUOTED_CORE | LPAREN_SQUARE | RPAREN_SQUARE )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((0 <= LA7_0 <= 95) or (97 <= LA7_0 <= 65535)):
                    alt7 = 1

                if alt7 == 1:
                    # SQLite.g:
                    pass
                    if (0 <= self.input.LA(1) <= 95) or (97 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop7




        finally:

            pass

    # $ANTLR end "ID_QUOTED_CORE_APOSTROPHE"



    # $ANTLR start "ID_QUOTED_SQUARE"
    def mID_QUOTED_SQUARE(self, ):

        try:
            # SQLite.g:956:26: ( ( LPAREN_SQUARE ID_QUOTED_CORE_SQUARE RPAREN_SQUARE ) )
            # SQLite.g:956:28: ( LPAREN_SQUARE ID_QUOTED_CORE_SQUARE RPAREN_SQUARE )
            pass
            # SQLite.g:956:28: ( LPAREN_SQUARE ID_QUOTED_CORE_SQUARE RPAREN_SQUARE )
            # SQLite.g:956:29: LPAREN_SQUARE ID_QUOTED_CORE_SQUARE RPAREN_SQUARE
            pass
            self.mLPAREN_SQUARE()
            self.mID_QUOTED_CORE_SQUARE()
            self.mRPAREN_SQUARE()







        finally:

            pass

    # $ANTLR end "ID_QUOTED_SQUARE"



    # $ANTLR start "ID_QUOTED_APOSTROPHE"
    def mID_QUOTED_APOSTROPHE(self, ):

        try:
            # SQLite.g:957:30: ( ( APOSTROPHE ID_QUOTED_CORE_APOSTROPHE APOSTROPHE ) )
            # SQLite.g:957:32: ( APOSTROPHE ID_QUOTED_CORE_APOSTROPHE APOSTROPHE )
            pass
            # SQLite.g:957:32: ( APOSTROPHE ID_QUOTED_CORE_APOSTROPHE APOSTROPHE )
            # SQLite.g:957:33: APOSTROPHE ID_QUOTED_CORE_APOSTROPHE APOSTROPHE
            pass
            self.mAPOSTROPHE()
            self.mID_QUOTED_CORE_APOSTROPHE()
            self.mAPOSTROPHE()







        finally:

            pass

    # $ANTLR end "ID_QUOTED_APOSTROPHE"



    # $ANTLR start "ID_QUOTED"
    def mID_QUOTED(self, ):

        try:
            # SQLite.g:958:19: ( ID_QUOTED_SQUARE | ID_QUOTED_APOSTROPHE )
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 91):
                alt8 = 1
            elif (LA8_0 == 96):
                alt8 = 2
            else:
                nvae = NoViableAltException("", 8, 0, self.input)

                raise nvae

            if alt8 == 1:
                # SQLite.g:958:21: ID_QUOTED_SQUARE
                pass
                self.mID_QUOTED_SQUARE()


            elif alt8 == 2:
                # SQLite.g:958:40: ID_QUOTED_APOSTROPHE
                pass
                self.mID_QUOTED_APOSTROPHE()



        finally:

            pass

    # $ANTLR end "ID_QUOTED"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # SQLite.g:960:3: ( ID_PLAIN | ID_QUOTED )
            alt9 = 2
            LA9_0 = self.input.LA(1)

            if ((65 <= LA9_0 <= 90) or LA9_0 == 95 or (97 <= LA9_0 <= 122)):
                alt9 = 1
            elif (LA9_0 == 91 or LA9_0 == 96):
                alt9 = 2
            else:
                nvae = NoViableAltException("", 9, 0, self.input)

                raise nvae

            if alt9 == 1:
                # SQLite.g:960:5: ID_PLAIN
                pass
                self.mID_PLAIN()


            elif alt9 == 2:
                # SQLite.g:960:16: ID_QUOTED
                pass
                self.mID_QUOTED()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "INTEGER"
    def mINTEGER(self, ):

        try:
            _type = INTEGER
            _channel = DEFAULT_CHANNEL

            # SQLite.g:964:8: ( ( '0' .. '9' )+ )
            # SQLite.g:964:10: ( '0' .. '9' )+
            pass
            # SQLite.g:964:10: ( '0' .. '9' )+
            cnt10 = 0
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if ((48 <= LA10_0 <= 57)):
                    alt10 = 1

                if alt10 == 1:
                    # SQLite.g:964:11: '0' .. '9'
                    pass
                    self.matchRange(48, 57)


                else:
                    if cnt10 >= 1:
                        break #loop10

                    eee = EarlyExitException(10, self.input)
                    raise eee

                cnt10 += 1

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTEGER"



    # $ANTLR start "FLOAT_EXP"
    def mFLOAT_EXP(self, ):

        try:
            # SQLite.g:965:20: ( ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+ )
            # SQLite.g:965:22: ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+
            pass
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # SQLite.g:965:32: ( '+' | '-' )?
            alt11 = 2
            LA11_0 = self.input.LA(1)

            if (LA11_0 == 43 or LA11_0 == 45):
                alt11 = 1
            if alt11 == 1:
                # SQLite.g:
                pass
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            # SQLite.g:965:43: ( '0' .. '9' )+
            cnt12 = 0
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((48 <= LA12_0 <= 57)):
                    alt12 = 1

                if alt12 == 1:
                    # SQLite.g:965:44: '0' .. '9'
                    pass
                    self.matchRange(48, 57)


                else:
                    if cnt12 >= 1:
                        break #loop12

                    eee = EarlyExitException(12, self.input)
                    raise eee

                cnt12 += 1




        finally:

            pass

    # $ANTLR end "FLOAT_EXP"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):

        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # SQLite.g:967:5: ( ( '0' .. '9' )+ DOT ( '0' .. '9' )* ( FLOAT_EXP )? | DOT ( '0' .. '9' )+ ( FLOAT_EXP )? | ( '0' .. '9' )+ FLOAT_EXP )
            alt19 = 3
            alt19 = self.dfa19.predict(self.input)
            if alt19 == 1:
                # SQLite.g:967:9: ( '0' .. '9' )+ DOT ( '0' .. '9' )* ( FLOAT_EXP )?
                pass
                # SQLite.g:967:9: ( '0' .. '9' )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((48 <= LA13_0 <= 57)):
                        alt13 = 1

                    if alt13 == 1:
                        # SQLite.g:967:10: '0' .. '9'
                        pass
                        self.matchRange(48, 57)


                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1
                self.mDOT()
                # SQLite.g:967:25: ( '0' .. '9' )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((48 <= LA14_0 <= 57)):
                        alt14 = 1

                    if alt14 == 1:
                        # SQLite.g:967:26: '0' .. '9'
                        pass
                        self.matchRange(48, 57)


                    else:
                        break #loop14
                    # SQLite.g:967:37: ( FLOAT_EXP )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 69 or LA15_0 == 101):
                    alt15 = 1
                if alt15 == 1:
                    # SQLite.g:967:37: FLOAT_EXP
                    pass
                    self.mFLOAT_EXP()





            elif alt19 == 2:
                # SQLite.g:968:9: DOT ( '0' .. '9' )+ ( FLOAT_EXP )?
                pass
                self.mDOT()
                # SQLite.g:968:13: ( '0' .. '9' )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if ((48 <= LA16_0 <= 57)):
                        alt16 = 1

                    if alt16 == 1:
                        # SQLite.g:968:14: '0' .. '9'
                        pass
                        self.matchRange(48, 57)


                    else:
                        if cnt16 >= 1:
                            break #loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1
                    # SQLite.g:968:25: ( FLOAT_EXP )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == 69 or LA17_0 == 101):
                    alt17 = 1
                if alt17 == 1:
                    # SQLite.g:968:25: FLOAT_EXP
                    pass
                    self.mFLOAT_EXP()





            elif alt19 == 3:
                # SQLite.g:969:9: ( '0' .. '9' )+ FLOAT_EXP
                pass
                # SQLite.g:969:9: ( '0' .. '9' )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if ((48 <= LA18_0 <= 57)):
                        alt18 = 1

                    if alt18 == 1:
                        # SQLite.g:969:10: '0' .. '9'
                        pass
                        self.matchRange(48, 57)


                    else:
                        if cnt18 >= 1:
                            break #loop18

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1
                self.mFLOAT_EXP()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "BLOB"
    def mBLOB(self, ):

        try:
            _type = BLOB
            _channel = DEFAULT_CHANNEL

            # SQLite.g:971:5: ( ( 'x' | 'X' ) QUOTE_SINGLE ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )+ QUOTE_SINGLE )
            # SQLite.g:971:7: ( 'x' | 'X' ) QUOTE_SINGLE ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )+ QUOTE_SINGLE
            pass
            if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            self.mQUOTE_SINGLE()
            # SQLite.g:971:30: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )+
            cnt20 = 0
            while True: #loop20
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((48 <= LA20_0 <= 57) or (65 <= LA20_0 <= 70) or (97 <= LA20_0 <= 102)):
                    alt20 = 1

                if alt20 == 1:
                    # SQLite.g:
                    pass
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (
                            97 <= self.input.LA(1) <= 102):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt20 >= 1:
                        break #loop20

                    eee = EarlyExitException(20, self.input)
                    raise eee

                cnt20 += 1
            self.mQUOTE_SINGLE()

            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BLOB"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            # SQLite.g:973:17: ( '/*' ( options {greedy=false; } : . )* '*/' )
            # SQLite.g:973:19: '/*' ( options {greedy=false; } : . )* '*/'
            pass
            self.match("/*")
            # SQLite.g:973:24: ( options {greedy=false; } : . )*
            while True: #loop21
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == 42):
                    LA21_1 = self.input.LA(2)

                    if (LA21_1 == 47):
                        alt21 = 2
                    elif ((0 <= LA21_1 <= 46) or (48 <= LA21_1 <= 65535)):
                        alt21 = 1


                elif ((0 <= LA21_0 <= 41) or (43 <= LA21_0 <= 65535)):
                    alt21 = 1

                if alt21 == 1:
                    # SQLite.g:973:52: .
                    pass
                    self.matchAny()


                else:
                    break #loop21
            self.match("*/")




        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):

        try:
            # SQLite.g:974:22: ( '--' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' | EOF ) )
            # SQLite.g:974:24: '--' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' | EOF )
            pass
            self.match("--")
            # SQLite.g:974:29: (~ ( '\\n' | '\\r' ) )*
            while True: #loop22
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if ((0 <= LA22_0 <= 9) or (11 <= LA22_0 <= 12) or (14 <= LA22_0 <= 65535)):
                    alt22 = 1

                if alt22 == 1:
                    # SQLite.g:974:29: ~ ( '\\n' | '\\r' )
                    pass
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (
                            14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop22
                # SQLite.g:974:43: ( ( '\\r' )? '\\n' | EOF )
            alt24 = 2
            LA24_0 = self.input.LA(1)

            if (LA24_0 == 10 or LA24_0 == 13):
                alt24 = 1
            else:
                alt24 = 2
            if alt24 == 1:
                # SQLite.g:974:44: ( '\\r' )? '\\n'
                pass
                # SQLite.g:974:44: ( '\\r' )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == 13):
                    alt23 = 1
                if alt23 == 1:
                    # SQLite.g:974:44: '\\r'
                    pass
                    self.match(13)

                self.match(10)


            elif alt24 == 2:
                # SQLite.g:974:55: EOF
                pass
                self.match(EOF)







        finally:

            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # SQLite.g:975:3: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' | COMMENT | LINE_COMMENT ) )
            # SQLite.g:975:5: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' | COMMENT | LINE_COMMENT )
            pass
            # SQLite.g:975:5: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' | COMMENT | LINE_COMMENT )
            alt25 = 7
            LA25 = self.input.LA(1)
            if LA25 == 32:
                alt25 = 1
            elif LA25 == 13:
                alt25 = 2
            elif LA25 == 9:
                alt25 = 3
            elif LA25 == 12:
                alt25 = 4
            elif LA25 == 10:
                alt25 = 5
            elif LA25 == 47:
                alt25 = 6
            elif LA25 == 45:
                alt25 = 7
            else:
                nvae = NoViableAltException("", 25, 0, self.input)

                raise nvae

            if alt25 == 1:
                # SQLite.g:975:6: ' '
                pass
                self.match(32)


            elif alt25 == 2:
                # SQLite.g:975:10: '\\r'
                pass
                self.match(13)


            elif alt25 == 3:
                # SQLite.g:975:15: '\\t'
                pass
                self.match(9)


            elif alt25 == 4:
                # SQLite.g:975:20: '\\u000C'
                pass
                self.match(12)


            elif alt25 == 5:
                # SQLite.g:975:29: '\\n'
                pass
                self.match(10)


            elif alt25 == 6:
                # SQLite.g:975:34: COMMENT
                pass
                self.mCOMMENT()


            elif alt25 == 7:
                # SQLite.g:975:42: LINE_COMMENT
                pass
                self.mLINE_COMMENT()



            #action start
            _channel = HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # SQLite.g:1:8: ( EQUALS | EQUALS2 | NOT_EQUALS | NOT_EQUALS2 | LESS | LESS_OR_EQ | GREATER | GREATER_OR_EQ | SHIFT_LEFT | SHIFT_RIGHT | AMPERSAND | PIPE | DOUBLE_PIPE | PLUS | MINUS | TILDA | ASTERISK | SLASH | BACKSLASH | PERCENT | SEMI | DOT | COMMA | LPAREN | RPAREN | QUESTION | COLON | AT | DOLLAR | QUOTE_DOUBLE | QUOTE_SINGLE | APOSTROPHE | LPAREN_SQUARE | RPAREN_SQUARE | UNDERSCORE | ABORT | ADD | AFTER | ALL | ALTER | ANALYZE | AND | AS | ASC | ATTACH | AUTOINCREMENT | BEFORE | BEGIN | BETWEEN | BY | CASCADE | CASE | CAST | CHECK | COLLATE | COLUMN | COMMIT | CONFLICT | CONSTRAINT | CREATE | CROSS | CURRENT_TIME | CURRENT_DATE | CURRENT_TIMESTAMP | DATABASE | DEFAULT | DEFERRABLE | DEFERRED | DELETE | DESC | DETACH | DISTINCT | DROP | EACH | ELSE | END | ESCAPE | EXCEPT | EXCLUSIVE | EXISTS | EXPLAIN | FAIL | FOR | FOREIGN | FROM | GLOB | GROUP | HAVING | IF | IGNORE | IMMEDIATE | IN | INDEX | INDEXED | INITIALLY | INNER | INSERT | INSTEAD | INTERSECT | INTO | IS | ISNULL | JOIN | KEY | LEFT | LIKE | LIMIT | MATCH | NATURAL | NOT | NOTNULL | NULL | OF | OFFSET | ON | OR | ORDER | OUTER | PLAN | PRAGMA | PRIMARY | QUERY | RAISE | REFERENCES | REGEXP | REINDEX | RELEASE | RENAME | REPLACE | RESTRICT | ROLLBACK | ROW | SAVEPOINT | SELECT | SET | TABLE | TEMPORARY | THEN | TO | TRANSACTION | TRIGGER | UNION | UNIQUE | UPDATE | USING | VACUUM | VALUES | VIEW | VIRTUAL | WHEN | WHERE | STRING | ID | INTEGER | FLOAT | BLOB | WS )
        alt26 = 157
        alt26 = self.dfa26.predict(self.input)
        if alt26 == 1:
            # SQLite.g:1:10: EQUALS
            pass
            self.mEQUALS()


        elif alt26 == 2:
            # SQLite.g:1:17: EQUALS2
            pass
            self.mEQUALS2()


        elif alt26 == 3:
            # SQLite.g:1:25: NOT_EQUALS
            pass
            self.mNOT_EQUALS()


        elif alt26 == 4:
            # SQLite.g:1:36: NOT_EQUALS2
            pass
            self.mNOT_EQUALS2()


        elif alt26 == 5:
            # SQLite.g:1:48: LESS
            pass
            self.mLESS()


        elif alt26 == 6:
            # SQLite.g:1:53: LESS_OR_EQ
            pass
            self.mLESS_OR_EQ()


        elif alt26 == 7:
            # SQLite.g:1:64: GREATER
            pass
            self.mGREATER()


        elif alt26 == 8:
            # SQLite.g:1:72: GREATER_OR_EQ
            pass
            self.mGREATER_OR_EQ()


        elif alt26 == 9:
            # SQLite.g:1:86: SHIFT_LEFT
            pass
            self.mSHIFT_LEFT()


        elif alt26 == 10:
            # SQLite.g:1:97: SHIFT_RIGHT
            pass
            self.mSHIFT_RIGHT()


        elif alt26 == 11:
            # SQLite.g:1:109: AMPERSAND
            pass
            self.mAMPERSAND()


        elif alt26 == 12:
            # SQLite.g:1:119: PIPE
            pass
            self.mPIPE()


        elif alt26 == 13:
            # SQLite.g:1:124: DOUBLE_PIPE
            pass
            self.mDOUBLE_PIPE()


        elif alt26 == 14:
            # SQLite.g:1:136: PLUS
            pass
            self.mPLUS()


        elif alt26 == 15:
            # SQLite.g:1:141: MINUS
            pass
            self.mMINUS()


        elif alt26 == 16:
            # SQLite.g:1:147: TILDA
            pass
            self.mTILDA()


        elif alt26 == 17:
            # SQLite.g:1:153: ASTERISK
            pass
            self.mASTERISK()


        elif alt26 == 18:
            # SQLite.g:1:162: SLASH
            pass
            self.mSLASH()


        elif alt26 == 19:
            # SQLite.g:1:168: BACKSLASH
            pass
            self.mBACKSLASH()


        elif alt26 == 20:
            # SQLite.g:1:178: PERCENT
            pass
            self.mPERCENT()


        elif alt26 == 21:
            # SQLite.g:1:186: SEMI
            pass
            self.mSEMI()


        elif alt26 == 22:
            # SQLite.g:1:191: DOT
            pass
            self.mDOT()


        elif alt26 == 23:
            # SQLite.g:1:195: COMMA
            pass
            self.mCOMMA()


        elif alt26 == 24:
            # SQLite.g:1:201: LPAREN
            pass
            self.mLPAREN()


        elif alt26 == 25:
            # SQLite.g:1:208: RPAREN
            pass
            self.mRPAREN()


        elif alt26 == 26:
            # SQLite.g:1:215: QUESTION
            pass
            self.mQUESTION()


        elif alt26 == 27:
            # SQLite.g:1:224: COLON
            pass
            self.mCOLON()


        elif alt26 == 28:
            # SQLite.g:1:230: AT
            pass
            self.mAT()


        elif alt26 == 29:
            # SQLite.g:1:233: DOLLAR
            pass
            self.mDOLLAR()


        elif alt26 == 30:
            # SQLite.g:1:240: QUOTE_DOUBLE
            pass
            self.mQUOTE_DOUBLE()


        elif alt26 == 31:
            # SQLite.g:1:253: QUOTE_SINGLE
            pass
            self.mQUOTE_SINGLE()


        elif alt26 == 32:
            # SQLite.g:1:266: APOSTROPHE
            pass
            self.mAPOSTROPHE()


        elif alt26 == 33:
            # SQLite.g:1:277: LPAREN_SQUARE
            pass
            self.mLPAREN_SQUARE()


        elif alt26 == 34:
            # SQLite.g:1:291: RPAREN_SQUARE
            pass
            self.mRPAREN_SQUARE()


        elif alt26 == 35:
            # SQLite.g:1:305: UNDERSCORE
            pass
            self.mUNDERSCORE()


        elif alt26 == 36:
            # SQLite.g:1:316: ABORT
            pass
            self.mABORT()


        elif alt26 == 37:
            # SQLite.g:1:322: ADD
            pass
            self.mADD()


        elif alt26 == 38:
            # SQLite.g:1:326: AFTER
            pass
            self.mAFTER()


        elif alt26 == 39:
            # SQLite.g:1:332: ALL
            pass
            self.mALL()


        elif alt26 == 40:
            # SQLite.g:1:336: ALTER
            pass
            self.mALTER()


        elif alt26 == 41:
            # SQLite.g:1:342: ANALYZE
            pass
            self.mANALYZE()


        elif alt26 == 42:
            # SQLite.g:1:350: AND
            pass
            self.mAND()


        elif alt26 == 43:
            # SQLite.g:1:354: AS
            pass
            self.mAS()


        elif alt26 == 44:
            # SQLite.g:1:357: ASC
            pass
            self.mASC()


        elif alt26 == 45:
            # SQLite.g:1:361: ATTACH
            pass
            self.mATTACH()


        elif alt26 == 46:
            # SQLite.g:1:368: AUTOINCREMENT
            pass
            self.mAUTOINCREMENT()


        elif alt26 == 47:
            # SQLite.g:1:382: BEFORE
            pass
            self.mBEFORE()


        elif alt26 == 48:
            # SQLite.g:1:389: BEGIN
            pass
            self.mBEGIN()


        elif alt26 == 49:
            # SQLite.g:1:395: BETWEEN
            pass
            self.mBETWEEN()


        elif alt26 == 50:
            # SQLite.g:1:403: BY
            pass
            self.mBY()


        elif alt26 == 51:
            # SQLite.g:1:406: CASCADE
            pass
            self.mCASCADE()


        elif alt26 == 52:
            # SQLite.g:1:414: CASE
            pass
            self.mCASE()


        elif alt26 == 53:
            # SQLite.g:1:419: CAST
            pass
            self.mCAST()


        elif alt26 == 54:
            # SQLite.g:1:424: CHECK
            pass
            self.mCHECK()


        elif alt26 == 55:
            # SQLite.g:1:430: COLLATE
            pass
            self.mCOLLATE()


        elif alt26 == 56:
            # SQLite.g:1:438: COLUMN
            pass
            self.mCOLUMN()


        elif alt26 == 57:
            # SQLite.g:1:445: COMMIT
            pass
            self.mCOMMIT()


        elif alt26 == 58:
            # SQLite.g:1:452: CONFLICT
            pass
            self.mCONFLICT()


        elif alt26 == 59:
            # SQLite.g:1:461: CONSTRAINT
            pass
            self.mCONSTRAINT()


        elif alt26 == 60:
            # SQLite.g:1:472: CREATE
            pass
            self.mCREATE()


        elif alt26 == 61:
            # SQLite.g:1:479: CROSS
            pass
            self.mCROSS()


        elif alt26 == 62:
            # SQLite.g:1:485: CURRENT_TIME
            pass
            self.mCURRENT_TIME()


        elif alt26 == 63:
            # SQLite.g:1:498: CURRENT_DATE
            pass
            self.mCURRENT_DATE()


        elif alt26 == 64:
            # SQLite.g:1:511: CURRENT_TIMESTAMP
            pass
            self.mCURRENT_TIMESTAMP()


        elif alt26 == 65:
            # SQLite.g:1:529: DATABASE
            pass
            self.mDATABASE()


        elif alt26 == 66:
            # SQLite.g:1:538: DEFAULT
            pass
            self.mDEFAULT()


        elif alt26 == 67:
            # SQLite.g:1:546: DEFERRABLE
            pass
            self.mDEFERRABLE()


        elif alt26 == 68:
            # SQLite.g:1:557: DEFERRED
            pass
            self.mDEFERRED()


        elif alt26 == 69:
            # SQLite.g:1:566: DELETE
            pass
            self.mDELETE()


        elif alt26 == 70:
            # SQLite.g:1:573: DESC
            pass
            self.mDESC()


        elif alt26 == 71:
            # SQLite.g:1:578: DETACH
            pass
            self.mDETACH()


        elif alt26 == 72:
            # SQLite.g:1:585: DISTINCT
            pass
            self.mDISTINCT()


        elif alt26 == 73:
            # SQLite.g:1:594: DROP
            pass
            self.mDROP()


        elif alt26 == 74:
            # SQLite.g:1:599: EACH
            pass
            self.mEACH()


        elif alt26 == 75:
            # SQLite.g:1:604: ELSE
            pass
            self.mELSE()


        elif alt26 == 76:
            # SQLite.g:1:609: END
            pass
            self.mEND()


        elif alt26 == 77:
            # SQLite.g:1:613: ESCAPE
            pass
            self.mESCAPE()


        elif alt26 == 78:
            # SQLite.g:1:620: EXCEPT
            pass
            self.mEXCEPT()


        elif alt26 == 79:
            # SQLite.g:1:627: EXCLUSIVE
            pass
            self.mEXCLUSIVE()


        elif alt26 == 80:
            # SQLite.g:1:637: EXISTS
            pass
            self.mEXISTS()


        elif alt26 == 81:
            # SQLite.g:1:644: EXPLAIN
            pass
            self.mEXPLAIN()


        elif alt26 == 82:
            # SQLite.g:1:652: FAIL
            pass
            self.mFAIL()


        elif alt26 == 83:
            # SQLite.g:1:657: FOR
            pass
            self.mFOR()


        elif alt26 == 84:
            # SQLite.g:1:661: FOREIGN
            pass
            self.mFOREIGN()


        elif alt26 == 85:
            # SQLite.g:1:669: FROM
            pass
            self.mFROM()


        elif alt26 == 86:
            # SQLite.g:1:674: GLOB
            pass
            self.mGLOB()


        elif alt26 == 87:
            # SQLite.g:1:679: GROUP
            pass
            self.mGROUP()


        elif alt26 == 88:
            # SQLite.g:1:685: HAVING
            pass
            self.mHAVING()


        elif alt26 == 89:
            # SQLite.g:1:692: IF
            pass
            self.mIF()


        elif alt26 == 90:
            # SQLite.g:1:695: IGNORE
            pass
            self.mIGNORE()


        elif alt26 == 91:
            # SQLite.g:1:702: IMMEDIATE
            pass
            self.mIMMEDIATE()


        elif alt26 == 92:
            # SQLite.g:1:712: IN
            pass
            self.mIN()


        elif alt26 == 93:
            # SQLite.g:1:715: INDEX
            pass
            self.mINDEX()


        elif alt26 == 94:
            # SQLite.g:1:721: INDEXED
            pass
            self.mINDEXED()


        elif alt26 == 95:
            # SQLite.g:1:729: INITIALLY
            pass
            self.mINITIALLY()


        elif alt26 == 96:
            # SQLite.g:1:739: INNER
            pass
            self.mINNER()


        elif alt26 == 97:
            # SQLite.g:1:745: INSERT
            pass
            self.mINSERT()


        elif alt26 == 98:
            # SQLite.g:1:752: INSTEAD
            pass
            self.mINSTEAD()


        elif alt26 == 99:
            # SQLite.g:1:760: INTERSECT
            pass
            self.mINTERSECT()


        elif alt26 == 100:
            # SQLite.g:1:770: INTO
            pass
            self.mINTO()


        elif alt26 == 101:
            # SQLite.g:1:775: IS
            pass
            self.mIS()


        elif alt26 == 102:
            # SQLite.g:1:778: ISNULL
            pass
            self.mISNULL()


        elif alt26 == 103:
            # SQLite.g:1:785: JOIN
            pass
            self.mJOIN()


        elif alt26 == 104:
            # SQLite.g:1:790: KEY
            pass
            self.mKEY()


        elif alt26 == 105:
            # SQLite.g:1:794: LEFT
            pass
            self.mLEFT()


        elif alt26 == 106:
            # SQLite.g:1:799: LIKE
            pass
            self.mLIKE()


        elif alt26 == 107:
            # SQLite.g:1:804: LIMIT
            pass
            self.mLIMIT()


        elif alt26 == 108:
            # SQLite.g:1:810: MATCH
            pass
            self.mMATCH()


        elif alt26 == 109:
            # SQLite.g:1:816: NATURAL
            pass
            self.mNATURAL()


        elif alt26 == 110:
            # SQLite.g:1:824: NOT
            pass
            self.mNOT()


        elif alt26 == 111:
            # SQLite.g:1:828: NOTNULL
            pass
            self.mNOTNULL()


        elif alt26 == 112:
            # SQLite.g:1:836: NULL
            pass
            self.mNULL()


        elif alt26 == 113:
            # SQLite.g:1:841: OF
            pass
            self.mOF()


        elif alt26 == 114:
            # SQLite.g:1:844: OFFSET
            pass
            self.mOFFSET()


        elif alt26 == 115:
            # SQLite.g:1:851: ON
            pass
            self.mON()


        elif alt26 == 116:
            # SQLite.g:1:854: OR
            pass
            self.mOR()


        elif alt26 == 117:
            # SQLite.g:1:857: ORDER
            pass
            self.mORDER()


        elif alt26 == 118:
            # SQLite.g:1:863: OUTER
            pass
            self.mOUTER()


        elif alt26 == 119:
            # SQLite.g:1:869: PLAN
            pass
            self.mPLAN()


        elif alt26 == 120:
            # SQLite.g:1:874: PRAGMA
            pass
            self.mPRAGMA()


        elif alt26 == 121:
            # SQLite.g:1:881: PRIMARY
            pass
            self.mPRIMARY()


        elif alt26 == 122:
            # SQLite.g:1:889: QUERY
            pass
            self.mQUERY()


        elif alt26 == 123:
            # SQLite.g:1:895: RAISE
            pass
            self.mRAISE()


        elif alt26 == 124:
            # SQLite.g:1:901: REFERENCES
            pass
            self.mREFERENCES()


        elif alt26 == 125:
            # SQLite.g:1:912: REGEXP
            pass
            self.mREGEXP()


        elif alt26 == 126:
            # SQLite.g:1:919: REINDEX
            pass
            self.mREINDEX()


        elif alt26 == 127:
            # SQLite.g:1:927: RELEASE
            pass
            self.mRELEASE()


        elif alt26 == 128:
            # SQLite.g:1:935: RENAME
            pass
            self.mRENAME()


        elif alt26 == 129:
            # SQLite.g:1:942: REPLACE
            pass
            self.mREPLACE()


        elif alt26 == 130:
            # SQLite.g:1:950: RESTRICT
            pass
            self.mRESTRICT()


        elif alt26 == 131:
            # SQLite.g:1:959: ROLLBACK
            pass
            self.mROLLBACK()


        elif alt26 == 132:
            # SQLite.g:1:968: ROW
            pass
            self.mROW()


        elif alt26 == 133:
            # SQLite.g:1:972: SAVEPOINT
            pass
            self.mSAVEPOINT()


        elif alt26 == 134:
            # SQLite.g:1:982: SELECT
            pass
            self.mSELECT()


        elif alt26 == 135:
            # SQLite.g:1:989: SET
            pass
            self.mSET()


        elif alt26 == 136:
            # SQLite.g:1:993: TABLE
            pass
            self.mTABLE()


        elif alt26 == 137:
            # SQLite.g:1:999: TEMPORARY
            pass
            self.mTEMPORARY()


        elif alt26 == 138:
            # SQLite.g:1:1009: THEN
            pass
            self.mTHEN()


        elif alt26 == 139:
            # SQLite.g:1:1014: TO
            pass
            self.mTO()


        elif alt26 == 140:
            # SQLite.g:1:1017: TRANSACTION
            pass
            self.mTRANSACTION()


        elif alt26 == 141:
            # SQLite.g:1:1029: TRIGGER
            pass
            self.mTRIGGER()


        elif alt26 == 142:
            # SQLite.g:1:1037: UNION
            pass
            self.mUNION()


        elif alt26 == 143:
            # SQLite.g:1:1043: UNIQUE
            pass
            self.mUNIQUE()


        elif alt26 == 144:
            # SQLite.g:1:1050: UPDATE
            pass
            self.mUPDATE()


        elif alt26 == 145:
            # SQLite.g:1:1057: USING
            pass
            self.mUSING()


        elif alt26 == 146:
            # SQLite.g:1:1063: VACUUM
            pass
            self.mVACUUM()


        elif alt26 == 147:
            # SQLite.g:1:1070: VALUES
            pass
            self.mVALUES()


        elif alt26 == 148:
            # SQLite.g:1:1077: VIEW
            pass
            self.mVIEW()


        elif alt26 == 149:
            # SQLite.g:1:1082: VIRTUAL
            pass
            self.mVIRTUAL()


        elif alt26 == 150:
            # SQLite.g:1:1090: WHEN
            pass
            self.mWHEN()


        elif alt26 == 151:
            # SQLite.g:1:1095: WHERE
            pass
            self.mWHERE()


        elif alt26 == 152:
            # SQLite.g:1:1101: STRING
            pass
            self.mSTRING()


        elif alt26 == 153:
            # SQLite.g:1:1108: ID
            pass
            self.mID()


        elif alt26 == 154:
            # SQLite.g:1:1111: INTEGER
            pass
            self.mINTEGER()


        elif alt26 == 155:
            # SQLite.g:1:1119: FLOAT
            pass
            self.mFLOAT()


        elif alt26 == 156:
            # SQLite.g:1:1125: BLOB
            pass
            self.mBLOB()


        elif alt26 == 157:
            # SQLite.g:1:1130: WS
            pass
            self.mWS()


    # lookup tables for DFA #19

    DFA19_eot = DFA.unpack(
        u"\5\uffff"
    )

    DFA19_eof = DFA.unpack(
        u"\5\uffff"
    )

    DFA19_min = DFA.unpack(
        u"\2\56\3\uffff"
    )

    DFA19_max = DFA.unpack(
        u"\1\71\1\145\3\uffff"
    )

    DFA19_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\1"
    )

    DFA19_special = DFA.unpack(
        u"\5\uffff"
    )

    DFA19_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\4\1\uffff\12\1\13\uffff\1\3\37\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #19

    class DFA19(DFA):
        pass


    # lookup tables for DFA #26

    DFA26_eot = DFA.unpack(
        u"\1\uffff\1\71\1\uffff\1\75\1\100\1\uffff\1\102\1\uffff\1\103\2"
        u"\uffff\1\104\3\uffff\1\105\7\uffff\1\107\1\111\1\112\1\113\1\uffff"
        u"\1\114\30\66\1\u0090\27\uffff\5\66\1\u0098\3\66\1\u009f\24\66\1"
        u"\u00bc\1\u00c2\1\u00c3\12\66\1\u00d0\1\u00d2\1\66\1\u00d5\11\66"
        u"\1\u00e9\11\66\2\uffff\1\66\1\u00f6\1\66\1\u00f8\3\66\1\uffff\1"
        u"\u00fc\1\66\1\u00fe\3\66\1\uffff\24\66\1\u011c\1\66\1\u011e\5\66"
        u"\1\uffff\5\66\2\uffff\4\66\1\u0130\5\66\1\u0136\1\66\1\uffff\1"
        u"\66\1\uffff\2\66\1\uffff\14\66\1\u0148\1\66\1\u014a\4\66\1\uffff"
        u"\14\66\1\uffff\1\66\1\uffff\3\66\1\uffff\1\66\1\uffff\3\66\1\u0165"
        u"\1\u0166\15\66\1\u0174\2\66\1\u0177\6\66\1\u017e\1\uffff\1\u017f"
        u"\1\uffff\1\66\1\u0181\1\u0182\1\u0183\2\66\1\u0186\11\66\1\u0190"
        u"\1\uffff\1\66\1\u0192\1\u0193\1\66\1\u0195\1\uffff\5\66\1\u019b"
        u"\13\66\1\uffff\1\66\1\uffff\5\66\1\u01ad\1\u01ae\6\66\1\u01b6\1"
        u"\66\1\u01b8\3\66\1\u01bc\1\u01bd\1\66\1\u01bf\1\66\1\u01c1\1\66"
        u"\2\uffff\3\66\1\u01c6\5\66\1\u01cc\3\66\1\uffff\2\66\1\uffff\6"
        u"\66\2\uffff\1\66\3\uffff\1\u01d9\1\66\1\uffff\1\66\1\u01dc\2\66"
        u"\1\u01df\4\66\1\uffff\1\u01e5\2\uffff\1\u01e6\1\uffff\3\66\1\u01ea"
        u"\1\u01eb\1\uffff\2\66\1\u01ee\10\66\1\u01f7\4\66\1\u01fc\2\uffff"
        u"\3\66\1\u0200\1\u0201\2\66\1\uffff\1\66\1\uffff\1\u0205\1\66\1"
        u"\u0207\2\uffff\1\66\1\uffff\1\u0209\1\uffff\3\66\1\u020d\1\uffff"
        u"\2\66\1\u0210\1\u0211\1\66\1\uffff\2\66\1\u0216\1\u0217\2\66\1"
        u"\u021a\1\66\1\u021c\1\66\1\u021e\1\66\1\uffff\1\u0220\1\66\1\uffff"
        u"\1\66\1\u0223\1\uffff\2\66\1\u0226\1\u0227\1\66\2\uffff\2\66\1"
        u"\u022b\2\uffff\1\u022c\1\66\1\uffff\1\66\1\u022f\4\66\1\u0234\1"
        u"\66\1\uffff\1\u0236\3\66\1\uffff\1\66\1\u023b\1\u023c\2\uffff\1"
        u"\u023d\1\u023e\1\66\1\uffff\1\u0240\1\uffff\1\66\1\uffff\1\u0242"
        u"\1\u0243\1\66\1\uffff\2\66\2\uffff\1\u0247\2\66\1\u024a\2\uffff"
        u"\2\66\1\uffff\1\66\1\uffff\1\u024e\1\uffff\1\u024f\1\uffff\1\66"
        u"\1\u0251\1\uffff\1\u0252\1\66\2\uffff\1\66\1\u0255\1\u0256\2\uffff"
        u"\1\u0257\1\66\1\uffff\1\u0259\1\u025a\1\u025b\1\66\1\uffff\1\66"
        u"\1\uffff\2\66\1\u0260\1\66\4\uffff\1\u0262\1\uffff\1\66\2\uffff"
        u"\2\66\1\u0267\1\uffff\1\66\1\u0269\1\uffff\1\u026a\1\u026b\1\66"
        u"\2\uffff\1\66\2\uffff\2\66\3\uffff\1\u0270\3\uffff\1\66\1\u0272"
        u"\2\66\1\uffff\1\66\1\uffff\4\66\1\uffff\1\66\3\uffff\1\u027b\1"
        u"\u027c\1\u027d\1\u027e\1\uffff\1\66\1\uffff\1\u0280\1\66\1\u01ae"
        u"\3\66\1\u0285\1\u0286\4\uffff\1\u0287\1\uffff\4\66\3\uffff\1\u028c"
        u"\1\66\1\u028e\1\u0290\1\uffff\1\u0291\1\uffff\1\66\2\uffff\3\66"
        u"\1\u0296\1\uffff"
    )

    DFA26_eof = DFA.unpack(
        u"\u0297\uffff"
    )

    DFA26_min = DFA.unpack(
        u"\1\11\1\75\1\uffff\1\74\1\75\1\uffff\1\174\1\uffff\1\55\2\uffff"
        u"\1\52\3\uffff\1\60\7\uffff\4\0\1\uffff\1\44\1\102\1\105\4\101\1"
        u"\114\1\101\1\106\1\117\2\105\2\101\1\106\1\114\1\125\3\101\1\116"
        u"\1\101\1\110\1\47\1\56\27\uffff\1\101\1\124\1\114\2\124\1\44\1"
        u"\117\1\104\1\106\1\44\1\123\1\122\1\105\1\114\1\105\1\106\1\124"
        u"\1\117\1\123\3\103\1\104\1\123\1\122\1\117\1\111\2\117\1\126\3"
        u"\44\1\116\1\115\1\111\1\131\1\113\1\106\1\124\1\114\2\124\2\44"
        u"\1\124\1\44\2\101\1\105\1\106\1\114\1\111\1\114\1\126\1\101\1\44"
        u"\1\102\1\105\1\115\1\104\2\111\1\103\2\105\2\uffff\1\114\1\44\1"
        u"\101\1\44\2\105\1\117\1\uffff\1\44\1\122\1\44\1\117\1\111\1\127"
        u"\1\uffff\1\103\1\122\1\101\1\123\1\106\1\115\1\114\1\103\1\101"
        u"\1\105\1\103\2\101\1\120\1\124\1\123\1\105\1\114\1\101\1\110\1"
        u"\44\1\105\1\44\1\115\1\114\1\102\1\125\1\111\1\uffff\4\105\1\124"
        u"\2\uffff\1\125\1\117\1\105\1\116\1\44\1\111\1\105\1\124\1\103\1"
        u"\114\1\44\1\125\1\uffff\1\123\1\uffff\2\105\1\uffff\1\116\1\107"
        u"\1\115\1\122\1\124\2\105\1\116\1\114\1\105\1\101\1\114\1\44\1\123"
        u"\1\44\2\105\1\116\1\107\1\uffff\1\114\1\116\1\120\1\101\1\117\1"
        u"\116\2\125\1\127\1\124\1\116\1\131\1\uffff\1\103\1\uffff\2\122"
        u"\1\111\1\uffff\1\124\1\uffff\1\122\1\116\1\105\2\44\1\101\1\105"
        u"\1\124\1\123\1\124\1\114\1\111\1\115\1\101\1\113\1\122\1\125\1"
        u"\124\1\44\1\103\1\102\1\44\1\111\1\124\1\125\1\120\1\101\1\120"
        u"\1\44\1\uffff\1\44\1\uffff\1\111\3\44\1\120\1\116\1\44\2\122\1"
        u"\105\1\122\1\130\1\111\1\114\1\122\1\104\1\44\1\uffff\1\124\2\44"
        u"\1\110\1\44\1\uffff\1\125\1\122\1\105\2\122\1\44\1\115\1\101\1"
        u"\131\1\122\1\130\1\101\1\104\1\101\1\122\1\115\1\102\1\uffff\1"
        u"\105\1\uffff\1\103\1\120\1\123\1\107\1\105\2\44\1\124\1\125\1\116"
        u"\1\107\1\125\1\105\1\44\1\125\1\44\1\105\1\132\1\110\2\44\1\116"
        u"\1\44\1\105\1\44\1\105\2\uffff\1\104\1\116\1\105\1\44\1\122\1\111"
        u"\1\124\1\116\1\124\1\44\1\122\1\114\1\105\1\uffff\1\110\1\101\1"
        u"\uffff\1\116\2\123\1\124\1\111\1\105\2\uffff\1\107\3\uffff\1\44"
        u"\1\107\1\uffff\1\123\1\44\1\101\1\124\1\44\1\101\1\114\1\105\1"
        u"\111\1\uffff\1\44\2\uffff\1\44\1\uffff\1\114\1\101\1\124\2\44\1"
        u"\uffff\1\101\1\122\1\44\1\111\1\120\1\123\1\105\1\103\2\105\1\101"
        u"\1\44\1\124\1\117\1\101\1\105\1\44\2\uffff\1\122\2\105\2\44\1\115"
        u"\1\123\1\uffff\1\101\1\uffff\1\44\1\105\1\44\2\uffff\1\103\1\uffff"
        u"\1\44\1\uffff\1\116\1\105\1\124\1\44\1\uffff\1\101\1\103\2\44\1"
        u"\105\1\uffff\1\101\1\124\2\44\1\123\1\103\1\44\1\111\1\44\1\116"
        u"\1\44\1\116\1\uffff\1\44\1\105\1\uffff\1\104\1\44\1\uffff\1\104"
        u"\1\114\2\44\1\101\2\uffff\2\114\1\44\2\uffff\1\44\1\131\1\uffff"
        u"\1\103\1\44\1\105\1\130\1\105\1\116\1\44\1\103\1\uffff\1\44\1\111"
        u"\1\103\1\122\1\uffff\1\101\2\44\2\uffff\2\44\1\114\1\uffff\1\44"
        u"\1\uffff\1\122\1\uffff\2\44\1\137\1\uffff\1\111\1\124\2\uffff\1"
        u"\44\1\102\1\104\1\44\2\uffff\1\105\1\124\1\uffff\1\126\1\uffff"
        u"\1\44\1\uffff\1\44\1\uffff\1\103\1\44\1\uffff\1\44\1\114\2\uffff"
        u"\1\124\2\44\2\uffff\1\44\1\124\1\uffff\3\44\1\103\1\uffff\1\113"
        u"\1\uffff\1\116\1\124\1\44\1\122\4\uffff\1\44\1\uffff\1\105\2\uffff"
        u"\1\104\1\116\1\44\1\uffff\1\114\1\44\1\uffff\2\44\1\105\2\uffff"
        u"\1\124\2\uffff\1\131\1\105\3\uffff\1\44\3\uffff\1\105\1\44\1\124"
        u"\1\111\1\uffff\1\131\1\uffff\1\115\1\111\1\101\1\124\1\uffff\1"
        u"\105\3\uffff\4\44\1\uffff\1\123\1\uffff\1\44\1\117\1\44\1\105\1"
        u"\115\1\124\2\44\4\uffff\1\44\1\uffff\2\116\2\105\3\uffff\1\44\1"
        u"\124\2\44\1\uffff\1\44\1\uffff\1\124\2\uffff\1\101\1\115\1\120"
        u"\1\44\1\uffff"
    )

    DFA26_max = DFA.unpack(
        u"\1\176\1\75\1\uffff\2\76\1\uffff\1\174\1\uffff\1\55\2\uffff\1\52"
        u"\3\uffff\1\71\7\uffff\4\uffff\1\uffff\1\172\1\165\1\171\1\165\1"
        u"\162\1\170\2\162\1\141\1\163\1\157\1\145\1\151\1\141\2\165\1\162"
        u"\1\165\1\157\1\145\1\162\1\163\1\151\1\150\1\47\1\145\27\uffff"
        u"\1\144\4\164\1\172\1\157\1\144\1\164\1\172\1\163\1\162\1\157\1"
        u"\156\1\145\2\164\1\157\1\163\1\160\2\143\1\144\1\163\1\162\1\157"
        u"\1\151\2\157\1\166\3\172\1\156\1\155\1\151\1\171\1\155\1\146\1"
        u"\164\1\154\2\164\2\172\1\164\1\172\1\141\1\151\1\145\1\163\1\167"
        u"\1\151\1\164\1\166\1\151\1\172\1\142\1\145\1\155\1\144\2\151\1"
        u"\154\1\162\1\145\2\uffff\1\154\1\172\1\141\1\172\2\145\1\157\1"
        u"\uffff\1\172\1\162\1\172\1\157\1\151\1\167\1\uffff\1\164\1\162"
        u"\1\141\2\163\1\155\1\165\1\143\2\145\1\143\2\141\1\160\1\164\1"
        u"\163\2\154\1\141\1\150\1\172\1\145\1\172\1\155\1\154\1\142\1\165"
        u"\1\151\1\uffff\1\157\1\145\1\164\1\145\1\164\2\uffff\1\165\1\157"
        u"\1\145\1\156\1\172\1\151\1\145\1\164\1\143\1\154\1\172\1\165\1"
        u"\uffff\1\163\1\uffff\2\145\1\uffff\1\156\1\147\1\155\1\162\1\164"
        u"\2\145\1\156\1\154\1\145\1\141\1\154\1\172\1\163\1\172\2\145\1"
        u"\156\1\147\1\uffff\1\154\1\156\1\160\1\141\1\161\1\156\2\165\1"
        u"\167\1\164\1\162\1\171\1\uffff\1\143\1\uffff\2\162\1\151\1\uffff"
        u"\1\164\1\uffff\1\162\1\156\1\145\2\172\1\141\1\145\1\164\1\163"
        u"\1\164\1\154\1\151\1\155\1\141\1\153\1\162\1\165\1\164\1\172\1"
        u"\143\1\142\1\172\1\151\1\164\1\165\1\160\1\141\1\160\1\172\1\uffff"
        u"\1\172\1\uffff\1\151\3\172\1\160\1\156\1\172\2\162\1\145\1\162"
        u"\1\170\1\151\1\154\1\162\1\144\1\172\1\uffff\1\164\2\172\1\150"
        u"\1\172\1\uffff\1\165\1\162\1\145\2\162\1\172\1\155\1\141\1\171"
        u"\1\162\1\170\1\141\1\144\1\141\1\162\1\155\1\142\1\uffff\1\145"
        u"\1\uffff\1\143\1\160\1\163\1\147\1\145\2\172\1\164\1\165\1\156"
        u"\1\147\1\165\1\145\1\172\1\165\1\172\1\145\1\172\1\150\2\172\1"
        u"\156\1\172\1\145\1\172\1\145\2\uffff\1\144\1\156\1\145\1\172\1"
        u"\162\1\151\1\164\1\156\1\164\1\172\1\162\1\154\1\145\1\uffff\1"
        u"\150\1\141\1\uffff\1\156\2\163\1\164\1\151\1\145\2\uffff\1\147"
        u"\3\uffff\1\172\1\147\1\uffff\1\163\1\172\1\141\1\164\1\172\1\141"
        u"\1\154\1\145\1\151\1\uffff\1\172\2\uffff\1\172\1\uffff\1\154\1"
        u"\141\1\164\2\172\1\uffff\1\141\1\162\1\172\1\151\1\160\1\163\1"
        u"\145\1\143\2\145\1\141\1\172\1\164\1\157\1\141\1\145\1\172\2\uffff"
        u"\1\162\2\145\2\172\1\155\1\163\1\uffff\1\141\1\uffff\1\172\1\145"
        u"\1\172\2\uffff\1\143\1\uffff\1\172\1\uffff\1\156\1\145\1\164\1"
        u"\172\1\uffff\1\141\1\143\2\172\1\145\1\uffff\1\145\1\164\2\172"
        u"\1\163\1\143\1\172\1\151\1\172\1\156\1\172\1\156\1\uffff\1\172"
        u"\1\145\1\uffff\1\144\1\172\1\uffff\1\144\1\154\2\172\1\141\2\uffff"
        u"\2\154\1\172\2\uffff\1\172\1\171\1\uffff\1\143\1\172\1\145\1\170"
        u"\1\145\1\156\1\172\1\143\1\uffff\1\172\1\151\1\143\1\162\1\uffff"
        u"\1\141\2\172\2\uffff\2\172\1\154\1\uffff\1\172\1\uffff\1\162\1"
        u"\uffff\2\172\1\137\1\uffff\1\151\1\164\2\uffff\1\172\1\142\1\144"
        u"\1\172\2\uffff\1\145\1\164\1\uffff\1\166\1\uffff\1\172\1\uffff"
        u"\1\172\1\uffff\1\143\1\172\1\uffff\1\172\1\154\2\uffff\1\164\2"
        u"\172\2\uffff\1\172\1\164\1\uffff\3\172\1\143\1\uffff\1\153\1\uffff"
        u"\1\156\1\164\1\172\1\162\4\uffff\1\172\1\uffff\1\145\2\uffff\1"
        u"\164\1\156\1\172\1\uffff\1\154\1\172\1\uffff\2\172\1\145\2\uffff"
        u"\1\164\2\uffff\1\171\1\145\3\uffff\1\172\3\uffff\1\145\1\172\1"
        u"\164\1\151\1\uffff\1\171\1\uffff\1\155\1\151\1\141\1\164\1\uffff"
        u"\1\145\3\uffff\4\172\1\uffff\1\163\1\uffff\1\172\1\157\1\172\1"
        u"\145\1\155\1\164\2\172\4\uffff\1\172\1\uffff\2\156\2\145\3\uffff"
        u"\1\172\1\164\2\172\1\uffff\1\172\1\uffff\1\164\2\uffff\1\141\1"
        u"\155\1\160\1\172\1\uffff"
    )

    DFA26_accept = DFA.unpack(
        u"\2\uffff\1\3\2\uffff\1\13\1\uffff\1\16\1\uffff\1\20\1\21\1\uffff"
        u"\1\23\1\24\1\25\1\uffff\1\27\1\30\1\31\1\32\1\33\1\34\1\35\4\uffff"
        u"\1\42\32\uffff\1\u0099\1\u009d\1\2\1\1\1\4\1\6\1\11\1\5\1\10\1"
        u"\12\1\7\1\15\1\14\1\17\1\22\1\26\1\u009b\1\36\1\u0098\1\37\1\40"
        u"\1\41\1\43\102\uffff\1\u009c\1\u009a\7\uffff\1\53\6\uffff\1\62"
        u"\34\uffff\1\134\5\uffff\1\131\1\145\14\uffff\1\161\1\uffff\1\164"
        u"\2\uffff\1\163\23\uffff\1\u008b\14\uffff\1\52\1\uffff\1\47\3\uffff"
        u"\1\54\1\uffff\1\45\35\uffff\1\114\1\uffff\1\123\21\uffff\1\150"
        u"\5\uffff\1\156\21\uffff\1\u0084\1\uffff\1\u0087\32\uffff\1\65\1"
        u"\64\15\uffff\1\106\2\uffff\1\111\6\uffff\1\112\1\113\1\uffff\1"
        u"\125\1\122\1\126\2\uffff\1\144\11\uffff\1\147\1\uffff\1\152\1\151"
        u"\1\uffff\1\160\5\uffff\1\167\21\uffff\1\u008a\1\u0089\7\uffff\1"
        u"\u0094\1\uffff\1\u0096\3\uffff\1\50\1\46\1\uffff\1\44\1\uffff\1"
        u"\60\4\uffff\1\75\5\uffff\1\66\14\uffff\1\127\2\uffff\1\140\2\uffff"
        u"\1\135\5\uffff\1\153\1\154\3\uffff\1\165\1\166\2\uffff\1\172\10"
        u"\uffff\1\173\4\uffff\1\u0088\3\uffff\1\u008e\1\u0091\3\uffff\1"
        u"\u0097\1\uffff\1\55\1\uffff\1\57\3\uffff\1\74\2\uffff\1\71\1\70"
        u"\4\uffff\1\105\1\107\2\uffff\1\120\1\uffff\1\116\1\uffff\1\115"
        u"\1\uffff\1\130\2\uffff\1\141\2\uffff\1\146\1\132\3\uffff\1\162"
        u"\1\170\2\uffff\1\175\4\uffff\1\u0080\1\uffff\1\u0086\4\uffff\1"
        u"\u0090\1\u008f\1\u0092\1\u0093\1\uffff\1\51\1\uffff\1\61\1\63\3"
        u"\uffff\1\67\2\uffff\1\102\3\uffff\1\121\1\124\1\uffff\1\142\1\136"
        u"\2\uffff\1\157\1\155\1\171\1\uffff\1\177\1\176\1\u0081\4\uffff"
        u"\1\u008d\1\uffff\1\u0095\4\uffff\1\72\1\uffff\1\104\1\101\1\110"
        u"\4\uffff\1\u0082\1\uffff\1\u0083\10\uffff\1\117\1\143\1\137\1\133"
        u"\1\uffff\1\u0085\4\uffff\1\73\1\103\1\174\4\uffff\1\u008c\1\uffff"
        u"\1\76\1\uffff\1\77\1\56\4\uffff\1\100"
    )

    DFA26_special = DFA.unpack(
        u"\27\uffff\1\1\1\2\1\0\1\3\u027c\uffff"
    )

    DFA26_transition = [
        DFA.unpack(u"\2\67\1\uffff\2\67\22\uffff\1\67\1\2\1\27\1\uffff\1"
                   u"\26\1\15\1\5\1\30\1\21\1\22\1\12\1\7\1\20\1\10\1\17\1\13\12\65"
                   u"\1\24\1\16\1\3\1\1\1\4\1\23\1\25\1\35\1\36\1\37\1\40\1\41\1\42"
                   u"\1\43\1\44\1\45\1\46\1\47\1\50\1\51\1\52\1\53\1\54\1\55\1\56\1"
                   u"\57\1\60\1\61\1\62\1\63\1\64\2\66\1\32\1\14\1\33\1\uffff\1\34\1"
                   u"\31\1\35\1\36\1\37\1\40\1\41\1\42\1\43\1\44\1\45\1\46\1\47\1\50"
                   u"\1\51\1\52\1\53\1\54\1\55\1\56\1\57\1\60\1\61\1\62\1\63\1\64\2"
                   u"\66\1\uffff\1\6\1\uffff\1\11"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\74\1\73\1\72"),
        DFA.unpack(u"\1\76\1\77"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\106"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\0\110"),
        DFA.unpack(u"\0\110"),
        DFA.unpack(u"\0\66"),
        DFA.unpack(u"\133\66\1\uffff\uffa4\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\123\1\uffff\1\124\1\uffff\1\120\5\uffff\1\117\1"
                   u"\uffff\1\115\4\uffff\1\122\1\116\1\121\14\uffff\1\123\1\uffff\1"
                   u"\124\1\uffff\1\120\5\uffff\1\117\1\uffff\1\115\4\uffff\1\122\1"
                   u"\116\1\121"),
        DFA.unpack(u"\1\125\23\uffff\1\126\13\uffff\1\125\23\uffff\1\126"),
        DFA.unpack(u"\1\127\6\uffff\1\133\6\uffff\1\132\2\uffff\1\131\2"
                   u"\uffff\1\130\13\uffff\1\127\6\uffff\1\133\6\uffff\1\132\2\uffff"
                   u"\1\131\2\uffff\1\130"),
        DFA.unpack(u"\1\135\3\uffff\1\134\3\uffff\1\137\10\uffff\1\136\16"
                   u"\uffff\1\135\3\uffff\1\134\3\uffff\1\137\10\uffff\1\136"),
        DFA.unpack(u"\1\142\12\uffff\1\144\1\uffff\1\143\4\uffff\1\141\4"
                   u"\uffff\1\140\10\uffff\1\142\12\uffff\1\144\1\uffff\1\143\4\uffff"
                   u"\1\141\4\uffff\1\140"),
        DFA.unpack(u"\1\147\15\uffff\1\145\2\uffff\1\146\16\uffff\1\147"
                   u"\15\uffff\1\145\2\uffff\1\146"),
        DFA.unpack(u"\1\150\5\uffff\1\151\31\uffff\1\150\5\uffff\1\151"),
        DFA.unpack(u"\1\152\37\uffff\1\152"),
        DFA.unpack(u"\1\154\1\156\5\uffff\1\157\1\153\4\uffff\1\155\22\uffff"
                   u"\1\154\1\156\5\uffff\1\157\1\153\4\uffff\1\155"),
        DFA.unpack(u"\1\160\37\uffff\1\160"),
        DFA.unpack(u"\1\161\37\uffff\1\161"),
        DFA.unpack(u"\1\163\3\uffff\1\162\33\uffff\1\163\3\uffff\1\162"),
        DFA.unpack(u"\1\164\37\uffff\1\164"),
        DFA.unpack(u"\1\167\15\uffff\1\166\5\uffff\1\165\13\uffff\1\167"
                   u"\15\uffff\1\166\5\uffff\1\165"),
        DFA.unpack(u"\1\170\7\uffff\1\173\3\uffff\1\171\2\uffff\1\172\20"
                   u"\uffff\1\170\7\uffff\1\173\3\uffff\1\171\2\uffff\1\172"),
        DFA.unpack(u"\1\174\5\uffff\1\175\31\uffff\1\174\5\uffff\1\175"),
        DFA.unpack(u"\1\176\37\uffff\1\176"),
        DFA.unpack(u"\1\u0081\3\uffff\1\177\11\uffff\1\u0080\21\uffff\1"
                   u"\u0081\3\uffff\1\177\11\uffff\1\u0080"),
        DFA.unpack(u"\1\u0083\3\uffff\1\u0082\33\uffff\1\u0083\3\uffff\1"
                   u"\u0082"),
        DFA.unpack(u"\1\u0086\3\uffff\1\u0088\2\uffff\1\u0087\6\uffff\1"
                   u"\u0085\2\uffff\1\u0084\16\uffff\1\u0086\3\uffff\1\u0088\2\uffff"
                   u"\1\u0087\6\uffff\1\u0085\2\uffff\1\u0084"),
        DFA.unpack(u"\1\u008a\1\uffff\1\u0089\2\uffff\1\u008b\32\uffff\1"
                   u"\u008a\1\uffff\1\u0089\2\uffff\1\u008b"),
        DFA.unpack(u"\1\u008c\7\uffff\1\u008d\27\uffff\1\u008c\7\uffff\1"
                   u"\u008d"),
        DFA.unpack(u"\1\u008e\37\uffff\1\u008e"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\1\106\1\uffff\12\65\13\uffff\1\106\37\uffff\1\106"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0091\2\uffff\1\u0092\34\uffff\1\u0091\2\uffff\1"
                   u"\u0092"),
        DFA.unpack(u"\1\u0093\37\uffff\1\u0093"),
        DFA.unpack(u"\1\u0094\7\uffff\1\u0095\27\uffff\1\u0094\7\uffff\1"
                   u"\u0095"),
        DFA.unpack(u"\1\u0096\37\uffff\1\u0096"),
        DFA.unpack(u"\1\u0097\37\uffff\1\u0097"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\2\66\1\u0099\27\66\4\uffff"
                   u"\1\66\1\uffff\2\66\1\u0099\27\66"),
        DFA.unpack(u"\1\u009a\37\uffff\1\u009a"),
        DFA.unpack(u"\1\u009b\37\uffff\1\u009b"),
        DFA.unpack(u"\1\u009c\1\u009d\14\uffff\1\u009e\21\uffff\1\u009c"
                   u"\1\u009d\14\uffff\1\u009e"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u00a0\37\uffff\1\u00a0"),
        DFA.unpack(u"\1\u00a1\37\uffff\1\u00a1"),
        DFA.unpack(u"\1\u00a2\11\uffff\1\u00a3\25\uffff\1\u00a2\11\uffff"
                   u"\1\u00a3"),
        DFA.unpack(u"\1\u00a6\1\u00a5\1\u00a4\35\uffff\1\u00a6\1\u00a5\1"
                   u"\u00a4"),
        DFA.unpack(u"\1\u00a7\37\uffff\1\u00a7"),
        DFA.unpack(u"\1\u00a8\5\uffff\1\u00a9\6\uffff\1\u00aa\1\u00ab\21"
                   u"\uffff\1\u00a8\5\uffff\1\u00a9\6\uffff\1\u00aa\1\u00ab"),
        DFA.unpack(u"\1\u00ac\37\uffff\1\u00ac"),
        DFA.unpack(u"\1\u00ad\37\uffff\1\u00ad"),
        DFA.unpack(u"\1\u00ae\37\uffff\1\u00ae"),
        DFA.unpack(u"\1\u00b0\5\uffff\1\u00af\6\uffff\1\u00b1\22\uffff\1"
                   u"\u00b0\5\uffff\1\u00af\6\uffff\1\u00b1"),
        DFA.unpack(u"\1\u00b2\37\uffff\1\u00b2"),
        DFA.unpack(u"\1\u00b3\37\uffff\1\u00b3"),
        DFA.unpack(u"\1\u00b4\37\uffff\1\u00b4"),
        DFA.unpack(u"\1\u00b5\37\uffff\1\u00b5"),
        DFA.unpack(u"\1\u00b6\37\uffff\1\u00b6"),
        DFA.unpack(u"\1\u00b7\37\uffff\1\u00b7"),
        DFA.unpack(u"\1\u00b8\37\uffff\1\u00b8"),
        DFA.unpack(u"\1\u00b9\37\uffff\1\u00b9"),
        DFA.unpack(u"\1\u00ba\37\uffff\1\u00ba"),
        DFA.unpack(u"\1\u00bb\37\uffff\1\u00bb"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\3\66\1\u00c0\4\66\1\u00c1"
                   u"\4\66\1\u00be\4\66\1\u00bf\1\u00bd\6\66\4\uffff\1\66\1\uffff\3"
                   u"\66\1\u00c0\4\66\1\u00c1\4\66\1\u00be\4\66\1\u00bf\1\u00bd\6\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\15\66\1\u00c4\14\66\4"
                   u"\uffff\1\66\1\uffff\15\66\1\u00c4\14\66"),
        DFA.unpack(u"\1\u00c5\37\uffff\1\u00c5"),
        DFA.unpack(u"\1\u00c6\37\uffff\1\u00c6"),
        DFA.unpack(u"\1\u00c7\37\uffff\1\u00c7"),
        DFA.unpack(u"\1\u00c8\37\uffff\1\u00c8"),
        DFA.unpack(u"\1\u00ca\1\uffff\1\u00c9\35\uffff\1\u00ca\1\uffff\1"
                   u"\u00c9"),
        DFA.unpack(u"\1\u00cb\37\uffff\1\u00cb"),
        DFA.unpack(u"\1\u00cc\37\uffff\1\u00cc"),
        DFA.unpack(u"\1\u00cd\37\uffff\1\u00cd"),
        DFA.unpack(u"\1\u00ce\37\uffff\1\u00ce"),
        DFA.unpack(u"\1\u00cf\37\uffff\1\u00cf"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\5\66\1\u00d1\24\66\4\uffff"
                   u"\1\66\1\uffff\5\66\1\u00d1\24\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\3\66\1\u00d3\26\66\4\uffff"
                   u"\1\66\1\uffff\3\66\1\u00d3\26\66"),
        DFA.unpack(u"\1\u00d4\37\uffff\1\u00d4"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u00d6\37\uffff\1\u00d6"),
        DFA.unpack(u"\1\u00d7\7\uffff\1\u00d8\27\uffff\1\u00d7\7\uffff\1"
                   u"\u00d8"),
        DFA.unpack(u"\1\u00d9\37\uffff\1\u00d9"),
        DFA.unpack(u"\1\u00df\1\u00db\1\uffff\1\u00dd\2\uffff\1\u00dc\1"
                   u"\uffff\1\u00e0\1\uffff\1\u00de\2\uffff\1\u00da\22\uffff\1\u00df"
                   u"\1\u00db\1\uffff\1\u00dd\2\uffff\1\u00dc\1\uffff\1\u00e0\1\uffff"
                   u"\1\u00de\2\uffff\1\u00da"),
        DFA.unpack(u"\1\u00e1\12\uffff\1\u00e2\24\uffff\1\u00e1\12\uffff"
                   u"\1\u00e2"),
        DFA.unpack(u"\1\u00e3\37\uffff\1\u00e3"),
        DFA.unpack(u"\1\u00e5\7\uffff\1\u00e4\27\uffff\1\u00e5\7\uffff\1"
                   u"\u00e4"),
        DFA.unpack(u"\1\u00e6\37\uffff\1\u00e6"),
        DFA.unpack(u"\1\u00e7\7\uffff\1\u00e8\27\uffff\1\u00e7\7\uffff\1"
                   u"\u00e8"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u00ea\37\uffff\1\u00ea"),
        DFA.unpack(u"\1\u00eb\37\uffff\1\u00eb"),
        DFA.unpack(u"\1\u00ec\37\uffff\1\u00ec"),
        DFA.unpack(u"\1\u00ed\37\uffff\1\u00ed"),
        DFA.unpack(u"\1\u00ee\37\uffff\1\u00ee"),
        DFA.unpack(u"\1\u00ef\37\uffff\1\u00ef"),
        DFA.unpack(u"\1\u00f0\10\uffff\1\u00f1\26\uffff\1\u00f0\10\uffff"
                   u"\1\u00f1"),
        DFA.unpack(u"\1\u00f2\14\uffff\1\u00f3\22\uffff\1\u00f2\14\uffff"
                   u"\1\u00f3"),
        DFA.unpack(u"\1\u00f4\37\uffff\1\u00f4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00f5\37\uffff\1\u00f5"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u00f7\37\uffff\1\u00f7"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u00f9\37\uffff\1\u00f9"),
        DFA.unpack(u"\1\u00fa\37\uffff\1\u00fa"),
        DFA.unpack(u"\1\u00fb\37\uffff\1\u00fb"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u00fd\37\uffff\1\u00fd"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u00ff\37\uffff\1\u00ff"),
        DFA.unpack(u"\1\u0100\37\uffff\1\u0100"),
        DFA.unpack(u"\1\u0101\37\uffff\1\u0101"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0104\1\uffff\1\u0103\16\uffff\1\u0102\16\uffff"
                   u"\1\u0104\1\uffff\1\u0103\16\uffff\1\u0102"),
        DFA.unpack(u"\1\u0105\37\uffff\1\u0105"),
        DFA.unpack(u"\1\u0106\37\uffff\1\u0106"),
        DFA.unpack(u"\1\u0107\37\uffff\1\u0107"),
        DFA.unpack(u"\1\u0109\14\uffff\1\u0108\22\uffff\1\u0109\14\uffff"
                   u"\1\u0108"),
        DFA.unpack(u"\1\u010a\37\uffff\1\u010a"),
        DFA.unpack(u"\1\u010c\10\uffff\1\u010b\26\uffff\1\u010c\10\uffff"
                   u"\1\u010b"),
        DFA.unpack(u"\1\u010d\37\uffff\1\u010d"),
        DFA.unpack(u"\1\u010f\3\uffff\1\u010e\33\uffff\1\u010f\3\uffff\1"
                   u"\u010e"),
        DFA.unpack(u"\1\u0110\37\uffff\1\u0110"),
        DFA.unpack(u"\1\u0111\37\uffff\1\u0111"),
        DFA.unpack(u"\1\u0112\37\uffff\1\u0112"),
        DFA.unpack(u"\1\u0113\37\uffff\1\u0113"),
        DFA.unpack(u"\1\u0114\37\uffff\1\u0114"),
        DFA.unpack(u"\1\u0115\37\uffff\1\u0115"),
        DFA.unpack(u"\1\u0116\37\uffff\1\u0116"),
        DFA.unpack(u"\1\u0118\6\uffff\1\u0117\30\uffff\1\u0118\6\uffff\1"
                   u"\u0117"),
        DFA.unpack(u"\1\u0119\37\uffff\1\u0119"),
        DFA.unpack(u"\1\u011a\37\uffff\1\u011a"),
        DFA.unpack(u"\1\u011b\37\uffff\1\u011b"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u011d\37\uffff\1\u011d"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\4\66\1\u011f\25\66\4\uffff"
                   u"\1\66\1\uffff\4\66\1\u011f\25\66"),
        DFA.unpack(u"\1\u0120\37\uffff\1\u0120"),
        DFA.unpack(u"\1\u0121\37\uffff\1\u0121"),
        DFA.unpack(u"\1\u0122\37\uffff\1\u0122"),
        DFA.unpack(u"\1\u0123\37\uffff\1\u0123"),
        DFA.unpack(u"\1\u0124\37\uffff\1\u0124"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0126\11\uffff\1\u0125\25\uffff\1\u0126\11\uffff"
                   u"\1\u0125"),
        DFA.unpack(u"\1\u0127\37\uffff\1\u0127"),
        DFA.unpack(u"\1\u0129\16\uffff\1\u0128\20\uffff\1\u0129\16\uffff"
                   u"\1\u0128"),
        DFA.unpack(u"\1\u012a\37\uffff\1\u012a"),
        DFA.unpack(u"\1\u012b\37\uffff\1\u012b"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u012c\37\uffff\1\u012c"),
        DFA.unpack(u"\1\u012d\37\uffff\1\u012d"),
        DFA.unpack(u"\1\u012e\37\uffff\1\u012e"),
        DFA.unpack(u"\1\u012f\37\uffff\1\u012f"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0131\37\uffff\1\u0131"),
        DFA.unpack(u"\1\u0132\37\uffff\1\u0132"),
        DFA.unpack(u"\1\u0133\37\uffff\1\u0133"),
        DFA.unpack(u"\1\u0134\37\uffff\1\u0134"),
        DFA.unpack(u"\1\u0135\37\uffff\1\u0135"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\15\66\1\u0137\14\66\4"
                   u"\uffff\1\66\1\uffff\15\66\1\u0137\14\66"),
        DFA.unpack(u"\1\u0138\37\uffff\1\u0138"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0139\37\uffff\1\u0139"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u013a\37\uffff\1\u013a"),
        DFA.unpack(u"\1\u013b\37\uffff\1\u013b"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u013c\37\uffff\1\u013c"),
        DFA.unpack(u"\1\u013d\37\uffff\1\u013d"),
        DFA.unpack(u"\1\u013e\37\uffff\1\u013e"),
        DFA.unpack(u"\1\u013f\37\uffff\1\u013f"),
        DFA.unpack(u"\1\u0140\37\uffff\1\u0140"),
        DFA.unpack(u"\1\u0141\37\uffff\1\u0141"),
        DFA.unpack(u"\1\u0142\37\uffff\1\u0142"),
        DFA.unpack(u"\1\u0143\37\uffff\1\u0143"),
        DFA.unpack(u"\1\u0144\37\uffff\1\u0144"),
        DFA.unpack(u"\1\u0145\37\uffff\1\u0145"),
        DFA.unpack(u"\1\u0146\37\uffff\1\u0146"),
        DFA.unpack(u"\1\u0147\37\uffff\1\u0147"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0149\37\uffff\1\u0149"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u014b\37\uffff\1\u014b"),
        DFA.unpack(u"\1\u014c\37\uffff\1\u014c"),
        DFA.unpack(u"\1\u014d\37\uffff\1\u014d"),
        DFA.unpack(u"\1\u014e\37\uffff\1\u014e"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u014f\37\uffff\1\u014f"),
        DFA.unpack(u"\1\u0150\37\uffff\1\u0150"),
        DFA.unpack(u"\1\u0151\37\uffff\1\u0151"),
        DFA.unpack(u"\1\u0152\37\uffff\1\u0152"),
        DFA.unpack(u"\1\u0154\1\uffff\1\u0153\35\uffff\1\u0154\1\uffff\1"
                   u"\u0153"),
        DFA.unpack(u"\1\u0155\37\uffff\1\u0155"),
        DFA.unpack(u"\1\u0156\37\uffff\1\u0156"),
        DFA.unpack(u"\1\u0157\37\uffff\1\u0157"),
        DFA.unpack(u"\1\u0158\37\uffff\1\u0158"),
        DFA.unpack(u"\1\u0159\37\uffff\1\u0159"),
        DFA.unpack(u"\1\u015a\3\uffff\1\u015b\33\uffff\1\u015a\3\uffff\1"
                   u"\u015b"),
        DFA.unpack(u"\1\u015c\37\uffff\1\u015c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u015d\37\uffff\1\u015d"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u015e\37\uffff\1\u015e"),
        DFA.unpack(u"\1\u015f\37\uffff\1\u015f"),
        DFA.unpack(u"\1\u0160\37\uffff\1\u0160"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0161\37\uffff\1\u0161"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0162\37\uffff\1\u0162"),
        DFA.unpack(u"\1\u0163\37\uffff\1\u0163"),
        DFA.unpack(u"\1\u0164\37\uffff\1\u0164"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0167\37\uffff\1\u0167"),
        DFA.unpack(u"\1\u0168\37\uffff\1\u0168"),
        DFA.unpack(u"\1\u0169\37\uffff\1\u0169"),
        DFA.unpack(u"\1\u016a\37\uffff\1\u016a"),
        DFA.unpack(u"\1\u016b\37\uffff\1\u016b"),
        DFA.unpack(u"\1\u016c\37\uffff\1\u016c"),
        DFA.unpack(u"\1\u016d\37\uffff\1\u016d"),
        DFA.unpack(u"\1\u016e\37\uffff\1\u016e"),
        DFA.unpack(u"\1\u016f\37\uffff\1\u016f"),
        DFA.unpack(u"\1\u0170\37\uffff\1\u0170"),
        DFA.unpack(u"\1\u0171\37\uffff\1\u0171"),
        DFA.unpack(u"\1\u0172\37\uffff\1\u0172"),
        DFA.unpack(u"\1\u0173\37\uffff\1\u0173"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0175\37\uffff\1\u0175"),
        DFA.unpack(u"\1\u0176\37\uffff\1\u0176"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0178\37\uffff\1\u0178"),
        DFA.unpack(u"\1\u0179\37\uffff\1\u0179"),
        DFA.unpack(u"\1\u017a\37\uffff\1\u017a"),
        DFA.unpack(u"\1\u017b\37\uffff\1\u017b"),
        DFA.unpack(u"\1\u017c\37\uffff\1\u017c"),
        DFA.unpack(u"\1\u017d\37\uffff\1\u017d"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0180\37\uffff\1\u0180"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0184\37\uffff\1\u0184"),
        DFA.unpack(u"\1\u0185\37\uffff\1\u0185"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0187\37\uffff\1\u0187"),
        DFA.unpack(u"\1\u0188\37\uffff\1\u0188"),
        DFA.unpack(u"\1\u0189\37\uffff\1\u0189"),
        DFA.unpack(u"\1\u018a\37\uffff\1\u018a"),
        DFA.unpack(u"\1\u018b\37\uffff\1\u018b"),
        DFA.unpack(u"\1\u018c\37\uffff\1\u018c"),
        DFA.unpack(u"\1\u018d\37\uffff\1\u018d"),
        DFA.unpack(u"\1\u018e\37\uffff\1\u018e"),
        DFA.unpack(u"\1\u018f\37\uffff\1\u018f"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0191\37\uffff\1\u0191"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0194\37\uffff\1\u0194"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0196\37\uffff\1\u0196"),
        DFA.unpack(u"\1\u0197\37\uffff\1\u0197"),
        DFA.unpack(u"\1\u0198\37\uffff\1\u0198"),
        DFA.unpack(u"\1\u0199\37\uffff\1\u0199"),
        DFA.unpack(u"\1\u019a\37\uffff\1\u019a"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u019c\37\uffff\1\u019c"),
        DFA.unpack(u"\1\u019d\37\uffff\1\u019d"),
        DFA.unpack(u"\1\u019e\37\uffff\1\u019e"),
        DFA.unpack(u"\1\u019f\37\uffff\1\u019f"),
        DFA.unpack(u"\1\u01a0\37\uffff\1\u01a0"),
        DFA.unpack(u"\1\u01a1\37\uffff\1\u01a1"),
        DFA.unpack(u"\1\u01a2\37\uffff\1\u01a2"),
        DFA.unpack(u"\1\u01a3\37\uffff\1\u01a3"),
        DFA.unpack(u"\1\u01a4\37\uffff\1\u01a4"),
        DFA.unpack(u"\1\u01a5\37\uffff\1\u01a5"),
        DFA.unpack(u"\1\u01a6\37\uffff\1\u01a6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01a7\37\uffff\1\u01a7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01a8\37\uffff\1\u01a8"),
        DFA.unpack(u"\1\u01a9\37\uffff\1\u01a9"),
        DFA.unpack(u"\1\u01aa\37\uffff\1\u01aa"),
        DFA.unpack(u"\1\u01ab\37\uffff\1\u01ab"),
        DFA.unpack(u"\1\u01ac\37\uffff\1\u01ac"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\16\66\1\u01af\13\66\4"
                   u"\uffff\1\66\1\uffff\16\66\1\u01af\13\66"),
        DFA.unpack(u"\1\u01b0\37\uffff\1\u01b0"),
        DFA.unpack(u"\1\u01b1\37\uffff\1\u01b1"),
        DFA.unpack(u"\1\u01b2\37\uffff\1\u01b2"),
        DFA.unpack(u"\1\u01b3\37\uffff\1\u01b3"),
        DFA.unpack(u"\1\u01b4\37\uffff\1\u01b4"),
        DFA.unpack(u"\1\u01b5\37\uffff\1\u01b5"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u01b7\37\uffff\1\u01b7"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u01b9\37\uffff\1\u01b9"),
        DFA.unpack(u"\1\u01ba\37\uffff\1\u01ba"),
        DFA.unpack(u"\1\u01bb\37\uffff\1\u01bb"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u01be\37\uffff\1\u01be"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u01c0\37\uffff\1\u01c0"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u01c2\37\uffff\1\u01c2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01c3\37\uffff\1\u01c3"),
        DFA.unpack(u"\1\u01c4\37\uffff\1\u01c4"),
        DFA.unpack(u"\1\u01c5\37\uffff\1\u01c5"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u01c7\37\uffff\1\u01c7"),
        DFA.unpack(u"\1\u01c8\37\uffff\1\u01c8"),
        DFA.unpack(u"\1\u01c9\37\uffff\1\u01c9"),
        DFA.unpack(u"\1\u01ca\37\uffff\1\u01ca"),
        DFA.unpack(u"\1\u01cb\37\uffff\1\u01cb"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u01cd\37\uffff\1\u01cd"),
        DFA.unpack(u"\1\u01ce\37\uffff\1\u01ce"),
        DFA.unpack(u"\1\u01cf\37\uffff\1\u01cf"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01d0\37\uffff\1\u01d0"),
        DFA.unpack(u"\1\u01d1\37\uffff\1\u01d1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01d2\37\uffff\1\u01d2"),
        DFA.unpack(u"\1\u01d3\37\uffff\1\u01d3"),
        DFA.unpack(u"\1\u01d4\37\uffff\1\u01d4"),
        DFA.unpack(u"\1\u01d5\37\uffff\1\u01d5"),
        DFA.unpack(u"\1\u01d6\37\uffff\1\u01d6"),
        DFA.unpack(u"\1\u01d7\37\uffff\1\u01d7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01d8\37\uffff\1\u01d8"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u01da\37\uffff\1\u01da"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01db\37\uffff\1\u01db"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u01dd\37\uffff\1\u01dd"),
        DFA.unpack(u"\1\u01de\37\uffff\1\u01de"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\4\66\1\u01e0\25\66\4\uffff"
                   u"\1\66\1\uffff\4\66\1\u01e0\25\66"),
        DFA.unpack(u"\1\u01e1\37\uffff\1\u01e1"),
        DFA.unpack(u"\1\u01e2\37\uffff\1\u01e2"),
        DFA.unpack(u"\1\u01e3\37\uffff\1\u01e3"),
        DFA.unpack(u"\1\u01e4\37\uffff\1\u01e4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01e7\37\uffff\1\u01e7"),
        DFA.unpack(u"\1\u01e8\37\uffff\1\u01e8"),
        DFA.unpack(u"\1\u01e9\37\uffff\1\u01e9"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01ec\37\uffff\1\u01ec"),
        DFA.unpack(u"\1\u01ed\37\uffff\1\u01ed"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u01ef\37\uffff\1\u01ef"),
        DFA.unpack(u"\1\u01f0\37\uffff\1\u01f0"),
        DFA.unpack(u"\1\u01f1\37\uffff\1\u01f1"),
        DFA.unpack(u"\1\u01f2\37\uffff\1\u01f2"),
        DFA.unpack(u"\1\u01f3\37\uffff\1\u01f3"),
        DFA.unpack(u"\1\u01f4\37\uffff\1\u01f4"),
        DFA.unpack(u"\1\u01f5\37\uffff\1\u01f5"),
        DFA.unpack(u"\1\u01f6\37\uffff\1\u01f6"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u01f8\37\uffff\1\u01f8"),
        DFA.unpack(u"\1\u01f9\37\uffff\1\u01f9"),
        DFA.unpack(u"\1\u01fa\37\uffff\1\u01fa"),
        DFA.unpack(u"\1\u01fb\37\uffff\1\u01fb"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01fd\37\uffff\1\u01fd"),
        DFA.unpack(u"\1\u01fe\37\uffff\1\u01fe"),
        DFA.unpack(u"\1\u01ff\37\uffff\1\u01ff"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0202\37\uffff\1\u0202"),
        DFA.unpack(u"\1\u0203\37\uffff\1\u0203"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0204\37\uffff\1\u0204"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0206\37\uffff\1\u0206"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0208\37\uffff\1\u0208"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u020a\37\uffff\1\u020a"),
        DFA.unpack(u"\1\u020b\37\uffff\1\u020b"),
        DFA.unpack(u"\1\u020c\37\uffff\1\u020c"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u020e\37\uffff\1\u020e"),
        DFA.unpack(u"\1\u020f\37\uffff\1\u020f"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0212\37\uffff\1\u0212"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0213\3\uffff\1\u0214\33\uffff\1\u0213\3\uffff\1"
                   u"\u0214"),
        DFA.unpack(u"\1\u0215\37\uffff\1\u0215"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0218\37\uffff\1\u0218"),
        DFA.unpack(u"\1\u0219\37\uffff\1\u0219"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u021b\37\uffff\1\u021b"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u021d\37\uffff\1\u021d"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u021f\37\uffff\1\u021f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0221\37\uffff\1\u0221"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0222\37\uffff\1\u0222"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0224\37\uffff\1\u0224"),
        DFA.unpack(u"\1\u0225\37\uffff\1\u0225"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0228\37\uffff\1\u0228"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0229\37\uffff\1\u0229"),
        DFA.unpack(u"\1\u022a\37\uffff\1\u022a"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u022d\37\uffff\1\u022d"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u022e\37\uffff\1\u022e"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0230\37\uffff\1\u0230"),
        DFA.unpack(u"\1\u0231\37\uffff\1\u0231"),
        DFA.unpack(u"\1\u0232\37\uffff\1\u0232"),
        DFA.unpack(u"\1\u0233\37\uffff\1\u0233"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0235\37\uffff\1\u0235"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0237\37\uffff\1\u0237"),
        DFA.unpack(u"\1\u0238\37\uffff\1\u0238"),
        DFA.unpack(u"\1\u0239\37\uffff\1\u0239"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u023a\37\uffff\1\u023a"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u023f\37\uffff\1\u023f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0241\37\uffff\1\u0241"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0244"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0245\37\uffff\1\u0245"),
        DFA.unpack(u"\1\u0246\37\uffff\1\u0246"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0248\37\uffff\1\u0248"),
        DFA.unpack(u"\1\u0249\37\uffff\1\u0249"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u024b\37\uffff\1\u024b"),
        DFA.unpack(u"\1\u024c\37\uffff\1\u024c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u024d\37\uffff\1\u024d"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0250\37\uffff\1\u0250"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0253\37\uffff\1\u0253"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0254\37\uffff\1\u0254"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0258\37\uffff\1\u0258"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u025c\37\uffff\1\u025c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u025d\37\uffff\1\u025d"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u025e\37\uffff\1\u025e"),
        DFA.unpack(u"\1\u025f\37\uffff\1\u025f"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0261\37\uffff\1\u0261"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0263\37\uffff\1\u0263"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0265\17\uffff\1\u0264\17\uffff\1\u0265\17\uffff"
                   u"\1\u0264"),
        DFA.unpack(u"\1\u0266\37\uffff\1\u0266"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0268\37\uffff\1\u0268"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u026c\37\uffff\1\u026c"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u026d\37\uffff\1\u026d"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u026e\37\uffff\1\u026e"),
        DFA.unpack(u"\1\u026f\37\uffff\1\u026f"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0271\37\uffff\1\u0271"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0273\37\uffff\1\u0273"),
        DFA.unpack(u"\1\u0274\37\uffff\1\u0274"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0275\37\uffff\1\u0275"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0276\37\uffff\1\u0276"),
        DFA.unpack(u"\1\u0277\37\uffff\1\u0277"),
        DFA.unpack(u"\1\u0278\37\uffff\1\u0278"),
        DFA.unpack(u"\1\u0279\37\uffff\1\u0279"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u027a\37\uffff\1\u027a"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u027f\37\uffff\1\u027f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0281\37\uffff\1\u0281"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u0282\37\uffff\1\u0282"),
        DFA.unpack(u"\1\u0283\37\uffff\1\u0283"),
        DFA.unpack(u"\1\u0284\37\uffff\1\u0284"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0288\37\uffff\1\u0288"),
        DFA.unpack(u"\1\u0289\37\uffff\1\u0289"),
        DFA.unpack(u"\1\u028a\37\uffff\1\u028a"),
        DFA.unpack(u"\1\u028b\37\uffff\1\u028b"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"\1\u028d\37\uffff\1\u028d"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\22\66\1\u028f\7\66\4\uffff"
                   u"\1\66\1\uffff\22\66\1\u028f\7\66"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0292\37\uffff\1\u0292"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0293\37\uffff\1\u0293"),
        DFA.unpack(u"\1\u0294\37\uffff\1\u0294"),
        DFA.unpack(u"\1\u0295\37\uffff\1\u0295"),
        DFA.unpack(u"\1\66\13\uffff\12\66\7\uffff\32\66\4\uffff\1\66\1\uffff"
                   u"\32\66"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #26

    class DFA26(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0:
                LA26_25 = input.LA(1)

                s = -1
                if ((0 <= LA26_25 <= 65535)):
                    s = 54

                else:
                    s = 74

                if s >= 0:
                    return s
            elif s == 1:
                LA26_23 = input.LA(1)

                s = -1
                if ((0 <= LA26_23 <= 65535)):
                    s = 72

                else:
                    s = 71

                if s >= 0:
                    return s
            elif s == 2:
                LA26_24 = input.LA(1)

                s = -1
                if ((0 <= LA26_24 <= 65535)):
                    s = 72

                else:
                    s = 73

                if s >= 0:
                    return s
            elif s == 3:
                LA26_26 = input.LA(1)

                s = -1
                if ((0 <= LA26_26 <= 90) or (92 <= LA26_26 <= 65535)):
                    s = 54

                else:
                    s = 75

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 26, _s, input)
            self_.error(nvae)
            raise nvae


def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain

    main = LexerMain(SQLiteLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
