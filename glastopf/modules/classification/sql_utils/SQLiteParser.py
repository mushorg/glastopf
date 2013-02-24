# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SQLite.g 2012-04-18 19:31:03

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *

         
#package org.tmatesoft.sqljet.core.internal.lang;



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
ROW=183
BLOB_LITERAL=7
TYPE_PARAMS=35
NOT=43
EXCEPT=120
EOF=-1
FOREIGN=163
STATEMENT=32
TYPE=34
RPAREN=50
CREATE=151
STRING_LITERAL=31
IS_NULL=25
USING=133
BIND=5
CREATE_TRIGGER=15
BEGIN=141
REGEXP=62
ANALYZE=108
FUNCTION_LITERAL=19
CONFLICT=150
APOSTROPHE=188
LESS_OR_EQ=65
ATTACH=105
VIRTUAL=152
D=195
E=196
F=197
ID_QUOTED=233
G=198
BLOB=92
A=192
B=193
C=194
ASC=112
L=203
M=204
N=205
O=206
TRANSACTION=145
KEY=159
H=199
I=200
BIND_NAME=6
J=201
ELSE=85
K=202
U=212
T=211
W=214
IN_VALUES=22
V=213
UNDERSCORE=191
Q=208
P=207
S=210
R=209
ROLLBACK=101
FAIL=103
Y=216
RESTRICT=166
X=215
Z=217
INTERSECT=119
GROUP=124
DROP_INDEX=16
WS=237
PLAN=39
ALIAS=4
END=86
RPAREN_SQUARE=190
CONSTRAINT=157
RENAME=171
ALTER=170
ID_PLAIN=227
STRING_CORE_DOUBLE=222
ISNULL=52
TABLE=153
FLOAT=90
STRING_CORE_SINGLE=221
ID_QUOTED_CORE_SQUARE=229
NOTNULL=53
NOT_EQUALS=58
ASTERISK=74
LPAREN=48
NOT_NULL=27
GREATER_OR_EQ=67
DOUBLE_PIPE=77
AT=98
AS=83
SLASH=75
IS_NOT=26
THEN=88
ID_QUOTED_CORE=228
OFFSET=116
REPLACE=111
LEFT=127
COLUMN=173
PLUS=72
PIPE=71
EXISTS=156
LIKE=60
COLLATE=79
ADD=172
INTEGER=89
OUTER=128
BY=42
DEFERRABLE=167
TO=147
ID_CORE=226
AMPERSAND=70
SET=139
HAVING=125
MINUS=73
IGNORE=100
SEMI=36
UNION=117
COLUMN_CONSTRAINT=8
COLON=97
FLOAT_EXP=234
COLUMNS=10
COMMIT=146
IN_TABLE=23
DATABASE=106
VACUUM=110
DROP=169
DETACH=107
WHEN=87
ID_QUOTED_APOSTROPHE=232
STRING_DOUBLE=224
STRING_SINGLE=223
NATURAL=126
BETWEEN=56
OPTIONS=28
STRING=91
CAST=82
STRING_CORE=220
TABLE_CONSTRAINT=33
ID_LITERAL=21
CURRENT_TIME=93
TRIGGER=176
CASE=84
EQUALS=51
CASCADE=165
RELEASE=149
EXPLAIN=37
GREATER=66
ESCAPE=46
INSERT=134
SAVEPOINT=148
LESS=64
RAISE=99
LPAREN_SQUARE=189
EACH=182
COMMENT=235
ABORT=102
SELECT=121
INTO=135
UNIQUE=161
GLOB=61
VIEW=174
LINE_COMMENT=236
NULL=55
QUOTE_DOUBLE=186
ON=132
MATCH=63
PRIMARY=158
DELETE=140
OF=180
SHIFT_LEFT=68
SHIFT_RIGHT=69
INTEGER_LITERAL=24
FUNCTION_EXPRESSION=20
OR=44
QUERY=38
CHECK=162
QUOTE_SINGLE=187
STRING_ESCAPE_DOUBLE=219
FROM=122
DISTINCT=81
TEMPORARY=154
CURRENT_DATE=94
BACKSLASH=184
DOLLAR=185
CONSTRAINTS=11
WHERE=123
COLUMN_EXPRESSION=9
INNER=129
STRING_ESCAPE_SINGLE=218
ORDER=114
LIMIT=115
PRAGMA=104
UPDATE=138
DEFERRED=142
FOR=181
SELECT_CORE=30
EXCLUSIVE=144
ID=80
AND=45
CROSS=130
IF=155
INDEX=175
TILDA=78
IN=47
COMMA=49
CREATE_TABLE=13
REFERENCES=164
IS=54
ALL=118
DOT=40
CURRENT_TIMESTAMP=95
CREATE_VIEW=14
INITIALLY=168
REINDEX=109
EQUALS2=57
PERCENT=76
AUTOINCREMENT=160
NOT_EQUALS2=59
DEFAULT=137
VALUES=136
BEFORE=177
AFTER=178
INSTEAD=179
ID_QUOTED_CORE_APOSTROPHE=230
JOIN=131
ID_QUOTED_SQUARE=231
FLOAT_LITERAL=18
INDEXED=41
CREATE_INDEX=12
QUESTION=96
ORDERING=29
IMMEDIATE=143
DESC=113
DROP_TABLE=17
ID_START=225

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ALIAS", "BIND", "BIND_NAME", "BLOB_LITERAL", "COLUMN_CONSTRAINT", "COLUMN_EXPRESSION", 
    "COLUMNS", "CONSTRAINTS", "CREATE_INDEX", "CREATE_TABLE", "CREATE_VIEW", 
    "CREATE_TRIGGER", "DROP_INDEX", "DROP_TABLE", "FLOAT_LITERAL", "FUNCTION_LITERAL", 
    "FUNCTION_EXPRESSION", "ID_LITERAL", "IN_VALUES", "IN_TABLE", "INTEGER_LITERAL", 
    "IS_NULL", "IS_NOT", "NOT_NULL", "OPTIONS", "ORDERING", "SELECT_CORE", 
    "STRING_LITERAL", "STATEMENT", "TABLE_CONSTRAINT", "TYPE", "TYPE_PARAMS", 
    "SEMI", "EXPLAIN", "QUERY", "PLAN", "DOT", "INDEXED", "BY", "NOT", "OR", 
    "AND", "ESCAPE", "IN", "LPAREN", "COMMA", "RPAREN", "EQUALS", "ISNULL", 
    "NOTNULL", "IS", "NULL", "BETWEEN", "EQUALS2", "NOT_EQUALS", "NOT_EQUALS2", 
    "LIKE", "GLOB", "REGEXP", "MATCH", "LESS", "LESS_OR_EQ", "GREATER", 
    "GREATER_OR_EQ", "SHIFT_LEFT", "SHIFT_RIGHT", "AMPERSAND", "PIPE", "PLUS", 
    "MINUS", "ASTERISK", "SLASH", "PERCENT", "DOUBLE_PIPE", "TILDA", "COLLATE", 
    "ID", "DISTINCT", "CAST", "AS", "CASE", "ELSE", "END", "WHEN", "THEN", 
    "INTEGER", "FLOAT", "STRING", "BLOB", "CURRENT_TIME", "CURRENT_DATE", 
    "CURRENT_TIMESTAMP", "QUESTION", "COLON", "AT", "RAISE", "IGNORE", "ROLLBACK", 
    "ABORT", "FAIL", "PRAGMA", "ATTACH", "DATABASE", "DETACH", "ANALYZE", 
    "REINDEX", "VACUUM", "REPLACE", "ASC", "DESC", "ORDER", "LIMIT", "OFFSET", 
    "UNION", "ALL", "INTERSECT", "EXCEPT", "SELECT", "FROM", "WHERE", "GROUP", 
    "HAVING", "NATURAL", "LEFT", "OUTER", "INNER", "CROSS", "JOIN", "ON", 
    "USING", "INSERT", "INTO", "VALUES", "DEFAULT", "UPDATE", "SET", "DELETE", 
    "BEGIN", "DEFERRED", "IMMEDIATE", "EXCLUSIVE", "TRANSACTION", "COMMIT", 
    "TO", "SAVEPOINT", "RELEASE", "CONFLICT", "CREATE", "VIRTUAL", "TABLE", 
    "TEMPORARY", "IF", "EXISTS", "CONSTRAINT", "PRIMARY", "KEY", "AUTOINCREMENT", 
    "UNIQUE", "CHECK", "FOREIGN", "REFERENCES", "CASCADE", "RESTRICT", "DEFERRABLE", 
    "INITIALLY", "DROP", "ALTER", "RENAME", "ADD", "COLUMN", "VIEW", "INDEX", 
    "TRIGGER", "BEFORE", "AFTER", "INSTEAD", "OF", "FOR", "EACH", "ROW", 
    "BACKSLASH", "DOLLAR", "QUOTE_DOUBLE", "QUOTE_SINGLE", "APOSTROPHE", 
    "LPAREN_SQUARE", "RPAREN_SQUARE", "UNDERSCORE", "A", "B", "C", "D", 
    "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
    "S", "T", "U", "V", "W", "X", "Y", "Z", "STRING_ESCAPE_SINGLE", "STRING_ESCAPE_DOUBLE", 
    "STRING_CORE", "STRING_CORE_SINGLE", "STRING_CORE_DOUBLE", "STRING_SINGLE", 
    "STRING_DOUBLE", "ID_START", "ID_CORE", "ID_PLAIN", "ID_QUOTED_CORE", 
    "ID_QUOTED_CORE_SQUARE", "ID_QUOTED_CORE_APOSTROPHE", "ID_QUOTED_SQUARE", 
    "ID_QUOTED_APOSTROPHE", "ID_QUOTED", "FLOAT_EXP", "COMMENT", "LINE_COMMENT", 
    "WS"
]




class SQLiteParser(Parser):
    grammarFileName = "SQLite.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(SQLiteParser, self).__init__(input, state, *args, **kwargs)

        self.dfa1 = self.DFA1(
            self, 1,
            eot = self.DFA1_eot,
            eof = self.DFA1_eof,
            min = self.DFA1_min,
            max = self.DFA1_max,
            accept = self.DFA1_accept,
            special = self.DFA1_special,
            transition = self.DFA1_transition
            )

        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )

        self.dfa4 = self.DFA4(
            self, 4,
            eot = self.DFA4_eot,
            eof = self.DFA4_eof,
            min = self.DFA4_min,
            max = self.DFA4_max,
            accept = self.DFA4_accept,
            special = self.DFA4_special,
            transition = self.DFA4_transition
            )

        self.dfa6 = self.DFA6(
            self, 6,
            eot = self.DFA6_eot,
            eof = self.DFA6_eof,
            min = self.DFA6_min,
            max = self.DFA6_max,
            accept = self.DFA6_accept,
            special = self.DFA6_special,
            transition = self.DFA6_transition
            )

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )

        self.dfa11 = self.DFA11(
            self, 11,
            eot = self.DFA11_eot,
            eof = self.DFA11_eof,
            min = self.DFA11_min,
            max = self.DFA11_max,
            accept = self.DFA11_accept,
            special = self.DFA11_special,
            transition = self.DFA11_transition
            )

        self.dfa12 = self.DFA12(
            self, 12,
            eot = self.DFA12_eot,
            eof = self.DFA12_eof,
            min = self.DFA12_min,
            max = self.DFA12_max,
            accept = self.DFA12_accept,
            special = self.DFA12_special,
            transition = self.DFA12_transition
            )

        self.dfa26 = self.DFA26(
            self, 26,
            eot = self.DFA26_eot,
            eof = self.DFA26_eof,
            min = self.DFA26_min,
            max = self.DFA26_max,
            accept = self.DFA26_accept,
            special = self.DFA26_special,
            transition = self.DFA26_transition
            )

        self.dfa14 = self.DFA14(
            self, 14,
            eot = self.DFA14_eot,
            eof = self.DFA14_eof,
            min = self.DFA14_min,
            max = self.DFA14_max,
            accept = self.DFA14_accept,
            special = self.DFA14_special,
            transition = self.DFA14_transition
            )

        self.dfa18 = self.DFA18(
            self, 18,
            eot = self.DFA18_eot,
            eof = self.DFA18_eof,
            min = self.DFA18_min,
            max = self.DFA18_max,
            accept = self.DFA18_accept,
            special = self.DFA18_special,
            transition = self.DFA18_transition
            )

        self.dfa25 = self.DFA25(
            self, 25,
            eot = self.DFA25_eot,
            eof = self.DFA25_eof,
            min = self.DFA25_min,
            max = self.DFA25_max,
            accept = self.DFA25_accept,
            special = self.DFA25_special,
            transition = self.DFA25_transition
            )

        self.dfa27 = self.DFA27(
            self, 27,
            eot = self.DFA27_eot,
            eof = self.DFA27_eof,
            min = self.DFA27_min,
            max = self.DFA27_max,
            accept = self.DFA27_accept,
            special = self.DFA27_special,
            transition = self.DFA27_transition
            )

        self.dfa28 = self.DFA28(
            self, 28,
            eot = self.DFA28_eot,
            eof = self.DFA28_eof,
            min = self.DFA28_min,
            max = self.DFA28_max,
            accept = self.DFA28_accept,
            special = self.DFA28_special,
            transition = self.DFA28_transition
            )

        self.dfa29 = self.DFA29(
            self, 29,
            eot = self.DFA29_eot,
            eof = self.DFA29_eof,
            min = self.DFA29_min,
            max = self.DFA29_max,
            accept = self.DFA29_accept,
            special = self.DFA29_special,
            transition = self.DFA29_transition
            )

        self.dfa30 = self.DFA30(
            self, 30,
            eot = self.DFA30_eot,
            eof = self.DFA30_eof,
            min = self.DFA30_min,
            max = self.DFA30_max,
            accept = self.DFA30_accept,
            special = self.DFA30_special,
            transition = self.DFA30_transition
            )

        self.dfa31 = self.DFA31(
            self, 31,
            eot = self.DFA31_eot,
            eof = self.DFA31_eof,
            min = self.DFA31_min,
            max = self.DFA31_max,
            accept = self.DFA31_accept,
            special = self.DFA31_special,
            transition = self.DFA31_transition
            )

        self.dfa32 = self.DFA32(
            self, 32,
            eot = self.DFA32_eot,
            eof = self.DFA32_eof,
            min = self.DFA32_min,
            max = self.DFA32_max,
            accept = self.DFA32_accept,
            special = self.DFA32_special,
            transition = self.DFA32_transition
            )

        self.dfa33 = self.DFA33(
            self, 33,
            eot = self.DFA33_eot,
            eof = self.DFA33_eof,
            min = self.DFA33_min,
            max = self.DFA33_max,
            accept = self.DFA33_accept,
            special = self.DFA33_special,
            transition = self.DFA33_transition
            )

        self.dfa42 = self.DFA42(
            self, 42,
            eot = self.DFA42_eot,
            eof = self.DFA42_eof,
            min = self.DFA42_min,
            max = self.DFA42_max,
            accept = self.DFA42_accept,
            special = self.DFA42_special,
            transition = self.DFA42_transition
            )

        self.dfa35 = self.DFA35(
            self, 35,
            eot = self.DFA35_eot,
            eof = self.DFA35_eof,
            min = self.DFA35_min,
            max = self.DFA35_max,
            accept = self.DFA35_accept,
            special = self.DFA35_special,
            transition = self.DFA35_transition
            )

        self.dfa34 = self.DFA34(
            self, 34,
            eot = self.DFA34_eot,
            eof = self.DFA34_eof,
            min = self.DFA34_min,
            max = self.DFA34_max,
            accept = self.DFA34_accept,
            special = self.DFA34_special,
            transition = self.DFA34_transition
            )

        self.dfa38 = self.DFA38(
            self, 38,
            eot = self.DFA38_eot,
            eof = self.DFA38_eof,
            min = self.DFA38_min,
            max = self.DFA38_max,
            accept = self.DFA38_accept,
            special = self.DFA38_special,
            transition = self.DFA38_transition
            )

        self.dfa36 = self.DFA36(
            self, 36,
            eot = self.DFA36_eot,
            eof = self.DFA36_eof,
            min = self.DFA36_min,
            max = self.DFA36_max,
            accept = self.DFA36_accept,
            special = self.DFA36_special,
            transition = self.DFA36_transition
            )

        self.dfa39 = self.DFA39(
            self, 39,
            eot = self.DFA39_eot,
            eof = self.DFA39_eof,
            min = self.DFA39_min,
            max = self.DFA39_max,
            accept = self.DFA39_accept,
            special = self.DFA39_special,
            transition = self.DFA39_transition
            )

        self.dfa44 = self.DFA44(
            self, 44,
            eot = self.DFA44_eot,
            eof = self.DFA44_eof,
            min = self.DFA44_min,
            max = self.DFA44_max,
            accept = self.DFA44_accept,
            special = self.DFA44_special,
            transition = self.DFA44_transition
            )

        self.dfa46 = self.DFA46(
            self, 46,
            eot = self.DFA46_eot,
            eof = self.DFA46_eof,
            min = self.DFA46_min,
            max = self.DFA46_max,
            accept = self.DFA46_accept,
            special = self.DFA46_special,
            transition = self.DFA46_transition
            )

        self.dfa48 = self.DFA48(
            self, 48,
            eot = self.DFA48_eot,
            eof = self.DFA48_eof,
            min = self.DFA48_min,
            max = self.DFA48_max,
            accept = self.DFA48_accept,
            special = self.DFA48_special,
            transition = self.DFA48_transition
            )

        self.dfa50 = self.DFA50(
            self, 50,
            eot = self.DFA50_eot,
            eof = self.DFA50_eof,
            min = self.DFA50_min,
            max = self.DFA50_max,
            accept = self.DFA50_accept,
            special = self.DFA50_special,
            transition = self.DFA50_transition
            )

        self.dfa53 = self.DFA53(
            self, 53,
            eot = self.DFA53_eot,
            eof = self.DFA53_eof,
            min = self.DFA53_min,
            max = self.DFA53_max,
            accept = self.DFA53_accept,
            special = self.DFA53_special,
            transition = self.DFA53_transition
            )

        self.dfa55 = self.DFA55(
            self, 55,
            eot = self.DFA55_eot,
            eof = self.DFA55_eof,
            min = self.DFA55_min,
            max = self.DFA55_max,
            accept = self.DFA55_accept,
            special = self.DFA55_special,
            transition = self.DFA55_transition
            )

        self.dfa57 = self.DFA57(
            self, 57,
            eot = self.DFA57_eot,
            eof = self.DFA57_eof,
            min = self.DFA57_min,
            max = self.DFA57_max,
            accept = self.DFA57_accept,
            special = self.DFA57_special,
            transition = self.DFA57_transition
            )

        self.dfa69 = self.DFA69(
            self, 69,
            eot = self.DFA69_eot,
            eof = self.DFA69_eof,
            min = self.DFA69_min,
            max = self.DFA69_max,
            accept = self.DFA69_accept,
            special = self.DFA69_special,
            transition = self.DFA69_transition
            )

        self.dfa70 = self.DFA70(
            self, 70,
            eot = self.DFA70_eot,
            eof = self.DFA70_eof,
            min = self.DFA70_min,
            max = self.DFA70_max,
            accept = self.DFA70_accept,
            special = self.DFA70_special,
            transition = self.DFA70_transition
            )

        self.dfa71 = self.DFA71(
            self, 71,
            eot = self.DFA71_eot,
            eof = self.DFA71_eof,
            min = self.DFA71_min,
            max = self.DFA71_max,
            accept = self.DFA71_accept,
            special = self.DFA71_special,
            transition = self.DFA71_transition
            )

        self.dfa72 = self.DFA72(
            self, 72,
            eot = self.DFA72_eot,
            eof = self.DFA72_eof,
            min = self.DFA72_min,
            max = self.DFA72_max,
            accept = self.DFA72_accept,
            special = self.DFA72_special,
            transition = self.DFA72_transition
            )

        self.dfa75 = self.DFA75(
            self, 75,
            eot = self.DFA75_eot,
            eof = self.DFA75_eof,
            min = self.DFA75_min,
            max = self.DFA75_max,
            accept = self.DFA75_accept,
            special = self.DFA75_special,
            transition = self.DFA75_transition
            )

        self.dfa73 = self.DFA73(
            self, 73,
            eot = self.DFA73_eot,
            eof = self.DFA73_eof,
            min = self.DFA73_min,
            max = self.DFA73_max,
            accept = self.DFA73_accept,
            special = self.DFA73_special,
            transition = self.DFA73_transition
            )

        self.dfa74 = self.DFA74(
            self, 74,
            eot = self.DFA74_eot,
            eof = self.DFA74_eof,
            min = self.DFA74_min,
            max = self.DFA74_max,
            accept = self.DFA74_accept,
            special = self.DFA74_special,
            transition = self.DFA74_transition
            )

        self.dfa78 = self.DFA78(
            self, 78,
            eot = self.DFA78_eot,
            eof = self.DFA78_eof,
            min = self.DFA78_min,
            max = self.DFA78_max,
            accept = self.DFA78_accept,
            special = self.DFA78_special,
            transition = self.DFA78_transition
            )

        self.dfa77 = self.DFA77(
            self, 77,
            eot = self.DFA77_eot,
            eof = self.DFA77_eof,
            min = self.DFA77_min,
            max = self.DFA77_max,
            accept = self.DFA77_accept,
            special = self.DFA77_special,
            transition = self.DFA77_transition
            )

        self.dfa76 = self.DFA76(
            self, 76,
            eot = self.DFA76_eot,
            eof = self.DFA76_eof,
            min = self.DFA76_min,
            max = self.DFA76_max,
            accept = self.DFA76_accept,
            special = self.DFA76_special,
            transition = self.DFA76_transition
            )

        self.dfa80 = self.DFA80(
            self, 80,
            eot = self.DFA80_eot,
            eof = self.DFA80_eof,
            min = self.DFA80_min,
            max = self.DFA80_max,
            accept = self.DFA80_accept,
            special = self.DFA80_special,
            transition = self.DFA80_transition
            )

        self.dfa79 = self.DFA79(
            self, 79,
            eot = self.DFA79_eot,
            eof = self.DFA79_eof,
            min = self.DFA79_min,
            max = self.DFA79_max,
            accept = self.DFA79_accept,
            special = self.DFA79_special,
            transition = self.DFA79_transition
            )

        self.dfa87 = self.DFA87(
            self, 87,
            eot = self.DFA87_eot,
            eof = self.DFA87_eof,
            min = self.DFA87_min,
            max = self.DFA87_max,
            accept = self.DFA87_accept,
            special = self.DFA87_special,
            transition = self.DFA87_transition
            )

        self.dfa81 = self.DFA81(
            self, 81,
            eot = self.DFA81_eot,
            eof = self.DFA81_eof,
            min = self.DFA81_min,
            max = self.DFA81_max,
            accept = self.DFA81_accept,
            special = self.DFA81_special,
            transition = self.DFA81_transition
            )

        self.dfa83 = self.DFA83(
            self, 83,
            eot = self.DFA83_eot,
            eof = self.DFA83_eof,
            min = self.DFA83_min,
            max = self.DFA83_max,
            accept = self.DFA83_accept,
            special = self.DFA83_special,
            transition = self.DFA83_transition
            )

        self.dfa84 = self.DFA84(
            self, 84,
            eot = self.DFA84_eot,
            eof = self.DFA84_eof,
            min = self.DFA84_min,
            max = self.DFA84_max,
            accept = self.DFA84_accept,
            special = self.DFA84_special,
            transition = self.DFA84_transition
            )

        self.dfa86 = self.DFA86(
            self, 86,
            eot = self.DFA86_eot,
            eof = self.DFA86_eof,
            min = self.DFA86_min,
            max = self.DFA86_max,
            accept = self.DFA86_accept,
            special = self.DFA86_special,
            transition = self.DFA86_transition
            )

        self.dfa97 = self.DFA97(
            self, 97,
            eot = self.DFA97_eot,
            eof = self.DFA97_eof,
            min = self.DFA97_min,
            max = self.DFA97_max,
            accept = self.DFA97_accept,
            special = self.DFA97_special,
            transition = self.DFA97_transition
            )

        self.dfa122 = self.DFA122(
            self, 122,
            eot = self.DFA122_eot,
            eof = self.DFA122_eof,
            min = self.DFA122_min,
            max = self.DFA122_max,
            accept = self.DFA122_accept,
            special = self.DFA122_special,
            transition = self.DFA122_transition
            )

        self.dfa126 = self.DFA126(
            self, 126,
            eot = self.DFA126_eot,
            eof = self.DFA126_eof,
            min = self.DFA126_min,
            max = self.DFA126_max,
            accept = self.DFA126_accept,
            special = self.DFA126_special,
            transition = self.DFA126_transition
            )

        self.dfa127 = self.DFA127(
            self, 127,
            eot = self.DFA127_eot,
            eof = self.DFA127_eof,
            min = self.DFA127_min,
            max = self.DFA127_max,
            accept = self.DFA127_accept,
            special = self.DFA127_special,
            transition = self.DFA127_transition
            )

        self.dfa128 = self.DFA128(
            self, 128,
            eot = self.DFA128_eot,
            eof = self.DFA128_eof,
            min = self.DFA128_min,
            max = self.DFA128_max,
            accept = self.DFA128_accept,
            special = self.DFA128_special,
            transition = self.DFA128_transition
            )

        self.dfa130 = self.DFA130(
            self, 130,
            eot = self.DFA130_eot,
            eof = self.DFA130_eof,
            min = self.DFA130_min,
            max = self.DFA130_max,
            accept = self.DFA130_accept,
            special = self.DFA130_special,
            transition = self.DFA130_transition
            )

        self.dfa131 = self.DFA131(
            self, 131,
            eot = self.DFA131_eot,
            eof = self.DFA131_eof,
            min = self.DFA131_min,
            max = self.DFA131_max,
            accept = self.DFA131_accept,
            special = self.DFA131_special,
            transition = self.DFA131_transition
            )

        self.dfa132 = self.DFA132(
            self, 132,
            eot = self.DFA132_eot,
            eof = self.DFA132_eof,
            min = self.DFA132_min,
            max = self.DFA132_max,
            accept = self.DFA132_accept,
            special = self.DFA132_special,
            transition = self.DFA132_transition
            )

        self.dfa133 = self.DFA133(
            self, 133,
            eot = self.DFA133_eot,
            eof = self.DFA133_eof,
            min = self.DFA133_min,
            max = self.DFA133_max,
            accept = self.DFA133_accept,
            special = self.DFA133_special,
            transition = self.DFA133_transition
            )

        self.dfa134 = self.DFA134(
            self, 134,
            eot = self.DFA134_eot,
            eof = self.DFA134_eof,
            min = self.DFA134_min,
            max = self.DFA134_max,
            accept = self.DFA134_accept,
            special = self.DFA134_special,
            transition = self.DFA134_transition
            )

        self.dfa135 = self.DFA135(
            self, 135,
            eot = self.DFA135_eot,
            eof = self.DFA135_eof,
            min = self.DFA135_min,
            max = self.DFA135_max,
            accept = self.DFA135_accept,
            special = self.DFA135_special,
            transition = self.DFA135_transition
            )

        self.dfa137 = self.DFA137(
            self, 137,
            eot = self.DFA137_eot,
            eof = self.DFA137_eof,
            min = self.DFA137_min,
            max = self.DFA137_max,
            accept = self.DFA137_accept,
            special = self.DFA137_special,
            transition = self.DFA137_transition
            )

        self.dfa146 = self.DFA146(
            self, 146,
            eot = self.DFA146_eot,
            eof = self.DFA146_eof,
            min = self.DFA146_min,
            max = self.DFA146_max,
            accept = self.DFA146_accept,
            special = self.DFA146_special,
            transition = self.DFA146_transition
            )

        self.dfa147 = self.DFA147(
            self, 147,
            eot = self.DFA147_eot,
            eof = self.DFA147_eof,
            min = self.DFA147_min,
            max = self.DFA147_max,
            accept = self.DFA147_accept,
            special = self.DFA147_special,
            transition = self.DFA147_transition
            )

        self.dfa148 = self.DFA148(
            self, 148,
            eot = self.DFA148_eot,
            eof = self.DFA148_eof,
            min = self.DFA148_min,
            max = self.DFA148_max,
            accept = self.DFA148_accept,
            special = self.DFA148_special,
            transition = self.DFA148_transition
            )

        self.dfa152 = self.DFA152(
            self, 152,
            eot = self.DFA152_eot,
            eof = self.DFA152_eof,
            min = self.DFA152_min,
            max = self.DFA152_max,
            accept = self.DFA152_accept,
            special = self.DFA152_special,
            transition = self.DFA152_transition
            )

        self.dfa172 = self.DFA172(
            self, 172,
            eot = self.DFA172_eot,
            eof = self.DFA172_eof,
            min = self.DFA172_min,
            max = self.DFA172_max,
            accept = self.DFA172_accept,
            special = self.DFA172_special,
            transition = self.DFA172_transition
            )

        self.dfa173 = self.DFA173(
            self, 173,
            eot = self.DFA173_eot,
            eof = self.DFA173_eof,
            min = self.DFA173_min,
            max = self.DFA173_max,
            accept = self.DFA173_accept,
            special = self.DFA173_special,
            transition = self.DFA173_transition
            )






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

    def unquoteId(self, id):
        if id == None:
            return None

        id_len = len(id)
        if id_len == 0:
            return ""

        first = id[0]
        last = id[id_len-1]
        if first == '[':
            first = ']'
        elif first == '\'':
            pass
        elif first == '"':
            pass
        elif first == '`':
            if first == last:
                return id[1,id_len-1]
        else:
            return id

    def emitErrorMessage(self, msg):
        #sys.stderr.write(msg + '\n')
        self.error = msg

    """def displayRecognitionError(self, tokenNames, e):
        hdr = "line %d:%d" % (e.line, e.charPositionInLine)
        msg = self.getErrorMessage(e, tokenNames)
        sys.stderr.write(hdr + ' ' + msg + '\n')
        raise Exception(hdr+" "+msg)"""

    """def displayRecognitionError(self, tokenNames, e):
        buffer = ""
        buffer += "[" + str(e) + "] "
        buffer += str(e.token)
        if e.token != None:
            stream = e.token.getInputStream()
            if stream != None:
                size = len(stream.strdata)
                if size > 0:
                    buffer += "\n" + stream.strdata
        raise Exception(e);"""

    """// Disable error recovery.
    protected Object recoverFromMismatchedToken(IntStream input, int ttype, BitSet follow) throws RecognitionException {
        throw new MismatchedTokenException(ttype, input);
    }

    // Delegate error reporting to caller.
    public void displayRecognitionError(String[] tokenNames, RecognitionException e) {
        final StringBuilder buffer = new StringBuilder();
        buffer.append("[").append(getErrorHeader(e)).append("] ");
        buffer.append(getErrorMessage(e, tokenNames));
        if(e.token!=null) {
          final CharStream stream = e.token.getInputStream();
          if(stream!=null) {
            int size = stream.size();
            if(size>0) {
              buffer.append("\n").append(stream.substring(0, size-1));
            }
          }
        }
        throw new SqlJetParserException(buffer.toString(), e);
    }

    // unquotes identifier
    private String unquoteId(String id) {
      if(id==null) {
        return null;
      }
      int len = id.length();
      if(len==0) {
        return "";
      }
      char first = id.charAt(0);
      char last = id.charAt(len-1);
      switch(first) {
        case '[' :
          first = ']';
        case '\'' :
        case '"' :
        case '`' :
          if(first==last) {
            return id.substring(1,len-1);
          }
        default:
          return id;
      }
    }"""



    class sql_stmt_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.sql_stmt_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "sql_stmt_list"
    # SQLite.g:142:1: sql_stmt_list : sql_stmt ( SEMI ( sql_stmt SEMI )* )? EOF ;
    def sql_stmt_list(self, ):

        retval = self.sql_stmt_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI2 = None
        SEMI4 = None
        EOF5 = None
        sql_stmt1 = None

        sql_stmt3 = None


        SEMI2_tree = None
        SEMI4_tree = None
        EOF5_tree = None

        try:
            try:
                # SQLite.g:142:14: ( sql_stmt ( SEMI ( sql_stmt SEMI )* )? EOF )
                # SQLite.g:142:16: sql_stmt ( SEMI ( sql_stmt SEMI )* )? EOF
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_sql_stmt_in_sql_stmt_list223)
                sql_stmt1 = self.sql_stmt()

                self._state.following.pop()
                self._adaptor.addChild(root_0, sql_stmt1.tree)
                # SQLite.g:142:25: ( SEMI ( sql_stmt SEMI )* )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == SEMI) :
                    alt2 = 1
                if alt2 == 1:
                    # SQLite.g:142:26: SEMI ( sql_stmt SEMI )*
                    pass 
                    SEMI2=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_sql_stmt_list226)
                    # SQLite.g:142:32: ( sql_stmt SEMI )*
                    while True: #loop1
                        alt1 = 2
                        alt1 = self.dfa1.predict(self.input)
                        if alt1 == 1:
                            # SQLite.g:142:33: sql_stmt SEMI
                            pass 
                            self._state.following.append(self.FOLLOW_sql_stmt_in_sql_stmt_list230)
                            sql_stmt3 = self.sql_stmt()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, sql_stmt3.tree)
                            SEMI4=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_sql_stmt_list232)


                        else:
                            break #loop1



                EOF5=self.match(self.input, EOF, self.FOLLOW_EOF_in_sql_stmt_list240)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "sql_stmt_list"

    class sql_stmt_itself_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.sql_stmt_itself_return, self).__init__()

            self.tree = None




    # $ANTLR start "sql_stmt_itself"
    # SQLite.g:144:1: sql_stmt_itself : sql_stmt ( SEMI )? EOF ;
    def sql_stmt_itself(self, ):

        retval = self.sql_stmt_itself_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI7 = None
        EOF8 = None
        sql_stmt6 = None


        SEMI7_tree = None
        EOF8_tree = None

        try:
            try:
                # SQLite.g:144:16: ( sql_stmt ( SEMI )? EOF )
                # SQLite.g:144:18: sql_stmt ( SEMI )? EOF
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_sql_stmt_in_sql_stmt_itself248)
                sql_stmt6 = self.sql_stmt()

                self._state.following.pop()
                self._adaptor.addChild(root_0, sql_stmt6.tree)
                # SQLite.g:144:27: ( SEMI )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == SEMI) :
                    alt3 = 1
                if alt3 == 1:
                    # SQLite.g:144:28: SEMI
                    pass 
                    SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_sql_stmt_itself251)



                EOF8=self.match(self.input, EOF, self.FOLLOW_EOF_in_sql_stmt_itself256)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "sql_stmt_itself"

    class sql_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.sql_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "sql_stmt"
    # SQLite.g:146:1: sql_stmt : ( EXPLAIN ( QUERY PLAN )? )? sql_stmt_core ;
    def sql_stmt(self, ):

        retval = self.sql_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EXPLAIN9 = None
        QUERY10 = None
        PLAN11 = None
        sql_stmt_core12 = None


        EXPLAIN9_tree = None
        QUERY10_tree = None
        PLAN11_tree = None

        try:
            try:
                # SQLite.g:146:9: ( ( EXPLAIN ( QUERY PLAN )? )? sql_stmt_core )
                # SQLite.g:146:11: ( EXPLAIN ( QUERY PLAN )? )? sql_stmt_core
                pass 
                root_0 = self._adaptor.nil()

                # SQLite.g:146:11: ( EXPLAIN ( QUERY PLAN )? )?
                alt5 = 2
                alt5 = self.dfa5.predict(self.input)
                if alt5 == 1:
                    # SQLite.g:146:12: EXPLAIN ( QUERY PLAN )?
                    pass 
                    EXPLAIN9=self.match(self.input, EXPLAIN, self.FOLLOW_EXPLAIN_in_sql_stmt265)

                    EXPLAIN9_tree = self._adaptor.createWithPayload(EXPLAIN9)
                    self._adaptor.addChild(root_0, EXPLAIN9_tree)

                    # SQLite.g:146:20: ( QUERY PLAN )?
                    alt4 = 2
                    alt4 = self.dfa4.predict(self.input)
                    if alt4 == 1:
                        # SQLite.g:146:21: QUERY PLAN
                        pass 
                        QUERY10=self.match(self.input, QUERY, self.FOLLOW_QUERY_in_sql_stmt268)

                        QUERY10_tree = self._adaptor.createWithPayload(QUERY10)
                        self._adaptor.addChild(root_0, QUERY10_tree)

                        PLAN11=self.match(self.input, PLAN, self.FOLLOW_PLAN_in_sql_stmt270)

                        PLAN11_tree = self._adaptor.createWithPayload(PLAN11)
                        self._adaptor.addChild(root_0, PLAN11_tree)







                self._state.following.append(self.FOLLOW_sql_stmt_core_in_sql_stmt276)
                sql_stmt_core12 = self.sql_stmt_core()

                self._state.following.pop()
                self._adaptor.addChild(root_0, sql_stmt_core12.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "sql_stmt"

    class sql_stmt_core_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.sql_stmt_core_return, self).__init__()

            self.tree = None




    # $ANTLR start "sql_stmt_core"
    # SQLite.g:148:1: sql_stmt_core : ( pragma_stmt | attach_stmt | detach_stmt | analyze_stmt | reindex_stmt | vacuum_stmt | select_stmt | insert_stmt | update_stmt | delete_stmt | begin_stmt | commit_stmt | rollback_stmt | savepoint_stmt | release_stmt | create_virtual_table_stmt | create_table_stmt | drop_table_stmt | alter_table_stmt | create_view_stmt | drop_view_stmt | create_index_stmt | drop_index_stmt | create_trigger_stmt | drop_trigger_stmt );
    def sql_stmt_core(self, ):

        retval = self.sql_stmt_core_return()
        retval.start = self.input.LT(1)

        root_0 = None

        pragma_stmt13 = None

        attach_stmt14 = None

        detach_stmt15 = None

        analyze_stmt16 = None

        reindex_stmt17 = None

        vacuum_stmt18 = None

        select_stmt19 = None

        insert_stmt20 = None

        update_stmt21 = None

        delete_stmt22 = None

        begin_stmt23 = None

        commit_stmt24 = None

        rollback_stmt25 = None

        savepoint_stmt26 = None

        release_stmt27 = None

        create_virtual_table_stmt28 = None

        create_table_stmt29 = None

        drop_table_stmt30 = None

        alter_table_stmt31 = None

        create_view_stmt32 = None

        drop_view_stmt33 = None

        create_index_stmt34 = None

        drop_index_stmt35 = None

        create_trigger_stmt36 = None

        drop_trigger_stmt37 = None



        try:
            try:
                # SQLite.g:149:3: ( pragma_stmt | attach_stmt | detach_stmt | analyze_stmt | reindex_stmt | vacuum_stmt | select_stmt | insert_stmt | update_stmt | delete_stmt | begin_stmt | commit_stmt | rollback_stmt | savepoint_stmt | release_stmt | create_virtual_table_stmt | create_table_stmt | drop_table_stmt | alter_table_stmt | create_view_stmt | drop_view_stmt | create_index_stmt | drop_index_stmt | create_trigger_stmt | drop_trigger_stmt )
                alt6 = 25
                alt6 = self.dfa6.predict(self.input)
                if alt6 == 1:
                    # SQLite.g:149:5: pragma_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pragma_stmt_in_sql_stmt_core286)
                    pragma_stmt13 = self.pragma_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, pragma_stmt13.tree)


                elif alt6 == 2:
                    # SQLite.g:150:5: attach_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attach_stmt_in_sql_stmt_core292)
                    attach_stmt14 = self.attach_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, attach_stmt14.tree)


                elif alt6 == 3:
                    # SQLite.g:151:5: detach_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_detach_stmt_in_sql_stmt_core298)
                    detach_stmt15 = self.detach_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, detach_stmt15.tree)


                elif alt6 == 4:
                    # SQLite.g:152:5: analyze_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_analyze_stmt_in_sql_stmt_core304)
                    analyze_stmt16 = self.analyze_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, analyze_stmt16.tree)


                elif alt6 == 5:
                    # SQLite.g:153:5: reindex_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_reindex_stmt_in_sql_stmt_core310)
                    reindex_stmt17 = self.reindex_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, reindex_stmt17.tree)


                elif alt6 == 6:
                    # SQLite.g:154:5: vacuum_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_vacuum_stmt_in_sql_stmt_core316)
                    vacuum_stmt18 = self.vacuum_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, vacuum_stmt18.tree)


                elif alt6 == 7:
                    # SQLite.g:156:5: select_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_select_stmt_in_sql_stmt_core323)
                    select_stmt19 = self.select_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, select_stmt19.tree)


                elif alt6 == 8:
                    # SQLite.g:157:5: insert_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_insert_stmt_in_sql_stmt_core329)
                    insert_stmt20 = self.insert_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, insert_stmt20.tree)


                elif alt6 == 9:
                    # SQLite.g:158:5: update_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_update_stmt_in_sql_stmt_core335)
                    update_stmt21 = self.update_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, update_stmt21.tree)


                elif alt6 == 10:
                    # SQLite.g:159:5: delete_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_delete_stmt_in_sql_stmt_core341)
                    delete_stmt22 = self.delete_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, delete_stmt22.tree)


                elif alt6 == 11:
                    # SQLite.g:160:5: begin_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_begin_stmt_in_sql_stmt_core347)
                    begin_stmt23 = self.begin_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, begin_stmt23.tree)


                elif alt6 == 12:
                    # SQLite.g:161:5: commit_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_commit_stmt_in_sql_stmt_core353)
                    commit_stmt24 = self.commit_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, commit_stmt24.tree)


                elif alt6 == 13:
                    # SQLite.g:162:5: rollback_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rollback_stmt_in_sql_stmt_core359)
                    rollback_stmt25 = self.rollback_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, rollback_stmt25.tree)


                elif alt6 == 14:
                    # SQLite.g:163:5: savepoint_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_savepoint_stmt_in_sql_stmt_core365)
                    savepoint_stmt26 = self.savepoint_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, savepoint_stmt26.tree)


                elif alt6 == 15:
                    # SQLite.g:164:5: release_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_release_stmt_in_sql_stmt_core371)
                    release_stmt27 = self.release_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, release_stmt27.tree)


                elif alt6 == 16:
                    # SQLite.g:166:5: create_virtual_table_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_create_virtual_table_stmt_in_sql_stmt_core378)
                    create_virtual_table_stmt28 = self.create_virtual_table_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, create_virtual_table_stmt28.tree)


                elif alt6 == 17:
                    # SQLite.g:167:5: create_table_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_create_table_stmt_in_sql_stmt_core384)
                    create_table_stmt29 = self.create_table_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, create_table_stmt29.tree)


                elif alt6 == 18:
                    # SQLite.g:168:5: drop_table_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_drop_table_stmt_in_sql_stmt_core390)
                    drop_table_stmt30 = self.drop_table_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, drop_table_stmt30.tree)


                elif alt6 == 19:
                    # SQLite.g:169:5: alter_table_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_alter_table_stmt_in_sql_stmt_core396)
                    alter_table_stmt31 = self.alter_table_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, alter_table_stmt31.tree)


                elif alt6 == 20:
                    # SQLite.g:170:5: create_view_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_create_view_stmt_in_sql_stmt_core402)
                    create_view_stmt32 = self.create_view_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, create_view_stmt32.tree)


                elif alt6 == 21:
                    # SQLite.g:171:5: drop_view_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_drop_view_stmt_in_sql_stmt_core408)
                    drop_view_stmt33 = self.drop_view_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, drop_view_stmt33.tree)


                elif alt6 == 22:
                    # SQLite.g:172:5: create_index_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_create_index_stmt_in_sql_stmt_core414)
                    create_index_stmt34 = self.create_index_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, create_index_stmt34.tree)


                elif alt6 == 23:
                    # SQLite.g:173:5: drop_index_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_drop_index_stmt_in_sql_stmt_core420)
                    drop_index_stmt35 = self.drop_index_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, drop_index_stmt35.tree)


                elif alt6 == 24:
                    # SQLite.g:174:5: create_trigger_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_create_trigger_stmt_in_sql_stmt_core426)
                    create_trigger_stmt36 = self.create_trigger_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, create_trigger_stmt36.tree)


                elif alt6 == 25:
                    # SQLite.g:175:5: drop_trigger_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_drop_trigger_stmt_in_sql_stmt_core432)
                    drop_trigger_stmt37 = self.drop_trigger_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, drop_trigger_stmt37.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "sql_stmt_core"

    class schema_create_table_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.schema_create_table_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "schema_create_table_stmt"
    # SQLite.g:178:1: schema_create_table_stmt : ( create_virtual_table_stmt | create_table_stmt );
    def schema_create_table_stmt(self, ):

        retval = self.schema_create_table_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        create_virtual_table_stmt38 = None

        create_table_stmt39 = None



        try:
            try:
                # SQLite.g:178:25: ( create_virtual_table_stmt | create_table_stmt )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == CREATE) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == VIRTUAL) :
                        alt7 = 1
                    elif ((TABLE <= LA7_1 <= TEMPORARY)) :
                        alt7 = 2
                    else:
                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # SQLite.g:178:27: create_virtual_table_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_create_virtual_table_stmt_in_schema_create_table_stmt442)
                    create_virtual_table_stmt38 = self.create_virtual_table_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, create_virtual_table_stmt38.tree)


                elif alt7 == 2:
                    # SQLite.g:178:55: create_table_stmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_create_table_stmt_in_schema_create_table_stmt446)
                    create_table_stmt39 = self.create_table_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, create_table_stmt39.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "schema_create_table_stmt"

    class qualified_table_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.qualified_table_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "qualified_table_name"
    # SQLite.g:180:1: qualified_table_name : (database_name= id DOT )? table_name= id ( INDEXED BY index_name= id | NOT INDEXED )? ;
    def qualified_table_name(self, ):

        retval = self.qualified_table_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOT40 = None
        INDEXED41 = None
        BY42 = None
        NOT43 = None
        INDEXED44 = None
        database_name = None

        table_name = None

        index_name = None


        DOT40_tree = None
        INDEXED41_tree = None
        BY42_tree = None
        NOT43_tree = None
        INDEXED44_tree = None

        try:
            try:
                # SQLite.g:180:21: ( (database_name= id DOT )? table_name= id ( INDEXED BY index_name= id | NOT INDEXED )? )
                # SQLite.g:180:23: (database_name= id DOT )? table_name= id ( INDEXED BY index_name= id | NOT INDEXED )?
                pass 
                root_0 = self._adaptor.nil()

                # SQLite.g:180:23: (database_name= id DOT )?
                alt8 = 2
                alt8 = self.dfa8.predict(self.input)
                if alt8 == 1:
                    # SQLite.g:180:24: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_qualified_table_name456)
                    database_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, database_name.tree)
                    DOT40=self.match(self.input, DOT, self.FOLLOW_DOT_in_qualified_table_name458)

                    DOT40_tree = self._adaptor.createWithPayload(DOT40)
                    self._adaptor.addChild(root_0, DOT40_tree)




                self._state.following.append(self.FOLLOW_id_in_qualified_table_name464)
                table_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, table_name.tree)
                # SQLite.g:180:61: ( INDEXED BY index_name= id | NOT INDEXED )?
                alt9 = 3
                LA9_0 = self.input.LA(1)

                if (LA9_0 == INDEXED) :
                    alt9 = 1
                elif (LA9_0 == NOT) :
                    alt9 = 2
                if alt9 == 1:
                    # SQLite.g:180:62: INDEXED BY index_name= id
                    pass 
                    INDEXED41=self.match(self.input, INDEXED, self.FOLLOW_INDEXED_in_qualified_table_name467)

                    INDEXED41_tree = self._adaptor.createWithPayload(INDEXED41)
                    self._adaptor.addChild(root_0, INDEXED41_tree)

                    BY42=self.match(self.input, BY, self.FOLLOW_BY_in_qualified_table_name469)

                    BY42_tree = self._adaptor.createWithPayload(BY42)
                    self._adaptor.addChild(root_0, BY42_tree)

                    self._state.following.append(self.FOLLOW_id_in_qualified_table_name473)
                    index_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, index_name.tree)


                elif alt9 == 2:
                    # SQLite.g:180:89: NOT INDEXED
                    pass 
                    NOT43=self.match(self.input, NOT, self.FOLLOW_NOT_in_qualified_table_name477)

                    NOT43_tree = self._adaptor.createWithPayload(NOT43)
                    self._adaptor.addChild(root_0, NOT43_tree)

                    INDEXED44=self.match(self.input, INDEXED, self.FOLLOW_INDEXED_in_qualified_table_name479)

                    INDEXED44_tree = self._adaptor.createWithPayload(INDEXED44)
                    self._adaptor.addChild(root_0, INDEXED44_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "qualified_table_name"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # SQLite.g:182:1: expr : or_subexpr ( OR or_subexpr )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR46 = None
        or_subexpr45 = None

        or_subexpr47 = None


        OR46_tree = None

        try:
            try:
                # SQLite.g:182:5: ( or_subexpr ( OR or_subexpr )* )
                # SQLite.g:182:7: or_subexpr ( OR or_subexpr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_or_subexpr_in_expr488)
                or_subexpr45 = self.or_subexpr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, or_subexpr45.tree)
                # SQLite.g:182:18: ( OR or_subexpr )*
                while True: #loop10
                    alt10 = 2
                    alt10 = self.dfa10.predict(self.input)
                    if alt10 == 1:
                        # SQLite.g:182:19: OR or_subexpr
                        pass 
                        OR46=self.match(self.input, OR, self.FOLLOW_OR_in_expr491)

                        OR46_tree = self._adaptor.createWithPayload(OR46)
                        root_0 = self._adaptor.becomeRoot(OR46_tree, root_0)

                        self._state.following.append(self.FOLLOW_or_subexpr_in_expr494)
                        or_subexpr47 = self.or_subexpr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, or_subexpr47.tree)


                    else:
                        break #loop10



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "expr"

    class or_subexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.or_subexpr_return, self).__init__()

            self.tree = None




    # $ANTLR start "or_subexpr"
    # SQLite.g:184:1: or_subexpr : and_subexpr ( AND and_subexpr )* ;
    def or_subexpr(self, ):

        retval = self.or_subexpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND49 = None
        and_subexpr48 = None

        and_subexpr50 = None


        AND49_tree = None

        try:
            try:
                # SQLite.g:184:11: ( and_subexpr ( AND and_subexpr )* )
                # SQLite.g:184:13: and_subexpr ( AND and_subexpr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_and_subexpr_in_or_subexpr503)
                and_subexpr48 = self.and_subexpr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, and_subexpr48.tree)
                # SQLite.g:184:25: ( AND and_subexpr )*
                while True: #loop11
                    alt11 = 2
                    alt11 = self.dfa11.predict(self.input)
                    if alt11 == 1:
                        # SQLite.g:184:26: AND and_subexpr
                        pass 
                        AND49=self.match(self.input, AND, self.FOLLOW_AND_in_or_subexpr506)

                        AND49_tree = self._adaptor.createWithPayload(AND49)
                        root_0 = self._adaptor.becomeRoot(AND49_tree, root_0)

                        self._state.following.append(self.FOLLOW_and_subexpr_in_or_subexpr509)
                        and_subexpr50 = self.and_subexpr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, and_subexpr50.tree)


                    else:
                        break #loop11



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "or_subexpr"

    class and_subexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.and_subexpr_return, self).__init__()

            self.tree = None




    # $ANTLR start "and_subexpr"
    # SQLite.g:186:1: and_subexpr : eq_subexpr ( cond_expr )? ;
    def and_subexpr(self, ):

        retval = self.and_subexpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        eq_subexpr51 = None

        cond_expr52 = None



        try:
            try:
                # SQLite.g:186:12: ( eq_subexpr ( cond_expr )? )
                # SQLite.g:186:14: eq_subexpr ( cond_expr )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_eq_subexpr_in_and_subexpr518)
                eq_subexpr51 = self.eq_subexpr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, eq_subexpr51.tree)
                # SQLite.g:186:34: ( cond_expr )?
                alt12 = 2
                alt12 = self.dfa12.predict(self.input)
                if alt12 == 1:
                    # SQLite.g:186:34: cond_expr
                    pass 
                    self._state.following.append(self.FOLLOW_cond_expr_in_and_subexpr520)
                    cond_expr52 = self.cond_expr()

                    self._state.following.pop()
                    root_0 = self._adaptor.becomeRoot(cond_expr52.tree, root_0)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "and_subexpr"

    class cond_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.cond_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "cond_expr"
    # SQLite.g:188:1: cond_expr : ( ( NOT )? match_op match_expr= eq_subexpr ( ESCAPE escape_expr= eq_subexpr )? -> ^( match_op $match_expr ( NOT )? ( ^( ESCAPE $escape_expr) )? ) | ( NOT )? IN LPAREN expr ( COMMA expr )* RPAREN -> ^( IN_VALUES ( NOT )? ^( IN ( expr )+ ) ) | ( NOT )? IN (database_name= id DOT )? table_name= id -> ^( IN_TABLE ( NOT )? ^( IN ^( $table_name ( $database_name)? ) ) ) | ( NOT )? IN LPAREN ( select_stmt )? RPAREN | ( NOT )? EQUALS LPAREN ( select_stmt )? RPAREN | ( ISNULL -> IS_NULL | NOTNULL -> NOT_NULL | IS NULL -> IS_NULL | NOT NULL -> NOT_NULL | IS NOT NULL -> NOT_NULL ) | IS NOT eq_subexpr | ( NOT )? BETWEEN e1= eq_subexpr AND e2= eq_subexpr -> ^( BETWEEN ( NOT )? ^( AND $e1 $e2) ) | ( ( EQUALS | EQUALS2 | NOT_EQUALS | NOT_EQUALS2 ) eq_subexpr )+ );
    def cond_expr(self, ):

        retval = self.cond_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT53 = None
        ESCAPE55 = None
        NOT56 = None
        IN57 = None
        LPAREN58 = None
        COMMA60 = None
        RPAREN62 = None
        NOT63 = None
        IN64 = None
        DOT65 = None
        NOT66 = None
        IN67 = None
        LPAREN68 = None
        RPAREN70 = None
        NOT71 = None
        EQUALS72 = None
        LPAREN73 = None
        RPAREN75 = None
        ISNULL76 = None
        NOTNULL77 = None
        IS78 = None
        NULL79 = None
        NOT80 = None
        NULL81 = None
        IS82 = None
        NOT83 = None
        NULL84 = None
        IS85 = None
        NOT86 = None
        NOT88 = None
        BETWEEN89 = None
        AND90 = None
        set91 = None
        match_expr = None

        escape_expr = None

        database_name = None

        table_name = None

        e1 = None

        e2 = None

        match_op54 = None

        expr59 = None

        expr61 = None

        select_stmt69 = None

        select_stmt74 = None

        eq_subexpr87 = None

        eq_subexpr92 = None


        NOT53_tree = None
        ESCAPE55_tree = None
        NOT56_tree = None
        IN57_tree = None
        LPAREN58_tree = None
        COMMA60_tree = None
        RPAREN62_tree = None
        NOT63_tree = None
        IN64_tree = None
        DOT65_tree = None
        NOT66_tree = None
        IN67_tree = None
        LPAREN68_tree = None
        RPAREN70_tree = None
        NOT71_tree = None
        EQUALS72_tree = None
        LPAREN73_tree = None
        RPAREN75_tree = None
        ISNULL76_tree = None
        NOTNULL77_tree = None
        IS78_tree = None
        NULL79_tree = None
        NOT80_tree = None
        NULL81_tree = None
        IS82_tree = None
        NOT83_tree = None
        NULL84_tree = None
        IS85_tree = None
        NOT86_tree = None
        NOT88_tree = None
        BETWEEN89_tree = None
        AND90_tree = None
        set91_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_IN = RewriteRuleTokenStream(self._adaptor, "token IN")
        stream_ESCAPE = RewriteRuleTokenStream(self._adaptor, "token ESCAPE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_IS = RewriteRuleTokenStream(self._adaptor, "token IS")
        stream_NULL = RewriteRuleTokenStream(self._adaptor, "token NULL")
        stream_ISNULL = RewriteRuleTokenStream(self._adaptor, "token ISNULL")
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_NOTNULL = RewriteRuleTokenStream(self._adaptor, "token NOTNULL")
        stream_AND = RewriteRuleTokenStream(self._adaptor, "token AND")
        stream_BETWEEN = RewriteRuleTokenStream(self._adaptor, "token BETWEEN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_match_op = RewriteRuleSubtreeStream(self._adaptor, "rule match_op")
        stream_eq_subexpr = RewriteRuleSubtreeStream(self._adaptor, "rule eq_subexpr")
        try:
            try:
                # SQLite.g:189:3: ( ( NOT )? match_op match_expr= eq_subexpr ( ESCAPE escape_expr= eq_subexpr )? -> ^( match_op $match_expr ( NOT )? ( ^( ESCAPE $escape_expr) )? ) | ( NOT )? IN LPAREN expr ( COMMA expr )* RPAREN -> ^( IN_VALUES ( NOT )? ^( IN ( expr )+ ) ) | ( NOT )? IN (database_name= id DOT )? table_name= id -> ^( IN_TABLE ( NOT )? ^( IN ^( $table_name ( $database_name)? ) ) ) | ( NOT )? IN LPAREN ( select_stmt )? RPAREN | ( NOT )? EQUALS LPAREN ( select_stmt )? RPAREN | ( ISNULL -> IS_NULL | NOTNULL -> NOT_NULL | IS NULL -> IS_NULL | NOT NULL -> NOT_NULL | IS NOT NULL -> NOT_NULL ) | IS NOT eq_subexpr | ( NOT )? BETWEEN e1= eq_subexpr AND e2= eq_subexpr -> ^( BETWEEN ( NOT )? ^( AND $e1 $e2) ) | ( ( EQUALS | EQUALS2 | NOT_EQUALS | NOT_EQUALS2 ) eq_subexpr )+ )
                alt26 = 9
                alt26 = self.dfa26.predict(self.input)
                if alt26 == 1:
                    # SQLite.g:189:5: ( NOT )? match_op match_expr= eq_subexpr ( ESCAPE escape_expr= eq_subexpr )?
                    pass 
                    # SQLite.g:189:5: ( NOT )?
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == NOT) :
                        alt13 = 1
                    if alt13 == 1:
                        # SQLite.g:189:5: NOT
                        pass 
                        NOT53=self.match(self.input, NOT, self.FOLLOW_NOT_in_cond_expr532) 
                        stream_NOT.add(NOT53)



                    self._state.following.append(self.FOLLOW_match_op_in_cond_expr535)
                    match_op54 = self.match_op()

                    self._state.following.pop()
                    stream_match_op.add(match_op54.tree)
                    self._state.following.append(self.FOLLOW_eq_subexpr_in_cond_expr539)
                    match_expr = self.eq_subexpr()

                    self._state.following.pop()
                    stream_eq_subexpr.add(match_expr.tree)
                    # SQLite.g:189:41: ( ESCAPE escape_expr= eq_subexpr )?
                    alt14 = 2
                    alt14 = self.dfa14.predict(self.input)
                    if alt14 == 1:
                        # SQLite.g:189:42: ESCAPE escape_expr= eq_subexpr
                        pass 
                        ESCAPE55=self.match(self.input, ESCAPE, self.FOLLOW_ESCAPE_in_cond_expr542) 
                        stream_ESCAPE.add(ESCAPE55)
                        self._state.following.append(self.FOLLOW_eq_subexpr_in_cond_expr546)
                        escape_expr = self.eq_subexpr()

                        self._state.following.pop()
                        stream_eq_subexpr.add(escape_expr.tree)




                    # AST Rewrite
                    # elements: NOT, match_expr, match_op, ESCAPE, escape_expr
                    # token labels: 
                    # rule labels: retval, match_expr, escape_expr
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if match_expr is not None:
                        stream_match_expr = RewriteRuleSubtreeStream(self._adaptor, "rule match_expr", match_expr.tree)
                    else:
                        stream_match_expr = RewriteRuleSubtreeStream(self._adaptor, "token match_expr", None)


                    if escape_expr is not None:
                        stream_escape_expr = RewriteRuleSubtreeStream(self._adaptor, "rule escape_expr", escape_expr.tree)
                    else:
                        stream_escape_expr = RewriteRuleSubtreeStream(self._adaptor, "token escape_expr", None)


                    root_0 = self._adaptor.nil()
                    # 189:74: -> ^( match_op $match_expr ( NOT )? ( ^( ESCAPE $escape_expr) )? )
                    # SQLite.g:189:77: ^( match_op $match_expr ( NOT )? ( ^( ESCAPE $escape_expr) )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_match_op.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_match_expr.nextTree())
                    # SQLite.g:189:100: ( NOT )?
                    if stream_NOT.hasNext():
                        self._adaptor.addChild(root_1, stream_NOT.nextNode())


                    stream_NOT.reset();
                    # SQLite.g:189:105: ( ^( ESCAPE $escape_expr) )?
                    if stream_ESCAPE.hasNext() or stream_escape_expr.hasNext():
                        # SQLite.g:189:105: ^( ESCAPE $escape_expr)
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(stream_ESCAPE.nextNode(), root_2)

                        self._adaptor.addChild(root_2, stream_escape_expr.nextTree())

                        self._adaptor.addChild(root_1, root_2)


                    stream_ESCAPE.reset();
                    stream_escape_expr.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt26 == 2:
                    # SQLite.g:190:5: ( NOT )? IN LPAREN expr ( COMMA expr )* RPAREN
                    pass 
                    # SQLite.g:190:5: ( NOT )?
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == NOT) :
                        alt15 = 1
                    if alt15 == 1:
                        # SQLite.g:190:5: NOT
                        pass 
                        NOT56=self.match(self.input, NOT, self.FOLLOW_NOT_in_cond_expr574) 
                        stream_NOT.add(NOT56)



                    IN57=self.match(self.input, IN, self.FOLLOW_IN_in_cond_expr577) 
                    stream_IN.add(IN57)
                    LPAREN58=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_cond_expr579) 
                    stream_LPAREN.add(LPAREN58)
                    self._state.following.append(self.FOLLOW_expr_in_cond_expr581)
                    expr59 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr59.tree)
                    # SQLite.g:190:25: ( COMMA expr )*
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == COMMA) :
                            alt16 = 1


                        if alt16 == 1:
                            # SQLite.g:190:26: COMMA expr
                            pass 
                            COMMA60=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_cond_expr584) 
                            stream_COMMA.add(COMMA60)
                            self._state.following.append(self.FOLLOW_expr_in_cond_expr586)
                            expr61 = self.expr()

                            self._state.following.pop()
                            stream_expr.add(expr61.tree)


                        else:
                            break #loop16
                    RPAREN62=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_cond_expr590) 
                    stream_RPAREN.add(RPAREN62)

                    # AST Rewrite
                    # elements: NOT, IN, expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 190:46: -> ^( IN_VALUES ( NOT )? ^( IN ( expr )+ ) )
                    # SQLite.g:190:49: ^( IN_VALUES ( NOT )? ^( IN ( expr )+ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IN_VALUES, "IN_VALUES"), root_1)

                    # SQLite.g:190:61: ( NOT )?
                    if stream_NOT.hasNext():
                        self._adaptor.addChild(root_1, stream_NOT.nextNode())


                    stream_NOT.reset();
                    # SQLite.g:190:66: ^( IN ( expr )+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_IN.nextNode(), root_2)

                    # SQLite.g:190:71: ( expr )+
                    if not (stream_expr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_expr.hasNext():
                        self._adaptor.addChild(root_2, stream_expr.nextTree())


                    stream_expr.reset()

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt26 == 3:
                    # SQLite.g:191:5: ( NOT )? IN (database_name= id DOT )? table_name= id
                    pass 
                    # SQLite.g:191:5: ( NOT )?
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == NOT) :
                        alt17 = 1
                    if alt17 == 1:
                        # SQLite.g:191:5: NOT
                        pass 
                        NOT63=self.match(self.input, NOT, self.FOLLOW_NOT_in_cond_expr612) 
                        stream_NOT.add(NOT63)



                    IN64=self.match(self.input, IN, self.FOLLOW_IN_in_cond_expr615) 
                    stream_IN.add(IN64)
                    # SQLite.g:191:13: (database_name= id DOT )?
                    alt18 = 2
                    alt18 = self.dfa18.predict(self.input)
                    if alt18 == 1:
                        # SQLite.g:191:14: database_name= id DOT
                        pass 
                        self._state.following.append(self.FOLLOW_id_in_cond_expr620)
                        database_name = self.id()

                        self._state.following.pop()
                        stream_id.add(database_name.tree)
                        DOT65=self.match(self.input, DOT, self.FOLLOW_DOT_in_cond_expr622) 
                        stream_DOT.add(DOT65)



                    self._state.following.append(self.FOLLOW_id_in_cond_expr628)
                    table_name = self.id()

                    self._state.following.pop()
                    stream_id.add(table_name.tree)

                    # AST Rewrite
                    # elements: IN, database_name, NOT, table_name
                    # token labels: 
                    # rule labels: database_name, retval, table_name
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if database_name is not None:
                        stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "rule database_name", database_name.tree)
                    else:
                        stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "token database_name", None)


                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if table_name is not None:
                        stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "rule table_name", table_name.tree)
                    else:
                        stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "token table_name", None)


                    root_0 = self._adaptor.nil()
                    # 191:51: -> ^( IN_TABLE ( NOT )? ^( IN ^( $table_name ( $database_name)? ) ) )
                    # SQLite.g:191:54: ^( IN_TABLE ( NOT )? ^( IN ^( $table_name ( $database_name)? ) ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IN_TABLE, "IN_TABLE"), root_1)

                    # SQLite.g:191:65: ( NOT )?
                    if stream_NOT.hasNext():
                        self._adaptor.addChild(root_1, stream_NOT.nextNode())


                    stream_NOT.reset();
                    # SQLite.g:191:70: ^( IN ^( $table_name ( $database_name)? ) )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_IN.nextNode(), root_2)

                    # SQLite.g:191:75: ^( $table_name ( $database_name)? )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(stream_table_name.nextNode(), root_3)

                    # SQLite.g:191:89: ( $database_name)?
                    if stream_database_name.hasNext():
                        self._adaptor.addChild(root_3, stream_database_name.nextTree())


                    stream_database_name.reset();

                    self._adaptor.addChild(root_2, root_3)

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt26 == 4:
                    # SQLite.g:192:5: ( NOT )? IN LPAREN ( select_stmt )? RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    # SQLite.g:192:5: ( NOT )?
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == NOT) :
                        alt19 = 1
                    if alt19 == 1:
                        # SQLite.g:192:5: NOT
                        pass 
                        NOT66=self.match(self.input, NOT, self.FOLLOW_NOT_in_cond_expr656)

                        NOT66_tree = self._adaptor.createWithPayload(NOT66)
                        self._adaptor.addChild(root_0, NOT66_tree)




                    IN67=self.match(self.input, IN, self.FOLLOW_IN_in_cond_expr659)

                    IN67_tree = self._adaptor.createWithPayload(IN67)
                    root_0 = self._adaptor.becomeRoot(IN67_tree, root_0)

                    LPAREN68=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_cond_expr662)
                    # SQLite.g:192:22: ( select_stmt )?
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == SELECT) :
                        alt20 = 1
                    if alt20 == 1:
                        # SQLite.g:192:22: select_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_select_stmt_in_cond_expr665)
                        select_stmt69 = self.select_stmt()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, select_stmt69.tree)



                    RPAREN70=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_cond_expr668)


                elif alt26 == 5:
                    # SQLite.g:193:5: ( NOT )? EQUALS LPAREN ( select_stmt )? RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    # SQLite.g:193:5: ( NOT )?
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == NOT) :
                        alt21 = 1
                    if alt21 == 1:
                        # SQLite.g:193:5: NOT
                        pass 
                        NOT71=self.match(self.input, NOT, self.FOLLOW_NOT_in_cond_expr675)

                        NOT71_tree = self._adaptor.createWithPayload(NOT71)
                        self._adaptor.addChild(root_0, NOT71_tree)




                    EQUALS72=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_cond_expr678)

                    EQUALS72_tree = self._adaptor.createWithPayload(EQUALS72)
                    root_0 = self._adaptor.becomeRoot(EQUALS72_tree, root_0)

                    LPAREN73=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_cond_expr681)
                    # SQLite.g:193:26: ( select_stmt )?
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == SELECT) :
                        alt22 = 1
                    if alt22 == 1:
                        # SQLite.g:193:26: select_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_select_stmt_in_cond_expr684)
                        select_stmt74 = self.select_stmt()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, select_stmt74.tree)



                    RPAREN75=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_cond_expr687)


                elif alt26 == 6:
                    # SQLite.g:194:5: ( ISNULL -> IS_NULL | NOTNULL -> NOT_NULL | IS NULL -> IS_NULL | NOT NULL -> NOT_NULL | IS NOT NULL -> NOT_NULL )
                    pass 
                    # SQLite.g:194:5: ( ISNULL -> IS_NULL | NOTNULL -> NOT_NULL | IS NULL -> IS_NULL | NOT NULL -> NOT_NULL | IS NOT NULL -> NOT_NULL )
                    alt23 = 5
                    LA23 = self.input.LA(1)
                    if LA23 == ISNULL:
                        alt23 = 1
                    elif LA23 == NOTNULL:
                        alt23 = 2
                    elif LA23 == IS:
                        LA23_3 = self.input.LA(2)

                        if (LA23_3 == NULL) :
                            alt23 = 3
                        elif (LA23_3 == NOT) :
                            alt23 = 5
                        else:
                            nvae = NoViableAltException("", 23, 3, self.input)

                            raise nvae

                    elif LA23 == NOT:
                        alt23 = 4
                    else:
                        nvae = NoViableAltException("", 23, 0, self.input)

                        raise nvae

                    if alt23 == 1:
                        # SQLite.g:194:6: ISNULL
                        pass 
                        ISNULL76=self.match(self.input, ISNULL, self.FOLLOW_ISNULL_in_cond_expr695) 
                        stream_ISNULL.add(ISNULL76)

                        # AST Rewrite
                        # elements: 
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 194:13: -> IS_NULL
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(IS_NULL, "IS_NULL"))



                        retval.tree = root_0


                    elif alt23 == 2:
                        # SQLite.g:194:26: NOTNULL
                        pass 
                        NOTNULL77=self.match(self.input, NOTNULL, self.FOLLOW_NOTNULL_in_cond_expr703) 
                        stream_NOTNULL.add(NOTNULL77)

                        # AST Rewrite
                        # elements: 
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 194:34: -> NOT_NULL
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(NOT_NULL, "NOT_NULL"))



                        retval.tree = root_0


                    elif alt23 == 3:
                        # SQLite.g:194:48: IS NULL
                        pass 
                        IS78=self.match(self.input, IS, self.FOLLOW_IS_in_cond_expr711) 
                        stream_IS.add(IS78)
                        NULL79=self.match(self.input, NULL, self.FOLLOW_NULL_in_cond_expr713) 
                        stream_NULL.add(NULL79)

                        # AST Rewrite
                        # elements: 
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 194:56: -> IS_NULL
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(IS_NULL, "IS_NULL"))



                        retval.tree = root_0


                    elif alt23 == 4:
                        # SQLite.g:194:69: NOT NULL
                        pass 
                        NOT80=self.match(self.input, NOT, self.FOLLOW_NOT_in_cond_expr721) 
                        stream_NOT.add(NOT80)
                        NULL81=self.match(self.input, NULL, self.FOLLOW_NULL_in_cond_expr723) 
                        stream_NULL.add(NULL81)

                        # AST Rewrite
                        # elements: 
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 194:78: -> NOT_NULL
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(NOT_NULL, "NOT_NULL"))



                        retval.tree = root_0


                    elif alt23 == 5:
                        # SQLite.g:194:92: IS NOT NULL
                        pass 
                        IS82=self.match(self.input, IS, self.FOLLOW_IS_in_cond_expr731) 
                        stream_IS.add(IS82)
                        NOT83=self.match(self.input, NOT, self.FOLLOW_NOT_in_cond_expr733) 
                        stream_NOT.add(NOT83)
                        NULL84=self.match(self.input, NULL, self.FOLLOW_NULL_in_cond_expr735) 
                        stream_NULL.add(NULL84)

                        # AST Rewrite
                        # elements: 
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 194:104: -> NOT_NULL
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(NOT_NULL, "NOT_NULL"))



                        retval.tree = root_0





                elif alt26 == 7:
                    # SQLite.g:195:5: IS NOT eq_subexpr
                    pass 
                    root_0 = self._adaptor.nil()

                    IS85=self.match(self.input, IS, self.FOLLOW_IS_in_cond_expr746)

                    IS85_tree = self._adaptor.createWithPayload(IS85)
                    self._adaptor.addChild(root_0, IS85_tree)

                    NOT86=self.match(self.input, NOT, self.FOLLOW_NOT_in_cond_expr748)

                    NOT86_tree = self._adaptor.createWithPayload(NOT86)
                    root_0 = self._adaptor.becomeRoot(NOT86_tree, root_0)

                    self._state.following.append(self.FOLLOW_eq_subexpr_in_cond_expr751)
                    eq_subexpr87 = self.eq_subexpr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, eq_subexpr87.tree)


                elif alt26 == 8:
                    # SQLite.g:196:5: ( NOT )? BETWEEN e1= eq_subexpr AND e2= eq_subexpr
                    pass 
                    # SQLite.g:196:5: ( NOT )?
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == NOT) :
                        alt24 = 1
                    if alt24 == 1:
                        # SQLite.g:196:5: NOT
                        pass 
                        NOT88=self.match(self.input, NOT, self.FOLLOW_NOT_in_cond_expr757) 
                        stream_NOT.add(NOT88)



                    BETWEEN89=self.match(self.input, BETWEEN, self.FOLLOW_BETWEEN_in_cond_expr760) 
                    stream_BETWEEN.add(BETWEEN89)
                    self._state.following.append(self.FOLLOW_eq_subexpr_in_cond_expr764)
                    e1 = self.eq_subexpr()

                    self._state.following.pop()
                    stream_eq_subexpr.add(e1.tree)
                    AND90=self.match(self.input, AND, self.FOLLOW_AND_in_cond_expr766) 
                    stream_AND.add(AND90)
                    self._state.following.append(self.FOLLOW_eq_subexpr_in_cond_expr770)
                    e2 = self.eq_subexpr()

                    self._state.following.pop()
                    stream_eq_subexpr.add(e2.tree)

                    # AST Rewrite
                    # elements: AND, e2, e1, NOT, BETWEEN
                    # token labels: 
                    # rule labels: retval, e1, e2
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if e1 is not None:
                        stream_e1 = RewriteRuleSubtreeStream(self._adaptor, "rule e1", e1.tree)
                    else:
                        stream_e1 = RewriteRuleSubtreeStream(self._adaptor, "token e1", None)


                    if e2 is not None:
                        stream_e2 = RewriteRuleSubtreeStream(self._adaptor, "rule e2", e2.tree)
                    else:
                        stream_e2 = RewriteRuleSubtreeStream(self._adaptor, "token e2", None)


                    root_0 = self._adaptor.nil()
                    # 196:50: -> ^( BETWEEN ( NOT )? ^( AND $e1 $e2) )
                    # SQLite.g:196:53: ^( BETWEEN ( NOT )? ^( AND $e1 $e2) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_BETWEEN.nextNode(), root_1)

                    # SQLite.g:196:63: ( NOT )?
                    if stream_NOT.hasNext():
                        self._adaptor.addChild(root_1, stream_NOT.nextNode())


                    stream_NOT.reset();
                    # SQLite.g:196:68: ^( AND $e1 $e2)
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_AND.nextNode(), root_2)

                    self._adaptor.addChild(root_2, stream_e1.nextTree())
                    self._adaptor.addChild(root_2, stream_e2.nextTree())

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt26 == 9:
                    # SQLite.g:197:5: ( ( EQUALS | EQUALS2 | NOT_EQUALS | NOT_EQUALS2 ) eq_subexpr )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # SQLite.g:197:5: ( ( EQUALS | EQUALS2 | NOT_EQUALS | NOT_EQUALS2 ) eq_subexpr )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        alt25 = self.dfa25.predict(self.input)
                        if alt25 == 1:
                            # SQLite.g:197:6: ( EQUALS | EQUALS2 | NOT_EQUALS | NOT_EQUALS2 ) eq_subexpr
                            pass 
                            set91 = self.input.LT(1)
                            set91 = self.input.LT(1)
                            if self.input.LA(1) == EQUALS or (EQUALS2 <= self.input.LA(1) <= NOT_EQUALS2):
                                self.input.consume()
                                root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set91), root_0)
                                self._state.errorRecovery = False

                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse


                            self._state.following.append(self.FOLLOW_eq_subexpr_in_cond_expr813)
                            eq_subexpr92 = self.eq_subexpr()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, eq_subexpr92.tree)


                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "cond_expr"

    class match_op_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.match_op_return, self).__init__()

            self.tree = None




    # $ANTLR start "match_op"
    # SQLite.g:200:1: match_op : ( LIKE | GLOB | REGEXP | MATCH );
    def match_op(self, ):

        retval = self.match_op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set93 = None

        set93_tree = None

        try:
            try:
                # SQLite.g:200:9: ( LIKE | GLOB | REGEXP | MATCH )
                # SQLite.g:
                pass 
                root_0 = self._adaptor.nil()

                set93 = self.input.LT(1)
                if (LIKE <= self.input.LA(1) <= MATCH):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set93))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "match_op"

    class eq_subexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.eq_subexpr_return, self).__init__()

            self.tree = None




    # $ANTLR start "eq_subexpr"
    # SQLite.g:202:1: eq_subexpr : neq_subexpr ( ( LESS | LESS_OR_EQ | GREATER | GREATER_OR_EQ ) neq_subexpr )* ;
    def eq_subexpr(self, ):

        retval = self.eq_subexpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set95 = None
        neq_subexpr94 = None

        neq_subexpr96 = None


        set95_tree = None

        try:
            try:
                # SQLite.g:202:11: ( neq_subexpr ( ( LESS | LESS_OR_EQ | GREATER | GREATER_OR_EQ ) neq_subexpr )* )
                # SQLite.g:202:13: neq_subexpr ( ( LESS | LESS_OR_EQ | GREATER | GREATER_OR_EQ ) neq_subexpr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_neq_subexpr_in_eq_subexpr846)
                neq_subexpr94 = self.neq_subexpr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, neq_subexpr94.tree)
                # SQLite.g:202:25: ( ( LESS | LESS_OR_EQ | GREATER | GREATER_OR_EQ ) neq_subexpr )*
                while True: #loop27
                    alt27 = 2
                    alt27 = self.dfa27.predict(self.input)
                    if alt27 == 1:
                        # SQLite.g:202:26: ( LESS | LESS_OR_EQ | GREATER | GREATER_OR_EQ ) neq_subexpr
                        pass 
                        set95 = self.input.LT(1)
                        set95 = self.input.LT(1)
                        if (LESS <= self.input.LA(1) <= GREATER_OR_EQ):
                            self.input.consume()
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set95), root_0)
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_neq_subexpr_in_eq_subexpr866)
                        neq_subexpr96 = self.neq_subexpr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, neq_subexpr96.tree)


                    else:
                        break #loop27



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "eq_subexpr"

    class neq_subexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.neq_subexpr_return, self).__init__()

            self.tree = None




    # $ANTLR start "neq_subexpr"
    # SQLite.g:204:1: neq_subexpr : bit_subexpr ( ( SHIFT_LEFT | SHIFT_RIGHT | AMPERSAND | PIPE ) bit_subexpr )* ;
    def neq_subexpr(self, ):

        retval = self.neq_subexpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set98 = None
        bit_subexpr97 = None

        bit_subexpr99 = None


        set98_tree = None

        try:
            try:
                # SQLite.g:204:12: ( bit_subexpr ( ( SHIFT_LEFT | SHIFT_RIGHT | AMPERSAND | PIPE ) bit_subexpr )* )
                # SQLite.g:204:14: bit_subexpr ( ( SHIFT_LEFT | SHIFT_RIGHT | AMPERSAND | PIPE ) bit_subexpr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_bit_subexpr_in_neq_subexpr875)
                bit_subexpr97 = self.bit_subexpr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, bit_subexpr97.tree)
                # SQLite.g:204:26: ( ( SHIFT_LEFT | SHIFT_RIGHT | AMPERSAND | PIPE ) bit_subexpr )*
                while True: #loop28
                    alt28 = 2
                    alt28 = self.dfa28.predict(self.input)
                    if alt28 == 1:
                        # SQLite.g:204:27: ( SHIFT_LEFT | SHIFT_RIGHT | AMPERSAND | PIPE ) bit_subexpr
                        pass 
                        set98 = self.input.LT(1)
                        set98 = self.input.LT(1)
                        if (SHIFT_LEFT <= self.input.LA(1) <= PIPE):
                            self.input.consume()
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set98), root_0)
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_bit_subexpr_in_neq_subexpr895)
                        bit_subexpr99 = self.bit_subexpr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, bit_subexpr99.tree)


                    else:
                        break #loop28



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "neq_subexpr"

    class bit_subexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.bit_subexpr_return, self).__init__()

            self.tree = None




    # $ANTLR start "bit_subexpr"
    # SQLite.g:206:1: bit_subexpr : add_subexpr ( ( PLUS | MINUS ) add_subexpr )* ;
    def bit_subexpr(self, ):

        retval = self.bit_subexpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set101 = None
        add_subexpr100 = None

        add_subexpr102 = None


        set101_tree = None

        try:
            try:
                # SQLite.g:206:12: ( add_subexpr ( ( PLUS | MINUS ) add_subexpr )* )
                # SQLite.g:206:14: add_subexpr ( ( PLUS | MINUS ) add_subexpr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_add_subexpr_in_bit_subexpr904)
                add_subexpr100 = self.add_subexpr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, add_subexpr100.tree)
                # SQLite.g:206:26: ( ( PLUS | MINUS ) add_subexpr )*
                while True: #loop29
                    alt29 = 2
                    alt29 = self.dfa29.predict(self.input)
                    if alt29 == 1:
                        # SQLite.g:206:27: ( PLUS | MINUS ) add_subexpr
                        pass 
                        set101 = self.input.LT(1)
                        set101 = self.input.LT(1)
                        if (PLUS <= self.input.LA(1) <= MINUS):
                            self.input.consume()
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set101), root_0)
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_add_subexpr_in_bit_subexpr916)
                        add_subexpr102 = self.add_subexpr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, add_subexpr102.tree)


                    else:
                        break #loop29



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "bit_subexpr"

    class add_subexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.add_subexpr_return, self).__init__()

            self.tree = None




    # $ANTLR start "add_subexpr"
    # SQLite.g:208:1: add_subexpr : mul_subexpr ( ( ASTERISK | SLASH | PERCENT ) mul_subexpr )* ;
    def add_subexpr(self, ):

        retval = self.add_subexpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set104 = None
        mul_subexpr103 = None

        mul_subexpr105 = None


        set104_tree = None

        try:
            try:
                # SQLite.g:208:12: ( mul_subexpr ( ( ASTERISK | SLASH | PERCENT ) mul_subexpr )* )
                # SQLite.g:208:14: mul_subexpr ( ( ASTERISK | SLASH | PERCENT ) mul_subexpr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_mul_subexpr_in_add_subexpr925)
                mul_subexpr103 = self.mul_subexpr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, mul_subexpr103.tree)
                # SQLite.g:208:26: ( ( ASTERISK | SLASH | PERCENT ) mul_subexpr )*
                while True: #loop30
                    alt30 = 2
                    alt30 = self.dfa30.predict(self.input)
                    if alt30 == 1:
                        # SQLite.g:208:27: ( ASTERISK | SLASH | PERCENT ) mul_subexpr
                        pass 
                        set104 = self.input.LT(1)
                        set104 = self.input.LT(1)
                        if (ASTERISK <= self.input.LA(1) <= PERCENT):
                            self.input.consume()
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set104), root_0)
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_mul_subexpr_in_add_subexpr941)
                        mul_subexpr105 = self.mul_subexpr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, mul_subexpr105.tree)


                    else:
                        break #loop30



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "add_subexpr"

    class mul_subexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.mul_subexpr_return, self).__init__()

            self.tree = None




    # $ANTLR start "mul_subexpr"
    # SQLite.g:210:1: mul_subexpr : con_subexpr ( DOUBLE_PIPE con_subexpr )* ;
    def mul_subexpr(self, ):

        retval = self.mul_subexpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOUBLE_PIPE107 = None
        con_subexpr106 = None

        con_subexpr108 = None


        DOUBLE_PIPE107_tree = None

        try:
            try:
                # SQLite.g:210:12: ( con_subexpr ( DOUBLE_PIPE con_subexpr )* )
                # SQLite.g:210:14: con_subexpr ( DOUBLE_PIPE con_subexpr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_con_subexpr_in_mul_subexpr950)
                con_subexpr106 = self.con_subexpr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, con_subexpr106.tree)
                # SQLite.g:210:26: ( DOUBLE_PIPE con_subexpr )*
                while True: #loop31
                    alt31 = 2
                    alt31 = self.dfa31.predict(self.input)
                    if alt31 == 1:
                        # SQLite.g:210:27: DOUBLE_PIPE con_subexpr
                        pass 
                        DOUBLE_PIPE107=self.match(self.input, DOUBLE_PIPE, self.FOLLOW_DOUBLE_PIPE_in_mul_subexpr953)

                        DOUBLE_PIPE107_tree = self._adaptor.createWithPayload(DOUBLE_PIPE107)
                        root_0 = self._adaptor.becomeRoot(DOUBLE_PIPE107_tree, root_0)

                        self._state.following.append(self.FOLLOW_con_subexpr_in_mul_subexpr956)
                        con_subexpr108 = self.con_subexpr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, con_subexpr108.tree)


                    else:
                        break #loop31



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "mul_subexpr"

    class con_subexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.con_subexpr_return, self).__init__()

            self.tree = None




    # $ANTLR start "con_subexpr"
    # SQLite.g:212:1: con_subexpr : ( unary_subexpr | unary_op unary_subexpr -> ^( unary_op unary_subexpr ) );
    def con_subexpr(self, ):

        retval = self.con_subexpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        unary_subexpr109 = None

        unary_op110 = None

        unary_subexpr111 = None


        stream_unary_subexpr = RewriteRuleSubtreeStream(self._adaptor, "rule unary_subexpr")
        stream_unary_op = RewriteRuleSubtreeStream(self._adaptor, "rule unary_op")
        try:
            try:
                # SQLite.g:212:12: ( unary_subexpr | unary_op unary_subexpr -> ^( unary_op unary_subexpr ) )
                alt32 = 2
                alt32 = self.dfa32.predict(self.input)
                if alt32 == 1:
                    # SQLite.g:212:14: unary_subexpr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_unary_subexpr_in_con_subexpr965)
                    unary_subexpr109 = self.unary_subexpr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unary_subexpr109.tree)


                elif alt32 == 2:
                    # SQLite.g:212:30: unary_op unary_subexpr
                    pass 
                    self._state.following.append(self.FOLLOW_unary_op_in_con_subexpr969)
                    unary_op110 = self.unary_op()

                    self._state.following.pop()
                    stream_unary_op.add(unary_op110.tree)
                    self._state.following.append(self.FOLLOW_unary_subexpr_in_con_subexpr971)
                    unary_subexpr111 = self.unary_subexpr()

                    self._state.following.pop()
                    stream_unary_subexpr.add(unary_subexpr111.tree)

                    # AST Rewrite
                    # elements: unary_subexpr, unary_op
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 212:53: -> ^( unary_op unary_subexpr )
                    # SQLite.g:212:56: ^( unary_op unary_subexpr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_unary_op.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_unary_subexpr.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "con_subexpr"

    class unary_op_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.unary_op_return, self).__init__()

            self.tree = None




    # $ANTLR start "unary_op"
    # SQLite.g:214:1: unary_op : ( PLUS | MINUS | TILDA | NOT );
    def unary_op(self, ):

        retval = self.unary_op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set112 = None

        set112_tree = None

        try:
            try:
                # SQLite.g:214:9: ( PLUS | MINUS | TILDA | NOT )
                # SQLite.g:
                pass 
                root_0 = self._adaptor.nil()

                set112 = self.input.LT(1)
                if self.input.LA(1) == NOT or (PLUS <= self.input.LA(1) <= MINUS) or self.input.LA(1) == TILDA:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set112))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "unary_op"

    class unary_subexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.unary_subexpr_return, self).__init__()

            self.tree = None




    # $ANTLR start "unary_subexpr"
    # SQLite.g:216:1: unary_subexpr : atom_expr ( COLLATE collation_name= ID )? ;
    def unary_subexpr(self, ):

        retval = self.unary_subexpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        collation_name = None
        COLLATE114 = None
        atom_expr113 = None


        collation_name_tree = None
        COLLATE114_tree = None

        try:
            try:
                # SQLite.g:216:14: ( atom_expr ( COLLATE collation_name= ID )? )
                # SQLite.g:216:16: atom_expr ( COLLATE collation_name= ID )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_atom_expr_in_unary_subexpr1005)
                atom_expr113 = self.atom_expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, atom_expr113.tree)
                # SQLite.g:216:26: ( COLLATE collation_name= ID )?
                alt33 = 2
                alt33 = self.dfa33.predict(self.input)
                if alt33 == 1:
                    # SQLite.g:216:27: COLLATE collation_name= ID
                    pass 
                    COLLATE114=self.match(self.input, COLLATE, self.FOLLOW_COLLATE_in_unary_subexpr1008)

                    COLLATE114_tree = self._adaptor.createWithPayload(COLLATE114)
                    root_0 = self._adaptor.becomeRoot(COLLATE114_tree, root_0)

                    collation_name=self.match(self.input, ID, self.FOLLOW_ID_in_unary_subexpr1013)

                    collation_name_tree = self._adaptor.createWithPayload(collation_name)
                    self._adaptor.addChild(root_0, collation_name_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "unary_subexpr"

    class atom_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.atom_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "atom_expr"
    # SQLite.g:218:1: atom_expr : ( literal_value | bind_parameter | ( (database_name= id DOT )? table_name= id DOT )? column_name= ID -> ^( COLUMN_EXPRESSION ^( $column_name ( ^( $table_name ( $database_name)? ) )? ) ) | name= ID LPAREN ( ( DISTINCT )? args+= expr ( COMMA args+= expr )* | ASTERISK )? RPAREN -> ^( FUNCTION_EXPRESSION $name ( DISTINCT )? ( $args)* ( ASTERISK )? ) | LPAREN expr RPAREN | CAST LPAREN expr AS type_name RPAREN | CASE (case_expr= expr )? ( when_expr )+ ( ELSE else_expr= expr )? END -> ^( CASE ( $case_expr)? ( when_expr )+ ( $else_expr)? ) | raise_function );
    def atom_expr(self, ):

        retval = self.atom_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        column_name = None
        name = None
        DOT117 = None
        DOT118 = None
        LPAREN119 = None
        DISTINCT120 = None
        COMMA121 = None
        ASTERISK122 = None
        RPAREN123 = None
        LPAREN124 = None
        RPAREN126 = None
        CAST127 = None
        LPAREN128 = None
        AS130 = None
        RPAREN132 = None
        CASE133 = None
        ELSE135 = None
        END136 = None
        list_args = None
        database_name = None

        table_name = None

        case_expr = None

        else_expr = None

        literal_value115 = None

        bind_parameter116 = None

        expr125 = None

        expr129 = None

        type_name131 = None

        when_expr134 = None

        raise_function137 = None

        args = None

        args = None
        column_name_tree = None
        name_tree = None
        DOT117_tree = None
        DOT118_tree = None
        LPAREN119_tree = None
        DISTINCT120_tree = None
        COMMA121_tree = None
        ASTERISK122_tree = None
        RPAREN123_tree = None
        LPAREN124_tree = None
        RPAREN126_tree = None
        CAST127_tree = None
        LPAREN128_tree = None
        AS130_tree = None
        RPAREN132_tree = None
        CASE133_tree = None
        ELSE135_tree = None
        END136_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_END = RewriteRuleTokenStream(self._adaptor, "token END")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_DISTINCT = RewriteRuleTokenStream(self._adaptor, "token DISTINCT")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_ASTERISK = RewriteRuleTokenStream(self._adaptor, "token ASTERISK")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_CASE = RewriteRuleTokenStream(self._adaptor, "token CASE")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_when_expr = RewriteRuleSubtreeStream(self._adaptor, "rule when_expr")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SQLite.g:219:3: ( literal_value | bind_parameter | ( (database_name= id DOT )? table_name= id DOT )? column_name= ID -> ^( COLUMN_EXPRESSION ^( $column_name ( ^( $table_name ( $database_name)? ) )? ) ) | name= ID LPAREN ( ( DISTINCT )? args+= expr ( COMMA args+= expr )* | ASTERISK )? RPAREN -> ^( FUNCTION_EXPRESSION $name ( DISTINCT )? ( $args)* ( ASTERISK )? ) | LPAREN expr RPAREN | CAST LPAREN expr AS type_name RPAREN | CASE (case_expr= expr )? ( when_expr )+ ( ELSE else_expr= expr )? END -> ^( CASE ( $case_expr)? ( when_expr )+ ( $else_expr)? ) | raise_function )
                alt42 = 8
                alt42 = self.dfa42.predict(self.input)
                if alt42 == 1:
                    # SQLite.g:219:5: literal_value
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_literal_value_in_atom_expr1025)
                    literal_value115 = self.literal_value()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, literal_value115.tree)


                elif alt42 == 2:
                    # SQLite.g:220:5: bind_parameter
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_bind_parameter_in_atom_expr1031)
                    bind_parameter116 = self.bind_parameter()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, bind_parameter116.tree)


                elif alt42 == 3:
                    # SQLite.g:221:5: ( (database_name= id DOT )? table_name= id DOT )? column_name= ID
                    pass 
                    # SQLite.g:221:5: ( (database_name= id DOT )? table_name= id DOT )?
                    alt35 = 2
                    alt35 = self.dfa35.predict(self.input)
                    if alt35 == 1:
                        # SQLite.g:221:6: (database_name= id DOT )? table_name= id DOT
                        pass 
                        # SQLite.g:221:6: (database_name= id DOT )?
                        alt34 = 2
                        alt34 = self.dfa34.predict(self.input)
                        if alt34 == 1:
                            # SQLite.g:221:7: database_name= id DOT
                            pass 
                            self._state.following.append(self.FOLLOW_id_in_atom_expr1041)
                            database_name = self.id()

                            self._state.following.pop()
                            stream_id.add(database_name.tree)
                            DOT117=self.match(self.input, DOT, self.FOLLOW_DOT_in_atom_expr1043) 
                            stream_DOT.add(DOT117)



                        self._state.following.append(self.FOLLOW_id_in_atom_expr1049)
                        table_name = self.id()

                        self._state.following.pop()
                        stream_id.add(table_name.tree)
                        DOT118=self.match(self.input, DOT, self.FOLLOW_DOT_in_atom_expr1051) 
                        stream_DOT.add(DOT118)



                    column_name=self.match(self.input, ID, self.FOLLOW_ID_in_atom_expr1057) 
                    stream_ID.add(column_name)

                    # AST Rewrite
                    # elements: table_name, column_name, database_name
                    # token labels: column_name
                    # rule labels: database_name, retval, table_name
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_column_name = RewriteRuleTokenStream(self._adaptor, "token column_name", column_name)

                    if database_name is not None:
                        stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "rule database_name", database_name.tree)
                    else:
                        stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "token database_name", None)


                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if table_name is not None:
                        stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "rule table_name", table_name.tree)
                    else:
                        stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "token table_name", None)


                    root_0 = self._adaptor.nil()
                    # 221:65: -> ^( COLUMN_EXPRESSION ^( $column_name ( ^( $table_name ( $database_name)? ) )? ) )
                    # SQLite.g:221:68: ^( COLUMN_EXPRESSION ^( $column_name ( ^( $table_name ( $database_name)? ) )? ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(COLUMN_EXPRESSION, "COLUMN_EXPRESSION"), root_1)

                    # SQLite.g:221:88: ^( $column_name ( ^( $table_name ( $database_name)? ) )? )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_column_name.nextNode(), root_2)

                    # SQLite.g:221:103: ( ^( $table_name ( $database_name)? ) )?
                    if stream_table_name.hasNext() or stream_database_name.hasNext():
                        # SQLite.g:221:103: ^( $table_name ( $database_name)? )
                        root_3 = self._adaptor.nil()
                        root_3 = self._adaptor.becomeRoot(stream_table_name.nextNode(), root_3)

                        # SQLite.g:221:117: ( $database_name)?
                        if stream_database_name.hasNext():
                            self._adaptor.addChild(root_3, stream_database_name.nextTree())


                        stream_database_name.reset();

                        self._adaptor.addChild(root_2, root_3)


                    stream_table_name.reset();
                    stream_database_name.reset();

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 4:
                    # SQLite.g:222:5: name= ID LPAREN ( ( DISTINCT )? args+= expr ( COMMA args+= expr )* | ASTERISK )? RPAREN
                    pass 
                    name=self.match(self.input, ID, self.FOLLOW_ID_in_atom_expr1086) 
                    stream_ID.add(name)
                    LPAREN119=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom_expr1088) 
                    stream_LPAREN.add(LPAREN119)
                    # SQLite.g:222:20: ( ( DISTINCT )? args+= expr ( COMMA args+= expr )* | ASTERISK )?
                    alt38 = 3
                    alt38 = self.dfa38.predict(self.input)
                    if alt38 == 1:
                        # SQLite.g:222:21: ( DISTINCT )? args+= expr ( COMMA args+= expr )*
                        pass 
                        # SQLite.g:222:21: ( DISTINCT )?
                        alt36 = 2
                        alt36 = self.dfa36.predict(self.input)
                        if alt36 == 1:
                            # SQLite.g:222:21: DISTINCT
                            pass 
                            DISTINCT120=self.match(self.input, DISTINCT, self.FOLLOW_DISTINCT_in_atom_expr1091) 
                            stream_DISTINCT.add(DISTINCT120)



                        self._state.following.append(self.FOLLOW_expr_in_atom_expr1096)
                        args = self.expr()

                        self._state.following.pop()
                        stream_expr.add(args.tree)
                        if list_args is None:
                            list_args = []
                        list_args.append(args.tree)

                        # SQLite.g:222:42: ( COMMA args+= expr )*
                        while True: #loop37
                            alt37 = 2
                            LA37_0 = self.input.LA(1)

                            if (LA37_0 == COMMA) :
                                alt37 = 1


                            if alt37 == 1:
                                # SQLite.g:222:43: COMMA args+= expr
                                pass 
                                COMMA121=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_atom_expr1099) 
                                stream_COMMA.add(COMMA121)
                                self._state.following.append(self.FOLLOW_expr_in_atom_expr1103)
                                args = self.expr()

                                self._state.following.pop()
                                stream_expr.add(args.tree)
                                if list_args is None:
                                    list_args = []
                                list_args.append(args.tree)



                            else:
                                break #loop37


                    elif alt38 == 2:
                        # SQLite.g:222:64: ASTERISK
                        pass 
                        ASTERISK122=self.match(self.input, ASTERISK, self.FOLLOW_ASTERISK_in_atom_expr1109) 
                        stream_ASTERISK.add(ASTERISK122)



                    RPAREN123=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom_expr1113) 
                    stream_RPAREN.add(RPAREN123)

                    # AST Rewrite
                    # elements: name, DISTINCT, args, ASTERISK
                    # token labels: name
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: args
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_name = RewriteRuleTokenStream(self._adaptor, "token name", name)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                    stream_args = RewriteRuleSubtreeStream(self._adaptor, "token args", list_args)
                    root_0 = self._adaptor.nil()
                    # 222:82: -> ^( FUNCTION_EXPRESSION $name ( DISTINCT )? ( $args)* ( ASTERISK )? )
                    # SQLite.g:222:85: ^( FUNCTION_EXPRESSION $name ( DISTINCT )? ( $args)* ( ASTERISK )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNCTION_EXPRESSION, "FUNCTION_EXPRESSION"), root_1)

                    self._adaptor.addChild(root_1, stream_name.nextNode())
                    # SQLite.g:222:113: ( DISTINCT )?
                    if stream_DISTINCT.hasNext():
                        self._adaptor.addChild(root_1, stream_DISTINCT.nextNode())


                    stream_DISTINCT.reset();
                    # SQLite.g:222:123: ( $args)*
                    while stream_args.hasNext():
                        self._adaptor.addChild(root_1, stream_args.nextTree())


                    stream_args.reset();
                    # SQLite.g:222:130: ( ASTERISK )?
                    if stream_ASTERISK.hasNext():
                        self._adaptor.addChild(root_1, stream_ASTERISK.nextNode())


                    stream_ASTERISK.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 5:
                    # SQLite.g:223:5: LPAREN expr RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN124=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom_expr1138)
                    self._state.following.append(self.FOLLOW_expr_in_atom_expr1141)
                    expr125 = self.expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expr125.tree)
                    RPAREN126=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom_expr1143)


                elif alt42 == 6:
                    # SQLite.g:224:5: CAST LPAREN expr AS type_name RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    CAST127=self.match(self.input, CAST, self.FOLLOW_CAST_in_atom_expr1150)

                    CAST127_tree = self._adaptor.createWithPayload(CAST127)
                    root_0 = self._adaptor.becomeRoot(CAST127_tree, root_0)

                    LPAREN128=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom_expr1153)
                    self._state.following.append(self.FOLLOW_expr_in_atom_expr1156)
                    expr129 = self.expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expr129.tree)
                    AS130=self.match(self.input, AS, self.FOLLOW_AS_in_atom_expr1158)
                    self._state.following.append(self.FOLLOW_type_name_in_atom_expr1161)
                    type_name131 = self.type_name()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, type_name131.tree)
                    RPAREN132=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom_expr1163)


                elif alt42 == 7:
                    # SQLite.g:227:5: CASE (case_expr= expr )? ( when_expr )+ ( ELSE else_expr= expr )? END
                    pass 
                    CASE133=self.match(self.input, CASE, self.FOLLOW_CASE_in_atom_expr1172) 
                    stream_CASE.add(CASE133)
                    # SQLite.g:227:10: (case_expr= expr )?
                    alt39 = 2
                    alt39 = self.dfa39.predict(self.input)
                    if alt39 == 1:
                        # SQLite.g:227:11: case_expr= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_atom_expr1177)
                        case_expr = self.expr()

                        self._state.following.pop()
                        stream_expr.add(case_expr.tree)



                    # SQLite.g:227:28: ( when_expr )+
                    cnt40 = 0
                    while True: #loop40
                        alt40 = 2
                        LA40_0 = self.input.LA(1)

                        if (LA40_0 == WHEN) :
                            alt40 = 1


                        if alt40 == 1:
                            # SQLite.g:227:28: when_expr
                            pass 
                            self._state.following.append(self.FOLLOW_when_expr_in_atom_expr1181)
                            when_expr134 = self.when_expr()

                            self._state.following.pop()
                            stream_when_expr.add(when_expr134.tree)


                        else:
                            if cnt40 >= 1:
                                break #loop40

                            eee = EarlyExitException(40, self.input)
                            raise eee

                        cnt40 += 1
                    # SQLite.g:227:39: ( ELSE else_expr= expr )?
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == ELSE) :
                        alt41 = 1
                    if alt41 == 1:
                        # SQLite.g:227:40: ELSE else_expr= expr
                        pass 
                        ELSE135=self.match(self.input, ELSE, self.FOLLOW_ELSE_in_atom_expr1185) 
                        stream_ELSE.add(ELSE135)
                        self._state.following.append(self.FOLLOW_expr_in_atom_expr1189)
                        else_expr = self.expr()

                        self._state.following.pop()
                        stream_expr.add(else_expr.tree)



                    END136=self.match(self.input, END, self.FOLLOW_END_in_atom_expr1193) 
                    stream_END.add(END136)

                    # AST Rewrite
                    # elements: case_expr, else_expr, when_expr, CASE
                    # token labels: 
                    # rule labels: retval, case_expr, else_expr
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if case_expr is not None:
                        stream_case_expr = RewriteRuleSubtreeStream(self._adaptor, "rule case_expr", case_expr.tree)
                    else:
                        stream_case_expr = RewriteRuleSubtreeStream(self._adaptor, "token case_expr", None)


                    if else_expr is not None:
                        stream_else_expr = RewriteRuleSubtreeStream(self._adaptor, "rule else_expr", else_expr.tree)
                    else:
                        stream_else_expr = RewriteRuleSubtreeStream(self._adaptor, "token else_expr", None)


                    root_0 = self._adaptor.nil()
                    # 227:66: -> ^( CASE ( $case_expr)? ( when_expr )+ ( $else_expr)? )
                    # SQLite.g:227:69: ^( CASE ( $case_expr)? ( when_expr )+ ( $else_expr)? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_CASE.nextNode(), root_1)

                    # SQLite.g:227:76: ( $case_expr)?
                    if stream_case_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_case_expr.nextTree())


                    stream_case_expr.reset();
                    # SQLite.g:227:88: ( when_expr )+
                    if not (stream_when_expr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_when_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_when_expr.nextTree())


                    stream_when_expr.reset()
                    # SQLite.g:227:99: ( $else_expr)?
                    if stream_else_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_else_expr.nextTree())


                    stream_else_expr.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 8:
                    # SQLite.g:228:5: raise_function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_raise_function_in_atom_expr1216)
                    raise_function137 = self.raise_function()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, raise_function137.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "atom_expr"

    class when_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.when_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "when_expr"
    # SQLite.g:231:1: when_expr : WHEN e1= expr THEN e2= expr -> ^( WHEN $e1 $e2) ;
    def when_expr(self, ):

        retval = self.when_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        WHEN138 = None
        THEN139 = None
        e1 = None

        e2 = None


        WHEN138_tree = None
        THEN139_tree = None
        stream_THEN = RewriteRuleTokenStream(self._adaptor, "token THEN")
        stream_WHEN = RewriteRuleTokenStream(self._adaptor, "token WHEN")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SQLite.g:231:10: ( WHEN e1= expr THEN e2= expr -> ^( WHEN $e1 $e2) )
                # SQLite.g:231:12: WHEN e1= expr THEN e2= expr
                pass 
                WHEN138=self.match(self.input, WHEN, self.FOLLOW_WHEN_in_when_expr1226) 
                stream_WHEN.add(WHEN138)
                self._state.following.append(self.FOLLOW_expr_in_when_expr1230)
                e1 = self.expr()

                self._state.following.pop()
                stream_expr.add(e1.tree)
                THEN139=self.match(self.input, THEN, self.FOLLOW_THEN_in_when_expr1232) 
                stream_THEN.add(THEN139)
                self._state.following.append(self.FOLLOW_expr_in_when_expr1236)
                e2 = self.expr()

                self._state.following.pop()
                stream_expr.add(e2.tree)

                # AST Rewrite
                # elements: e2, WHEN, e1
                # token labels: 
                # rule labels: retval, e1, e2
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if e1 is not None:
                    stream_e1 = RewriteRuleSubtreeStream(self._adaptor, "rule e1", e1.tree)
                else:
                    stream_e1 = RewriteRuleSubtreeStream(self._adaptor, "token e1", None)


                if e2 is not None:
                    stream_e2 = RewriteRuleSubtreeStream(self._adaptor, "rule e2", e2.tree)
                else:
                    stream_e2 = RewriteRuleSubtreeStream(self._adaptor, "token e2", None)


                root_0 = self._adaptor.nil()
                # 231:38: -> ^( WHEN $e1 $e2)
                # SQLite.g:231:41: ^( WHEN $e1 $e2)
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_WHEN.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_e1.nextTree())
                self._adaptor.addChild(root_1, stream_e2.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "when_expr"

    class literal_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.literal_value_return, self).__init__()

            self.tree = None




    # $ANTLR start "literal_value"
    # SQLite.g:233:1: literal_value : ( INTEGER -> ^( INTEGER_LITERAL INTEGER ) | FLOAT -> ^( FLOAT_LITERAL FLOAT ) | STRING -> ^( STRING_LITERAL STRING ) | BLOB -> ^( BLOB_LITERAL BLOB ) | NULL | CURRENT_TIME -> ^( FUNCTION_LITERAL CURRENT_TIME ) | CURRENT_DATE -> ^( FUNCTION_LITERAL CURRENT_DATE ) | CURRENT_TIMESTAMP -> ^( FUNCTION_LITERAL CURRENT_TIMESTAMP ) );
    def literal_value(self, ):

        retval = self.literal_value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INTEGER140 = None
        FLOAT141 = None
        STRING142 = None
        BLOB143 = None
        NULL144 = None
        CURRENT_TIME145 = None
        CURRENT_DATE146 = None
        CURRENT_TIMESTAMP147 = None

        INTEGER140_tree = None
        FLOAT141_tree = None
        STRING142_tree = None
        BLOB143_tree = None
        NULL144_tree = None
        CURRENT_TIME145_tree = None
        CURRENT_DATE146_tree = None
        CURRENT_TIMESTAMP147_tree = None
        stream_INTEGER = RewriteRuleTokenStream(self._adaptor, "token INTEGER")
        stream_BLOB = RewriteRuleTokenStream(self._adaptor, "token BLOB")
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")
        stream_CURRENT_TIMESTAMP = RewriteRuleTokenStream(self._adaptor, "token CURRENT_TIMESTAMP")
        stream_CURRENT_DATE = RewriteRuleTokenStream(self._adaptor, "token CURRENT_DATE")
        stream_CURRENT_TIME = RewriteRuleTokenStream(self._adaptor, "token CURRENT_TIME")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")

        try:
            try:
                # SQLite.g:234:3: ( INTEGER -> ^( INTEGER_LITERAL INTEGER ) | FLOAT -> ^( FLOAT_LITERAL FLOAT ) | STRING -> ^( STRING_LITERAL STRING ) | BLOB -> ^( BLOB_LITERAL BLOB ) | NULL | CURRENT_TIME -> ^( FUNCTION_LITERAL CURRENT_TIME ) | CURRENT_DATE -> ^( FUNCTION_LITERAL CURRENT_DATE ) | CURRENT_TIMESTAMP -> ^( FUNCTION_LITERAL CURRENT_TIMESTAMP ) )
                alt43 = 8
                LA43 = self.input.LA(1)
                if LA43 == INTEGER:
                    alt43 = 1
                elif LA43 == FLOAT:
                    alt43 = 2
                elif LA43 == STRING:
                    alt43 = 3
                elif LA43 == BLOB:
                    alt43 = 4
                elif LA43 == NULL:
                    alt43 = 5
                elif LA43 == CURRENT_TIME:
                    alt43 = 6
                elif LA43 == CURRENT_DATE:
                    alt43 = 7
                elif LA43 == CURRENT_TIMESTAMP:
                    alt43 = 8
                else:
                    nvae = NoViableAltException("", 43, 0, self.input)

                    raise nvae

                if alt43 == 1:
                    # SQLite.g:234:5: INTEGER
                    pass 
                    INTEGER140=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_literal_value1258) 
                    stream_INTEGER.add(INTEGER140)

                    # AST Rewrite
                    # elements: INTEGER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 234:13: -> ^( INTEGER_LITERAL INTEGER )
                    # SQLite.g:234:16: ^( INTEGER_LITERAL INTEGER )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INTEGER_LITERAL, "INTEGER_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_INTEGER.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt43 == 2:
                    # SQLite.g:235:5: FLOAT
                    pass 
                    FLOAT141=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_literal_value1272) 
                    stream_FLOAT.add(FLOAT141)

                    # AST Rewrite
                    # elements: FLOAT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 235:11: -> ^( FLOAT_LITERAL FLOAT )
                    # SQLite.g:235:14: ^( FLOAT_LITERAL FLOAT )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FLOAT_LITERAL, "FLOAT_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_FLOAT.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt43 == 3:
                    # SQLite.g:236:5: STRING
                    pass 
                    STRING142=self.match(self.input, STRING, self.FOLLOW_STRING_in_literal_value1286) 
                    stream_STRING.add(STRING142)

                    # AST Rewrite
                    # elements: STRING
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 236:12: -> ^( STRING_LITERAL STRING )
                    # SQLite.g:236:15: ^( STRING_LITERAL STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(STRING_LITERAL, "STRING_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt43 == 4:
                    # SQLite.g:237:5: BLOB
                    pass 
                    BLOB143=self.match(self.input, BLOB, self.FOLLOW_BLOB_in_literal_value1300) 
                    stream_BLOB.add(BLOB143)

                    # AST Rewrite
                    # elements: BLOB
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 237:10: -> ^( BLOB_LITERAL BLOB )
                    # SQLite.g:237:13: ^( BLOB_LITERAL BLOB )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOB_LITERAL, "BLOB_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_BLOB.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt43 == 5:
                    # SQLite.g:238:5: NULL
                    pass 
                    root_0 = self._adaptor.nil()

                    NULL144=self.match(self.input, NULL, self.FOLLOW_NULL_in_literal_value1314)

                    NULL144_tree = self._adaptor.createWithPayload(NULL144)
                    self._adaptor.addChild(root_0, NULL144_tree)



                elif alt43 == 6:
                    # SQLite.g:239:5: CURRENT_TIME
                    pass 
                    CURRENT_TIME145=self.match(self.input, CURRENT_TIME, self.FOLLOW_CURRENT_TIME_in_literal_value1320) 
                    stream_CURRENT_TIME.add(CURRENT_TIME145)

                    # AST Rewrite
                    # elements: CURRENT_TIME
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 239:18: -> ^( FUNCTION_LITERAL CURRENT_TIME )
                    # SQLite.g:239:21: ^( FUNCTION_LITERAL CURRENT_TIME )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNCTION_LITERAL, "FUNCTION_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_CURRENT_TIME.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt43 == 7:
                    # SQLite.g:240:5: CURRENT_DATE
                    pass 
                    CURRENT_DATE146=self.match(self.input, CURRENT_DATE, self.FOLLOW_CURRENT_DATE_in_literal_value1334) 
                    stream_CURRENT_DATE.add(CURRENT_DATE146)

                    # AST Rewrite
                    # elements: CURRENT_DATE
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 240:18: -> ^( FUNCTION_LITERAL CURRENT_DATE )
                    # SQLite.g:240:21: ^( FUNCTION_LITERAL CURRENT_DATE )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNCTION_LITERAL, "FUNCTION_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_CURRENT_DATE.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt43 == 8:
                    # SQLite.g:241:5: CURRENT_TIMESTAMP
                    pass 
                    CURRENT_TIMESTAMP147=self.match(self.input, CURRENT_TIMESTAMP, self.FOLLOW_CURRENT_TIMESTAMP_in_literal_value1348) 
                    stream_CURRENT_TIMESTAMP.add(CURRENT_TIMESTAMP147)

                    # AST Rewrite
                    # elements: CURRENT_TIMESTAMP
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 241:23: -> ^( FUNCTION_LITERAL CURRENT_TIMESTAMP )
                    # SQLite.g:241:26: ^( FUNCTION_LITERAL CURRENT_TIMESTAMP )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNCTION_LITERAL, "FUNCTION_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_CURRENT_TIMESTAMP.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "literal_value"

    class bind_parameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.bind_parameter_return, self).__init__()

            self.tree = None




    # $ANTLR start "bind_parameter"
    # SQLite.g:244:1: bind_parameter : ( QUESTION -> BIND | QUESTION position= INTEGER -> ^( BIND $position) | COLON name= id -> ^( BIND_NAME $name) | AT name= id -> ^( BIND_NAME $name) );
    def bind_parameter(self, ):

        retval = self.bind_parameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        position = None
        QUESTION148 = None
        QUESTION149 = None
        COLON150 = None
        AT151 = None
        name = None


        position_tree = None
        QUESTION148_tree = None
        QUESTION149_tree = None
        COLON150_tree = None
        AT151_tree = None
        stream_AT = RewriteRuleTokenStream(self._adaptor, "token AT")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_INTEGER = RewriteRuleTokenStream(self._adaptor, "token INTEGER")
        stream_QUESTION = RewriteRuleTokenStream(self._adaptor, "token QUESTION")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        try:
            try:
                # SQLite.g:245:3: ( QUESTION -> BIND | QUESTION position= INTEGER -> ^( BIND $position) | COLON name= id -> ^( BIND_NAME $name) | AT name= id -> ^( BIND_NAME $name) )
                alt44 = 4
                alt44 = self.dfa44.predict(self.input)
                if alt44 == 1:
                    # SQLite.g:245:5: QUESTION
                    pass 
                    QUESTION148=self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_bind_parameter1369) 
                    stream_QUESTION.add(QUESTION148)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 245:14: -> BIND
                    self._adaptor.addChild(root_0, self._adaptor.createFromType(BIND, "BIND"))



                    retval.tree = root_0


                elif alt44 == 2:
                    # SQLite.g:246:5: QUESTION position= INTEGER
                    pass 
                    QUESTION149=self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_bind_parameter1379) 
                    stream_QUESTION.add(QUESTION149)
                    position=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_bind_parameter1383) 
                    stream_INTEGER.add(position)

                    # AST Rewrite
                    # elements: position
                    # token labels: position
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_position = RewriteRuleTokenStream(self._adaptor, "token position", position)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 246:31: -> ^( BIND $position)
                    # SQLite.g:246:34: ^( BIND $position)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BIND, "BIND"), root_1)

                    self._adaptor.addChild(root_1, stream_position.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt44 == 3:
                    # SQLite.g:247:5: COLON name= id
                    pass 
                    COLON150=self.match(self.input, COLON, self.FOLLOW_COLON_in_bind_parameter1398) 
                    stream_COLON.add(COLON150)
                    self._state.following.append(self.FOLLOW_id_in_bind_parameter1402)
                    name = self.id()

                    self._state.following.pop()
                    stream_id.add(name.tree)

                    # AST Rewrite
                    # elements: name
                    # token labels: 
                    # rule labels: retval, name
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if name is not None:
                        stream_name = RewriteRuleSubtreeStream(self._adaptor, "rule name", name.tree)
                    else:
                        stream_name = RewriteRuleSubtreeStream(self._adaptor, "token name", None)


                    root_0 = self._adaptor.nil()
                    # 247:19: -> ^( BIND_NAME $name)
                    # SQLite.g:247:22: ^( BIND_NAME $name)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BIND_NAME, "BIND_NAME"), root_1)

                    self._adaptor.addChild(root_1, stream_name.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt44 == 4:
                    # SQLite.g:248:5: AT name= id
                    pass 
                    AT151=self.match(self.input, AT, self.FOLLOW_AT_in_bind_parameter1417) 
                    stream_AT.add(AT151)
                    self._state.following.append(self.FOLLOW_id_in_bind_parameter1421)
                    name = self.id()

                    self._state.following.pop()
                    stream_id.add(name.tree)

                    # AST Rewrite
                    # elements: name
                    # token labels: 
                    # rule labels: retval, name
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if name is not None:
                        stream_name = RewriteRuleSubtreeStream(self._adaptor, "rule name", name.tree)
                    else:
                        stream_name = RewriteRuleSubtreeStream(self._adaptor, "token name", None)


                    root_0 = self._adaptor.nil()
                    # 248:16: -> ^( BIND_NAME $name)
                    # SQLite.g:248:19: ^( BIND_NAME $name)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BIND_NAME, "BIND_NAME"), root_1)

                    self._adaptor.addChild(root_1, stream_name.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "bind_parameter"

    class raise_function_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.raise_function_return, self).__init__()

            self.tree = None




    # $ANTLR start "raise_function"
    # SQLite.g:253:1: raise_function : RAISE LPAREN ( IGNORE | ( ROLLBACK | ABORT | FAIL ) COMMA error_message= STRING ) RPAREN ;
    def raise_function(self, ):

        retval = self.raise_function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        error_message = None
        RAISE152 = None
        LPAREN153 = None
        IGNORE154 = None
        set155 = None
        COMMA156 = None
        RPAREN157 = None

        error_message_tree = None
        RAISE152_tree = None
        LPAREN153_tree = None
        IGNORE154_tree = None
        set155_tree = None
        COMMA156_tree = None
        RPAREN157_tree = None

        try:
            try:
                # SQLite.g:253:15: ( RAISE LPAREN ( IGNORE | ( ROLLBACK | ABORT | FAIL ) COMMA error_message= STRING ) RPAREN )
                # SQLite.g:253:17: RAISE LPAREN ( IGNORE | ( ROLLBACK | ABORT | FAIL ) COMMA error_message= STRING ) RPAREN
                pass 
                root_0 = self._adaptor.nil()

                RAISE152=self.match(self.input, RAISE, self.FOLLOW_RAISE_in_raise_function1442)

                RAISE152_tree = self._adaptor.createWithPayload(RAISE152)
                root_0 = self._adaptor.becomeRoot(RAISE152_tree, root_0)

                LPAREN153=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_raise_function1445)
                # SQLite.g:253:32: ( IGNORE | ( ROLLBACK | ABORT | FAIL ) COMMA error_message= STRING )
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if (LA45_0 == IGNORE) :
                    alt45 = 1
                elif ((ROLLBACK <= LA45_0 <= FAIL)) :
                    alt45 = 2
                else:
                    nvae = NoViableAltException("", 45, 0, self.input)

                    raise nvae

                if alt45 == 1:
                    # SQLite.g:253:33: IGNORE
                    pass 
                    IGNORE154=self.match(self.input, IGNORE, self.FOLLOW_IGNORE_in_raise_function1449)

                    IGNORE154_tree = self._adaptor.createWithPayload(IGNORE154)
                    self._adaptor.addChild(root_0, IGNORE154_tree)



                elif alt45 == 2:
                    # SQLite.g:253:42: ( ROLLBACK | ABORT | FAIL ) COMMA error_message= STRING
                    pass 
                    set155 = self.input.LT(1)
                    if (ROLLBACK <= self.input.LA(1) <= FAIL):
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set155))
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    COMMA156=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_raise_function1465)
                    error_message=self.match(self.input, STRING, self.FOLLOW_STRING_in_raise_function1470)

                    error_message_tree = self._adaptor.createWithPayload(error_message)
                    self._adaptor.addChild(root_0, error_message_tree)




                RPAREN157=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_raise_function1473)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "raise_function"

    class type_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.type_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "type_name"
    # SQLite.g:255:1: type_name : (names+= ID )+ ( LPAREN size1= signed_number ( COMMA size2= signed_number )? RPAREN )? -> ^( TYPE ^( TYPE_PARAMS ( $size1)? ( $size2)? ) ( $names)+ ) ;
    def type_name(self, ):

        retval = self.type_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN158 = None
        COMMA159 = None
        RPAREN160 = None
        names = None
        list_names = None
        size1 = None

        size2 = None


        LPAREN158_tree = None
        COMMA159_tree = None
        RPAREN160_tree = None
        names_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_signed_number = RewriteRuleSubtreeStream(self._adaptor, "rule signed_number")
        try:
            try:
                # SQLite.g:255:10: ( (names+= ID )+ ( LPAREN size1= signed_number ( COMMA size2= signed_number )? RPAREN )? -> ^( TYPE ^( TYPE_PARAMS ( $size1)? ( $size2)? ) ( $names)+ ) )
                # SQLite.g:255:12: (names+= ID )+ ( LPAREN size1= signed_number ( COMMA size2= signed_number )? RPAREN )?
                pass 
                # SQLite.g:255:17: (names+= ID )+
                cnt46 = 0
                while True: #loop46
                    alt46 = 2
                    alt46 = self.dfa46.predict(self.input)
                    if alt46 == 1:
                        # SQLite.g:255:17: names+= ID
                        pass 
                        names=self.match(self.input, ID, self.FOLLOW_ID_in_type_name1483) 
                        stream_ID.add(names)
                        if list_names is None:
                            list_names = []
                        list_names.append(names)



                    else:
                        if cnt46 >= 1:
                            break #loop46

                        eee = EarlyExitException(46, self.input)
                        raise eee

                    cnt46 += 1
                # SQLite.g:255:23: ( LPAREN size1= signed_number ( COMMA size2= signed_number )? RPAREN )?
                alt48 = 2
                alt48 = self.dfa48.predict(self.input)
                if alt48 == 1:
                    # SQLite.g:255:24: LPAREN size1= signed_number ( COMMA size2= signed_number )? RPAREN
                    pass 
                    LPAREN158=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_type_name1487) 
                    stream_LPAREN.add(LPAREN158)
                    self._state.following.append(self.FOLLOW_signed_number_in_type_name1491)
                    size1 = self.signed_number()

                    self._state.following.pop()
                    stream_signed_number.add(size1.tree)
                    # SQLite.g:255:51: ( COMMA size2= signed_number )?
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == COMMA) :
                        alt47 = 1
                    if alt47 == 1:
                        # SQLite.g:255:52: COMMA size2= signed_number
                        pass 
                        COMMA159=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_type_name1494) 
                        stream_COMMA.add(COMMA159)
                        self._state.following.append(self.FOLLOW_signed_number_in_type_name1498)
                        size2 = self.signed_number()

                        self._state.following.pop()
                        stream_signed_number.add(size2.tree)



                    RPAREN160=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_type_name1502) 
                    stream_RPAREN.add(RPAREN160)




                # AST Rewrite
                # elements: names, size2, size1
                # token labels: 
                # rule labels: retval, size2, size1
                # token list labels: names
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_names = RewriteRuleTokenStream(self._adaptor, "token names", list_names)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if size2 is not None:
                    stream_size2 = RewriteRuleSubtreeStream(self._adaptor, "rule size2", size2.tree)
                else:
                    stream_size2 = RewriteRuleSubtreeStream(self._adaptor, "token size2", None)


                if size1 is not None:
                    stream_size1 = RewriteRuleSubtreeStream(self._adaptor, "rule size1", size1.tree)
                else:
                    stream_size1 = RewriteRuleSubtreeStream(self._adaptor, "token size1", None)


                root_0 = self._adaptor.nil()
                # 256:1: -> ^( TYPE ^( TYPE_PARAMS ( $size1)? ( $size2)? ) ( $names)+ )
                # SQLite.g:256:4: ^( TYPE ^( TYPE_PARAMS ( $size1)? ( $size2)? ) ( $names)+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE, "TYPE"), root_1)

                # SQLite.g:256:11: ^( TYPE_PARAMS ( $size1)? ( $size2)? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE_PARAMS, "TYPE_PARAMS"), root_2)

                # SQLite.g:256:25: ( $size1)?
                if stream_size1.hasNext():
                    self._adaptor.addChild(root_2, stream_size1.nextTree())


                stream_size1.reset();
                # SQLite.g:256:33: ( $size2)?
                if stream_size2.hasNext():
                    self._adaptor.addChild(root_2, stream_size2.nextTree())


                stream_size2.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:256:42: ( $names)+
                if not (stream_names.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_names.hasNext():
                    self._adaptor.addChild(root_1, stream_names.nextNode())


                stream_names.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "type_name"

    class signed_number_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.signed_number_return, self).__init__()

            self.tree = None




    # $ANTLR start "signed_number"
    # SQLite.g:258:1: signed_number : ( PLUS | MINUS )? ( INTEGER | FLOAT ) ;
    def signed_number(self, ):

        retval = self.signed_number_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set161 = None
        set162 = None

        set161_tree = None
        set162_tree = None

        try:
            try:
                # SQLite.g:258:14: ( ( PLUS | MINUS )? ( INTEGER | FLOAT ) )
                # SQLite.g:258:16: ( PLUS | MINUS )? ( INTEGER | FLOAT )
                pass 
                root_0 = self._adaptor.nil()

                # SQLite.g:258:16: ( PLUS | MINUS )?
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if ((PLUS <= LA49_0 <= MINUS)) :
                    alt49 = 1
                if alt49 == 1:
                    # SQLite.g:
                    pass 
                    set161 = self.input.LT(1)
                    if (PLUS <= self.input.LA(1) <= MINUS):
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set161))
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse





                set162 = self.input.LT(1)
                if (INTEGER <= self.input.LA(1) <= FLOAT):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set162))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "signed_number"

    class pragma_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.pragma_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "pragma_stmt"
    # SQLite.g:261:1: pragma_stmt : PRAGMA (database_name= id DOT )? pragma_name= id ( EQUALS pragma_value | LPAREN pragma_value RPAREN )? -> ^( PRAGMA ^( $pragma_name ( $database_name)? ) ( pragma_value )? ) ;
    def pragma_stmt(self, ):

        retval = self.pragma_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PRAGMA163 = None
        DOT164 = None
        EQUALS165 = None
        LPAREN167 = None
        RPAREN169 = None
        database_name = None

        pragma_name = None

        pragma_value166 = None

        pragma_value168 = None


        PRAGMA163_tree = None
        DOT164_tree = None
        EQUALS165_tree = None
        LPAREN167_tree = None
        RPAREN169_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_EQUALS = RewriteRuleTokenStream(self._adaptor, "token EQUALS")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_PRAGMA = RewriteRuleTokenStream(self._adaptor, "token PRAGMA")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_pragma_value = RewriteRuleSubtreeStream(self._adaptor, "rule pragma_value")
        try:
            try:
                # SQLite.g:261:12: ( PRAGMA (database_name= id DOT )? pragma_name= id ( EQUALS pragma_value | LPAREN pragma_value RPAREN )? -> ^( PRAGMA ^( $pragma_name ( $database_name)? ) ( pragma_value )? ) )
                # SQLite.g:261:14: PRAGMA (database_name= id DOT )? pragma_name= id ( EQUALS pragma_value | LPAREN pragma_value RPAREN )?
                pass 
                PRAGMA163=self.match(self.input, PRAGMA, self.FOLLOW_PRAGMA_in_pragma_stmt1556) 
                stream_PRAGMA.add(PRAGMA163)
                # SQLite.g:261:21: (database_name= id DOT )?
                alt50 = 2
                alt50 = self.dfa50.predict(self.input)
                if alt50 == 1:
                    # SQLite.g:261:22: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_pragma_stmt1561)
                    database_name = self.id()

                    self._state.following.pop()
                    stream_id.add(database_name.tree)
                    DOT164=self.match(self.input, DOT, self.FOLLOW_DOT_in_pragma_stmt1563) 
                    stream_DOT.add(DOT164)



                self._state.following.append(self.FOLLOW_id_in_pragma_stmt1569)
                pragma_name = self.id()

                self._state.following.pop()
                stream_id.add(pragma_name.tree)
                # SQLite.g:261:60: ( EQUALS pragma_value | LPAREN pragma_value RPAREN )?
                alt51 = 3
                LA51_0 = self.input.LA(1)

                if (LA51_0 == EQUALS) :
                    alt51 = 1
                elif (LA51_0 == LPAREN) :
                    alt51 = 2
                if alt51 == 1:
                    # SQLite.g:261:61: EQUALS pragma_value
                    pass 
                    EQUALS165=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_pragma_stmt1572) 
                    stream_EQUALS.add(EQUALS165)
                    self._state.following.append(self.FOLLOW_pragma_value_in_pragma_stmt1574)
                    pragma_value166 = self.pragma_value()

                    self._state.following.pop()
                    stream_pragma_value.add(pragma_value166.tree)


                elif alt51 == 2:
                    # SQLite.g:261:83: LPAREN pragma_value RPAREN
                    pass 
                    LPAREN167=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_pragma_stmt1578) 
                    stream_LPAREN.add(LPAREN167)
                    self._state.following.append(self.FOLLOW_pragma_value_in_pragma_stmt1580)
                    pragma_value168 = self.pragma_value()

                    self._state.following.pop()
                    stream_pragma_value.add(pragma_value168.tree)
                    RPAREN169=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pragma_stmt1582) 
                    stream_RPAREN.add(RPAREN169)




                # AST Rewrite
                # elements: pragma_value, pragma_name, PRAGMA, database_name
                # token labels: 
                # rule labels: database_name, retval, pragma_name
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if database_name is not None:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "rule database_name", database_name.tree)
                else:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "token database_name", None)


                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if pragma_name is not None:
                    stream_pragma_name = RewriteRuleSubtreeStream(self._adaptor, "rule pragma_name", pragma_name.tree)
                else:
                    stream_pragma_name = RewriteRuleSubtreeStream(self._adaptor, "token pragma_name", None)


                root_0 = self._adaptor.nil()
                # 262:1: -> ^( PRAGMA ^( $pragma_name ( $database_name)? ) ( pragma_value )? )
                # SQLite.g:262:4: ^( PRAGMA ^( $pragma_name ( $database_name)? ) ( pragma_value )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_PRAGMA.nextNode(), root_1)

                # SQLite.g:262:13: ^( $pragma_name ( $database_name)? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(stream_pragma_name.nextNode(), root_2)

                # SQLite.g:262:28: ( $database_name)?
                if stream_database_name.hasNext():
                    self._adaptor.addChild(root_2, stream_database_name.nextTree())


                stream_database_name.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:262:45: ( pragma_value )?
                if stream_pragma_value.hasNext():
                    self._adaptor.addChild(root_1, stream_pragma_value.nextTree())


                stream_pragma_value.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pragma_stmt"

    class pragma_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.pragma_value_return, self).__init__()

            self.tree = None




    # $ANTLR start "pragma_value"
    # SQLite.g:264:1: pragma_value : ( signed_number -> ^( FLOAT_LITERAL signed_number ) | ID -> ^( ID_LITERAL ID ) | STRING -> ^( STRING_LITERAL STRING ) );
    def pragma_value(self, ):

        retval = self.pragma_value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID171 = None
        STRING172 = None
        signed_number170 = None


        ID171_tree = None
        STRING172_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")
        stream_signed_number = RewriteRuleSubtreeStream(self._adaptor, "rule signed_number")
        try:
            try:
                # SQLite.g:265:2: ( signed_number -> ^( FLOAT_LITERAL signed_number ) | ID -> ^( ID_LITERAL ID ) | STRING -> ^( STRING_LITERAL STRING ) )
                alt52 = 3
                LA52 = self.input.LA(1)
                if LA52 == PLUS or LA52 == MINUS or LA52 == INTEGER or LA52 == FLOAT:
                    alt52 = 1
                elif LA52 == ID:
                    alt52 = 2
                elif LA52 == STRING:
                    alt52 = 3
                else:
                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae

                if alt52 == 1:
                    # SQLite.g:265:4: signed_number
                    pass 
                    self._state.following.append(self.FOLLOW_signed_number_in_pragma_value1611)
                    signed_number170 = self.signed_number()

                    self._state.following.pop()
                    stream_signed_number.add(signed_number170.tree)

                    # AST Rewrite
                    # elements: signed_number
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 265:18: -> ^( FLOAT_LITERAL signed_number )
                    # SQLite.g:265:21: ^( FLOAT_LITERAL signed_number )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FLOAT_LITERAL, "FLOAT_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_signed_number.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt52 == 2:
                    # SQLite.g:266:4: ID
                    pass 
                    ID171=self.match(self.input, ID, self.FOLLOW_ID_in_pragma_value1624) 
                    stream_ID.add(ID171)

                    # AST Rewrite
                    # elements: ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 266:7: -> ^( ID_LITERAL ID )
                    # SQLite.g:266:10: ^( ID_LITERAL ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ID_LITERAL, "ID_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt52 == 3:
                    # SQLite.g:267:4: STRING
                    pass 
                    STRING172=self.match(self.input, STRING, self.FOLLOW_STRING_in_pragma_value1637) 
                    stream_STRING.add(STRING172)

                    # AST Rewrite
                    # elements: STRING
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 267:11: -> ^( STRING_LITERAL STRING )
                    # SQLite.g:267:14: ^( STRING_LITERAL STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(STRING_LITERAL, "STRING_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pragma_value"

    class attach_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.attach_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "attach_stmt"
    # SQLite.g:271:1: attach_stmt : ATTACH ( DATABASE )? filename= id AS database_name= id ;
    def attach_stmt(self, ):

        retval = self.attach_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ATTACH173 = None
        DATABASE174 = None
        AS175 = None
        filename = None

        database_name = None


        ATTACH173_tree = None
        DATABASE174_tree = None
        AS175_tree = None

        try:
            try:
                # SQLite.g:271:12: ( ATTACH ( DATABASE )? filename= id AS database_name= id )
                # SQLite.g:271:14: ATTACH ( DATABASE )? filename= id AS database_name= id
                pass 
                root_0 = self._adaptor.nil()

                ATTACH173=self.match(self.input, ATTACH, self.FOLLOW_ATTACH_in_attach_stmt1655)

                ATTACH173_tree = self._adaptor.createWithPayload(ATTACH173)
                self._adaptor.addChild(root_0, ATTACH173_tree)

                # SQLite.g:271:21: ( DATABASE )?
                alt53 = 2
                alt53 = self.dfa53.predict(self.input)
                if alt53 == 1:
                    # SQLite.g:271:22: DATABASE
                    pass 
                    DATABASE174=self.match(self.input, DATABASE, self.FOLLOW_DATABASE_in_attach_stmt1658)

                    DATABASE174_tree = self._adaptor.createWithPayload(DATABASE174)
                    self._adaptor.addChild(root_0, DATABASE174_tree)




                self._state.following.append(self.FOLLOW_id_in_attach_stmt1664)
                filename = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, filename.tree)
                AS175=self.match(self.input, AS, self.FOLLOW_AS_in_attach_stmt1666)

                AS175_tree = self._adaptor.createWithPayload(AS175)
                self._adaptor.addChild(root_0, AS175_tree)

                self._state.following.append(self.FOLLOW_id_in_attach_stmt1670)
                database_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, database_name.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "attach_stmt"

    class detach_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.detach_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "detach_stmt"
    # SQLite.g:274:1: detach_stmt : DETACH ( DATABASE )? database_name= id ;
    def detach_stmt(self, ):

        retval = self.detach_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DETACH176 = None
        DATABASE177 = None
        database_name = None


        DETACH176_tree = None
        DATABASE177_tree = None

        try:
            try:
                # SQLite.g:274:12: ( DETACH ( DATABASE )? database_name= id )
                # SQLite.g:274:14: DETACH ( DATABASE )? database_name= id
                pass 
                root_0 = self._adaptor.nil()

                DETACH176=self.match(self.input, DETACH, self.FOLLOW_DETACH_in_detach_stmt1678)

                DETACH176_tree = self._adaptor.createWithPayload(DETACH176)
                self._adaptor.addChild(root_0, DETACH176_tree)

                # SQLite.g:274:21: ( DATABASE )?
                alt54 = 2
                LA54_0 = self.input.LA(1)

                if (LA54_0 == DATABASE) :
                    LA54_1 = self.input.LA(2)

                    if ((EXPLAIN <= LA54_1 <= PLAN) or (INDEXED <= LA54_1 <= BY) or (OR <= LA54_1 <= ESCAPE) or (IS <= LA54_1 <= BETWEEN) or (COLLATE <= LA54_1 <= THEN) or LA54_1 == STRING or (CURRENT_TIME <= LA54_1 <= CURRENT_TIMESTAMP) or (RAISE <= LA54_1 <= ROW)) :
                        alt54 = 1
                if alt54 == 1:
                    # SQLite.g:274:22: DATABASE
                    pass 
                    DATABASE177=self.match(self.input, DATABASE, self.FOLLOW_DATABASE_in_detach_stmt1681)

                    DATABASE177_tree = self._adaptor.createWithPayload(DATABASE177)
                    self._adaptor.addChild(root_0, DATABASE177_tree)




                self._state.following.append(self.FOLLOW_id_in_detach_stmt1687)
                database_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, database_name.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "detach_stmt"

    class analyze_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.analyze_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "analyze_stmt"
    # SQLite.g:277:1: analyze_stmt : ANALYZE (database_or_table_name= id | database_name= id DOT table_name= id )? ;
    def analyze_stmt(self, ):

        retval = self.analyze_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ANALYZE178 = None
        DOT179 = None
        database_or_table_name = None

        database_name = None

        table_name = None


        ANALYZE178_tree = None
        DOT179_tree = None

        try:
            try:
                # SQLite.g:277:13: ( ANALYZE (database_or_table_name= id | database_name= id DOT table_name= id )? )
                # SQLite.g:277:15: ANALYZE (database_or_table_name= id | database_name= id DOT table_name= id )?
                pass 
                root_0 = self._adaptor.nil()

                ANALYZE178=self.match(self.input, ANALYZE, self.FOLLOW_ANALYZE_in_analyze_stmt1695)

                ANALYZE178_tree = self._adaptor.createWithPayload(ANALYZE178)
                self._adaptor.addChild(root_0, ANALYZE178_tree)

                # SQLite.g:277:23: (database_or_table_name= id | database_name= id DOT table_name= id )?
                alt55 = 3
                alt55 = self.dfa55.predict(self.input)
                if alt55 == 1:
                    # SQLite.g:277:24: database_or_table_name= id
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_analyze_stmt1700)
                    database_or_table_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, database_or_table_name.tree)


                elif alt55 == 2:
                    # SQLite.g:277:52: database_name= id DOT table_name= id
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_analyze_stmt1706)
                    database_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, database_name.tree)
                    DOT179=self.match(self.input, DOT, self.FOLLOW_DOT_in_analyze_stmt1708)

                    DOT179_tree = self._adaptor.createWithPayload(DOT179)
                    self._adaptor.addChild(root_0, DOT179_tree)

                    self._state.following.append(self.FOLLOW_id_in_analyze_stmt1712)
                    table_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, table_name.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "analyze_stmt"

    class reindex_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.reindex_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "reindex_stmt"
    # SQLite.g:280:1: reindex_stmt : REINDEX (database_name= id DOT )? collation_or_table_or_index_name= id ;
    def reindex_stmt(self, ):

        retval = self.reindex_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        REINDEX180 = None
        DOT181 = None
        database_name = None

        collation_or_table_or_index_name = None


        REINDEX180_tree = None
        DOT181_tree = None

        try:
            try:
                # SQLite.g:280:13: ( REINDEX (database_name= id DOT )? collation_or_table_or_index_name= id )
                # SQLite.g:280:15: REINDEX (database_name= id DOT )? collation_or_table_or_index_name= id
                pass 
                root_0 = self._adaptor.nil()

                REINDEX180=self.match(self.input, REINDEX, self.FOLLOW_REINDEX_in_reindex_stmt1722)

                REINDEX180_tree = self._adaptor.createWithPayload(REINDEX180)
                self._adaptor.addChild(root_0, REINDEX180_tree)

                # SQLite.g:280:23: (database_name= id DOT )?
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if (LA56_0 == ID or LA56_0 == STRING) :
                    LA56_1 = self.input.LA(2)

                    if (LA56_1 == DOT) :
                        alt56 = 1
                elif ((EXPLAIN <= LA56_0 <= PLAN) or (INDEXED <= LA56_0 <= BY) or (OR <= LA56_0 <= ESCAPE) or (IS <= LA56_0 <= BETWEEN) or LA56_0 == COLLATE or (DISTINCT <= LA56_0 <= THEN) or (CURRENT_TIME <= LA56_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA56_0 <= ROW)) :
                    LA56_2 = self.input.LA(2)

                    if (LA56_2 == DOT) :
                        alt56 = 1
                if alt56 == 1:
                    # SQLite.g:280:24: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_reindex_stmt1727)
                    database_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, database_name.tree)
                    DOT181=self.match(self.input, DOT, self.FOLLOW_DOT_in_reindex_stmt1729)

                    DOT181_tree = self._adaptor.createWithPayload(DOT181)
                    self._adaptor.addChild(root_0, DOT181_tree)




                self._state.following.append(self.FOLLOW_id_in_reindex_stmt1735)
                collation_or_table_or_index_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, collation_or_table_or_index_name.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "reindex_stmt"

    class vacuum_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.vacuum_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "vacuum_stmt"
    # SQLite.g:283:1: vacuum_stmt : VACUUM ;
    def vacuum_stmt(self, ):

        retval = self.vacuum_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        VACUUM182 = None

        VACUUM182_tree = None

        try:
            try:
                # SQLite.g:283:12: ( VACUUM )
                # SQLite.g:283:14: VACUUM
                pass 
                root_0 = self._adaptor.nil()

                VACUUM182=self.match(self.input, VACUUM, self.FOLLOW_VACUUM_in_vacuum_stmt1743)

                VACUUM182_tree = self._adaptor.createWithPayload(VACUUM182)
                self._adaptor.addChild(root_0, VACUUM182_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "vacuum_stmt"

    class operation_conflict_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.operation_conflict_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "operation_conflict_clause"
    # SQLite.g:289:1: operation_conflict_clause : OR ( ROLLBACK | ABORT | FAIL | IGNORE | REPLACE ) ;
    def operation_conflict_clause(self, ):

        retval = self.operation_conflict_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR183 = None
        set184 = None

        OR183_tree = None
        set184_tree = None

        try:
            try:
                # SQLite.g:289:26: ( OR ( ROLLBACK | ABORT | FAIL | IGNORE | REPLACE ) )
                # SQLite.g:289:28: OR ( ROLLBACK | ABORT | FAIL | IGNORE | REPLACE )
                pass 
                root_0 = self._adaptor.nil()

                OR183=self.match(self.input, OR, self.FOLLOW_OR_in_operation_conflict_clause1754)

                OR183_tree = self._adaptor.createWithPayload(OR183)
                self._adaptor.addChild(root_0, OR183_tree)

                set184 = self.input.LT(1)
                if (IGNORE <= self.input.LA(1) <= FAIL) or self.input.LA(1) == REPLACE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set184))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "operation_conflict_clause"

    class ordering_term_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.ordering_term_return, self).__init__()

            self.tree = None




    # $ANTLR start "ordering_term"
    # SQLite.g:291:1: ordering_term : expr ( ASC | DESC )? -> ^( ORDERING expr ( ASC )? ( DESC )? ) ;
    def ordering_term(self, ):

        retval = self.ordering_term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASC186 = None
        DESC187 = None
        expr185 = None


        ASC186_tree = None
        DESC187_tree = None
        stream_ASC = RewriteRuleTokenStream(self._adaptor, "token ASC")
        stream_DESC = RewriteRuleTokenStream(self._adaptor, "token DESC")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SQLite.g:291:14: ( expr ( ASC | DESC )? -> ^( ORDERING expr ( ASC )? ( DESC )? ) )
                # SQLite.g:291:16: expr ( ASC | DESC )?
                pass 
                self._state.following.append(self.FOLLOW_expr_in_ordering_term1781)
                expr185 = self.expr()

                self._state.following.pop()
                stream_expr.add(expr185.tree)
                # SQLite.g:291:82: ( ASC | DESC )?
                alt57 = 3
                alt57 = self.dfa57.predict(self.input)
                if alt57 == 1:
                    # SQLite.g:291:83: ASC
                    pass 
                    ASC186=self.match(self.input, ASC, self.FOLLOW_ASC_in_ordering_term1786) 
                    stream_ASC.add(ASC186)


                elif alt57 == 2:
                    # SQLite.g:291:89: DESC
                    pass 
                    DESC187=self.match(self.input, DESC, self.FOLLOW_DESC_in_ordering_term1790) 
                    stream_DESC.add(DESC187)




                # AST Rewrite
                # elements: ASC, expr, DESC
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 292:1: -> ^( ORDERING expr ( ASC )? ( DESC )? )
                # SQLite.g:292:4: ^( ORDERING expr ( ASC )? ( DESC )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ORDERING, "ORDERING"), root_1)

                self._adaptor.addChild(root_1, stream_expr.nextTree())
                # SQLite.g:292:20: ( ASC )?
                if stream_ASC.hasNext():
                    self._adaptor.addChild(root_1, stream_ASC.nextNode())


                stream_ASC.reset();
                # SQLite.g:292:27: ( DESC )?
                if stream_DESC.hasNext():
                    self._adaptor.addChild(root_1, stream_DESC.nextNode())


                stream_DESC.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "ordering_term"

    class operation_limited_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.operation_limited_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "operation_limited_clause"
    # SQLite.g:294:1: operation_limited_clause : ( ORDER BY ordering_term ( COMMA ordering_term )* )? LIMIT limit= INTEGER ( ( OFFSET | COMMA ) offset= INTEGER )? ;
    def operation_limited_clause(self, ):

        retval = self.operation_limited_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        limit = None
        offset = None
        ORDER188 = None
        BY189 = None
        COMMA191 = None
        LIMIT193 = None
        set194 = None
        ordering_term190 = None

        ordering_term192 = None


        limit_tree = None
        offset_tree = None
        ORDER188_tree = None
        BY189_tree = None
        COMMA191_tree = None
        LIMIT193_tree = None
        set194_tree = None

        try:
            try:
                # SQLite.g:294:25: ( ( ORDER BY ordering_term ( COMMA ordering_term )* )? LIMIT limit= INTEGER ( ( OFFSET | COMMA ) offset= INTEGER )? )
                # SQLite.g:295:3: ( ORDER BY ordering_term ( COMMA ordering_term )* )? LIMIT limit= INTEGER ( ( OFFSET | COMMA ) offset= INTEGER )?
                pass 
                root_0 = self._adaptor.nil()

                # SQLite.g:295:3: ( ORDER BY ordering_term ( COMMA ordering_term )* )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == ORDER) :
                    alt59 = 1
                if alt59 == 1:
                    # SQLite.g:295:4: ORDER BY ordering_term ( COMMA ordering_term )*
                    pass 
                    ORDER188=self.match(self.input, ORDER, self.FOLLOW_ORDER_in_operation_limited_clause1820)

                    ORDER188_tree = self._adaptor.createWithPayload(ORDER188)
                    self._adaptor.addChild(root_0, ORDER188_tree)

                    BY189=self.match(self.input, BY, self.FOLLOW_BY_in_operation_limited_clause1822)

                    BY189_tree = self._adaptor.createWithPayload(BY189)
                    self._adaptor.addChild(root_0, BY189_tree)

                    self._state.following.append(self.FOLLOW_ordering_term_in_operation_limited_clause1824)
                    ordering_term190 = self.ordering_term()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, ordering_term190.tree)
                    # SQLite.g:295:27: ( COMMA ordering_term )*
                    while True: #loop58
                        alt58 = 2
                        LA58_0 = self.input.LA(1)

                        if (LA58_0 == COMMA) :
                            alt58 = 1


                        if alt58 == 1:
                            # SQLite.g:295:28: COMMA ordering_term
                            pass 
                            COMMA191=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operation_limited_clause1827)

                            COMMA191_tree = self._adaptor.createWithPayload(COMMA191)
                            self._adaptor.addChild(root_0, COMMA191_tree)

                            self._state.following.append(self.FOLLOW_ordering_term_in_operation_limited_clause1829)
                            ordering_term192 = self.ordering_term()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, ordering_term192.tree)


                        else:
                            break #loop58



                LIMIT193=self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_operation_limited_clause1837)

                LIMIT193_tree = self._adaptor.createWithPayload(LIMIT193)
                self._adaptor.addChild(root_0, LIMIT193_tree)

                limit=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_operation_limited_clause1841)

                limit_tree = self._adaptor.createWithPayload(limit)
                self._adaptor.addChild(root_0, limit_tree)

                # SQLite.g:296:23: ( ( OFFSET | COMMA ) offset= INTEGER )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == COMMA or LA60_0 == OFFSET) :
                    alt60 = 1
                if alt60 == 1:
                    # SQLite.g:296:24: ( OFFSET | COMMA ) offset= INTEGER
                    pass 
                    set194 = self.input.LT(1)
                    if self.input.LA(1) == COMMA or self.input.LA(1) == OFFSET:
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set194))
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    offset=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_operation_limited_clause1854)

                    offset_tree = self._adaptor.createWithPayload(offset)
                    self._adaptor.addChild(root_0, offset_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "operation_limited_clause"

    class select_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.select_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "select_stmt"
    # SQLite.g:299:1: select_stmt : select_list ( ORDER BY ordering_term ( COMMA ordering_term )* )? ( LIMIT limit= INTEGER ( ( OFFSET | COMMA ) offset= INTEGER )? )? -> ^( SELECT select_list ( ^( ORDER ( ordering_term )+ ) )? ( ^( LIMIT $limit ( $offset)? ) )? ) ;
    def select_stmt(self, ):

        retval = self.select_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        limit = None
        offset = None
        ORDER196 = None
        BY197 = None
        COMMA199 = None
        LIMIT201 = None
        OFFSET202 = None
        COMMA203 = None
        select_list195 = None

        ordering_term198 = None

        ordering_term200 = None


        limit_tree = None
        offset_tree = None
        ORDER196_tree = None
        BY197_tree = None
        COMMA199_tree = None
        LIMIT201_tree = None
        OFFSET202_tree = None
        COMMA203_tree = None
        stream_INTEGER = RewriteRuleTokenStream(self._adaptor, "token INTEGER")
        stream_BY = RewriteRuleTokenStream(self._adaptor, "token BY")
        stream_ORDER = RewriteRuleTokenStream(self._adaptor, "token ORDER")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LIMIT = RewriteRuleTokenStream(self._adaptor, "token LIMIT")
        stream_OFFSET = RewriteRuleTokenStream(self._adaptor, "token OFFSET")
        stream_select_list = RewriteRuleSubtreeStream(self._adaptor, "rule select_list")
        stream_ordering_term = RewriteRuleSubtreeStream(self._adaptor, "rule ordering_term")
        try:
            try:
                # SQLite.g:299:12: ( select_list ( ORDER BY ordering_term ( COMMA ordering_term )* )? ( LIMIT limit= INTEGER ( ( OFFSET | COMMA ) offset= INTEGER )? )? -> ^( SELECT select_list ( ^( ORDER ( ordering_term )+ ) )? ( ^( LIMIT $limit ( $offset)? ) )? ) )
                # SQLite.g:299:14: select_list ( ORDER BY ordering_term ( COMMA ordering_term )* )? ( LIMIT limit= INTEGER ( ( OFFSET | COMMA ) offset= INTEGER )? )?
                pass 
                self._state.following.append(self.FOLLOW_select_list_in_select_stmt1864)
                select_list195 = self.select_list()

                self._state.following.pop()
                stream_select_list.add(select_list195.tree)
                # SQLite.g:300:3: ( ORDER BY ordering_term ( COMMA ordering_term )* )?
                alt62 = 2
                LA62_0 = self.input.LA(1)

                if (LA62_0 == ORDER) :
                    alt62 = 1
                if alt62 == 1:
                    # SQLite.g:300:4: ORDER BY ordering_term ( COMMA ordering_term )*
                    pass 
                    ORDER196=self.match(self.input, ORDER, self.FOLLOW_ORDER_in_select_stmt1869) 
                    stream_ORDER.add(ORDER196)
                    BY197=self.match(self.input, BY, self.FOLLOW_BY_in_select_stmt1871) 
                    stream_BY.add(BY197)
                    self._state.following.append(self.FOLLOW_ordering_term_in_select_stmt1873)
                    ordering_term198 = self.ordering_term()

                    self._state.following.pop()
                    stream_ordering_term.add(ordering_term198.tree)
                    # SQLite.g:300:27: ( COMMA ordering_term )*
                    while True: #loop61
                        alt61 = 2
                        LA61_0 = self.input.LA(1)

                        if (LA61_0 == COMMA) :
                            alt61 = 1


                        if alt61 == 1:
                            # SQLite.g:300:28: COMMA ordering_term
                            pass 
                            COMMA199=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_select_stmt1876) 
                            stream_COMMA.add(COMMA199)
                            self._state.following.append(self.FOLLOW_ordering_term_in_select_stmt1878)
                            ordering_term200 = self.ordering_term()

                            self._state.following.pop()
                            stream_ordering_term.add(ordering_term200.tree)


                        else:
                            break #loop61



                # SQLite.g:301:3: ( LIMIT limit= INTEGER ( ( OFFSET | COMMA ) offset= INTEGER )? )?
                alt65 = 2
                LA65_0 = self.input.LA(1)

                if (LA65_0 == LIMIT) :
                    alt65 = 1
                if alt65 == 1:
                    # SQLite.g:301:4: LIMIT limit= INTEGER ( ( OFFSET | COMMA ) offset= INTEGER )?
                    pass 
                    LIMIT201=self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_select_stmt1887) 
                    stream_LIMIT.add(LIMIT201)
                    limit=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_select_stmt1891) 
                    stream_INTEGER.add(limit)
                    # SQLite.g:301:24: ( ( OFFSET | COMMA ) offset= INTEGER )?
                    alt64 = 2
                    LA64_0 = self.input.LA(1)

                    if (LA64_0 == COMMA or LA64_0 == OFFSET) :
                        alt64 = 1
                    if alt64 == 1:
                        # SQLite.g:301:25: ( OFFSET | COMMA ) offset= INTEGER
                        pass 
                        # SQLite.g:301:25: ( OFFSET | COMMA )
                        alt63 = 2
                        LA63_0 = self.input.LA(1)

                        if (LA63_0 == OFFSET) :
                            alt63 = 1
                        elif (LA63_0 == COMMA) :
                            alt63 = 2
                        else:
                            nvae = NoViableAltException("", 63, 0, self.input)

                            raise nvae

                        if alt63 == 1:
                            # SQLite.g:301:26: OFFSET
                            pass 
                            OFFSET202=self.match(self.input, OFFSET, self.FOLLOW_OFFSET_in_select_stmt1895) 
                            stream_OFFSET.add(OFFSET202)


                        elif alt63 == 2:
                            # SQLite.g:301:35: COMMA
                            pass 
                            COMMA203=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_select_stmt1899) 
                            stream_COMMA.add(COMMA203)



                        offset=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_select_stmt1904) 
                        stream_INTEGER.add(offset)







                # AST Rewrite
                # elements: LIMIT, limit, select_list, ordering_term, offset, ORDER
                # token labels: limit, offset
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_limit = RewriteRuleTokenStream(self._adaptor, "token limit", limit)
                stream_offset = RewriteRuleTokenStream(self._adaptor, "token offset", offset)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 302:1: -> ^( SELECT select_list ( ^( ORDER ( ordering_term )+ ) )? ( ^( LIMIT $limit ( $offset)? ) )? )
                # SQLite.g:302:4: ^( SELECT select_list ( ^( ORDER ( ordering_term )+ ) )? ( ^( LIMIT $limit ( $offset)? ) )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SELECT, "SELECT"), root_1)

                self._adaptor.addChild(root_1, stream_select_list.nextTree())
                # SQLite.g:303:22: ( ^( ORDER ( ordering_term )+ ) )?
                if stream_ordering_term.hasNext() or stream_ORDER.hasNext():
                    # SQLite.g:303:22: ^( ORDER ( ordering_term )+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_ORDER.nextNode(), root_2)

                    # SQLite.g:303:30: ( ordering_term )+
                    if not (stream_ordering_term.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ordering_term.hasNext():
                        self._adaptor.addChild(root_2, stream_ordering_term.nextTree())


                    stream_ordering_term.reset()

                    self._adaptor.addChild(root_1, root_2)


                stream_ordering_term.reset();
                stream_ORDER.reset();
                # SQLite.g:303:47: ( ^( LIMIT $limit ( $offset)? ) )?
                if stream_LIMIT.hasNext() or stream_limit.hasNext() or stream_offset.hasNext():
                    # SQLite.g:303:47: ^( LIMIT $limit ( $offset)? )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_LIMIT.nextNode(), root_2)

                    self._adaptor.addChild(root_2, stream_limit.nextNode())
                    # SQLite.g:303:62: ( $offset)?
                    if stream_offset.hasNext():
                        self._adaptor.addChild(root_2, stream_offset.nextNode())


                    stream_offset.reset();

                    self._adaptor.addChild(root_1, root_2)


                stream_LIMIT.reset();
                stream_limit.reset();
                stream_offset.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "select_stmt"

    class select_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.select_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "select_list"
    # SQLite.g:306:1: select_list : select_core ( select_op select_core )* ;
    def select_list(self, ):

        retval = self.select_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        select_core204 = None

        select_op205 = None

        select_core206 = None



        try:
            try:
                # SQLite.g:306:12: ( select_core ( select_op select_core )* )
                # SQLite.g:307:3: select_core ( select_op select_core )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_select_core_in_select_list1949)
                select_core204 = self.select_core()

                self._state.following.pop()
                self._adaptor.addChild(root_0, select_core204.tree)
                # SQLite.g:307:15: ( select_op select_core )*
                while True: #loop66
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if (LA66_0 == UNION or (INTERSECT <= LA66_0 <= EXCEPT)) :
                        alt66 = 1


                    if alt66 == 1:
                        # SQLite.g:307:16: select_op select_core
                        pass 
                        self._state.following.append(self.FOLLOW_select_op_in_select_list1952)
                        select_op205 = self.select_op()

                        self._state.following.pop()
                        root_0 = self._adaptor.becomeRoot(select_op205.tree, root_0)
                        self._state.following.append(self.FOLLOW_select_core_in_select_list1955)
                        select_core206 = self.select_core()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, select_core206.tree)


                    else:
                        break #loop66



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "select_list"

    class select_op_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.select_op_return, self).__init__()

            self.tree = None




    # $ANTLR start "select_op"
    # SQLite.g:309:1: select_op : ( UNION ( ALL )? | INTERSECT | EXCEPT );
    def select_op(self, ):

        retval = self.select_op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        UNION207 = None
        ALL208 = None
        INTERSECT209 = None
        EXCEPT210 = None

        UNION207_tree = None
        ALL208_tree = None
        INTERSECT209_tree = None
        EXCEPT210_tree = None

        try:
            try:
                # SQLite.g:309:10: ( UNION ( ALL )? | INTERSECT | EXCEPT )
                alt68 = 3
                LA68 = self.input.LA(1)
                if LA68 == UNION:
                    alt68 = 1
                elif LA68 == INTERSECT:
                    alt68 = 2
                elif LA68 == EXCEPT:
                    alt68 = 3
                else:
                    nvae = NoViableAltException("", 68, 0, self.input)

                    raise nvae

                if alt68 == 1:
                    # SQLite.g:309:12: UNION ( ALL )?
                    pass 
                    root_0 = self._adaptor.nil()

                    UNION207=self.match(self.input, UNION, self.FOLLOW_UNION_in_select_op1964)

                    UNION207_tree = self._adaptor.createWithPayload(UNION207)
                    root_0 = self._adaptor.becomeRoot(UNION207_tree, root_0)

                    # SQLite.g:309:19: ( ALL )?
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if (LA67_0 == ALL) :
                        alt67 = 1
                    if alt67 == 1:
                        # SQLite.g:309:20: ALL
                        pass 
                        ALL208=self.match(self.input, ALL, self.FOLLOW_ALL_in_select_op1968)

                        ALL208_tree = self._adaptor.createWithPayload(ALL208)
                        self._adaptor.addChild(root_0, ALL208_tree)






                elif alt68 == 2:
                    # SQLite.g:309:28: INTERSECT
                    pass 
                    root_0 = self._adaptor.nil()

                    INTERSECT209=self.match(self.input, INTERSECT, self.FOLLOW_INTERSECT_in_select_op1974)

                    INTERSECT209_tree = self._adaptor.createWithPayload(INTERSECT209)
                    self._adaptor.addChild(root_0, INTERSECT209_tree)



                elif alt68 == 3:
                    # SQLite.g:309:40: EXCEPT
                    pass 
                    root_0 = self._adaptor.nil()

                    EXCEPT210=self.match(self.input, EXCEPT, self.FOLLOW_EXCEPT_in_select_op1978)

                    EXCEPT210_tree = self._adaptor.createWithPayload(EXCEPT210)
                    self._adaptor.addChild(root_0, EXCEPT210_tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "select_op"

    class select_core_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.select_core_return, self).__init__()

            self.tree = None




    # $ANTLR start "select_core"
    # SQLite.g:311:1: select_core : SELECT ( ALL | DISTINCT )? result_column ( COMMA result_column )* ( FROM join_source )? ( WHERE where_expr= expr )? ( GROUP BY ordering_term ( COMMA ordering_term )* ( HAVING having_expr= expr )? )? -> ^( SELECT_CORE ( DISTINCT )? ^( COLUMNS ( result_column )+ ) ( ^( FROM join_source ) )? ( ^( WHERE $where_expr) )? ( ^( GROUP ( ordering_term )+ ( ^( HAVING $having_expr) )? ) )? ) ;
    def select_core(self, ):

        retval = self.select_core_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SELECT211 = None
        ALL212 = None
        DISTINCT213 = None
        COMMA215 = None
        FROM217 = None
        WHERE219 = None
        GROUP220 = None
        BY221 = None
        COMMA223 = None
        HAVING225 = None
        where_expr = None

        having_expr = None

        result_column214 = None

        result_column216 = None

        join_source218 = None

        ordering_term222 = None

        ordering_term224 = None


        SELECT211_tree = None
        ALL212_tree = None
        DISTINCT213_tree = None
        COMMA215_tree = None
        FROM217_tree = None
        WHERE219_tree = None
        GROUP220_tree = None
        BY221_tree = None
        COMMA223_tree = None
        HAVING225_tree = None
        stream_WHERE = RewriteRuleTokenStream(self._adaptor, "token WHERE")
        stream_GROUP = RewriteRuleTokenStream(self._adaptor, "token GROUP")
        stream_BY = RewriteRuleTokenStream(self._adaptor, "token BY")
        stream_HAVING = RewriteRuleTokenStream(self._adaptor, "token HAVING")
        stream_FROM = RewriteRuleTokenStream(self._adaptor, "token FROM")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_SELECT = RewriteRuleTokenStream(self._adaptor, "token SELECT")
        stream_DISTINCT = RewriteRuleTokenStream(self._adaptor, "token DISTINCT")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_ordering_term = RewriteRuleSubtreeStream(self._adaptor, "rule ordering_term")
        stream_result_column = RewriteRuleSubtreeStream(self._adaptor, "rule result_column")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_join_source = RewriteRuleSubtreeStream(self._adaptor, "rule join_source")
        try:
            try:
                # SQLite.g:311:12: ( SELECT ( ALL | DISTINCT )? result_column ( COMMA result_column )* ( FROM join_source )? ( WHERE where_expr= expr )? ( GROUP BY ordering_term ( COMMA ordering_term )* ( HAVING having_expr= expr )? )? -> ^( SELECT_CORE ( DISTINCT )? ^( COLUMNS ( result_column )+ ) ( ^( FROM join_source ) )? ( ^( WHERE $where_expr) )? ( ^( GROUP ( ordering_term )+ ( ^( HAVING $having_expr) )? ) )? ) )
                # SQLite.g:312:3: SELECT ( ALL | DISTINCT )? result_column ( COMMA result_column )* ( FROM join_source )? ( WHERE where_expr= expr )? ( GROUP BY ordering_term ( COMMA ordering_term )* ( HAVING having_expr= expr )? )?
                pass 
                SELECT211=self.match(self.input, SELECT, self.FOLLOW_SELECT_in_select_core1987) 
                stream_SELECT.add(SELECT211)
                # SQLite.g:312:10: ( ALL | DISTINCT )?
                alt69 = 3
                alt69 = self.dfa69.predict(self.input)
                if alt69 == 1:
                    # SQLite.g:312:11: ALL
                    pass 
                    ALL212=self.match(self.input, ALL, self.FOLLOW_ALL_in_select_core1990) 
                    stream_ALL.add(ALL212)


                elif alt69 == 2:
                    # SQLite.g:312:17: DISTINCT
                    pass 
                    DISTINCT213=self.match(self.input, DISTINCT, self.FOLLOW_DISTINCT_in_select_core1994) 
                    stream_DISTINCT.add(DISTINCT213)



                self._state.following.append(self.FOLLOW_result_column_in_select_core1998)
                result_column214 = self.result_column()

                self._state.following.pop()
                stream_result_column.add(result_column214.tree)
                # SQLite.g:312:42: ( COMMA result_column )*
                while True: #loop70
                    alt70 = 2
                    alt70 = self.dfa70.predict(self.input)
                    if alt70 == 1:
                        # SQLite.g:312:43: COMMA result_column
                        pass 
                        COMMA215=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_select_core2001) 
                        stream_COMMA.add(COMMA215)
                        self._state.following.append(self.FOLLOW_result_column_in_select_core2003)
                        result_column216 = self.result_column()

                        self._state.following.pop()
                        stream_result_column.add(result_column216.tree)


                    else:
                        break #loop70
                # SQLite.g:312:65: ( FROM join_source )?
                alt71 = 2
                alt71 = self.dfa71.predict(self.input)
                if alt71 == 1:
                    # SQLite.g:312:66: FROM join_source
                    pass 
                    FROM217=self.match(self.input, FROM, self.FOLLOW_FROM_in_select_core2008) 
                    stream_FROM.add(FROM217)
                    self._state.following.append(self.FOLLOW_join_source_in_select_core2010)
                    join_source218 = self.join_source()

                    self._state.following.pop()
                    stream_join_source.add(join_source218.tree)



                # SQLite.g:312:85: ( WHERE where_expr= expr )?
                alt72 = 2
                alt72 = self.dfa72.predict(self.input)
                if alt72 == 1:
                    # SQLite.g:312:86: WHERE where_expr= expr
                    pass 
                    WHERE219=self.match(self.input, WHERE, self.FOLLOW_WHERE_in_select_core2015) 
                    stream_WHERE.add(WHERE219)
                    self._state.following.append(self.FOLLOW_expr_in_select_core2019)
                    where_expr = self.expr()

                    self._state.following.pop()
                    stream_expr.add(where_expr.tree)



                # SQLite.g:313:3: ( GROUP BY ordering_term ( COMMA ordering_term )* ( HAVING having_expr= expr )? )?
                alt75 = 2
                alt75 = self.dfa75.predict(self.input)
                if alt75 == 1:
                    # SQLite.g:313:5: GROUP BY ordering_term ( COMMA ordering_term )* ( HAVING having_expr= expr )?
                    pass 
                    GROUP220=self.match(self.input, GROUP, self.FOLLOW_GROUP_in_select_core2027) 
                    stream_GROUP.add(GROUP220)
                    BY221=self.match(self.input, BY, self.FOLLOW_BY_in_select_core2029) 
                    stream_BY.add(BY221)
                    self._state.following.append(self.FOLLOW_ordering_term_in_select_core2031)
                    ordering_term222 = self.ordering_term()

                    self._state.following.pop()
                    stream_ordering_term.add(ordering_term222.tree)
                    # SQLite.g:313:28: ( COMMA ordering_term )*
                    while True: #loop73
                        alt73 = 2
                        alt73 = self.dfa73.predict(self.input)
                        if alt73 == 1:
                            # SQLite.g:313:29: COMMA ordering_term
                            pass 
                            COMMA223=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_select_core2034) 
                            stream_COMMA.add(COMMA223)
                            self._state.following.append(self.FOLLOW_ordering_term_in_select_core2036)
                            ordering_term224 = self.ordering_term()

                            self._state.following.pop()
                            stream_ordering_term.add(ordering_term224.tree)


                        else:
                            break #loop73
                    # SQLite.g:313:51: ( HAVING having_expr= expr )?
                    alt74 = 2
                    alt74 = self.dfa74.predict(self.input)
                    if alt74 == 1:
                        # SQLite.g:313:52: HAVING having_expr= expr
                        pass 
                        HAVING225=self.match(self.input, HAVING, self.FOLLOW_HAVING_in_select_core2041) 
                        stream_HAVING.add(HAVING225)
                        self._state.following.append(self.FOLLOW_expr_in_select_core2045)
                        having_expr = self.expr()

                        self._state.following.pop()
                        stream_expr.add(having_expr.tree)







                # AST Rewrite
                # elements: HAVING, having_expr, FROM, GROUP, where_expr, DISTINCT, ordering_term, result_column, join_source, WHERE
                # token labels: 
                # rule labels: retval, having_expr, where_expr
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if having_expr is not None:
                    stream_having_expr = RewriteRuleSubtreeStream(self._adaptor, "rule having_expr", having_expr.tree)
                else:
                    stream_having_expr = RewriteRuleSubtreeStream(self._adaptor, "token having_expr", None)


                if where_expr is not None:
                    stream_where_expr = RewriteRuleSubtreeStream(self._adaptor, "rule where_expr", where_expr.tree)
                else:
                    stream_where_expr = RewriteRuleSubtreeStream(self._adaptor, "token where_expr", None)


                root_0 = self._adaptor.nil()
                # 314:1: -> ^( SELECT_CORE ( DISTINCT )? ^( COLUMNS ( result_column )+ ) ( ^( FROM join_source ) )? ( ^( WHERE $where_expr) )? ( ^( GROUP ( ordering_term )+ ( ^( HAVING $having_expr) )? ) )? )
                # SQLite.g:314:4: ^( SELECT_CORE ( DISTINCT )? ^( COLUMNS ( result_column )+ ) ( ^( FROM join_source ) )? ( ^( WHERE $where_expr) )? ( ^( GROUP ( ordering_term )+ ( ^( HAVING $having_expr) )? ) )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SELECT_CORE, "SELECT_CORE"), root_1)

                # SQLite.g:315:15: ( DISTINCT )?
                if stream_DISTINCT.hasNext():
                    self._adaptor.addChild(root_1, stream_DISTINCT.nextNode())


                stream_DISTINCT.reset();
                # SQLite.g:315:27: ^( COLUMNS ( result_column )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(COLUMNS, "COLUMNS"), root_2)

                # SQLite.g:315:37: ( result_column )+
                if not (stream_result_column.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_result_column.hasNext():
                    self._adaptor.addChild(root_2, stream_result_column.nextTree())


                stream_result_column.reset()

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:315:53: ( ^( FROM join_source ) )?
                if stream_FROM.hasNext() or stream_join_source.hasNext():
                    # SQLite.g:315:53: ^( FROM join_source )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_FROM.nextNode(), root_2)

                    self._adaptor.addChild(root_2, stream_join_source.nextTree())

                    self._adaptor.addChild(root_1, root_2)


                stream_FROM.reset();
                stream_join_source.reset();
                # SQLite.g:315:74: ( ^( WHERE $where_expr) )?
                if stream_where_expr.hasNext() or stream_WHERE.hasNext():
                    # SQLite.g:315:74: ^( WHERE $where_expr)
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_WHERE.nextNode(), root_2)

                    self._adaptor.addChild(root_2, stream_where_expr.nextTree())

                    self._adaptor.addChild(root_1, root_2)


                stream_where_expr.reset();
                stream_WHERE.reset();
                # SQLite.g:316:3: ( ^( GROUP ( ordering_term )+ ( ^( HAVING $having_expr) )? ) )?
                if stream_HAVING.hasNext() or stream_having_expr.hasNext() or stream_GROUP.hasNext() or stream_ordering_term.hasNext():
                    # SQLite.g:316:3: ^( GROUP ( ordering_term )+ ( ^( HAVING $having_expr) )? )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_GROUP.nextNode(), root_2)

                    # SQLite.g:316:11: ( ordering_term )+
                    if not (stream_ordering_term.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ordering_term.hasNext():
                        self._adaptor.addChild(root_2, stream_ordering_term.nextTree())


                    stream_ordering_term.reset()
                    # SQLite.g:316:26: ( ^( HAVING $having_expr) )?
                    if stream_HAVING.hasNext() or stream_having_expr.hasNext():
                        # SQLite.g:316:26: ^( HAVING $having_expr)
                        root_3 = self._adaptor.nil()
                        root_3 = self._adaptor.becomeRoot(stream_HAVING.nextNode(), root_3)

                        self._adaptor.addChild(root_3, stream_having_expr.nextTree())

                        self._adaptor.addChild(root_2, root_3)


                    stream_HAVING.reset();
                    stream_having_expr.reset();

                    self._adaptor.addChild(root_1, root_2)


                stream_HAVING.reset();
                stream_having_expr.reset();
                stream_GROUP.reset();
                stream_ordering_term.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "select_core"

    class result_column_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.result_column_return, self).__init__()

            self.tree = None




    # $ANTLR start "result_column"
    # SQLite.g:319:1: result_column : ( ASTERISK | table_name= id DOT ASTERISK -> ^( ASTERISK $table_name) | expr ( ( AS )? column_alias= id )? -> ^( ALIAS expr ( $column_alias)? ) );
    def result_column(self, ):

        retval = self.result_column_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASTERISK226 = None
        DOT227 = None
        ASTERISK228 = None
        AS230 = None
        table_name = None

        column_alias = None

        expr229 = None


        ASTERISK226_tree = None
        DOT227_tree = None
        ASTERISK228_tree = None
        AS230_tree = None
        stream_AS = RewriteRuleTokenStream(self._adaptor, "token AS")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ASTERISK = RewriteRuleTokenStream(self._adaptor, "token ASTERISK")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SQLite.g:320:3: ( ASTERISK | table_name= id DOT ASTERISK -> ^( ASTERISK $table_name) | expr ( ( AS )? column_alias= id )? -> ^( ALIAS expr ( $column_alias)? ) )
                alt78 = 3
                alt78 = self.dfa78.predict(self.input)
                if alt78 == 1:
                    # SQLite.g:320:5: ASTERISK
                    pass 
                    root_0 = self._adaptor.nil()

                    ASTERISK226=self.match(self.input, ASTERISK, self.FOLLOW_ASTERISK_in_result_column2115)

                    ASTERISK226_tree = self._adaptor.createWithPayload(ASTERISK226)
                    self._adaptor.addChild(root_0, ASTERISK226_tree)



                elif alt78 == 2:
                    # SQLite.g:321:5: table_name= id DOT ASTERISK
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_result_column2123)
                    table_name = self.id()

                    self._state.following.pop()
                    stream_id.add(table_name.tree)
                    DOT227=self.match(self.input, DOT, self.FOLLOW_DOT_in_result_column2125) 
                    stream_DOT.add(DOT227)
                    ASTERISK228=self.match(self.input, ASTERISK, self.FOLLOW_ASTERISK_in_result_column2127) 
                    stream_ASTERISK.add(ASTERISK228)

                    # AST Rewrite
                    # elements: ASTERISK, table_name
                    # token labels: 
                    # rule labels: retval, table_name
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if table_name is not None:
                        stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "rule table_name", table_name.tree)
                    else:
                        stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "token table_name", None)


                    root_0 = self._adaptor.nil()
                    # 321:32: -> ^( ASTERISK $table_name)
                    # SQLite.g:321:35: ^( ASTERISK $table_name)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_ASTERISK.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_table_name.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt78 == 3:
                    # SQLite.g:322:5: expr ( ( AS )? column_alias= id )?
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_result_column2142)
                    expr229 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr229.tree)
                    # SQLite.g:322:10: ( ( AS )? column_alias= id )?
                    alt77 = 2
                    alt77 = self.dfa77.predict(self.input)
                    if alt77 == 1:
                        # SQLite.g:322:11: ( AS )? column_alias= id
                        pass 
                        # SQLite.g:322:11: ( AS )?
                        alt76 = 2
                        alt76 = self.dfa76.predict(self.input)
                        if alt76 == 1:
                            # SQLite.g:322:12: AS
                            pass 
                            AS230=self.match(self.input, AS, self.FOLLOW_AS_in_result_column2146) 
                            stream_AS.add(AS230)



                        self._state.following.append(self.FOLLOW_id_in_result_column2152)
                        column_alias = self.id()

                        self._state.following.pop()
                        stream_id.add(column_alias.tree)




                    # AST Rewrite
                    # elements: column_alias, expr
                    # token labels: 
                    # rule labels: retval, column_alias
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if column_alias is not None:
                        stream_column_alias = RewriteRuleSubtreeStream(self._adaptor, "rule column_alias", column_alias.tree)
                    else:
                        stream_column_alias = RewriteRuleSubtreeStream(self._adaptor, "token column_alias", None)


                    root_0 = self._adaptor.nil()
                    # 322:35: -> ^( ALIAS expr ( $column_alias)? )
                    # SQLite.g:322:38: ^( ALIAS expr ( $column_alias)? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ALIAS, "ALIAS"), root_1)

                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # SQLite.g:322:51: ( $column_alias)?
                    if stream_column_alias.hasNext():
                        self._adaptor.addChild(root_1, stream_column_alias.nextTree())


                    stream_column_alias.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "result_column"

    class join_source_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.join_source_return, self).__init__()

            self.tree = None




    # $ANTLR start "join_source"
    # SQLite.g:324:1: join_source : single_source ( join_op single_source ( join_constraint )? )* ;
    def join_source(self, ):

        retval = self.join_source_return()
        retval.start = self.input.LT(1)

        root_0 = None

        single_source231 = None

        join_op232 = None

        single_source233 = None

        join_constraint234 = None



        try:
            try:
                # SQLite.g:324:12: ( single_source ( join_op single_source ( join_constraint )? )* )
                # SQLite.g:324:14: single_source ( join_op single_source ( join_constraint )? )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_single_source_in_join_source2173)
                single_source231 = self.single_source()

                self._state.following.pop()
                self._adaptor.addChild(root_0, single_source231.tree)
                # SQLite.g:324:28: ( join_op single_source ( join_constraint )? )*
                while True: #loop80
                    alt80 = 2
                    alt80 = self.dfa80.predict(self.input)
                    if alt80 == 1:
                        # SQLite.g:324:29: join_op single_source ( join_constraint )?
                        pass 
                        self._state.following.append(self.FOLLOW_join_op_in_join_source2176)
                        join_op232 = self.join_op()

                        self._state.following.pop()
                        root_0 = self._adaptor.becomeRoot(join_op232.tree, root_0)
                        self._state.following.append(self.FOLLOW_single_source_in_join_source2179)
                        single_source233 = self.single_source()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, single_source233.tree)
                        # SQLite.g:324:52: ( join_constraint )?
                        alt79 = 2
                        alt79 = self.dfa79.predict(self.input)
                        if alt79 == 1:
                            # SQLite.g:324:53: join_constraint
                            pass 
                            self._state.following.append(self.FOLLOW_join_constraint_in_join_source2182)
                            join_constraint234 = self.join_constraint()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, join_constraint234.tree)





                    else:
                        break #loop80



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "join_source"

    class single_source_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.single_source_return, self).__init__()

            self.tree = None




    # $ANTLR start "single_source"
    # SQLite.g:326:1: single_source : ( (database_name= id DOT )? table_name= ID ( ( AS )? table_alias= ID )? ( INDEXED BY index_name= id | NOT INDEXED )? -> ^( ALIAS ^( $table_name ( $database_name)? ) ( $table_alias)? ( ^( INDEXED ( NOT )? ( $index_name)? ) )? ) | LPAREN select_stmt RPAREN ( ( AS )? table_alias= ID )? -> ^( ALIAS select_stmt ( $table_alias)? ) | LPAREN join_source RPAREN );
    def single_source(self, ):

        retval = self.single_source_return()
        retval.start = self.input.LT(1)

        root_0 = None

        table_name = None
        table_alias = None
        DOT235 = None
        AS236 = None
        INDEXED237 = None
        BY238 = None
        NOT239 = None
        INDEXED240 = None
        LPAREN241 = None
        RPAREN243 = None
        AS244 = None
        LPAREN245 = None
        RPAREN247 = None
        database_name = None

        index_name = None

        select_stmt242 = None

        join_source246 = None


        table_name_tree = None
        table_alias_tree = None
        DOT235_tree = None
        AS236_tree = None
        INDEXED237_tree = None
        BY238_tree = None
        NOT239_tree = None
        INDEXED240_tree = None
        LPAREN241_tree = None
        RPAREN243_tree = None
        AS244_tree = None
        LPAREN245_tree = None
        RPAREN247_tree = None
        stream_INDEXED = RewriteRuleTokenStream(self._adaptor, "token INDEXED")
        stream_AS = RewriteRuleTokenStream(self._adaptor, "token AS")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_BY = RewriteRuleTokenStream(self._adaptor, "token BY")
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_select_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule select_stmt")
        try:
            try:
                # SQLite.g:327:3: ( (database_name= id DOT )? table_name= ID ( ( AS )? table_alias= ID )? ( INDEXED BY index_name= id | NOT INDEXED )? -> ^( ALIAS ^( $table_name ( $database_name)? ) ( $table_alias)? ( ^( INDEXED ( NOT )? ( $index_name)? ) )? ) | LPAREN select_stmt RPAREN ( ( AS )? table_alias= ID )? -> ^( ALIAS select_stmt ( $table_alias)? ) | LPAREN join_source RPAREN )
                alt87 = 3
                alt87 = self.dfa87.predict(self.input)
                if alt87 == 1:
                    # SQLite.g:327:5: (database_name= id DOT )? table_name= ID ( ( AS )? table_alias= ID )? ( INDEXED BY index_name= id | NOT INDEXED )?
                    pass 
                    # SQLite.g:327:5: (database_name= id DOT )?
                    alt81 = 2
                    alt81 = self.dfa81.predict(self.input)
                    if alt81 == 1:
                        # SQLite.g:327:6: database_name= id DOT
                        pass 
                        self._state.following.append(self.FOLLOW_id_in_single_source2199)
                        database_name = self.id()

                        self._state.following.pop()
                        stream_id.add(database_name.tree)
                        DOT235=self.match(self.input, DOT, self.FOLLOW_DOT_in_single_source2201) 
                        stream_DOT.add(DOT235)



                    table_name=self.match(self.input, ID, self.FOLLOW_ID_in_single_source2207) 
                    stream_ID.add(table_name)
                    # SQLite.g:327:43: ( ( AS )? table_alias= ID )?
                    alt83 = 2
                    alt83 = self.dfa83.predict(self.input)
                    if alt83 == 1:
                        # SQLite.g:327:44: ( AS )? table_alias= ID
                        pass 
                        # SQLite.g:327:44: ( AS )?
                        alt82 = 2
                        LA82_0 = self.input.LA(1)

                        if (LA82_0 == AS) :
                            alt82 = 1
                        if alt82 == 1:
                            # SQLite.g:327:45: AS
                            pass 
                            AS236=self.match(self.input, AS, self.FOLLOW_AS_in_single_source2211) 
                            stream_AS.add(AS236)



                        table_alias=self.match(self.input, ID, self.FOLLOW_ID_in_single_source2217) 
                        stream_ID.add(table_alias)



                    # SQLite.g:327:67: ( INDEXED BY index_name= id | NOT INDEXED )?
                    alt84 = 3
                    alt84 = self.dfa84.predict(self.input)
                    if alt84 == 1:
                        # SQLite.g:327:68: INDEXED BY index_name= id
                        pass 
                        INDEXED237=self.match(self.input, INDEXED, self.FOLLOW_INDEXED_in_single_source2222) 
                        stream_INDEXED.add(INDEXED237)
                        BY238=self.match(self.input, BY, self.FOLLOW_BY_in_single_source2224) 
                        stream_BY.add(BY238)
                        self._state.following.append(self.FOLLOW_id_in_single_source2228)
                        index_name = self.id()

                        self._state.following.pop()
                        stream_id.add(index_name.tree)


                    elif alt84 == 2:
                        # SQLite.g:327:95: NOT INDEXED
                        pass 
                        NOT239=self.match(self.input, NOT, self.FOLLOW_NOT_in_single_source2232) 
                        stream_NOT.add(NOT239)
                        INDEXED240=self.match(self.input, INDEXED, self.FOLLOW_INDEXED_in_single_source2234) 
                        stream_INDEXED.add(INDEXED240)




                    # AST Rewrite
                    # elements: database_name, NOT, INDEXED, table_name, table_alias, index_name
                    # token labels: table_name, table_alias
                    # rule labels: index_name, database_name, retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_table_name = RewriteRuleTokenStream(self._adaptor, "token table_name", table_name)
                    stream_table_alias = RewriteRuleTokenStream(self._adaptor, "token table_alias", table_alias)

                    if index_name is not None:
                        stream_index_name = RewriteRuleSubtreeStream(self._adaptor, "rule index_name", index_name.tree)
                    else:
                        stream_index_name = RewriteRuleSubtreeStream(self._adaptor, "token index_name", None)


                    if database_name is not None:
                        stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "rule database_name", database_name.tree)
                    else:
                        stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "token database_name", None)


                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 328:3: -> ^( ALIAS ^( $table_name ( $database_name)? ) ( $table_alias)? ( ^( INDEXED ( NOT )? ( $index_name)? ) )? )
                    # SQLite.g:328:6: ^( ALIAS ^( $table_name ( $database_name)? ) ( $table_alias)? ( ^( INDEXED ( NOT )? ( $index_name)? ) )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ALIAS, "ALIAS"), root_1)

                    # SQLite.g:328:14: ^( $table_name ( $database_name)? )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_table_name.nextNode(), root_2)

                    # SQLite.g:328:28: ( $database_name)?
                    if stream_database_name.hasNext():
                        self._adaptor.addChild(root_2, stream_database_name.nextTree())


                    stream_database_name.reset();

                    self._adaptor.addChild(root_1, root_2)
                    # SQLite.g:328:45: ( $table_alias)?
                    if stream_table_alias.hasNext():
                        self._adaptor.addChild(root_1, stream_table_alias.nextNode())


                    stream_table_alias.reset();
                    # SQLite.g:328:59: ( ^( INDEXED ( NOT )? ( $index_name)? ) )?
                    if stream_NOT.hasNext() or stream_INDEXED.hasNext() or stream_index_name.hasNext():
                        # SQLite.g:328:59: ^( INDEXED ( NOT )? ( $index_name)? )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(stream_INDEXED.nextNode(), root_2)

                        # SQLite.g:328:69: ( NOT )?
                        if stream_NOT.hasNext():
                            self._adaptor.addChild(root_2, stream_NOT.nextNode())


                        stream_NOT.reset();
                        # SQLite.g:328:74: ( $index_name)?
                        if stream_index_name.hasNext():
                            self._adaptor.addChild(root_2, stream_index_name.nextTree())


                        stream_index_name.reset();

                        self._adaptor.addChild(root_1, root_2)


                    stream_NOT.reset();
                    stream_INDEXED.reset();
                    stream_index_name.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt87 == 2:
                    # SQLite.g:329:5: LPAREN select_stmt RPAREN ( ( AS )? table_alias= ID )?
                    pass 
                    LPAREN241=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_single_source2275) 
                    stream_LPAREN.add(LPAREN241)
                    self._state.following.append(self.FOLLOW_select_stmt_in_single_source2277)
                    select_stmt242 = self.select_stmt()

                    self._state.following.pop()
                    stream_select_stmt.add(select_stmt242.tree)
                    RPAREN243=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_single_source2279) 
                    stream_RPAREN.add(RPAREN243)
                    # SQLite.g:329:31: ( ( AS )? table_alias= ID )?
                    alt86 = 2
                    alt86 = self.dfa86.predict(self.input)
                    if alt86 == 1:
                        # SQLite.g:329:32: ( AS )? table_alias= ID
                        pass 
                        # SQLite.g:329:32: ( AS )?
                        alt85 = 2
                        LA85_0 = self.input.LA(1)

                        if (LA85_0 == AS) :
                            alt85 = 1
                        if alt85 == 1:
                            # SQLite.g:329:33: AS
                            pass 
                            AS244=self.match(self.input, AS, self.FOLLOW_AS_in_single_source2283) 
                            stream_AS.add(AS244)



                        table_alias=self.match(self.input, ID, self.FOLLOW_ID_in_single_source2289) 
                        stream_ID.add(table_alias)




                    # AST Rewrite
                    # elements: table_alias, select_stmt
                    # token labels: table_alias
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_table_alias = RewriteRuleTokenStream(self._adaptor, "token table_alias", table_alias)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 330:3: -> ^( ALIAS select_stmt ( $table_alias)? )
                    # SQLite.g:330:6: ^( ALIAS select_stmt ( $table_alias)? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ALIAS, "ALIAS"), root_1)

                    self._adaptor.addChild(root_1, stream_select_stmt.nextTree())
                    # SQLite.g:330:26: ( $table_alias)?
                    if stream_table_alias.hasNext():
                        self._adaptor.addChild(root_1, stream_table_alias.nextNode())


                    stream_table_alias.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt87 == 3:
                    # SQLite.g:331:5: LPAREN join_source RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN245=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_single_source2311)
                    self._state.following.append(self.FOLLOW_join_source_in_single_source2314)
                    join_source246 = self.join_source()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, join_source246.tree)
                    RPAREN247=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_single_source2316)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "single_source"

    class join_op_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.join_op_return, self).__init__()

            self.tree = None




    # $ANTLR start "join_op"
    # SQLite.g:333:1: join_op : ( COMMA | ( NATURAL )? ( ( LEFT )? ( OUTER )? | INNER | CROSS ) JOIN );
    def join_op(self, ):

        retval = self.join_op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA248 = None
        NATURAL249 = None
        LEFT250 = None
        OUTER251 = None
        INNER252 = None
        CROSS253 = None
        JOIN254 = None

        COMMA248_tree = None
        NATURAL249_tree = None
        LEFT250_tree = None
        OUTER251_tree = None
        INNER252_tree = None
        CROSS253_tree = None
        JOIN254_tree = None

        try:
            try:
                # SQLite.g:334:3: ( COMMA | ( NATURAL )? ( ( LEFT )? ( OUTER )? | INNER | CROSS ) JOIN )
                alt92 = 2
                LA92_0 = self.input.LA(1)

                if (LA92_0 == COMMA) :
                    alt92 = 1
                elif ((NATURAL <= LA92_0 <= JOIN)) :
                    alt92 = 2
                else:
                    nvae = NoViableAltException("", 92, 0, self.input)

                    raise nvae

                if alt92 == 1:
                    # SQLite.g:334:5: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA248=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_join_op2327)

                    COMMA248_tree = self._adaptor.createWithPayload(COMMA248)
                    self._adaptor.addChild(root_0, COMMA248_tree)



                elif alt92 == 2:
                    # SQLite.g:335:5: ( NATURAL )? ( ( LEFT )? ( OUTER )? | INNER | CROSS ) JOIN
                    pass 
                    root_0 = self._adaptor.nil()

                    # SQLite.g:335:5: ( NATURAL )?
                    alt88 = 2
                    LA88_0 = self.input.LA(1)

                    if (LA88_0 == NATURAL) :
                        alt88 = 1
                    if alt88 == 1:
                        # SQLite.g:335:6: NATURAL
                        pass 
                        NATURAL249=self.match(self.input, NATURAL, self.FOLLOW_NATURAL_in_join_op2334)

                        NATURAL249_tree = self._adaptor.createWithPayload(NATURAL249)
                        self._adaptor.addChild(root_0, NATURAL249_tree)




                    # SQLite.g:335:16: ( ( LEFT )? ( OUTER )? | INNER | CROSS )
                    alt91 = 3
                    LA91 = self.input.LA(1)
                    if LA91 == LEFT or LA91 == OUTER or LA91 == JOIN:
                        alt91 = 1
                    elif LA91 == INNER:
                        alt91 = 2
                    elif LA91 == CROSS:
                        alt91 = 3
                    else:
                        nvae = NoViableAltException("", 91, 0, self.input)

                        raise nvae

                    if alt91 == 1:
                        # SQLite.g:335:17: ( LEFT )? ( OUTER )?
                        pass 
                        # SQLite.g:335:17: ( LEFT )?
                        alt89 = 2
                        LA89_0 = self.input.LA(1)

                        if (LA89_0 == LEFT) :
                            alt89 = 1
                        if alt89 == 1:
                            # SQLite.g:335:18: LEFT
                            pass 
                            LEFT250=self.match(self.input, LEFT, self.FOLLOW_LEFT_in_join_op2340)

                            LEFT250_tree = self._adaptor.createWithPayload(LEFT250)
                            self._adaptor.addChild(root_0, LEFT250_tree)




                        # SQLite.g:335:25: ( OUTER )?
                        alt90 = 2
                        LA90_0 = self.input.LA(1)

                        if (LA90_0 == OUTER) :
                            alt90 = 1
                        if alt90 == 1:
                            # SQLite.g:335:26: OUTER
                            pass 
                            OUTER251=self.match(self.input, OUTER, self.FOLLOW_OUTER_in_join_op2345)

                            OUTER251_tree = self._adaptor.createWithPayload(OUTER251)
                            self._adaptor.addChild(root_0, OUTER251_tree)






                    elif alt91 == 2:
                        # SQLite.g:335:36: INNER
                        pass 
                        INNER252=self.match(self.input, INNER, self.FOLLOW_INNER_in_join_op2351)

                        INNER252_tree = self._adaptor.createWithPayload(INNER252)
                        self._adaptor.addChild(root_0, INNER252_tree)



                    elif alt91 == 3:
                        # SQLite.g:335:44: CROSS
                        pass 
                        CROSS253=self.match(self.input, CROSS, self.FOLLOW_CROSS_in_join_op2355)

                        CROSS253_tree = self._adaptor.createWithPayload(CROSS253)
                        self._adaptor.addChild(root_0, CROSS253_tree)




                    JOIN254=self.match(self.input, JOIN, self.FOLLOW_JOIN_in_join_op2358)

                    JOIN254_tree = self._adaptor.createWithPayload(JOIN254)
                    root_0 = self._adaptor.becomeRoot(JOIN254_tree, root_0)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "join_op"

    class join_constraint_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.join_constraint_return, self).__init__()

            self.tree = None




    # $ANTLR start "join_constraint"
    # SQLite.g:337:1: join_constraint : ( ON expr | USING LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN -> ^( USING ( $column_names)+ ) );
    def join_constraint(self, ):

        retval = self.join_constraint_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ON255 = None
        USING257 = None
        LPAREN258 = None
        COMMA259 = None
        RPAREN260 = None
        list_column_names = None
        expr256 = None

        column_names = None

        column_names = None
        ON255_tree = None
        USING257_tree = None
        LPAREN258_tree = None
        COMMA259_tree = None
        RPAREN260_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_USING = RewriteRuleTokenStream(self._adaptor, "token USING")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        try:
            try:
                # SQLite.g:338:3: ( ON expr | USING LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN -> ^( USING ( $column_names)+ ) )
                alt94 = 2
                LA94_0 = self.input.LA(1)

                if (LA94_0 == ON) :
                    alt94 = 1
                elif (LA94_0 == USING) :
                    alt94 = 2
                else:
                    nvae = NoViableAltException("", 94, 0, self.input)

                    raise nvae

                if alt94 == 1:
                    # SQLite.g:338:5: ON expr
                    pass 
                    root_0 = self._adaptor.nil()

                    ON255=self.match(self.input, ON, self.FOLLOW_ON_in_join_constraint2369)

                    ON255_tree = self._adaptor.createWithPayload(ON255)
                    root_0 = self._adaptor.becomeRoot(ON255_tree, root_0)

                    self._state.following.append(self.FOLLOW_expr_in_join_constraint2372)
                    expr256 = self.expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expr256.tree)


                elif alt94 == 2:
                    # SQLite.g:339:5: USING LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN
                    pass 
                    USING257=self.match(self.input, USING, self.FOLLOW_USING_in_join_constraint2378) 
                    stream_USING.add(USING257)
                    LPAREN258=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_join_constraint2380) 
                    stream_LPAREN.add(LPAREN258)
                    self._state.following.append(self.FOLLOW_id_in_join_constraint2384)
                    column_names = self.id()

                    self._state.following.pop()
                    stream_id.add(column_names.tree)
                    if list_column_names is None:
                        list_column_names = []
                    list_column_names.append(column_names.tree)

                    # SQLite.g:339:35: ( COMMA column_names+= id )*
                    while True: #loop93
                        alt93 = 2
                        LA93_0 = self.input.LA(1)

                        if (LA93_0 == COMMA) :
                            alt93 = 1


                        if alt93 == 1:
                            # SQLite.g:339:36: COMMA column_names+= id
                            pass 
                            COMMA259=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_join_constraint2387) 
                            stream_COMMA.add(COMMA259)
                            self._state.following.append(self.FOLLOW_id_in_join_constraint2391)
                            column_names = self.id()

                            self._state.following.pop()
                            stream_id.add(column_names.tree)
                            if list_column_names is None:
                                list_column_names = []
                            list_column_names.append(column_names.tree)



                        else:
                            break #loop93
                    RPAREN260=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_join_constraint2395) 
                    stream_RPAREN.add(RPAREN260)

                    # AST Rewrite
                    # elements: column_names, USING
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: column_names
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                    stream_column_names = RewriteRuleSubtreeStream(self._adaptor, "token column_names", list_column_names)
                    root_0 = self._adaptor.nil()
                    # 339:68: -> ^( USING ( $column_names)+ )
                    # SQLite.g:339:71: ^( USING ( $column_names)+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_USING.nextNode(), root_1)

                    # SQLite.g:339:79: ( $column_names)+
                    if not (stream_column_names.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_column_names.hasNext():
                        self._adaptor.addChild(root_1, stream_column_names.nextTree())


                    stream_column_names.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "join_constraint"

    class insert_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.insert_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "insert_stmt"
    # SQLite.g:342:1: insert_stmt : ( INSERT ( operation_conflict_clause )? | REPLACE ) INTO (database_name= id DOT )? table_name= id ( ( LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN )? ( VALUES LPAREN values+= expr ( COMMA values+= expr )* RPAREN | select_stmt ) | DEFAULT VALUES ) ;
    def insert_stmt(self, ):

        retval = self.insert_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INSERT261 = None
        REPLACE263 = None
        INTO264 = None
        DOT265 = None
        LPAREN266 = None
        COMMA267 = None
        RPAREN268 = None
        VALUES269 = None
        LPAREN270 = None
        COMMA271 = None
        RPAREN272 = None
        DEFAULT274 = None
        VALUES275 = None
        list_column_names = None
        list_values = None
        database_name = None

        table_name = None

        operation_conflict_clause262 = None

        select_stmt273 = None

        column_names = None

        values = None

        column_names = None
        values = None
        INSERT261_tree = None
        REPLACE263_tree = None
        INTO264_tree = None
        DOT265_tree = None
        LPAREN266_tree = None
        COMMA267_tree = None
        RPAREN268_tree = None
        VALUES269_tree = None
        LPAREN270_tree = None
        COMMA271_tree = None
        RPAREN272_tree = None
        DEFAULT274_tree = None
        VALUES275_tree = None

        try:
            try:
                # SQLite.g:342:12: ( ( INSERT ( operation_conflict_clause )? | REPLACE ) INTO (database_name= id DOT )? table_name= id ( ( LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN )? ( VALUES LPAREN values+= expr ( COMMA values+= expr )* RPAREN | select_stmt ) | DEFAULT VALUES ) )
                # SQLite.g:342:14: ( INSERT ( operation_conflict_clause )? | REPLACE ) INTO (database_name= id DOT )? table_name= id ( ( LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN )? ( VALUES LPAREN values+= expr ( COMMA values+= expr )* RPAREN | select_stmt ) | DEFAULT VALUES )
                pass 
                root_0 = self._adaptor.nil()

                # SQLite.g:342:14: ( INSERT ( operation_conflict_clause )? | REPLACE )
                alt96 = 2
                LA96_0 = self.input.LA(1)

                if (LA96_0 == INSERT) :
                    alt96 = 1
                elif (LA96_0 == REPLACE) :
                    alt96 = 2
                else:
                    nvae = NoViableAltException("", 96, 0, self.input)

                    raise nvae

                if alt96 == 1:
                    # SQLite.g:342:15: INSERT ( operation_conflict_clause )?
                    pass 
                    INSERT261=self.match(self.input, INSERT, self.FOLLOW_INSERT_in_insert_stmt2414)

                    INSERT261_tree = self._adaptor.createWithPayload(INSERT261)
                    self._adaptor.addChild(root_0, INSERT261_tree)

                    # SQLite.g:342:22: ( operation_conflict_clause )?
                    alt95 = 2
                    LA95_0 = self.input.LA(1)

                    if (LA95_0 == OR) :
                        alt95 = 1
                    if alt95 == 1:
                        # SQLite.g:342:23: operation_conflict_clause
                        pass 
                        self._state.following.append(self.FOLLOW_operation_conflict_clause_in_insert_stmt2417)
                        operation_conflict_clause262 = self.operation_conflict_clause()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, operation_conflict_clause262.tree)





                elif alt96 == 2:
                    # SQLite.g:342:53: REPLACE
                    pass 
                    REPLACE263=self.match(self.input, REPLACE, self.FOLLOW_REPLACE_in_insert_stmt2423)

                    REPLACE263_tree = self._adaptor.createWithPayload(REPLACE263)
                    self._adaptor.addChild(root_0, REPLACE263_tree)




                INTO264=self.match(self.input, INTO, self.FOLLOW_INTO_in_insert_stmt2426)

                INTO264_tree = self._adaptor.createWithPayload(INTO264)
                self._adaptor.addChild(root_0, INTO264_tree)

                # SQLite.g:342:67: (database_name= id DOT )?
                alt97 = 2
                alt97 = self.dfa97.predict(self.input)
                if alt97 == 1:
                    # SQLite.g:342:68: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_insert_stmt2431)
                    database_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, database_name.tree)
                    DOT265=self.match(self.input, DOT, self.FOLLOW_DOT_in_insert_stmt2433)

                    DOT265_tree = self._adaptor.createWithPayload(DOT265)
                    self._adaptor.addChild(root_0, DOT265_tree)




                self._state.following.append(self.FOLLOW_id_in_insert_stmt2439)
                table_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, table_name.tree)
                # SQLite.g:343:3: ( ( LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN )? ( VALUES LPAREN values+= expr ( COMMA values+= expr )* RPAREN | select_stmt ) | DEFAULT VALUES )
                alt102 = 2
                LA102_0 = self.input.LA(1)

                if (LA102_0 == LPAREN or LA102_0 == SELECT or LA102_0 == VALUES) :
                    alt102 = 1
                elif (LA102_0 == DEFAULT) :
                    alt102 = 2
                else:
                    nvae = NoViableAltException("", 102, 0, self.input)

                    raise nvae

                if alt102 == 1:
                    # SQLite.g:343:5: ( LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN )? ( VALUES LPAREN values+= expr ( COMMA values+= expr )* RPAREN | select_stmt )
                    pass 
                    # SQLite.g:343:5: ( LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN )?
                    alt99 = 2
                    LA99_0 = self.input.LA(1)

                    if (LA99_0 == LPAREN) :
                        alt99 = 1
                    if alt99 == 1:
                        # SQLite.g:343:6: LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN
                        pass 
                        LPAREN266=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_insert_stmt2446)

                        LPAREN266_tree = self._adaptor.createWithPayload(LPAREN266)
                        self._adaptor.addChild(root_0, LPAREN266_tree)

                        self._state.following.append(self.FOLLOW_id_in_insert_stmt2450)
                        column_names = self.id()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, column_names.tree)
                        if list_column_names is None:
                            list_column_names = []
                        list_column_names.append(column_names.tree)

                        # SQLite.g:343:30: ( COMMA column_names+= id )*
                        while True: #loop98
                            alt98 = 2
                            LA98_0 = self.input.LA(1)

                            if (LA98_0 == COMMA) :
                                alt98 = 1


                            if alt98 == 1:
                                # SQLite.g:343:31: COMMA column_names+= id
                                pass 
                                COMMA267=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_insert_stmt2453)

                                COMMA267_tree = self._adaptor.createWithPayload(COMMA267)
                                self._adaptor.addChild(root_0, COMMA267_tree)

                                self._state.following.append(self.FOLLOW_id_in_insert_stmt2457)
                                column_names = self.id()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, column_names.tree)
                                if list_column_names is None:
                                    list_column_names = []
                                list_column_names.append(column_names.tree)



                            else:
                                break #loop98
                        RPAREN268=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_insert_stmt2461)

                        RPAREN268_tree = self._adaptor.createWithPayload(RPAREN268)
                        self._adaptor.addChild(root_0, RPAREN268_tree)




                    # SQLite.g:344:5: ( VALUES LPAREN values+= expr ( COMMA values+= expr )* RPAREN | select_stmt )
                    alt101 = 2
                    LA101_0 = self.input.LA(1)

                    if (LA101_0 == VALUES) :
                        alt101 = 1
                    elif (LA101_0 == SELECT) :
                        alt101 = 2
                    else:
                        nvae = NoViableAltException("", 101, 0, self.input)

                        raise nvae

                    if alt101 == 1:
                        # SQLite.g:344:6: VALUES LPAREN values+= expr ( COMMA values+= expr )* RPAREN
                        pass 
                        VALUES269=self.match(self.input, VALUES, self.FOLLOW_VALUES_in_insert_stmt2470)

                        VALUES269_tree = self._adaptor.createWithPayload(VALUES269)
                        self._adaptor.addChild(root_0, VALUES269_tree)

                        LPAREN270=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_insert_stmt2472)

                        LPAREN270_tree = self._adaptor.createWithPayload(LPAREN270)
                        self._adaptor.addChild(root_0, LPAREN270_tree)

                        self._state.following.append(self.FOLLOW_expr_in_insert_stmt2476)
                        values = self.expr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, values.tree)
                        if list_values is None:
                            list_values = []
                        list_values.append(values.tree)

                        # SQLite.g:344:33: ( COMMA values+= expr )*
                        while True: #loop100
                            alt100 = 2
                            LA100_0 = self.input.LA(1)

                            if (LA100_0 == COMMA) :
                                alt100 = 1


                            if alt100 == 1:
                                # SQLite.g:344:34: COMMA values+= expr
                                pass 
                                COMMA271=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_insert_stmt2479)

                                COMMA271_tree = self._adaptor.createWithPayload(COMMA271)
                                self._adaptor.addChild(root_0, COMMA271_tree)

                                self._state.following.append(self.FOLLOW_expr_in_insert_stmt2483)
                                values = self.expr()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, values.tree)
                                if list_values is None:
                                    list_values = []
                                list_values.append(values.tree)



                            else:
                                break #loop100
                        RPAREN272=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_insert_stmt2487)

                        RPAREN272_tree = self._adaptor.createWithPayload(RPAREN272)
                        self._adaptor.addChild(root_0, RPAREN272_tree)



                    elif alt101 == 2:
                        # SQLite.g:344:64: select_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_select_stmt_in_insert_stmt2491)
                        select_stmt273 = self.select_stmt()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, select_stmt273.tree)





                elif alt102 == 2:
                    # SQLite.g:345:5: DEFAULT VALUES
                    pass 
                    DEFAULT274=self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_insert_stmt2498)

                    DEFAULT274_tree = self._adaptor.createWithPayload(DEFAULT274)
                    self._adaptor.addChild(root_0, DEFAULT274_tree)

                    VALUES275=self.match(self.input, VALUES, self.FOLLOW_VALUES_in_insert_stmt2500)

                    VALUES275_tree = self._adaptor.createWithPayload(VALUES275)
                    self._adaptor.addChild(root_0, VALUES275_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "insert_stmt"

    class update_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.update_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "update_stmt"
    # SQLite.g:348:1: update_stmt : UPDATE ( operation_conflict_clause )? qualified_table_name SET values+= update_set ( COMMA values+= update_set )* ( WHERE expr )? ( operation_limited_clause )? ;
    def update_stmt(self, ):

        retval = self.update_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        UPDATE276 = None
        SET279 = None
        COMMA280 = None
        WHERE281 = None
        list_values = None
        operation_conflict_clause277 = None

        qualified_table_name278 = None

        expr282 = None

        operation_limited_clause283 = None

        values = None

        values = None
        UPDATE276_tree = None
        SET279_tree = None
        COMMA280_tree = None
        WHERE281_tree = None

        try:
            try:
                # SQLite.g:348:12: ( UPDATE ( operation_conflict_clause )? qualified_table_name SET values+= update_set ( COMMA values+= update_set )* ( WHERE expr )? ( operation_limited_clause )? )
                # SQLite.g:348:14: UPDATE ( operation_conflict_clause )? qualified_table_name SET values+= update_set ( COMMA values+= update_set )* ( WHERE expr )? ( operation_limited_clause )?
                pass 
                root_0 = self._adaptor.nil()

                UPDATE276=self.match(self.input, UPDATE, self.FOLLOW_UPDATE_in_update_stmt2510)

                UPDATE276_tree = self._adaptor.createWithPayload(UPDATE276)
                self._adaptor.addChild(root_0, UPDATE276_tree)

                # SQLite.g:348:21: ( operation_conflict_clause )?
                alt103 = 2
                LA103_0 = self.input.LA(1)

                if (LA103_0 == OR) :
                    LA103_1 = self.input.LA(2)

                    if ((IGNORE <= LA103_1 <= FAIL) or LA103_1 == REPLACE) :
                        alt103 = 1
                if alt103 == 1:
                    # SQLite.g:348:22: operation_conflict_clause
                    pass 
                    self._state.following.append(self.FOLLOW_operation_conflict_clause_in_update_stmt2513)
                    operation_conflict_clause277 = self.operation_conflict_clause()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, operation_conflict_clause277.tree)



                self._state.following.append(self.FOLLOW_qualified_table_name_in_update_stmt2517)
                qualified_table_name278 = self.qualified_table_name()

                self._state.following.pop()
                self._adaptor.addChild(root_0, qualified_table_name278.tree)
                SET279=self.match(self.input, SET, self.FOLLOW_SET_in_update_stmt2521)

                SET279_tree = self._adaptor.createWithPayload(SET279)
                self._adaptor.addChild(root_0, SET279_tree)

                self._state.following.append(self.FOLLOW_update_set_in_update_stmt2525)
                values = self.update_set()

                self._state.following.pop()
                self._adaptor.addChild(root_0, values.tree)
                if list_values is None:
                    list_values = []
                list_values.append(values.tree)

                # SQLite.g:349:26: ( COMMA values+= update_set )*
                while True: #loop104
                    alt104 = 2
                    LA104_0 = self.input.LA(1)

                    if (LA104_0 == COMMA) :
                        alt104 = 1


                    if alt104 == 1:
                        # SQLite.g:349:27: COMMA values+= update_set
                        pass 
                        COMMA280=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_update_stmt2528)

                        COMMA280_tree = self._adaptor.createWithPayload(COMMA280)
                        self._adaptor.addChild(root_0, COMMA280_tree)

                        self._state.following.append(self.FOLLOW_update_set_in_update_stmt2532)
                        values = self.update_set()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, values.tree)
                        if list_values is None:
                            list_values = []
                        list_values.append(values.tree)



                    else:
                        break #loop104
                # SQLite.g:349:54: ( WHERE expr )?
                alt105 = 2
                LA105_0 = self.input.LA(1)

                if (LA105_0 == WHERE) :
                    alt105 = 1
                if alt105 == 1:
                    # SQLite.g:349:55: WHERE expr
                    pass 
                    WHERE281=self.match(self.input, WHERE, self.FOLLOW_WHERE_in_update_stmt2537)

                    WHERE281_tree = self._adaptor.createWithPayload(WHERE281)
                    self._adaptor.addChild(root_0, WHERE281_tree)

                    self._state.following.append(self.FOLLOW_expr_in_update_stmt2539)
                    expr282 = self.expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expr282.tree)



                # SQLite.g:349:68: ( operation_limited_clause )?
                alt106 = 2
                LA106_0 = self.input.LA(1)

                if ((ORDER <= LA106_0 <= LIMIT)) :
                    alt106 = 1
                if alt106 == 1:
                    # SQLite.g:349:69: operation_limited_clause
                    pass 
                    self._state.following.append(self.FOLLOW_operation_limited_clause_in_update_stmt2544)
                    operation_limited_clause283 = self.operation_limited_clause()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, operation_limited_clause283.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "update_stmt"

    class update_set_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.update_set_return, self).__init__()

            self.tree = None




    # $ANTLR start "update_set"
    # SQLite.g:351:1: update_set : column_name= id EQUALS expr ;
    def update_set(self, ):

        retval = self.update_set_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQUALS284 = None
        column_name = None

        expr285 = None


        EQUALS284_tree = None

        try:
            try:
                # SQLite.g:351:11: (column_name= id EQUALS expr )
                # SQLite.g:351:13: column_name= id EQUALS expr
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_id_in_update_set2555)
                column_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, column_name.tree)
                EQUALS284=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_update_set2557)

                EQUALS284_tree = self._adaptor.createWithPayload(EQUALS284)
                self._adaptor.addChild(root_0, EQUALS284_tree)

                self._state.following.append(self.FOLLOW_expr_in_update_set2559)
                expr285 = self.expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expr285.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "update_set"

    class delete_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.delete_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "delete_stmt"
    # SQLite.g:354:1: delete_stmt : DELETE FROM qualified_table_name ( WHERE expr )? ( operation_limited_clause )? ;
    def delete_stmt(self, ):

        retval = self.delete_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DELETE286 = None
        FROM287 = None
        WHERE289 = None
        qualified_table_name288 = None

        expr290 = None

        operation_limited_clause291 = None


        DELETE286_tree = None
        FROM287_tree = None
        WHERE289_tree = None

        try:
            try:
                # SQLite.g:354:12: ( DELETE FROM qualified_table_name ( WHERE expr )? ( operation_limited_clause )? )
                # SQLite.g:354:14: DELETE FROM qualified_table_name ( WHERE expr )? ( operation_limited_clause )?
                pass 
                root_0 = self._adaptor.nil()

                DELETE286=self.match(self.input, DELETE, self.FOLLOW_DELETE_in_delete_stmt2567)

                DELETE286_tree = self._adaptor.createWithPayload(DELETE286)
                self._adaptor.addChild(root_0, DELETE286_tree)

                FROM287=self.match(self.input, FROM, self.FOLLOW_FROM_in_delete_stmt2569)

                FROM287_tree = self._adaptor.createWithPayload(FROM287)
                self._adaptor.addChild(root_0, FROM287_tree)

                self._state.following.append(self.FOLLOW_qualified_table_name_in_delete_stmt2571)
                qualified_table_name288 = self.qualified_table_name()

                self._state.following.pop()
                self._adaptor.addChild(root_0, qualified_table_name288.tree)
                # SQLite.g:354:47: ( WHERE expr )?
                alt107 = 2
                LA107_0 = self.input.LA(1)

                if (LA107_0 == WHERE) :
                    alt107 = 1
                if alt107 == 1:
                    # SQLite.g:354:48: WHERE expr
                    pass 
                    WHERE289=self.match(self.input, WHERE, self.FOLLOW_WHERE_in_delete_stmt2574)

                    WHERE289_tree = self._adaptor.createWithPayload(WHERE289)
                    self._adaptor.addChild(root_0, WHERE289_tree)

                    self._state.following.append(self.FOLLOW_expr_in_delete_stmt2576)
                    expr290 = self.expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expr290.tree)



                # SQLite.g:354:61: ( operation_limited_clause )?
                alt108 = 2
                LA108_0 = self.input.LA(1)

                if ((ORDER <= LA108_0 <= LIMIT)) :
                    alt108 = 1
                if alt108 == 1:
                    # SQLite.g:354:62: operation_limited_clause
                    pass 
                    self._state.following.append(self.FOLLOW_operation_limited_clause_in_delete_stmt2581)
                    operation_limited_clause291 = self.operation_limited_clause()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, operation_limited_clause291.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "delete_stmt"

    class begin_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.begin_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "begin_stmt"
    # SQLite.g:357:1: begin_stmt : BEGIN ( DEFERRED | IMMEDIATE | EXCLUSIVE )? ( TRANSACTION )? ;
    def begin_stmt(self, ):

        retval = self.begin_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BEGIN292 = None
        set293 = None
        TRANSACTION294 = None

        BEGIN292_tree = None
        set293_tree = None
        TRANSACTION294_tree = None

        try:
            try:
                # SQLite.g:357:11: ( BEGIN ( DEFERRED | IMMEDIATE | EXCLUSIVE )? ( TRANSACTION )? )
                # SQLite.g:357:13: BEGIN ( DEFERRED | IMMEDIATE | EXCLUSIVE )? ( TRANSACTION )?
                pass 
                root_0 = self._adaptor.nil()

                BEGIN292=self.match(self.input, BEGIN, self.FOLLOW_BEGIN_in_begin_stmt2591)

                BEGIN292_tree = self._adaptor.createWithPayload(BEGIN292)
                self._adaptor.addChild(root_0, BEGIN292_tree)

                # SQLite.g:357:19: ( DEFERRED | IMMEDIATE | EXCLUSIVE )?
                alt109 = 2
                LA109_0 = self.input.LA(1)

                if ((DEFERRED <= LA109_0 <= EXCLUSIVE)) :
                    alt109 = 1
                if alt109 == 1:
                    # SQLite.g:
                    pass 
                    set293 = self.input.LT(1)
                    if (DEFERRED <= self.input.LA(1) <= EXCLUSIVE):
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set293))
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse





                # SQLite.g:357:55: ( TRANSACTION )?
                alt110 = 2
                LA110_0 = self.input.LA(1)

                if (LA110_0 == TRANSACTION) :
                    alt110 = 1
                if alt110 == 1:
                    # SQLite.g:357:56: TRANSACTION
                    pass 
                    TRANSACTION294=self.match(self.input, TRANSACTION, self.FOLLOW_TRANSACTION_in_begin_stmt2607)

                    TRANSACTION294_tree = self._adaptor.createWithPayload(TRANSACTION294)
                    self._adaptor.addChild(root_0, TRANSACTION294_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "begin_stmt"

    class commit_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.commit_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "commit_stmt"
    # SQLite.g:360:1: commit_stmt : ( COMMIT | END ) ( TRANSACTION )? ;
    def commit_stmt(self, ):

        retval = self.commit_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set295 = None
        TRANSACTION296 = None

        set295_tree = None
        TRANSACTION296_tree = None

        try:
            try:
                # SQLite.g:360:12: ( ( COMMIT | END ) ( TRANSACTION )? )
                # SQLite.g:360:14: ( COMMIT | END ) ( TRANSACTION )?
                pass 
                root_0 = self._adaptor.nil()

                set295 = self.input.LT(1)
                if self.input.LA(1) == END or self.input.LA(1) == COMMIT:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set295))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse


                # SQLite.g:360:29: ( TRANSACTION )?
                alt111 = 2
                LA111_0 = self.input.LA(1)

                if (LA111_0 == TRANSACTION) :
                    alt111 = 1
                if alt111 == 1:
                    # SQLite.g:360:30: TRANSACTION
                    pass 
                    TRANSACTION296=self.match(self.input, TRANSACTION, self.FOLLOW_TRANSACTION_in_commit_stmt2626)

                    TRANSACTION296_tree = self._adaptor.createWithPayload(TRANSACTION296)
                    self._adaptor.addChild(root_0, TRANSACTION296_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "commit_stmt"

    class rollback_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.rollback_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "rollback_stmt"
    # SQLite.g:363:1: rollback_stmt : ROLLBACK ( TRANSACTION )? ( TO ( SAVEPOINT )? savepoint_name= id )? ;
    def rollback_stmt(self, ):

        retval = self.rollback_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ROLLBACK297 = None
        TRANSACTION298 = None
        TO299 = None
        SAVEPOINT300 = None
        savepoint_name = None


        ROLLBACK297_tree = None
        TRANSACTION298_tree = None
        TO299_tree = None
        SAVEPOINT300_tree = None

        try:
            try:
                # SQLite.g:363:14: ( ROLLBACK ( TRANSACTION )? ( TO ( SAVEPOINT )? savepoint_name= id )? )
                # SQLite.g:363:16: ROLLBACK ( TRANSACTION )? ( TO ( SAVEPOINT )? savepoint_name= id )?
                pass 
                root_0 = self._adaptor.nil()

                ROLLBACK297=self.match(self.input, ROLLBACK, self.FOLLOW_ROLLBACK_in_rollback_stmt2636)

                ROLLBACK297_tree = self._adaptor.createWithPayload(ROLLBACK297)
                self._adaptor.addChild(root_0, ROLLBACK297_tree)

                # SQLite.g:363:25: ( TRANSACTION )?
                alt112 = 2
                LA112_0 = self.input.LA(1)

                if (LA112_0 == TRANSACTION) :
                    alt112 = 1
                if alt112 == 1:
                    # SQLite.g:363:26: TRANSACTION
                    pass 
                    TRANSACTION298=self.match(self.input, TRANSACTION, self.FOLLOW_TRANSACTION_in_rollback_stmt2639)

                    TRANSACTION298_tree = self._adaptor.createWithPayload(TRANSACTION298)
                    self._adaptor.addChild(root_0, TRANSACTION298_tree)




                # SQLite.g:363:40: ( TO ( SAVEPOINT )? savepoint_name= id )?
                alt114 = 2
                LA114_0 = self.input.LA(1)

                if (LA114_0 == TO) :
                    alt114 = 1
                if alt114 == 1:
                    # SQLite.g:363:41: TO ( SAVEPOINT )? savepoint_name= id
                    pass 
                    TO299=self.match(self.input, TO, self.FOLLOW_TO_in_rollback_stmt2644)

                    TO299_tree = self._adaptor.createWithPayload(TO299)
                    self._adaptor.addChild(root_0, TO299_tree)

                    # SQLite.g:363:44: ( SAVEPOINT )?
                    alt113 = 2
                    LA113_0 = self.input.LA(1)

                    if (LA113_0 == SAVEPOINT) :
                        LA113_1 = self.input.LA(2)

                        if ((EXPLAIN <= LA113_1 <= PLAN) or (INDEXED <= LA113_1 <= BY) or (OR <= LA113_1 <= ESCAPE) or (IS <= LA113_1 <= BETWEEN) or (COLLATE <= LA113_1 <= THEN) or LA113_1 == STRING or (CURRENT_TIME <= LA113_1 <= CURRENT_TIMESTAMP) or (RAISE <= LA113_1 <= ROW)) :
                            alt113 = 1
                    if alt113 == 1:
                        # SQLite.g:363:45: SAVEPOINT
                        pass 
                        SAVEPOINT300=self.match(self.input, SAVEPOINT, self.FOLLOW_SAVEPOINT_in_rollback_stmt2647)

                        SAVEPOINT300_tree = self._adaptor.createWithPayload(SAVEPOINT300)
                        self._adaptor.addChild(root_0, SAVEPOINT300_tree)




                    self._state.following.append(self.FOLLOW_id_in_rollback_stmt2653)
                    savepoint_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, savepoint_name.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "rollback_stmt"

    class savepoint_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.savepoint_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "savepoint_stmt"
    # SQLite.g:366:1: savepoint_stmt : SAVEPOINT savepoint_name= id ;
    def savepoint_stmt(self, ):

        retval = self.savepoint_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SAVEPOINT301 = None
        savepoint_name = None


        SAVEPOINT301_tree = None

        try:
            try:
                # SQLite.g:366:15: ( SAVEPOINT savepoint_name= id )
                # SQLite.g:366:17: SAVEPOINT savepoint_name= id
                pass 
                root_0 = self._adaptor.nil()

                SAVEPOINT301=self.match(self.input, SAVEPOINT, self.FOLLOW_SAVEPOINT_in_savepoint_stmt2663)

                SAVEPOINT301_tree = self._adaptor.createWithPayload(SAVEPOINT301)
                self._adaptor.addChild(root_0, SAVEPOINT301_tree)

                self._state.following.append(self.FOLLOW_id_in_savepoint_stmt2667)
                savepoint_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, savepoint_name.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "savepoint_stmt"

    class release_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.release_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "release_stmt"
    # SQLite.g:369:1: release_stmt : RELEASE ( SAVEPOINT )? savepoint_name= id ;
    def release_stmt(self, ):

        retval = self.release_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RELEASE302 = None
        SAVEPOINT303 = None
        savepoint_name = None


        RELEASE302_tree = None
        SAVEPOINT303_tree = None

        try:
            try:
                # SQLite.g:369:13: ( RELEASE ( SAVEPOINT )? savepoint_name= id )
                # SQLite.g:369:15: RELEASE ( SAVEPOINT )? savepoint_name= id
                pass 
                root_0 = self._adaptor.nil()

                RELEASE302=self.match(self.input, RELEASE, self.FOLLOW_RELEASE_in_release_stmt2675)

                RELEASE302_tree = self._adaptor.createWithPayload(RELEASE302)
                self._adaptor.addChild(root_0, RELEASE302_tree)

                # SQLite.g:369:23: ( SAVEPOINT )?
                alt115 = 2
                LA115_0 = self.input.LA(1)

                if (LA115_0 == SAVEPOINT) :
                    LA115_1 = self.input.LA(2)

                    if ((EXPLAIN <= LA115_1 <= PLAN) or (INDEXED <= LA115_1 <= BY) or (OR <= LA115_1 <= ESCAPE) or (IS <= LA115_1 <= BETWEEN) or (COLLATE <= LA115_1 <= THEN) or LA115_1 == STRING or (CURRENT_TIME <= LA115_1 <= CURRENT_TIMESTAMP) or (RAISE <= LA115_1 <= ROW)) :
                        alt115 = 1
                if alt115 == 1:
                    # SQLite.g:369:24: SAVEPOINT
                    pass 
                    SAVEPOINT303=self.match(self.input, SAVEPOINT, self.FOLLOW_SAVEPOINT_in_release_stmt2678)

                    SAVEPOINT303_tree = self._adaptor.createWithPayload(SAVEPOINT303)
                    self._adaptor.addChild(root_0, SAVEPOINT303_tree)




                self._state.following.append(self.FOLLOW_id_in_release_stmt2684)
                savepoint_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, savepoint_name.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "release_stmt"

    class table_conflict_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.table_conflict_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "table_conflict_clause"
    # SQLite.g:376:1: table_conflict_clause : ON CONFLICT ( ROLLBACK | ABORT | FAIL | IGNORE | REPLACE ) ;
    def table_conflict_clause(self, ):

        retval = self.table_conflict_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ON304 = None
        CONFLICT305 = None
        set306 = None

        ON304_tree = None
        CONFLICT305_tree = None
        set306_tree = None

        try:
            try:
                # SQLite.g:376:22: ( ON CONFLICT ( ROLLBACK | ABORT | FAIL | IGNORE | REPLACE ) )
                # SQLite.g:376:24: ON CONFLICT ( ROLLBACK | ABORT | FAIL | IGNORE | REPLACE )
                pass 
                root_0 = self._adaptor.nil()

                ON304=self.match(self.input, ON, self.FOLLOW_ON_in_table_conflict_clause2696)
                CONFLICT305=self.match(self.input, CONFLICT, self.FOLLOW_CONFLICT_in_table_conflict_clause2699)

                CONFLICT305_tree = self._adaptor.createWithPayload(CONFLICT305)
                root_0 = self._adaptor.becomeRoot(CONFLICT305_tree, root_0)

                set306 = self.input.LT(1)
                if (IGNORE <= self.input.LA(1) <= FAIL) or self.input.LA(1) == REPLACE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set306))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "table_conflict_clause"

    class create_virtual_table_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.create_virtual_table_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "create_virtual_table_stmt"
    # SQLite.g:380:1: create_virtual_table_stmt : CREATE VIRTUAL TABLE (database_name= id DOT )? table_name= id USING module_name= id ( LPAREN column_def ( COMMA column_def )* RPAREN )? -> ^( CREATE_TABLE ^( OPTIONS VIRTUAL ) ^( $table_name ( $database_name)? ) ^( $module_name) ( ^( COLUMNS ( column_def )+ ) )? ) ;
    def create_virtual_table_stmt(self, ):

        retval = self.create_virtual_table_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CREATE307 = None
        VIRTUAL308 = None
        TABLE309 = None
        DOT310 = None
        USING311 = None
        LPAREN312 = None
        COMMA314 = None
        RPAREN316 = None
        database_name = None

        table_name = None

        module_name = None

        column_def313 = None

        column_def315 = None


        CREATE307_tree = None
        VIRTUAL308_tree = None
        TABLE309_tree = None
        DOT310_tree = None
        USING311_tree = None
        LPAREN312_tree = None
        COMMA314_tree = None
        RPAREN316_tree = None
        stream_TABLE = RewriteRuleTokenStream(self._adaptor, "token TABLE")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_CREATE = RewriteRuleTokenStream(self._adaptor, "token CREATE")
        stream_USING = RewriteRuleTokenStream(self._adaptor, "token USING")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_VIRTUAL = RewriteRuleTokenStream(self._adaptor, "token VIRTUAL")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_column_def = RewriteRuleSubtreeStream(self._adaptor, "rule column_def")
        try:
            try:
                # SQLite.g:380:26: ( CREATE VIRTUAL TABLE (database_name= id DOT )? table_name= id USING module_name= id ( LPAREN column_def ( COMMA column_def )* RPAREN )? -> ^( CREATE_TABLE ^( OPTIONS VIRTUAL ) ^( $table_name ( $database_name)? ) ^( $module_name) ( ^( COLUMNS ( column_def )+ ) )? ) )
                # SQLite.g:380:28: CREATE VIRTUAL TABLE (database_name= id DOT )? table_name= id USING module_name= id ( LPAREN column_def ( COMMA column_def )* RPAREN )?
                pass 
                CREATE307=self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_virtual_table_stmt2729) 
                stream_CREATE.add(CREATE307)
                VIRTUAL308=self.match(self.input, VIRTUAL, self.FOLLOW_VIRTUAL_in_create_virtual_table_stmt2731) 
                stream_VIRTUAL.add(VIRTUAL308)
                TABLE309=self.match(self.input, TABLE, self.FOLLOW_TABLE_in_create_virtual_table_stmt2733) 
                stream_TABLE.add(TABLE309)
                # SQLite.g:380:49: (database_name= id DOT )?
                alt116 = 2
                LA116_0 = self.input.LA(1)

                if (LA116_0 == ID or LA116_0 == STRING) :
                    LA116_1 = self.input.LA(2)

                    if (LA116_1 == DOT) :
                        alt116 = 1
                elif ((EXPLAIN <= LA116_0 <= PLAN) or (INDEXED <= LA116_0 <= BY) or (OR <= LA116_0 <= ESCAPE) or (IS <= LA116_0 <= BETWEEN) or LA116_0 == COLLATE or (DISTINCT <= LA116_0 <= THEN) or (CURRENT_TIME <= LA116_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA116_0 <= ROW)) :
                    LA116_2 = self.input.LA(2)

                    if (LA116_2 == DOT) :
                        alt116 = 1
                if alt116 == 1:
                    # SQLite.g:380:50: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_create_virtual_table_stmt2738)
                    database_name = self.id()

                    self._state.following.pop()
                    stream_id.add(database_name.tree)
                    DOT310=self.match(self.input, DOT, self.FOLLOW_DOT_in_create_virtual_table_stmt2740) 
                    stream_DOT.add(DOT310)



                self._state.following.append(self.FOLLOW_id_in_create_virtual_table_stmt2746)
                table_name = self.id()

                self._state.following.pop()
                stream_id.add(table_name.tree)
                USING311=self.match(self.input, USING, self.FOLLOW_USING_in_create_virtual_table_stmt2750) 
                stream_USING.add(USING311)
                self._state.following.append(self.FOLLOW_id_in_create_virtual_table_stmt2754)
                module_name = self.id()

                self._state.following.pop()
                stream_id.add(module_name.tree)
                # SQLite.g:381:24: ( LPAREN column_def ( COMMA column_def )* RPAREN )?
                alt118 = 2
                LA118_0 = self.input.LA(1)

                if (LA118_0 == LPAREN) :
                    alt118 = 1
                if alt118 == 1:
                    # SQLite.g:381:25: LPAREN column_def ( COMMA column_def )* RPAREN
                    pass 
                    LPAREN312=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_create_virtual_table_stmt2757) 
                    stream_LPAREN.add(LPAREN312)
                    self._state.following.append(self.FOLLOW_column_def_in_create_virtual_table_stmt2759)
                    column_def313 = self.column_def()

                    self._state.following.pop()
                    stream_column_def.add(column_def313.tree)
                    # SQLite.g:381:43: ( COMMA column_def )*
                    while True: #loop117
                        alt117 = 2
                        LA117_0 = self.input.LA(1)

                        if (LA117_0 == COMMA) :
                            alt117 = 1


                        if alt117 == 1:
                            # SQLite.g:381:44: COMMA column_def
                            pass 
                            COMMA314=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_create_virtual_table_stmt2762) 
                            stream_COMMA.add(COMMA314)
                            self._state.following.append(self.FOLLOW_column_def_in_create_virtual_table_stmt2764)
                            column_def315 = self.column_def()

                            self._state.following.pop()
                            stream_column_def.add(column_def315.tree)


                        else:
                            break #loop117
                    RPAREN316=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_create_virtual_table_stmt2768) 
                    stream_RPAREN.add(RPAREN316)




                # AST Rewrite
                # elements: column_def, VIRTUAL, database_name, module_name, table_name
                # token labels: 
                # rule labels: database_name, retval, table_name, module_name
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if database_name is not None:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "rule database_name", database_name.tree)
                else:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "token database_name", None)


                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if table_name is not None:
                    stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "rule table_name", table_name.tree)
                else:
                    stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "token table_name", None)


                if module_name is not None:
                    stream_module_name = RewriteRuleSubtreeStream(self._adaptor, "rule module_name", module_name.tree)
                else:
                    stream_module_name = RewriteRuleSubtreeStream(self._adaptor, "token module_name", None)


                root_0 = self._adaptor.nil()
                # 382:3: -> ^( CREATE_TABLE ^( OPTIONS VIRTUAL ) ^( $table_name ( $database_name)? ) ^( $module_name) ( ^( COLUMNS ( column_def )+ ) )? )
                # SQLite.g:382:6: ^( CREATE_TABLE ^( OPTIONS VIRTUAL ) ^( $table_name ( $database_name)? ) ^( $module_name) ( ^( COLUMNS ( column_def )+ ) )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CREATE_TABLE, "CREATE_TABLE"), root_1)

                # SQLite.g:382:21: ^( OPTIONS VIRTUAL )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTIONS, "OPTIONS"), root_2)

                self._adaptor.addChild(root_2, stream_VIRTUAL.nextNode())

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:382:40: ^( $table_name ( $database_name)? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(stream_table_name.nextNode(), root_2)

                # SQLite.g:382:54: ( $database_name)?
                if stream_database_name.hasNext():
                    self._adaptor.addChild(root_2, stream_database_name.nextTree())


                stream_database_name.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:382:71: ^( $module_name)
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(stream_module_name.nextNode(), root_2)

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:382:87: ( ^( COLUMNS ( column_def )+ ) )?
                if stream_column_def.hasNext():
                    # SQLite.g:382:87: ^( COLUMNS ( column_def )+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(COLUMNS, "COLUMNS"), root_2)

                    # SQLite.g:382:97: ( column_def )+
                    if not (stream_column_def.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_column_def.hasNext():
                        self._adaptor.addChild(root_2, stream_column_def.nextTree())


                    stream_column_def.reset()

                    self._adaptor.addChild(root_1, root_2)


                stream_column_def.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "create_virtual_table_stmt"

    class create_table_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.create_table_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "create_table_stmt"
    # SQLite.g:385:1: create_table_stmt : CREATE ( TEMPORARY )? TABLE ( IF NOT EXISTS )? (database_name= id DOT )? table_name= id ( LPAREN column_def ( COMMA column_def )* ( ( COMMA )? table_constraint )* RPAREN | AS select_stmt ) -> ^( CREATE_TABLE ^( OPTIONS ( TEMPORARY )? ( EXISTS )? ) ^( $table_name ( $database_name)? ) ( ^( COLUMNS ( column_def )+ ) )? ( ^( CONSTRAINTS ( table_constraint )* ) )? ( select_stmt )? ) ;
    def create_table_stmt(self, ):

        retval = self.create_table_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CREATE317 = None
        TEMPORARY318 = None
        TABLE319 = None
        IF320 = None
        NOT321 = None
        EXISTS322 = None
        DOT323 = None
        LPAREN324 = None
        COMMA326 = None
        COMMA328 = None
        RPAREN330 = None
        AS331 = None
        database_name = None

        table_name = None

        column_def325 = None

        column_def327 = None

        table_constraint329 = None

        select_stmt332 = None


        CREATE317_tree = None
        TEMPORARY318_tree = None
        TABLE319_tree = None
        IF320_tree = None
        NOT321_tree = None
        EXISTS322_tree = None
        DOT323_tree = None
        LPAREN324_tree = None
        COMMA326_tree = None
        COMMA328_tree = None
        RPAREN330_tree = None
        AS331_tree = None
        stream_TABLE = RewriteRuleTokenStream(self._adaptor, "token TABLE")
        stream_AS = RewriteRuleTokenStream(self._adaptor, "token AS")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_CREATE = RewriteRuleTokenStream(self._adaptor, "token CREATE")
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_EXISTS = RewriteRuleTokenStream(self._adaptor, "token EXISTS")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_TEMPORARY = RewriteRuleTokenStream(self._adaptor, "token TEMPORARY")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_select_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule select_stmt")
        stream_column_def = RewriteRuleSubtreeStream(self._adaptor, "rule column_def")
        stream_table_constraint = RewriteRuleSubtreeStream(self._adaptor, "rule table_constraint")
        try:
            try:
                # SQLite.g:385:18: ( CREATE ( TEMPORARY )? TABLE ( IF NOT EXISTS )? (database_name= id DOT )? table_name= id ( LPAREN column_def ( COMMA column_def )* ( ( COMMA )? table_constraint )* RPAREN | AS select_stmt ) -> ^( CREATE_TABLE ^( OPTIONS ( TEMPORARY )? ( EXISTS )? ) ^( $table_name ( $database_name)? ) ( ^( COLUMNS ( column_def )+ ) )? ( ^( CONSTRAINTS ( table_constraint )* ) )? ( select_stmt )? ) )
                # SQLite.g:385:20: CREATE ( TEMPORARY )? TABLE ( IF NOT EXISTS )? (database_name= id DOT )? table_name= id ( LPAREN column_def ( COMMA column_def )* ( ( COMMA )? table_constraint )* RPAREN | AS select_stmt )
                pass 
                CREATE317=self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_table_stmt2814) 
                stream_CREATE.add(CREATE317)
                # SQLite.g:385:27: ( TEMPORARY )?
                alt119 = 2
                LA119_0 = self.input.LA(1)

                if (LA119_0 == TEMPORARY) :
                    alt119 = 1
                if alt119 == 1:
                    # SQLite.g:385:27: TEMPORARY
                    pass 
                    TEMPORARY318=self.match(self.input, TEMPORARY, self.FOLLOW_TEMPORARY_in_create_table_stmt2816) 
                    stream_TEMPORARY.add(TEMPORARY318)



                TABLE319=self.match(self.input, TABLE, self.FOLLOW_TABLE_in_create_table_stmt2819) 
                stream_TABLE.add(TABLE319)
                # SQLite.g:385:44: ( IF NOT EXISTS )?
                alt120 = 2
                LA120_0 = self.input.LA(1)

                if (LA120_0 == IF) :
                    LA120_1 = self.input.LA(2)

                    if (LA120_1 == NOT) :
                        alt120 = 1
                if alt120 == 1:
                    # SQLite.g:385:45: IF NOT EXISTS
                    pass 
                    IF320=self.match(self.input, IF, self.FOLLOW_IF_in_create_table_stmt2822) 
                    stream_IF.add(IF320)
                    NOT321=self.match(self.input, NOT, self.FOLLOW_NOT_in_create_table_stmt2824) 
                    stream_NOT.add(NOT321)
                    EXISTS322=self.match(self.input, EXISTS, self.FOLLOW_EXISTS_in_create_table_stmt2826) 
                    stream_EXISTS.add(EXISTS322)



                # SQLite.g:385:61: (database_name= id DOT )?
                alt121 = 2
                LA121_0 = self.input.LA(1)

                if (LA121_0 == ID or LA121_0 == STRING) :
                    LA121_1 = self.input.LA(2)

                    if (LA121_1 == DOT) :
                        alt121 = 1
                elif ((EXPLAIN <= LA121_0 <= PLAN) or (INDEXED <= LA121_0 <= BY) or (OR <= LA121_0 <= ESCAPE) or (IS <= LA121_0 <= BETWEEN) or LA121_0 == COLLATE or (DISTINCT <= LA121_0 <= THEN) or (CURRENT_TIME <= LA121_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA121_0 <= ROW)) :
                    LA121_2 = self.input.LA(2)

                    if (LA121_2 == DOT) :
                        alt121 = 1
                if alt121 == 1:
                    # SQLite.g:385:62: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_create_table_stmt2833)
                    database_name = self.id()

                    self._state.following.pop()
                    stream_id.add(database_name.tree)
                    DOT323=self.match(self.input, DOT, self.FOLLOW_DOT_in_create_table_stmt2835) 
                    stream_DOT.add(DOT323)



                self._state.following.append(self.FOLLOW_id_in_create_table_stmt2841)
                table_name = self.id()

                self._state.following.pop()
                stream_id.add(table_name.tree)
                # SQLite.g:386:3: ( LPAREN column_def ( COMMA column_def )* ( ( COMMA )? table_constraint )* RPAREN | AS select_stmt )
                alt125 = 2
                LA125_0 = self.input.LA(1)

                if (LA125_0 == LPAREN) :
                    alt125 = 1
                elif (LA125_0 == AS) :
                    alt125 = 2
                else:
                    nvae = NoViableAltException("", 125, 0, self.input)

                    raise nvae

                if alt125 == 1:
                    # SQLite.g:386:5: LPAREN column_def ( COMMA column_def )* ( ( COMMA )? table_constraint )* RPAREN
                    pass 
                    LPAREN324=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_create_table_stmt2847) 
                    stream_LPAREN.add(LPAREN324)
                    self._state.following.append(self.FOLLOW_column_def_in_create_table_stmt2849)
                    column_def325 = self.column_def()

                    self._state.following.pop()
                    stream_column_def.add(column_def325.tree)
                    # SQLite.g:386:23: ( COMMA column_def )*
                    while True: #loop122
                        alt122 = 2
                        alt122 = self.dfa122.predict(self.input)
                        if alt122 == 1:
                            # SQLite.g:386:24: COMMA column_def
                            pass 
                            COMMA326=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_create_table_stmt2852) 
                            stream_COMMA.add(COMMA326)
                            self._state.following.append(self.FOLLOW_column_def_in_create_table_stmt2854)
                            column_def327 = self.column_def()

                            self._state.following.pop()
                            stream_column_def.add(column_def327.tree)


                        else:
                            break #loop122
                    # SQLite.g:386:43: ( ( COMMA )? table_constraint )*
                    while True: #loop124
                        alt124 = 2
                        LA124_0 = self.input.LA(1)

                        if (LA124_0 == COMMA or (CONSTRAINT <= LA124_0 <= PRIMARY) or (UNIQUE <= LA124_0 <= FOREIGN)) :
                            alt124 = 1


                        if alt124 == 1:
                            # SQLite.g:386:44: ( COMMA )? table_constraint
                            pass 
                            # SQLite.g:386:44: ( COMMA )?
                            alt123 = 2
                            LA123_0 = self.input.LA(1)

                            if (LA123_0 == COMMA) :
                                alt123 = 1
                            if alt123 == 1:
                                # SQLite.g:386:44: COMMA
                                pass 
                                COMMA328=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_create_table_stmt2859) 
                                stream_COMMA.add(COMMA328)



                            self._state.following.append(self.FOLLOW_table_constraint_in_create_table_stmt2862)
                            table_constraint329 = self.table_constraint()

                            self._state.following.pop()
                            stream_table_constraint.add(table_constraint329.tree)


                        else:
                            break #loop124
                    RPAREN330=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_create_table_stmt2866) 
                    stream_RPAREN.add(RPAREN330)


                elif alt125 == 2:
                    # SQLite.g:387:5: AS select_stmt
                    pass 
                    AS331=self.match(self.input, AS, self.FOLLOW_AS_in_create_table_stmt2872) 
                    stream_AS.add(AS331)
                    self._state.following.append(self.FOLLOW_select_stmt_in_create_table_stmt2874)
                    select_stmt332 = self.select_stmt()

                    self._state.following.pop()
                    stream_select_stmt.add(select_stmt332.tree)




                # AST Rewrite
                # elements: select_stmt, TEMPORARY, table_constraint, database_name, column_def, table_name, EXISTS
                # token labels: 
                # rule labels: database_name, retval, table_name
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if database_name is not None:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "rule database_name", database_name.tree)
                else:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "token database_name", None)


                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if table_name is not None:
                    stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "rule table_name", table_name.tree)
                else:
                    stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "token table_name", None)


                root_0 = self._adaptor.nil()
                # 388:1: -> ^( CREATE_TABLE ^( OPTIONS ( TEMPORARY )? ( EXISTS )? ) ^( $table_name ( $database_name)? ) ( ^( COLUMNS ( column_def )+ ) )? ( ^( CONSTRAINTS ( table_constraint )* ) )? ( select_stmt )? )
                # SQLite.g:388:4: ^( CREATE_TABLE ^( OPTIONS ( TEMPORARY )? ( EXISTS )? ) ^( $table_name ( $database_name)? ) ( ^( COLUMNS ( column_def )+ ) )? ( ^( CONSTRAINTS ( table_constraint )* ) )? ( select_stmt )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CREATE_TABLE, "CREATE_TABLE"), root_1)

                # SQLite.g:388:19: ^( OPTIONS ( TEMPORARY )? ( EXISTS )? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTIONS, "OPTIONS"), root_2)

                # SQLite.g:388:29: ( TEMPORARY )?
                if stream_TEMPORARY.hasNext():
                    self._adaptor.addChild(root_2, stream_TEMPORARY.nextNode())


                stream_TEMPORARY.reset();
                # SQLite.g:388:40: ( EXISTS )?
                if stream_EXISTS.hasNext():
                    self._adaptor.addChild(root_2, stream_EXISTS.nextNode())


                stream_EXISTS.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:388:49: ^( $table_name ( $database_name)? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(stream_table_name.nextNode(), root_2)

                # SQLite.g:388:63: ( $database_name)?
                if stream_database_name.hasNext():
                    self._adaptor.addChild(root_2, stream_database_name.nextTree())


                stream_database_name.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:389:3: ( ^( COLUMNS ( column_def )+ ) )?
                if stream_column_def.hasNext():
                    # SQLite.g:389:3: ^( COLUMNS ( column_def )+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(COLUMNS, "COLUMNS"), root_2)

                    # SQLite.g:389:13: ( column_def )+
                    if not (stream_column_def.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_column_def.hasNext():
                        self._adaptor.addChild(root_2, stream_column_def.nextTree())


                    stream_column_def.reset()

                    self._adaptor.addChild(root_1, root_2)


                stream_column_def.reset();
                # SQLite.g:389:27: ( ^( CONSTRAINTS ( table_constraint )* ) )?
                if stream_table_constraint.hasNext():
                    # SQLite.g:389:27: ^( CONSTRAINTS ( table_constraint )* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(CONSTRAINTS, "CONSTRAINTS"), root_2)

                    # SQLite.g:389:41: ( table_constraint )*
                    while stream_table_constraint.hasNext():
                        self._adaptor.addChild(root_2, stream_table_constraint.nextTree())


                    stream_table_constraint.reset();

                    self._adaptor.addChild(root_1, root_2)


                stream_table_constraint.reset();
                # SQLite.g:389:61: ( select_stmt )?
                if stream_select_stmt.hasNext():
                    self._adaptor.addChild(root_1, stream_select_stmt.nextTree())


                stream_select_stmt.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "create_table_stmt"

    class column_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.column_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "column_def"
    # SQLite.g:391:1: column_def : name= id_column_def ( type_name )? ( column_constraint )* -> ^( $name ^( CONSTRAINTS ( column_constraint )* ) ( type_name )? ) ;
    def column_def(self, ):

        retval = self.column_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        name = None

        type_name333 = None

        column_constraint334 = None


        stream_column_constraint = RewriteRuleSubtreeStream(self._adaptor, "rule column_constraint")
        stream_id_column_def = RewriteRuleSubtreeStream(self._adaptor, "rule id_column_def")
        stream_type_name = RewriteRuleSubtreeStream(self._adaptor, "rule type_name")
        try:
            try:
                # SQLite.g:391:11: (name= id_column_def ( type_name )? ( column_constraint )* -> ^( $name ^( CONSTRAINTS ( column_constraint )* ) ( type_name )? ) )
                # SQLite.g:391:13: name= id_column_def ( type_name )? ( column_constraint )*
                pass 
                self._state.following.append(self.FOLLOW_id_column_def_in_column_def2930)
                name = self.id_column_def()

                self._state.following.pop()
                stream_id_column_def.add(name.tree)
                # SQLite.g:391:32: ( type_name )?
                alt126 = 2
                alt126 = self.dfa126.predict(self.input)
                if alt126 == 1:
                    # SQLite.g:391:32: type_name
                    pass 
                    self._state.following.append(self.FOLLOW_type_name_in_column_def2932)
                    type_name333 = self.type_name()

                    self._state.following.pop()
                    stream_type_name.add(type_name333.tree)



                # SQLite.g:391:43: ( column_constraint )*
                while True: #loop127
                    alt127 = 2
                    alt127 = self.dfa127.predict(self.input)
                    if alt127 == 1:
                        # SQLite.g:391:43: column_constraint
                        pass 
                        self._state.following.append(self.FOLLOW_column_constraint_in_column_def2935)
                        column_constraint334 = self.column_constraint()

                        self._state.following.pop()
                        stream_column_constraint.add(column_constraint334.tree)


                    else:
                        break #loop127

                # AST Rewrite
                # elements: column_constraint, name, type_name
                # token labels: 
                # rule labels: retval, name
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if name is not None:
                    stream_name = RewriteRuleSubtreeStream(self._adaptor, "rule name", name.tree)
                else:
                    stream_name = RewriteRuleSubtreeStream(self._adaptor, "token name", None)


                root_0 = self._adaptor.nil()
                # 392:1: -> ^( $name ^( CONSTRAINTS ( column_constraint )* ) ( type_name )? )
                # SQLite.g:392:4: ^( $name ^( CONSTRAINTS ( column_constraint )* ) ( type_name )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_name.nextNode(), root_1)

                # SQLite.g:392:12: ^( CONSTRAINTS ( column_constraint )* )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(CONSTRAINTS, "CONSTRAINTS"), root_2)

                # SQLite.g:392:26: ( column_constraint )*
                while stream_column_constraint.hasNext():
                    self._adaptor.addChild(root_2, stream_column_constraint.nextTree())


                stream_column_constraint.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:392:46: ( type_name )?
                if stream_type_name.hasNext():
                    self._adaptor.addChild(root_1, stream_type_name.nextTree())


                stream_type_name.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "column_def"

    class column_constraint_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.column_constraint_return, self).__init__()

            self.tree = None




    # $ANTLR start "column_constraint"
    # SQLite.g:394:1: column_constraint : ( CONSTRAINT name= id )? ( column_constraint_pk | column_constraint_not_null | column_constraint_null | column_constraint_unique | column_constraint_check | column_constraint_default | column_constraint_collate | fk_clause ) -> ^( COLUMN_CONSTRAINT ( column_constraint_pk )? ( column_constraint_not_null )? ( column_constraint_null )? ( column_constraint_unique )? ( column_constraint_check )? ( column_constraint_default )? ( column_constraint_collate )? ( fk_clause )? ( $name)? ) ;
    def column_constraint(self, ):

        retval = self.column_constraint_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CONSTRAINT335 = None
        name = None

        column_constraint_pk336 = None

        column_constraint_not_null337 = None

        column_constraint_null338 = None

        column_constraint_unique339 = None

        column_constraint_check340 = None

        column_constraint_default341 = None

        column_constraint_collate342 = None

        fk_clause343 = None


        CONSTRAINT335_tree = None
        stream_CONSTRAINT = RewriteRuleTokenStream(self._adaptor, "token CONSTRAINT")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_column_constraint_default = RewriteRuleSubtreeStream(self._adaptor, "rule column_constraint_default")
        stream_column_constraint_check = RewriteRuleSubtreeStream(self._adaptor, "rule column_constraint_check")
        stream_column_constraint_pk = RewriteRuleSubtreeStream(self._adaptor, "rule column_constraint_pk")
        stream_column_constraint_null = RewriteRuleSubtreeStream(self._adaptor, "rule column_constraint_null")
        stream_column_constraint_collate = RewriteRuleSubtreeStream(self._adaptor, "rule column_constraint_collate")
        stream_column_constraint_unique = RewriteRuleSubtreeStream(self._adaptor, "rule column_constraint_unique")
        stream_fk_clause = RewriteRuleSubtreeStream(self._adaptor, "rule fk_clause")
        stream_column_constraint_not_null = RewriteRuleSubtreeStream(self._adaptor, "rule column_constraint_not_null")
        try:
            try:
                # SQLite.g:394:18: ( ( CONSTRAINT name= id )? ( column_constraint_pk | column_constraint_not_null | column_constraint_null | column_constraint_unique | column_constraint_check | column_constraint_default | column_constraint_collate | fk_clause ) -> ^( COLUMN_CONSTRAINT ( column_constraint_pk )? ( column_constraint_not_null )? ( column_constraint_null )? ( column_constraint_unique )? ( column_constraint_check )? ( column_constraint_default )? ( column_constraint_collate )? ( fk_clause )? ( $name)? ) )
                # SQLite.g:394:20: ( CONSTRAINT name= id )? ( column_constraint_pk | column_constraint_not_null | column_constraint_null | column_constraint_unique | column_constraint_check | column_constraint_default | column_constraint_collate | fk_clause )
                pass 
                # SQLite.g:394:20: ( CONSTRAINT name= id )?
                alt128 = 2
                alt128 = self.dfa128.predict(self.input)
                if alt128 == 1:
                    # SQLite.g:394:21: CONSTRAINT name= id
                    pass 
                    CONSTRAINT335=self.match(self.input, CONSTRAINT, self.FOLLOW_CONSTRAINT_in_column_constraint2961) 
                    stream_CONSTRAINT.add(CONSTRAINT335)
                    self._state.following.append(self.FOLLOW_id_in_column_constraint2965)
                    name = self.id()

                    self._state.following.pop()
                    stream_id.add(name.tree)



                # SQLite.g:395:3: ( column_constraint_pk | column_constraint_not_null | column_constraint_null | column_constraint_unique | column_constraint_check | column_constraint_default | column_constraint_collate | fk_clause )
                alt129 = 8
                LA129 = self.input.LA(1)
                if LA129 == PRIMARY:
                    alt129 = 1
                elif LA129 == NOT:
                    alt129 = 2
                elif LA129 == NULL:
                    alt129 = 3
                elif LA129 == UNIQUE:
                    alt129 = 4
                elif LA129 == CHECK:
                    alt129 = 5
                elif LA129 == DEFAULT:
                    alt129 = 6
                elif LA129 == COLLATE:
                    alt129 = 7
                elif LA129 == REFERENCES:
                    alt129 = 8
                else:
                    nvae = NoViableAltException("", 129, 0, self.input)

                    raise nvae

                if alt129 == 1:
                    # SQLite.g:395:5: column_constraint_pk
                    pass 
                    self._state.following.append(self.FOLLOW_column_constraint_pk_in_column_constraint2973)
                    column_constraint_pk336 = self.column_constraint_pk()

                    self._state.following.pop()
                    stream_column_constraint_pk.add(column_constraint_pk336.tree)


                elif alt129 == 2:
                    # SQLite.g:396:5: column_constraint_not_null
                    pass 
                    self._state.following.append(self.FOLLOW_column_constraint_not_null_in_column_constraint2979)
                    column_constraint_not_null337 = self.column_constraint_not_null()

                    self._state.following.pop()
                    stream_column_constraint_not_null.add(column_constraint_not_null337.tree)


                elif alt129 == 3:
                    # SQLite.g:397:5: column_constraint_null
                    pass 
                    self._state.following.append(self.FOLLOW_column_constraint_null_in_column_constraint2985)
                    column_constraint_null338 = self.column_constraint_null()

                    self._state.following.pop()
                    stream_column_constraint_null.add(column_constraint_null338.tree)


                elif alt129 == 4:
                    # SQLite.g:398:5: column_constraint_unique
                    pass 
                    self._state.following.append(self.FOLLOW_column_constraint_unique_in_column_constraint2991)
                    column_constraint_unique339 = self.column_constraint_unique()

                    self._state.following.pop()
                    stream_column_constraint_unique.add(column_constraint_unique339.tree)


                elif alt129 == 5:
                    # SQLite.g:399:5: column_constraint_check
                    pass 
                    self._state.following.append(self.FOLLOW_column_constraint_check_in_column_constraint2997)
                    column_constraint_check340 = self.column_constraint_check()

                    self._state.following.pop()
                    stream_column_constraint_check.add(column_constraint_check340.tree)


                elif alt129 == 6:
                    # SQLite.g:400:5: column_constraint_default
                    pass 
                    self._state.following.append(self.FOLLOW_column_constraint_default_in_column_constraint3003)
                    column_constraint_default341 = self.column_constraint_default()

                    self._state.following.pop()
                    stream_column_constraint_default.add(column_constraint_default341.tree)


                elif alt129 == 7:
                    # SQLite.g:401:5: column_constraint_collate
                    pass 
                    self._state.following.append(self.FOLLOW_column_constraint_collate_in_column_constraint3009)
                    column_constraint_collate342 = self.column_constraint_collate()

                    self._state.following.pop()
                    stream_column_constraint_collate.add(column_constraint_collate342.tree)


                elif alt129 == 8:
                    # SQLite.g:402:5: fk_clause
                    pass 
                    self._state.following.append(self.FOLLOW_fk_clause_in_column_constraint3015)
                    fk_clause343 = self.fk_clause()

                    self._state.following.pop()
                    stream_fk_clause.add(fk_clause343.tree)




                # AST Rewrite
                # elements: fk_clause, column_constraint_default, name, column_constraint_unique, column_constraint_pk, column_constraint_check, column_constraint_not_null, column_constraint_null, column_constraint_collate
                # token labels: 
                # rule labels: retval, name
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if name is not None:
                    stream_name = RewriteRuleSubtreeStream(self._adaptor, "rule name", name.tree)
                else:
                    stream_name = RewriteRuleSubtreeStream(self._adaptor, "token name", None)


                root_0 = self._adaptor.nil()
                # 403:1: -> ^( COLUMN_CONSTRAINT ( column_constraint_pk )? ( column_constraint_not_null )? ( column_constraint_null )? ( column_constraint_unique )? ( column_constraint_check )? ( column_constraint_default )? ( column_constraint_collate )? ( fk_clause )? ( $name)? )
                # SQLite.g:403:4: ^( COLUMN_CONSTRAINT ( column_constraint_pk )? ( column_constraint_not_null )? ( column_constraint_null )? ( column_constraint_unique )? ( column_constraint_check )? ( column_constraint_default )? ( column_constraint_collate )? ( fk_clause )? ( $name)? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(COLUMN_CONSTRAINT, "COLUMN_CONSTRAINT"), root_1)

                # SQLite.g:404:3: ( column_constraint_pk )?
                if stream_column_constraint_pk.hasNext():
                    self._adaptor.addChild(root_1, stream_column_constraint_pk.nextTree())


                stream_column_constraint_pk.reset();
                # SQLite.g:405:3: ( column_constraint_not_null )?
                if stream_column_constraint_not_null.hasNext():
                    self._adaptor.addChild(root_1, stream_column_constraint_not_null.nextTree())


                stream_column_constraint_not_null.reset();
                # SQLite.g:406:3: ( column_constraint_null )?
                if stream_column_constraint_null.hasNext():
                    self._adaptor.addChild(root_1, stream_column_constraint_null.nextTree())


                stream_column_constraint_null.reset();
                # SQLite.g:407:3: ( column_constraint_unique )?
                if stream_column_constraint_unique.hasNext():
                    self._adaptor.addChild(root_1, stream_column_constraint_unique.nextTree())


                stream_column_constraint_unique.reset();
                # SQLite.g:408:3: ( column_constraint_check )?
                if stream_column_constraint_check.hasNext():
                    self._adaptor.addChild(root_1, stream_column_constraint_check.nextTree())


                stream_column_constraint_check.reset();
                # SQLite.g:409:3: ( column_constraint_default )?
                if stream_column_constraint_default.hasNext():
                    self._adaptor.addChild(root_1, stream_column_constraint_default.nextTree())


                stream_column_constraint_default.reset();
                # SQLite.g:410:3: ( column_constraint_collate )?
                if stream_column_constraint_collate.hasNext():
                    self._adaptor.addChild(root_1, stream_column_constraint_collate.nextTree())


                stream_column_constraint_collate.reset();
                # SQLite.g:411:3: ( fk_clause )?
                if stream_fk_clause.hasNext():
                    self._adaptor.addChild(root_1, stream_fk_clause.nextTree())


                stream_fk_clause.reset();
                # SQLite.g:412:3: ( $name)?
                if stream_name.hasNext():
                    self._adaptor.addChild(root_1, stream_name.nextTree())


                stream_name.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "column_constraint"

    class column_constraint_pk_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.column_constraint_pk_return, self).__init__()

            self.tree = None




    # $ANTLR start "column_constraint_pk"
    # SQLite.g:414:1: column_constraint_pk : PRIMARY KEY ( ASC | DESC )? ( table_conflict_clause )? ( AUTOINCREMENT )? ;
    def column_constraint_pk(self, ):

        retval = self.column_constraint_pk_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PRIMARY344 = None
        KEY345 = None
        set346 = None
        AUTOINCREMENT348 = None
        table_conflict_clause347 = None


        PRIMARY344_tree = None
        KEY345_tree = None
        set346_tree = None
        AUTOINCREMENT348_tree = None

        try:
            try:
                # SQLite.g:414:21: ( PRIMARY KEY ( ASC | DESC )? ( table_conflict_clause )? ( AUTOINCREMENT )? )
                # SQLite.g:414:23: PRIMARY KEY ( ASC | DESC )? ( table_conflict_clause )? ( AUTOINCREMENT )?
                pass 
                root_0 = self._adaptor.nil()

                PRIMARY344=self.match(self.input, PRIMARY, self.FOLLOW_PRIMARY_in_column_constraint_pk3075)

                PRIMARY344_tree = self._adaptor.createWithPayload(PRIMARY344)
                root_0 = self._adaptor.becomeRoot(PRIMARY344_tree, root_0)

                KEY345=self.match(self.input, KEY, self.FOLLOW_KEY_in_column_constraint_pk3078)
                # SQLite.g:414:37: ( ASC | DESC )?
                alt130 = 2
                alt130 = self.dfa130.predict(self.input)
                if alt130 == 1:
                    # SQLite.g:
                    pass 
                    set346 = self.input.LT(1)
                    if (ASC <= self.input.LA(1) <= DESC):
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set346))
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse





                # SQLite.g:414:51: ( table_conflict_clause )?
                alt131 = 2
                alt131 = self.dfa131.predict(self.input)
                if alt131 == 1:
                    # SQLite.g:414:51: table_conflict_clause
                    pass 
                    self._state.following.append(self.FOLLOW_table_conflict_clause_in_column_constraint_pk3090)
                    table_conflict_clause347 = self.table_conflict_clause()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, table_conflict_clause347.tree)



                # SQLite.g:414:74: ( AUTOINCREMENT )?
                alt132 = 2
                alt132 = self.dfa132.predict(self.input)
                if alt132 == 1:
                    # SQLite.g:414:75: AUTOINCREMENT
                    pass 
                    AUTOINCREMENT348=self.match(self.input, AUTOINCREMENT, self.FOLLOW_AUTOINCREMENT_in_column_constraint_pk3094)

                    AUTOINCREMENT348_tree = self._adaptor.createWithPayload(AUTOINCREMENT348)
                    self._adaptor.addChild(root_0, AUTOINCREMENT348_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "column_constraint_pk"

    class column_constraint_not_null_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.column_constraint_not_null_return, self).__init__()

            self.tree = None




    # $ANTLR start "column_constraint_not_null"
    # SQLite.g:416:1: column_constraint_not_null : NOT NULL ( table_conflict_clause )? -> ^( NOT_NULL ( table_conflict_clause )? ) ;
    def column_constraint_not_null(self, ):

        retval = self.column_constraint_not_null_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT349 = None
        NULL350 = None
        table_conflict_clause351 = None


        NOT349_tree = None
        NULL350_tree = None
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_NULL = RewriteRuleTokenStream(self._adaptor, "token NULL")
        stream_table_conflict_clause = RewriteRuleSubtreeStream(self._adaptor, "rule table_conflict_clause")
        try:
            try:
                # SQLite.g:416:27: ( NOT NULL ( table_conflict_clause )? -> ^( NOT_NULL ( table_conflict_clause )? ) )
                # SQLite.g:416:29: NOT NULL ( table_conflict_clause )?
                pass 
                NOT349=self.match(self.input, NOT, self.FOLLOW_NOT_in_column_constraint_not_null3103) 
                stream_NOT.add(NOT349)
                NULL350=self.match(self.input, NULL, self.FOLLOW_NULL_in_column_constraint_not_null3105) 
                stream_NULL.add(NULL350)
                # SQLite.g:416:38: ( table_conflict_clause )?
                alt133 = 2
                alt133 = self.dfa133.predict(self.input)
                if alt133 == 1:
                    # SQLite.g:416:38: table_conflict_clause
                    pass 
                    self._state.following.append(self.FOLLOW_table_conflict_clause_in_column_constraint_not_null3107)
                    table_conflict_clause351 = self.table_conflict_clause()

                    self._state.following.pop()
                    stream_table_conflict_clause.add(table_conflict_clause351.tree)




                # AST Rewrite
                # elements: table_conflict_clause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 416:61: -> ^( NOT_NULL ( table_conflict_clause )? )
                # SQLite.g:416:64: ^( NOT_NULL ( table_conflict_clause )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NOT_NULL, "NOT_NULL"), root_1)

                # SQLite.g:416:75: ( table_conflict_clause )?
                if stream_table_conflict_clause.hasNext():
                    self._adaptor.addChild(root_1, stream_table_conflict_clause.nextTree())


                stream_table_conflict_clause.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "column_constraint_not_null"

    class column_constraint_null_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.column_constraint_null_return, self).__init__()

            self.tree = None




    # $ANTLR start "column_constraint_null"
    # SQLite.g:418:1: column_constraint_null : NULL ( table_conflict_clause )? -> ^( IS_NULL ( table_conflict_clause )? ) ;
    def column_constraint_null(self, ):

        retval = self.column_constraint_null_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NULL352 = None
        table_conflict_clause353 = None


        NULL352_tree = None
        stream_NULL = RewriteRuleTokenStream(self._adaptor, "token NULL")
        stream_table_conflict_clause = RewriteRuleSubtreeStream(self._adaptor, "rule table_conflict_clause")
        try:
            try:
                # SQLite.g:418:23: ( NULL ( table_conflict_clause )? -> ^( IS_NULL ( table_conflict_clause )? ) )
                # SQLite.g:418:25: NULL ( table_conflict_clause )?
                pass 
                NULL352=self.match(self.input, NULL, self.FOLLOW_NULL_in_column_constraint_null3124) 
                stream_NULL.add(NULL352)
                # SQLite.g:418:30: ( table_conflict_clause )?
                alt134 = 2
                alt134 = self.dfa134.predict(self.input)
                if alt134 == 1:
                    # SQLite.g:418:30: table_conflict_clause
                    pass 
                    self._state.following.append(self.FOLLOW_table_conflict_clause_in_column_constraint_null3126)
                    table_conflict_clause353 = self.table_conflict_clause()

                    self._state.following.pop()
                    stream_table_conflict_clause.add(table_conflict_clause353.tree)




                # AST Rewrite
                # elements: table_conflict_clause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 418:53: -> ^( IS_NULL ( table_conflict_clause )? )
                # SQLite.g:418:56: ^( IS_NULL ( table_conflict_clause )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IS_NULL, "IS_NULL"), root_1)

                # SQLite.g:418:66: ( table_conflict_clause )?
                if stream_table_conflict_clause.hasNext():
                    self._adaptor.addChild(root_1, stream_table_conflict_clause.nextTree())


                stream_table_conflict_clause.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "column_constraint_null"

    class column_constraint_unique_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.column_constraint_unique_return, self).__init__()

            self.tree = None




    # $ANTLR start "column_constraint_unique"
    # SQLite.g:420:1: column_constraint_unique : UNIQUE ( table_conflict_clause )? ;
    def column_constraint_unique(self, ):

        retval = self.column_constraint_unique_return()
        retval.start = self.input.LT(1)

        root_0 = None

        UNIQUE354 = None
        table_conflict_clause355 = None


        UNIQUE354_tree = None

        try:
            try:
                # SQLite.g:420:25: ( UNIQUE ( table_conflict_clause )? )
                # SQLite.g:420:27: UNIQUE ( table_conflict_clause )?
                pass 
                root_0 = self._adaptor.nil()

                UNIQUE354=self.match(self.input, UNIQUE, self.FOLLOW_UNIQUE_in_column_constraint_unique3143)

                UNIQUE354_tree = self._adaptor.createWithPayload(UNIQUE354)
                root_0 = self._adaptor.becomeRoot(UNIQUE354_tree, root_0)

                # SQLite.g:420:35: ( table_conflict_clause )?
                alt135 = 2
                alt135 = self.dfa135.predict(self.input)
                if alt135 == 1:
                    # SQLite.g:420:35: table_conflict_clause
                    pass 
                    self._state.following.append(self.FOLLOW_table_conflict_clause_in_column_constraint_unique3146)
                    table_conflict_clause355 = self.table_conflict_clause()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, table_conflict_clause355.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "column_constraint_unique"

    class column_constraint_check_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.column_constraint_check_return, self).__init__()

            self.tree = None




    # $ANTLR start "column_constraint_check"
    # SQLite.g:422:1: column_constraint_check : CHECK LPAREN expr RPAREN ;
    def column_constraint_check(self, ):

        retval = self.column_constraint_check_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CHECK356 = None
        LPAREN357 = None
        RPAREN359 = None
        expr358 = None


        CHECK356_tree = None
        LPAREN357_tree = None
        RPAREN359_tree = None

        try:
            try:
                # SQLite.g:422:24: ( CHECK LPAREN expr RPAREN )
                # SQLite.g:422:26: CHECK LPAREN expr RPAREN
                pass 
                root_0 = self._adaptor.nil()

                CHECK356=self.match(self.input, CHECK, self.FOLLOW_CHECK_in_column_constraint_check3154)

                CHECK356_tree = self._adaptor.createWithPayload(CHECK356)
                root_0 = self._adaptor.becomeRoot(CHECK356_tree, root_0)

                LPAREN357=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_column_constraint_check3157)
                self._state.following.append(self.FOLLOW_expr_in_column_constraint_check3160)
                expr358 = self.expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expr358.tree)
                RPAREN359=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_column_constraint_check3162)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "column_constraint_check"

    class numeric_literal_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.numeric_literal_value_return, self).__init__()

            self.tree = None




    # $ANTLR start "numeric_literal_value"
    # SQLite.g:424:1: numeric_literal_value : ( INTEGER -> ^( INTEGER_LITERAL INTEGER ) | FLOAT -> ^( FLOAT_LITERAL FLOAT ) );
    def numeric_literal_value(self, ):

        retval = self.numeric_literal_value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INTEGER360 = None
        FLOAT361 = None

        INTEGER360_tree = None
        FLOAT361_tree = None
        stream_INTEGER = RewriteRuleTokenStream(self._adaptor, "token INTEGER")
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")

        try:
            try:
                # SQLite.g:425:3: ( INTEGER -> ^( INTEGER_LITERAL INTEGER ) | FLOAT -> ^( FLOAT_LITERAL FLOAT ) )
                alt136 = 2
                LA136_0 = self.input.LA(1)

                if (LA136_0 == INTEGER) :
                    alt136 = 1
                elif (LA136_0 == FLOAT) :
                    alt136 = 2
                else:
                    nvae = NoViableAltException("", 136, 0, self.input)

                    raise nvae

                if alt136 == 1:
                    # SQLite.g:425:5: INTEGER
                    pass 
                    INTEGER360=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_numeric_literal_value3173) 
                    stream_INTEGER.add(INTEGER360)

                    # AST Rewrite
                    # elements: INTEGER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 425:13: -> ^( INTEGER_LITERAL INTEGER )
                    # SQLite.g:425:16: ^( INTEGER_LITERAL INTEGER )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INTEGER_LITERAL, "INTEGER_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_INTEGER.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt136 == 2:
                    # SQLite.g:426:5: FLOAT
                    pass 
                    FLOAT361=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_numeric_literal_value3187) 
                    stream_FLOAT.add(FLOAT361)

                    # AST Rewrite
                    # elements: FLOAT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 426:11: -> ^( FLOAT_LITERAL FLOAT )
                    # SQLite.g:426:14: ^( FLOAT_LITERAL FLOAT )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FLOAT_LITERAL, "FLOAT_LITERAL"), root_1)

                    self._adaptor.addChild(root_1, stream_FLOAT.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "numeric_literal_value"

    class signed_default_number_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.signed_default_number_return, self).__init__()

            self.tree = None




    # $ANTLR start "signed_default_number"
    # SQLite.g:429:1: signed_default_number : ( PLUS | MINUS ) numeric_literal_value ;
    def signed_default_number(self, ):

        retval = self.signed_default_number_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set362 = None
        numeric_literal_value363 = None


        set362_tree = None

        try:
            try:
                # SQLite.g:429:22: ( ( PLUS | MINUS ) numeric_literal_value )
                # SQLite.g:429:24: ( PLUS | MINUS ) numeric_literal_value
                pass 
                root_0 = self._adaptor.nil()

                set362 = self.input.LT(1)
                set362 = self.input.LT(1)
                if (PLUS <= self.input.LA(1) <= MINUS):
                    self.input.consume()
                    root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set362), root_0)
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self._state.following.append(self.FOLLOW_numeric_literal_value_in_signed_default_number3214)
                numeric_literal_value363 = self.numeric_literal_value()

                self._state.following.pop()
                self._adaptor.addChild(root_0, numeric_literal_value363.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "signed_default_number"

    class column_constraint_default_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.column_constraint_default_return, self).__init__()

            self.tree = None




    # $ANTLR start "column_constraint_default"
    # SQLite.g:432:1: column_constraint_default : DEFAULT ( signed_default_number | literal_value | LPAREN expr RPAREN ) ;
    def column_constraint_default(self, ):

        retval = self.column_constraint_default_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DEFAULT364 = None
        LPAREN367 = None
        RPAREN369 = None
        signed_default_number365 = None

        literal_value366 = None

        expr368 = None


        DEFAULT364_tree = None
        LPAREN367_tree = None
        RPAREN369_tree = None

        try:
            try:
                # SQLite.g:432:26: ( DEFAULT ( signed_default_number | literal_value | LPAREN expr RPAREN ) )
                # SQLite.g:432:28: DEFAULT ( signed_default_number | literal_value | LPAREN expr RPAREN )
                pass 
                root_0 = self._adaptor.nil()

                DEFAULT364=self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_column_constraint_default3222)

                DEFAULT364_tree = self._adaptor.createWithPayload(DEFAULT364)
                root_0 = self._adaptor.becomeRoot(DEFAULT364_tree, root_0)

                # SQLite.g:432:37: ( signed_default_number | literal_value | LPAREN expr RPAREN )
                alt137 = 3
                alt137 = self.dfa137.predict(self.input)
                if alt137 == 1:
                    # SQLite.g:432:38: signed_default_number
                    pass 
                    self._state.following.append(self.FOLLOW_signed_default_number_in_column_constraint_default3226)
                    signed_default_number365 = self.signed_default_number()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, signed_default_number365.tree)


                elif alt137 == 2:
                    # SQLite.g:432:62: literal_value
                    pass 
                    self._state.following.append(self.FOLLOW_literal_value_in_column_constraint_default3230)
                    literal_value366 = self.literal_value()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, literal_value366.tree)


                elif alt137 == 3:
                    # SQLite.g:432:78: LPAREN expr RPAREN
                    pass 
                    LPAREN367=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_column_constraint_default3234)
                    self._state.following.append(self.FOLLOW_expr_in_column_constraint_default3237)
                    expr368 = self.expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expr368.tree)
                    RPAREN369=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_column_constraint_default3239)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "column_constraint_default"

    class column_constraint_collate_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.column_constraint_collate_return, self).__init__()

            self.tree = None




    # $ANTLR start "column_constraint_collate"
    # SQLite.g:434:1: column_constraint_collate : COLLATE collation_name= id ;
    def column_constraint_collate(self, ):

        retval = self.column_constraint_collate_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLLATE370 = None
        collation_name = None


        COLLATE370_tree = None

        try:
            try:
                # SQLite.g:434:26: ( COLLATE collation_name= id )
                # SQLite.g:434:28: COLLATE collation_name= id
                pass 
                root_0 = self._adaptor.nil()

                COLLATE370=self.match(self.input, COLLATE, self.FOLLOW_COLLATE_in_column_constraint_collate3248)

                COLLATE370_tree = self._adaptor.createWithPayload(COLLATE370)
                root_0 = self._adaptor.becomeRoot(COLLATE370_tree, root_0)

                self._state.following.append(self.FOLLOW_id_in_column_constraint_collate3253)
                collation_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, collation_name.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "column_constraint_collate"

    class table_constraint_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.table_constraint_return, self).__init__()

            self.tree = None




    # $ANTLR start "table_constraint"
    # SQLite.g:436:1: table_constraint : ( CONSTRAINT name= id )? ( table_constraint_pk | table_constraint_unique | table_constraint_check | table_constraint_fk ) -> ^( TABLE_CONSTRAINT ( table_constraint_pk )? ( table_constraint_unique )? ( table_constraint_check )? ( table_constraint_fk )? ( $name)? ) ;
    def table_constraint(self, ):

        retval = self.table_constraint_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CONSTRAINT371 = None
        name = None

        table_constraint_pk372 = None

        table_constraint_unique373 = None

        table_constraint_check374 = None

        table_constraint_fk375 = None


        CONSTRAINT371_tree = None
        stream_CONSTRAINT = RewriteRuleTokenStream(self._adaptor, "token CONSTRAINT")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_table_constraint_pk = RewriteRuleSubtreeStream(self._adaptor, "rule table_constraint_pk")
        stream_table_constraint_fk = RewriteRuleSubtreeStream(self._adaptor, "rule table_constraint_fk")
        stream_table_constraint_unique = RewriteRuleSubtreeStream(self._adaptor, "rule table_constraint_unique")
        stream_table_constraint_check = RewriteRuleSubtreeStream(self._adaptor, "rule table_constraint_check")
        try:
            try:
                # SQLite.g:436:17: ( ( CONSTRAINT name= id )? ( table_constraint_pk | table_constraint_unique | table_constraint_check | table_constraint_fk ) -> ^( TABLE_CONSTRAINT ( table_constraint_pk )? ( table_constraint_unique )? ( table_constraint_check )? ( table_constraint_fk )? ( $name)? ) )
                # SQLite.g:436:19: ( CONSTRAINT name= id )? ( table_constraint_pk | table_constraint_unique | table_constraint_check | table_constraint_fk )
                pass 
                # SQLite.g:436:19: ( CONSTRAINT name= id )?
                alt138 = 2
                LA138_0 = self.input.LA(1)

                if (LA138_0 == CONSTRAINT) :
                    alt138 = 1
                if alt138 == 1:
                    # SQLite.g:436:20: CONSTRAINT name= id
                    pass 
                    CONSTRAINT371=self.match(self.input, CONSTRAINT, self.FOLLOW_CONSTRAINT_in_table_constraint3262) 
                    stream_CONSTRAINT.add(CONSTRAINT371)
                    self._state.following.append(self.FOLLOW_id_in_table_constraint3266)
                    name = self.id()

                    self._state.following.pop()
                    stream_id.add(name.tree)



                # SQLite.g:437:3: ( table_constraint_pk | table_constraint_unique | table_constraint_check | table_constraint_fk )
                alt139 = 4
                LA139 = self.input.LA(1)
                if LA139 == PRIMARY:
                    alt139 = 1
                elif LA139 == UNIQUE:
                    alt139 = 2
                elif LA139 == CHECK:
                    alt139 = 3
                elif LA139 == FOREIGN:
                    alt139 = 4
                else:
                    nvae = NoViableAltException("", 139, 0, self.input)

                    raise nvae

                if alt139 == 1:
                    # SQLite.g:437:5: table_constraint_pk
                    pass 
                    self._state.following.append(self.FOLLOW_table_constraint_pk_in_table_constraint3274)
                    table_constraint_pk372 = self.table_constraint_pk()

                    self._state.following.pop()
                    stream_table_constraint_pk.add(table_constraint_pk372.tree)


                elif alt139 == 2:
                    # SQLite.g:438:5: table_constraint_unique
                    pass 
                    self._state.following.append(self.FOLLOW_table_constraint_unique_in_table_constraint3280)
                    table_constraint_unique373 = self.table_constraint_unique()

                    self._state.following.pop()
                    stream_table_constraint_unique.add(table_constraint_unique373.tree)


                elif alt139 == 3:
                    # SQLite.g:439:5: table_constraint_check
                    pass 
                    self._state.following.append(self.FOLLOW_table_constraint_check_in_table_constraint3286)
                    table_constraint_check374 = self.table_constraint_check()

                    self._state.following.pop()
                    stream_table_constraint_check.add(table_constraint_check374.tree)


                elif alt139 == 4:
                    # SQLite.g:440:5: table_constraint_fk
                    pass 
                    self._state.following.append(self.FOLLOW_table_constraint_fk_in_table_constraint3292)
                    table_constraint_fk375 = self.table_constraint_fk()

                    self._state.following.pop()
                    stream_table_constraint_fk.add(table_constraint_fk375.tree)




                # AST Rewrite
                # elements: table_constraint_pk, table_constraint_check, table_constraint_unique, name, table_constraint_fk
                # token labels: 
                # rule labels: retval, name
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if name is not None:
                    stream_name = RewriteRuleSubtreeStream(self._adaptor, "rule name", name.tree)
                else:
                    stream_name = RewriteRuleSubtreeStream(self._adaptor, "token name", None)


                root_0 = self._adaptor.nil()
                # 441:1: -> ^( TABLE_CONSTRAINT ( table_constraint_pk )? ( table_constraint_unique )? ( table_constraint_check )? ( table_constraint_fk )? ( $name)? )
                # SQLite.g:441:4: ^( TABLE_CONSTRAINT ( table_constraint_pk )? ( table_constraint_unique )? ( table_constraint_check )? ( table_constraint_fk )? ( $name)? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TABLE_CONSTRAINT, "TABLE_CONSTRAINT"), root_1)

                # SQLite.g:442:3: ( table_constraint_pk )?
                if stream_table_constraint_pk.hasNext():
                    self._adaptor.addChild(root_1, stream_table_constraint_pk.nextTree())


                stream_table_constraint_pk.reset();
                # SQLite.g:443:3: ( table_constraint_unique )?
                if stream_table_constraint_unique.hasNext():
                    self._adaptor.addChild(root_1, stream_table_constraint_unique.nextTree())


                stream_table_constraint_unique.reset();
                # SQLite.g:444:3: ( table_constraint_check )?
                if stream_table_constraint_check.hasNext():
                    self._adaptor.addChild(root_1, stream_table_constraint_check.nextTree())


                stream_table_constraint_check.reset();
                # SQLite.g:445:3: ( table_constraint_fk )?
                if stream_table_constraint_fk.hasNext():
                    self._adaptor.addChild(root_1, stream_table_constraint_fk.nextTree())


                stream_table_constraint_fk.reset();
                # SQLite.g:446:3: ( $name)?
                if stream_name.hasNext():
                    self._adaptor.addChild(root_1, stream_name.nextTree())


                stream_name.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "table_constraint"

    class table_constraint_pk_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.table_constraint_pk_return, self).__init__()

            self.tree = None




    # $ANTLR start "table_constraint_pk"
    # SQLite.g:448:1: table_constraint_pk : PRIMARY KEY LPAREN indexed_columns+= id ( COMMA indexed_columns+= id )* RPAREN ( table_conflict_clause )? -> ^( PRIMARY ^( COLUMNS ( $indexed_columns)+ ) ( table_conflict_clause )? ) ;
    def table_constraint_pk(self, ):

        retval = self.table_constraint_pk_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PRIMARY376 = None
        KEY377 = None
        LPAREN378 = None
        COMMA379 = None
        RPAREN380 = None
        list_indexed_columns = None
        table_conflict_clause381 = None

        indexed_columns = None

        indexed_columns = None
        PRIMARY376_tree = None
        KEY377_tree = None
        LPAREN378_tree = None
        COMMA379_tree = None
        RPAREN380_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_PRIMARY = RewriteRuleTokenStream(self._adaptor, "token PRIMARY")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_KEY = RewriteRuleTokenStream(self._adaptor, "token KEY")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_table_conflict_clause = RewriteRuleSubtreeStream(self._adaptor, "rule table_conflict_clause")
        try:
            try:
                # SQLite.g:448:20: ( PRIMARY KEY LPAREN indexed_columns+= id ( COMMA indexed_columns+= id )* RPAREN ( table_conflict_clause )? -> ^( PRIMARY ^( COLUMNS ( $indexed_columns)+ ) ( table_conflict_clause )? ) )
                # SQLite.g:448:22: PRIMARY KEY LPAREN indexed_columns+= id ( COMMA indexed_columns+= id )* RPAREN ( table_conflict_clause )?
                pass 
                PRIMARY376=self.match(self.input, PRIMARY, self.FOLLOW_PRIMARY_in_table_constraint_pk3332) 
                stream_PRIMARY.add(PRIMARY376)
                KEY377=self.match(self.input, KEY, self.FOLLOW_KEY_in_table_constraint_pk3334) 
                stream_KEY.add(KEY377)
                LPAREN378=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_table_constraint_pk3338) 
                stream_LPAREN.add(LPAREN378)
                self._state.following.append(self.FOLLOW_id_in_table_constraint_pk3342)
                indexed_columns = self.id()

                self._state.following.pop()
                stream_id.add(indexed_columns.tree)
                if list_indexed_columns is None:
                    list_indexed_columns = []
                list_indexed_columns.append(indexed_columns.tree)

                # SQLite.g:449:30: ( COMMA indexed_columns+= id )*
                while True: #loop140
                    alt140 = 2
                    LA140_0 = self.input.LA(1)

                    if (LA140_0 == COMMA) :
                        alt140 = 1


                    if alt140 == 1:
                        # SQLite.g:449:31: COMMA indexed_columns+= id
                        pass 
                        COMMA379=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_table_constraint_pk3345) 
                        stream_COMMA.add(COMMA379)
                        self._state.following.append(self.FOLLOW_id_in_table_constraint_pk3349)
                        indexed_columns = self.id()

                        self._state.following.pop()
                        stream_id.add(indexed_columns.tree)
                        if list_indexed_columns is None:
                            list_indexed_columns = []
                        list_indexed_columns.append(indexed_columns.tree)



                    else:
                        break #loop140
                RPAREN380=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_table_constraint_pk3353) 
                stream_RPAREN.add(RPAREN380)
                # SQLite.g:449:66: ( table_conflict_clause )?
                alt141 = 2
                LA141_0 = self.input.LA(1)

                if (LA141_0 == ON) :
                    alt141 = 1
                if alt141 == 1:
                    # SQLite.g:449:66: table_conflict_clause
                    pass 
                    self._state.following.append(self.FOLLOW_table_conflict_clause_in_table_constraint_pk3355)
                    table_conflict_clause381 = self.table_conflict_clause()

                    self._state.following.pop()
                    stream_table_conflict_clause.add(table_conflict_clause381.tree)




                # AST Rewrite
                # elements: indexed_columns, PRIMARY, table_conflict_clause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: indexed_columns
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                stream_indexed_columns = RewriteRuleSubtreeStream(self._adaptor, "token indexed_columns", list_indexed_columns)
                root_0 = self._adaptor.nil()
                # 450:1: -> ^( PRIMARY ^( COLUMNS ( $indexed_columns)+ ) ( table_conflict_clause )? )
                # SQLite.g:450:4: ^( PRIMARY ^( COLUMNS ( $indexed_columns)+ ) ( table_conflict_clause )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_PRIMARY.nextNode(), root_1)

                # SQLite.g:450:14: ^( COLUMNS ( $indexed_columns)+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(COLUMNS, "COLUMNS"), root_2)

                # SQLite.g:450:24: ( $indexed_columns)+
                if not (stream_indexed_columns.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_indexed_columns.hasNext():
                    self._adaptor.addChild(root_2, stream_indexed_columns.nextTree())


                stream_indexed_columns.reset()

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:450:43: ( table_conflict_clause )?
                if stream_table_conflict_clause.hasNext():
                    self._adaptor.addChild(root_1, stream_table_conflict_clause.nextTree())


                stream_table_conflict_clause.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "table_constraint_pk"

    class table_constraint_unique_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.table_constraint_unique_return, self).__init__()

            self.tree = None




    # $ANTLR start "table_constraint_unique"
    # SQLite.g:452:1: table_constraint_unique : UNIQUE LPAREN indexed_columns+= id ( COMMA indexed_columns+= id )* RPAREN ( table_conflict_clause )? -> ^( UNIQUE ^( COLUMNS ( $indexed_columns)+ ) ( table_conflict_clause )? ) ;
    def table_constraint_unique(self, ):

        retval = self.table_constraint_unique_return()
        retval.start = self.input.LT(1)

        root_0 = None

        UNIQUE382 = None
        LPAREN383 = None
        COMMA384 = None
        RPAREN385 = None
        list_indexed_columns = None
        table_conflict_clause386 = None

        indexed_columns = None

        indexed_columns = None
        UNIQUE382_tree = None
        LPAREN383_tree = None
        COMMA384_tree = None
        RPAREN385_tree = None
        stream_UNIQUE = RewriteRuleTokenStream(self._adaptor, "token UNIQUE")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_table_conflict_clause = RewriteRuleSubtreeStream(self._adaptor, "rule table_conflict_clause")
        try:
            try:
                # SQLite.g:452:24: ( UNIQUE LPAREN indexed_columns+= id ( COMMA indexed_columns+= id )* RPAREN ( table_conflict_clause )? -> ^( UNIQUE ^( COLUMNS ( $indexed_columns)+ ) ( table_conflict_clause )? ) )
                # SQLite.g:452:26: UNIQUE LPAREN indexed_columns+= id ( COMMA indexed_columns+= id )* RPAREN ( table_conflict_clause )?
                pass 
                UNIQUE382=self.match(self.input, UNIQUE, self.FOLLOW_UNIQUE_in_table_constraint_unique3380) 
                stream_UNIQUE.add(UNIQUE382)
                LPAREN383=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_table_constraint_unique3384) 
                stream_LPAREN.add(LPAREN383)
                self._state.following.append(self.FOLLOW_id_in_table_constraint_unique3388)
                indexed_columns = self.id()

                self._state.following.pop()
                stream_id.add(indexed_columns.tree)
                if list_indexed_columns is None:
                    list_indexed_columns = []
                list_indexed_columns.append(indexed_columns.tree)

                # SQLite.g:453:30: ( COMMA indexed_columns+= id )*
                while True: #loop142
                    alt142 = 2
                    LA142_0 = self.input.LA(1)

                    if (LA142_0 == COMMA) :
                        alt142 = 1


                    if alt142 == 1:
                        # SQLite.g:453:31: COMMA indexed_columns+= id
                        pass 
                        COMMA384=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_table_constraint_unique3391) 
                        stream_COMMA.add(COMMA384)
                        self._state.following.append(self.FOLLOW_id_in_table_constraint_unique3395)
                        indexed_columns = self.id()

                        self._state.following.pop()
                        stream_id.add(indexed_columns.tree)
                        if list_indexed_columns is None:
                            list_indexed_columns = []
                        list_indexed_columns.append(indexed_columns.tree)



                    else:
                        break #loop142
                RPAREN385=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_table_constraint_unique3399) 
                stream_RPAREN.add(RPAREN385)
                # SQLite.g:453:66: ( table_conflict_clause )?
                alt143 = 2
                LA143_0 = self.input.LA(1)

                if (LA143_0 == ON) :
                    alt143 = 1
                if alt143 == 1:
                    # SQLite.g:453:66: table_conflict_clause
                    pass 
                    self._state.following.append(self.FOLLOW_table_conflict_clause_in_table_constraint_unique3401)
                    table_conflict_clause386 = self.table_conflict_clause()

                    self._state.following.pop()
                    stream_table_conflict_clause.add(table_conflict_clause386.tree)




                # AST Rewrite
                # elements: table_conflict_clause, UNIQUE, indexed_columns
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: indexed_columns
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                stream_indexed_columns = RewriteRuleSubtreeStream(self._adaptor, "token indexed_columns", list_indexed_columns)
                root_0 = self._adaptor.nil()
                # 454:1: -> ^( UNIQUE ^( COLUMNS ( $indexed_columns)+ ) ( table_conflict_clause )? )
                # SQLite.g:454:4: ^( UNIQUE ^( COLUMNS ( $indexed_columns)+ ) ( table_conflict_clause )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_UNIQUE.nextNode(), root_1)

                # SQLite.g:454:13: ^( COLUMNS ( $indexed_columns)+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(COLUMNS, "COLUMNS"), root_2)

                # SQLite.g:454:23: ( $indexed_columns)+
                if not (stream_indexed_columns.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_indexed_columns.hasNext():
                    self._adaptor.addChild(root_2, stream_indexed_columns.nextTree())


                stream_indexed_columns.reset()

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:454:42: ( table_conflict_clause )?
                if stream_table_conflict_clause.hasNext():
                    self._adaptor.addChild(root_1, stream_table_conflict_clause.nextTree())


                stream_table_conflict_clause.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "table_constraint_unique"

    class table_constraint_check_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.table_constraint_check_return, self).__init__()

            self.tree = None




    # $ANTLR start "table_constraint_check"
    # SQLite.g:456:1: table_constraint_check : CHECK LPAREN expr RPAREN ;
    def table_constraint_check(self, ):

        retval = self.table_constraint_check_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CHECK387 = None
        LPAREN388 = None
        RPAREN390 = None
        expr389 = None


        CHECK387_tree = None
        LPAREN388_tree = None
        RPAREN390_tree = None

        try:
            try:
                # SQLite.g:456:23: ( CHECK LPAREN expr RPAREN )
                # SQLite.g:456:25: CHECK LPAREN expr RPAREN
                pass 
                root_0 = self._adaptor.nil()

                CHECK387=self.match(self.input, CHECK, self.FOLLOW_CHECK_in_table_constraint_check3426)

                CHECK387_tree = self._adaptor.createWithPayload(CHECK387)
                root_0 = self._adaptor.becomeRoot(CHECK387_tree, root_0)

                LPAREN388=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_table_constraint_check3429)
                self._state.following.append(self.FOLLOW_expr_in_table_constraint_check3432)
                expr389 = self.expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expr389.tree)
                RPAREN390=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_table_constraint_check3434)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "table_constraint_check"

    class table_constraint_fk_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.table_constraint_fk_return, self).__init__()

            self.tree = None




    # $ANTLR start "table_constraint_fk"
    # SQLite.g:458:1: table_constraint_fk : FOREIGN KEY LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN fk_clause -> ^( FOREIGN ^( COLUMNS ( $column_names)+ ) fk_clause ) ;
    def table_constraint_fk(self, ):

        retval = self.table_constraint_fk_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FOREIGN391 = None
        KEY392 = None
        LPAREN393 = None
        COMMA394 = None
        RPAREN395 = None
        list_column_names = None
        fk_clause396 = None

        column_names = None

        column_names = None
        FOREIGN391_tree = None
        KEY392_tree = None
        LPAREN393_tree = None
        COMMA394_tree = None
        RPAREN395_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_FOREIGN = RewriteRuleTokenStream(self._adaptor, "token FOREIGN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_KEY = RewriteRuleTokenStream(self._adaptor, "token KEY")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_fk_clause = RewriteRuleSubtreeStream(self._adaptor, "rule fk_clause")
        try:
            try:
                # SQLite.g:458:20: ( FOREIGN KEY LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN fk_clause -> ^( FOREIGN ^( COLUMNS ( $column_names)+ ) fk_clause ) )
                # SQLite.g:458:22: FOREIGN KEY LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN fk_clause
                pass 
                FOREIGN391=self.match(self.input, FOREIGN, self.FOLLOW_FOREIGN_in_table_constraint_fk3442) 
                stream_FOREIGN.add(FOREIGN391)
                KEY392=self.match(self.input, KEY, self.FOLLOW_KEY_in_table_constraint_fk3444) 
                stream_KEY.add(KEY392)
                LPAREN393=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_table_constraint_fk3446) 
                stream_LPAREN.add(LPAREN393)
                self._state.following.append(self.FOLLOW_id_in_table_constraint_fk3450)
                column_names = self.id()

                self._state.following.pop()
                stream_id.add(column_names.tree)
                if list_column_names is None:
                    list_column_names = []
                list_column_names.append(column_names.tree)

                # SQLite.g:458:58: ( COMMA column_names+= id )*
                while True: #loop144
                    alt144 = 2
                    LA144_0 = self.input.LA(1)

                    if (LA144_0 == COMMA) :
                        alt144 = 1


                    if alt144 == 1:
                        # SQLite.g:458:59: COMMA column_names+= id
                        pass 
                        COMMA394=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_table_constraint_fk3453) 
                        stream_COMMA.add(COMMA394)
                        self._state.following.append(self.FOLLOW_id_in_table_constraint_fk3457)
                        column_names = self.id()

                        self._state.following.pop()
                        stream_id.add(column_names.tree)
                        if list_column_names is None:
                            list_column_names = []
                        list_column_names.append(column_names.tree)



                    else:
                        break #loop144
                RPAREN395=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_table_constraint_fk3461) 
                stream_RPAREN.add(RPAREN395)
                self._state.following.append(self.FOLLOW_fk_clause_in_table_constraint_fk3463)
                fk_clause396 = self.fk_clause()

                self._state.following.pop()
                stream_fk_clause.add(fk_clause396.tree)

                # AST Rewrite
                # elements: FOREIGN, column_names, fk_clause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: column_names
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                stream_column_names = RewriteRuleSubtreeStream(self._adaptor, "token column_names", list_column_names)
                root_0 = self._adaptor.nil()
                # 459:1: -> ^( FOREIGN ^( COLUMNS ( $column_names)+ ) fk_clause )
                # SQLite.g:459:4: ^( FOREIGN ^( COLUMNS ( $column_names)+ ) fk_clause )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_FOREIGN.nextNode(), root_1)

                # SQLite.g:459:14: ^( COLUMNS ( $column_names)+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(COLUMNS, "COLUMNS"), root_2)

                # SQLite.g:459:24: ( $column_names)+
                if not (stream_column_names.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_column_names.hasNext():
                    self._adaptor.addChild(root_2, stream_column_names.nextTree())


                stream_column_names.reset()

                self._adaptor.addChild(root_1, root_2)
                self._adaptor.addChild(root_1, stream_fk_clause.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "table_constraint_fk"

    class fk_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.fk_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "fk_clause"
    # SQLite.g:461:1: fk_clause : REFERENCES foreign_table= id ( LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN )? ( fk_clause_action )* ( fk_clause_deferrable )? -> ^( REFERENCES $foreign_table ^( COLUMNS ( $column_names)+ ) ( fk_clause_action )* ( fk_clause_deferrable )? ) ;
    def fk_clause(self, ):

        retval = self.fk_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        REFERENCES397 = None
        LPAREN398 = None
        COMMA399 = None
        RPAREN400 = None
        list_column_names = None
        foreign_table = None

        fk_clause_action401 = None

        fk_clause_deferrable402 = None

        column_names = None

        column_names = None
        REFERENCES397_tree = None
        LPAREN398_tree = None
        COMMA399_tree = None
        RPAREN400_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_REFERENCES = RewriteRuleTokenStream(self._adaptor, "token REFERENCES")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_fk_clause_action = RewriteRuleSubtreeStream(self._adaptor, "rule fk_clause_action")
        stream_fk_clause_deferrable = RewriteRuleSubtreeStream(self._adaptor, "rule fk_clause_deferrable")
        try:
            try:
                # SQLite.g:461:10: ( REFERENCES foreign_table= id ( LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN )? ( fk_clause_action )* ( fk_clause_deferrable )? -> ^( REFERENCES $foreign_table ^( COLUMNS ( $column_names)+ ) ( fk_clause_action )* ( fk_clause_deferrable )? ) )
                # SQLite.g:461:12: REFERENCES foreign_table= id ( LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN )? ( fk_clause_action )* ( fk_clause_deferrable )?
                pass 
                REFERENCES397=self.match(self.input, REFERENCES, self.FOLLOW_REFERENCES_in_fk_clause3486) 
                stream_REFERENCES.add(REFERENCES397)
                self._state.following.append(self.FOLLOW_id_in_fk_clause3490)
                foreign_table = self.id()

                self._state.following.pop()
                stream_id.add(foreign_table.tree)
                # SQLite.g:461:40: ( LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN )?
                alt146 = 2
                alt146 = self.dfa146.predict(self.input)
                if alt146 == 1:
                    # SQLite.g:461:41: LPAREN column_names+= id ( COMMA column_names+= id )* RPAREN
                    pass 
                    LPAREN398=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_fk_clause3493) 
                    stream_LPAREN.add(LPAREN398)
                    self._state.following.append(self.FOLLOW_id_in_fk_clause3497)
                    column_names = self.id()

                    self._state.following.pop()
                    stream_id.add(column_names.tree)
                    if list_column_names is None:
                        list_column_names = []
                    list_column_names.append(column_names.tree)

                    # SQLite.g:461:65: ( COMMA column_names+= id )*
                    while True: #loop145
                        alt145 = 2
                        LA145_0 = self.input.LA(1)

                        if (LA145_0 == COMMA) :
                            alt145 = 1


                        if alt145 == 1:
                            # SQLite.g:461:66: COMMA column_names+= id
                            pass 
                            COMMA399=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fk_clause3500) 
                            stream_COMMA.add(COMMA399)
                            self._state.following.append(self.FOLLOW_id_in_fk_clause3504)
                            column_names = self.id()

                            self._state.following.pop()
                            stream_id.add(column_names.tree)
                            if list_column_names is None:
                                list_column_names = []
                            list_column_names.append(column_names.tree)



                        else:
                            break #loop145
                    RPAREN400=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_fk_clause3508) 
                    stream_RPAREN.add(RPAREN400)



                # SQLite.g:462:3: ( fk_clause_action )*
                while True: #loop147
                    alt147 = 2
                    alt147 = self.dfa147.predict(self.input)
                    if alt147 == 1:
                        # SQLite.g:462:3: fk_clause_action
                        pass 
                        self._state.following.append(self.FOLLOW_fk_clause_action_in_fk_clause3514)
                        fk_clause_action401 = self.fk_clause_action()

                        self._state.following.pop()
                        stream_fk_clause_action.add(fk_clause_action401.tree)


                    else:
                        break #loop147
                # SQLite.g:462:21: ( fk_clause_deferrable )?
                alt148 = 2
                alt148 = self.dfa148.predict(self.input)
                if alt148 == 1:
                    # SQLite.g:462:21: fk_clause_deferrable
                    pass 
                    self._state.following.append(self.FOLLOW_fk_clause_deferrable_in_fk_clause3517)
                    fk_clause_deferrable402 = self.fk_clause_deferrable()

                    self._state.following.pop()
                    stream_fk_clause_deferrable.add(fk_clause_deferrable402.tree)




                # AST Rewrite
                # elements: REFERENCES, column_names, fk_clause_action, fk_clause_deferrable, foreign_table
                # token labels: 
                # rule labels: retval, foreign_table
                # token list labels: 
                # rule list labels: column_names
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if foreign_table is not None:
                    stream_foreign_table = RewriteRuleSubtreeStream(self._adaptor, "rule foreign_table", foreign_table.tree)
                else:
                    stream_foreign_table = RewriteRuleSubtreeStream(self._adaptor, "token foreign_table", None)

                stream_column_names = RewriteRuleSubtreeStream(self._adaptor, "token column_names", list_column_names)
                root_0 = self._adaptor.nil()
                # 463:1: -> ^( REFERENCES $foreign_table ^( COLUMNS ( $column_names)+ ) ( fk_clause_action )* ( fk_clause_deferrable )? )
                # SQLite.g:463:4: ^( REFERENCES $foreign_table ^( COLUMNS ( $column_names)+ ) ( fk_clause_action )* ( fk_clause_deferrable )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_REFERENCES.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_foreign_table.nextTree())
                # SQLite.g:463:32: ^( COLUMNS ( $column_names)+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(COLUMNS, "COLUMNS"), root_2)

                # SQLite.g:463:42: ( $column_names)+
                if not (stream_column_names.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_column_names.hasNext():
                    self._adaptor.addChild(root_2, stream_column_names.nextTree())


                stream_column_names.reset()

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:463:58: ( fk_clause_action )*
                while stream_fk_clause_action.hasNext():
                    self._adaptor.addChild(root_1, stream_fk_clause_action.nextTree())


                stream_fk_clause_action.reset();
                # SQLite.g:463:76: ( fk_clause_deferrable )?
                if stream_fk_clause_deferrable.hasNext():
                    self._adaptor.addChild(root_1, stream_fk_clause_deferrable.nextTree())


                stream_fk_clause_deferrable.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fk_clause"

    class fk_clause_action_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.fk_clause_action_return, self).__init__()

            self.tree = None




    # $ANTLR start "fk_clause_action"
    # SQLite.g:465:1: fk_clause_action : ( ON ( DELETE | UPDATE | INSERT ) ( SET NULL | SET DEFAULT | CASCADE | RESTRICT ) | MATCH id );
    def fk_clause_action(self, ):

        retval = self.fk_clause_action_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ON403 = None
        set404 = None
        SET405 = None
        NULL406 = None
        SET407 = None
        DEFAULT408 = None
        CASCADE409 = None
        RESTRICT410 = None
        MATCH411 = None
        id412 = None


        ON403_tree = None
        set404_tree = None
        SET405_tree = None
        NULL406_tree = None
        SET407_tree = None
        DEFAULT408_tree = None
        CASCADE409_tree = None
        RESTRICT410_tree = None
        MATCH411_tree = None

        try:
            try:
                # SQLite.g:466:3: ( ON ( DELETE | UPDATE | INSERT ) ( SET NULL | SET DEFAULT | CASCADE | RESTRICT ) | MATCH id )
                alt150 = 2
                LA150_0 = self.input.LA(1)

                if (LA150_0 == ON) :
                    alt150 = 1
                elif (LA150_0 == MATCH) :
                    alt150 = 2
                else:
                    nvae = NoViableAltException("", 150, 0, self.input)

                    raise nvae

                if alt150 == 1:
                    # SQLite.g:466:5: ON ( DELETE | UPDATE | INSERT ) ( SET NULL | SET DEFAULT | CASCADE | RESTRICT )
                    pass 
                    root_0 = self._adaptor.nil()

                    ON403=self.match(self.input, ON, self.FOLLOW_ON_in_fk_clause_action3551)

                    ON403_tree = self._adaptor.createWithPayload(ON403)
                    root_0 = self._adaptor.becomeRoot(ON403_tree, root_0)

                    set404 = self.input.LT(1)
                    if self.input.LA(1) == INSERT or self.input.LA(1) == UPDATE or self.input.LA(1) == DELETE:
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set404))
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    # SQLite.g:466:36: ( SET NULL | SET DEFAULT | CASCADE | RESTRICT )
                    alt149 = 4
                    LA149 = self.input.LA(1)
                    if LA149 == SET:
                        LA149_1 = self.input.LA(2)

                        if (LA149_1 == NULL) :
                            alt149 = 1
                        elif (LA149_1 == DEFAULT) :
                            alt149 = 2
                        else:
                            nvae = NoViableAltException("", 149, 1, self.input)

                            raise nvae

                    elif LA149 == CASCADE:
                        alt149 = 3
                    elif LA149 == RESTRICT:
                        alt149 = 4
                    else:
                        nvae = NoViableAltException("", 149, 0, self.input)

                        raise nvae

                    if alt149 == 1:
                        # SQLite.g:466:37: SET NULL
                        pass 
                        SET405=self.match(self.input, SET, self.FOLLOW_SET_in_fk_clause_action3567)
                        NULL406=self.match(self.input, NULL, self.FOLLOW_NULL_in_fk_clause_action3570)

                        NULL406_tree = self._adaptor.createWithPayload(NULL406)
                        self._adaptor.addChild(root_0, NULL406_tree)



                    elif alt149 == 2:
                        # SQLite.g:466:49: SET DEFAULT
                        pass 
                        SET407=self.match(self.input, SET, self.FOLLOW_SET_in_fk_clause_action3574)
                        DEFAULT408=self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_fk_clause_action3577)

                        DEFAULT408_tree = self._adaptor.createWithPayload(DEFAULT408)
                        self._adaptor.addChild(root_0, DEFAULT408_tree)



                    elif alt149 == 3:
                        # SQLite.g:466:64: CASCADE
                        pass 
                        CASCADE409=self.match(self.input, CASCADE, self.FOLLOW_CASCADE_in_fk_clause_action3581)

                        CASCADE409_tree = self._adaptor.createWithPayload(CASCADE409)
                        self._adaptor.addChild(root_0, CASCADE409_tree)



                    elif alt149 == 4:
                        # SQLite.g:466:74: RESTRICT
                        pass 
                        RESTRICT410=self.match(self.input, RESTRICT, self.FOLLOW_RESTRICT_in_fk_clause_action3585)

                        RESTRICT410_tree = self._adaptor.createWithPayload(RESTRICT410)
                        self._adaptor.addChild(root_0, RESTRICT410_tree)






                elif alt150 == 2:
                    # SQLite.g:467:5: MATCH id
                    pass 
                    root_0 = self._adaptor.nil()

                    MATCH411=self.match(self.input, MATCH, self.FOLLOW_MATCH_in_fk_clause_action3592)

                    MATCH411_tree = self._adaptor.createWithPayload(MATCH411)
                    root_0 = self._adaptor.becomeRoot(MATCH411_tree, root_0)

                    self._state.following.append(self.FOLLOW_id_in_fk_clause_action3595)
                    id412 = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, id412.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fk_clause_action"

    class fk_clause_deferrable_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.fk_clause_deferrable_return, self).__init__()

            self.tree = None




    # $ANTLR start "fk_clause_deferrable"
    # SQLite.g:469:1: fk_clause_deferrable : ( NOT )? DEFERRABLE ( INITIALLY DEFERRED | INITIALLY IMMEDIATE )? ;
    def fk_clause_deferrable(self, ):

        retval = self.fk_clause_deferrable_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT413 = None
        DEFERRABLE414 = None
        INITIALLY415 = None
        DEFERRED416 = None
        INITIALLY417 = None
        IMMEDIATE418 = None

        NOT413_tree = None
        DEFERRABLE414_tree = None
        INITIALLY415_tree = None
        DEFERRED416_tree = None
        INITIALLY417_tree = None
        IMMEDIATE418_tree = None

        try:
            try:
                # SQLite.g:469:21: ( ( NOT )? DEFERRABLE ( INITIALLY DEFERRED | INITIALLY IMMEDIATE )? )
                # SQLite.g:469:23: ( NOT )? DEFERRABLE ( INITIALLY DEFERRED | INITIALLY IMMEDIATE )?
                pass 
                root_0 = self._adaptor.nil()

                # SQLite.g:469:23: ( NOT )?
                alt151 = 2
                LA151_0 = self.input.LA(1)

                if (LA151_0 == NOT) :
                    alt151 = 1
                if alt151 == 1:
                    # SQLite.g:469:24: NOT
                    pass 
                    NOT413=self.match(self.input, NOT, self.FOLLOW_NOT_in_fk_clause_deferrable3603)

                    NOT413_tree = self._adaptor.createWithPayload(NOT413)
                    self._adaptor.addChild(root_0, NOT413_tree)




                DEFERRABLE414=self.match(self.input, DEFERRABLE, self.FOLLOW_DEFERRABLE_in_fk_clause_deferrable3607)

                DEFERRABLE414_tree = self._adaptor.createWithPayload(DEFERRABLE414)
                root_0 = self._adaptor.becomeRoot(DEFERRABLE414_tree, root_0)

                # SQLite.g:469:42: ( INITIALLY DEFERRED | INITIALLY IMMEDIATE )?
                alt152 = 3
                alt152 = self.dfa152.predict(self.input)
                if alt152 == 1:
                    # SQLite.g:469:43: INITIALLY DEFERRED
                    pass 
                    INITIALLY415=self.match(self.input, INITIALLY, self.FOLLOW_INITIALLY_in_fk_clause_deferrable3611)
                    DEFERRED416=self.match(self.input, DEFERRED, self.FOLLOW_DEFERRED_in_fk_clause_deferrable3614)

                    DEFERRED416_tree = self._adaptor.createWithPayload(DEFERRED416)
                    self._adaptor.addChild(root_0, DEFERRED416_tree)



                elif alt152 == 2:
                    # SQLite.g:469:65: INITIALLY IMMEDIATE
                    pass 
                    INITIALLY417=self.match(self.input, INITIALLY, self.FOLLOW_INITIALLY_in_fk_clause_deferrable3618)
                    IMMEDIATE418=self.match(self.input, IMMEDIATE, self.FOLLOW_IMMEDIATE_in_fk_clause_deferrable3621)

                    IMMEDIATE418_tree = self._adaptor.createWithPayload(IMMEDIATE418)
                    self._adaptor.addChild(root_0, IMMEDIATE418_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fk_clause_deferrable"

    class drop_table_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.drop_table_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "drop_table_stmt"
    # SQLite.g:472:1: drop_table_stmt : DROP TABLE ( IF EXISTS )? (database_name= id DOT )? table_name= id -> ^( DROP_TABLE ^( OPTIONS ( EXISTS )? ) ^( $table_name ( $database_name)? ) ) ;
    def drop_table_stmt(self, ):

        retval = self.drop_table_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DROP419 = None
        TABLE420 = None
        IF421 = None
        EXISTS422 = None
        DOT423 = None
        database_name = None

        table_name = None


        DROP419_tree = None
        TABLE420_tree = None
        IF421_tree = None
        EXISTS422_tree = None
        DOT423_tree = None
        stream_TABLE = RewriteRuleTokenStream(self._adaptor, "token TABLE")
        stream_EXISTS = RewriteRuleTokenStream(self._adaptor, "token EXISTS")
        stream_DROP = RewriteRuleTokenStream(self._adaptor, "token DROP")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        try:
            try:
                # SQLite.g:472:16: ( DROP TABLE ( IF EXISTS )? (database_name= id DOT )? table_name= id -> ^( DROP_TABLE ^( OPTIONS ( EXISTS )? ) ^( $table_name ( $database_name)? ) ) )
                # SQLite.g:472:18: DROP TABLE ( IF EXISTS )? (database_name= id DOT )? table_name= id
                pass 
                DROP419=self.match(self.input, DROP, self.FOLLOW_DROP_in_drop_table_stmt3631) 
                stream_DROP.add(DROP419)
                TABLE420=self.match(self.input, TABLE, self.FOLLOW_TABLE_in_drop_table_stmt3633) 
                stream_TABLE.add(TABLE420)
                # SQLite.g:472:29: ( IF EXISTS )?
                alt153 = 2
                LA153_0 = self.input.LA(1)

                if (LA153_0 == IF) :
                    LA153_1 = self.input.LA(2)

                    if (LA153_1 == EXISTS) :
                        alt153 = 1
                if alt153 == 1:
                    # SQLite.g:472:30: IF EXISTS
                    pass 
                    IF421=self.match(self.input, IF, self.FOLLOW_IF_in_drop_table_stmt3636) 
                    stream_IF.add(IF421)
                    EXISTS422=self.match(self.input, EXISTS, self.FOLLOW_EXISTS_in_drop_table_stmt3638) 
                    stream_EXISTS.add(EXISTS422)



                # SQLite.g:472:42: (database_name= id DOT )?
                alt154 = 2
                LA154_0 = self.input.LA(1)

                if (LA154_0 == ID or LA154_0 == STRING) :
                    LA154_1 = self.input.LA(2)

                    if (LA154_1 == DOT) :
                        alt154 = 1
                elif ((EXPLAIN <= LA154_0 <= PLAN) or (INDEXED <= LA154_0 <= BY) or (OR <= LA154_0 <= ESCAPE) or (IS <= LA154_0 <= BETWEEN) or LA154_0 == COLLATE or (DISTINCT <= LA154_0 <= THEN) or (CURRENT_TIME <= LA154_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA154_0 <= ROW)) :
                    LA154_2 = self.input.LA(2)

                    if (LA154_2 == DOT) :
                        alt154 = 1
                if alt154 == 1:
                    # SQLite.g:472:43: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_drop_table_stmt3645)
                    database_name = self.id()

                    self._state.following.pop()
                    stream_id.add(database_name.tree)
                    DOT423=self.match(self.input, DOT, self.FOLLOW_DOT_in_drop_table_stmt3647) 
                    stream_DOT.add(DOT423)



                self._state.following.append(self.FOLLOW_id_in_drop_table_stmt3653)
                table_name = self.id()

                self._state.following.pop()
                stream_id.add(table_name.tree)

                # AST Rewrite
                # elements: EXISTS, table_name, database_name
                # token labels: 
                # rule labels: database_name, retval, table_name
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if database_name is not None:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "rule database_name", database_name.tree)
                else:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "token database_name", None)


                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if table_name is not None:
                    stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "rule table_name", table_name.tree)
                else:
                    stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "token table_name", None)


                root_0 = self._adaptor.nil()
                # 473:1: -> ^( DROP_TABLE ^( OPTIONS ( EXISTS )? ) ^( $table_name ( $database_name)? ) )
                # SQLite.g:473:4: ^( DROP_TABLE ^( OPTIONS ( EXISTS )? ) ^( $table_name ( $database_name)? ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(DROP_TABLE, "DROP_TABLE"), root_1)

                # SQLite.g:473:17: ^( OPTIONS ( EXISTS )? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTIONS, "OPTIONS"), root_2)

                # SQLite.g:473:27: ( EXISTS )?
                if stream_EXISTS.hasNext():
                    self._adaptor.addChild(root_2, stream_EXISTS.nextNode())


                stream_EXISTS.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:473:36: ^( $table_name ( $database_name)? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(stream_table_name.nextNode(), root_2)

                # SQLite.g:473:50: ( $database_name)?
                if stream_database_name.hasNext():
                    self._adaptor.addChild(root_2, stream_database_name.nextTree())


                stream_database_name.reset();

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "drop_table_stmt"

    class alter_table_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.alter_table_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "alter_table_stmt"
    # SQLite.g:476:1: alter_table_stmt : ALTER TABLE (database_name= id DOT )? table_name= id ( RENAME TO new_table_name= id | ADD ( COLUMN )? column_def ) ;
    def alter_table_stmt(self, ):

        retval = self.alter_table_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ALTER424 = None
        TABLE425 = None
        DOT426 = None
        RENAME427 = None
        TO428 = None
        ADD429 = None
        COLUMN430 = None
        database_name = None

        table_name = None

        new_table_name = None

        column_def431 = None


        ALTER424_tree = None
        TABLE425_tree = None
        DOT426_tree = None
        RENAME427_tree = None
        TO428_tree = None
        ADD429_tree = None
        COLUMN430_tree = None

        try:
            try:
                # SQLite.g:476:17: ( ALTER TABLE (database_name= id DOT )? table_name= id ( RENAME TO new_table_name= id | ADD ( COLUMN )? column_def ) )
                # SQLite.g:476:19: ALTER TABLE (database_name= id DOT )? table_name= id ( RENAME TO new_table_name= id | ADD ( COLUMN )? column_def )
                pass 
                root_0 = self._adaptor.nil()

                ALTER424=self.match(self.input, ALTER, self.FOLLOW_ALTER_in_alter_table_stmt3683)

                ALTER424_tree = self._adaptor.createWithPayload(ALTER424)
                self._adaptor.addChild(root_0, ALTER424_tree)

                TABLE425=self.match(self.input, TABLE, self.FOLLOW_TABLE_in_alter_table_stmt3685)

                TABLE425_tree = self._adaptor.createWithPayload(TABLE425)
                self._adaptor.addChild(root_0, TABLE425_tree)

                # SQLite.g:476:31: (database_name= id DOT )?
                alt155 = 2
                LA155_0 = self.input.LA(1)

                if (LA155_0 == ID or LA155_0 == STRING) :
                    LA155_1 = self.input.LA(2)

                    if (LA155_1 == DOT) :
                        alt155 = 1
                elif ((EXPLAIN <= LA155_0 <= PLAN) or (INDEXED <= LA155_0 <= BY) or (OR <= LA155_0 <= ESCAPE) or (IS <= LA155_0 <= BETWEEN) or LA155_0 == COLLATE or (DISTINCT <= LA155_0 <= THEN) or (CURRENT_TIME <= LA155_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA155_0 <= ROW)) :
                    LA155_2 = self.input.LA(2)

                    if (LA155_2 == DOT) :
                        alt155 = 1
                if alt155 == 1:
                    # SQLite.g:476:32: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_alter_table_stmt3690)
                    database_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, database_name.tree)
                    DOT426=self.match(self.input, DOT, self.FOLLOW_DOT_in_alter_table_stmt3692)

                    DOT426_tree = self._adaptor.createWithPayload(DOT426)
                    self._adaptor.addChild(root_0, DOT426_tree)




                self._state.following.append(self.FOLLOW_id_in_alter_table_stmt3698)
                table_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, table_name.tree)
                # SQLite.g:476:69: ( RENAME TO new_table_name= id | ADD ( COLUMN )? column_def )
                alt157 = 2
                LA157_0 = self.input.LA(1)

                if (LA157_0 == RENAME) :
                    alt157 = 1
                elif (LA157_0 == ADD) :
                    alt157 = 2
                else:
                    nvae = NoViableAltException("", 157, 0, self.input)

                    raise nvae

                if alt157 == 1:
                    # SQLite.g:476:70: RENAME TO new_table_name= id
                    pass 
                    RENAME427=self.match(self.input, RENAME, self.FOLLOW_RENAME_in_alter_table_stmt3701)

                    RENAME427_tree = self._adaptor.createWithPayload(RENAME427)
                    self._adaptor.addChild(root_0, RENAME427_tree)

                    TO428=self.match(self.input, TO, self.FOLLOW_TO_in_alter_table_stmt3703)

                    TO428_tree = self._adaptor.createWithPayload(TO428)
                    self._adaptor.addChild(root_0, TO428_tree)

                    self._state.following.append(self.FOLLOW_id_in_alter_table_stmt3707)
                    new_table_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, new_table_name.tree)


                elif alt157 == 2:
                    # SQLite.g:476:100: ADD ( COLUMN )? column_def
                    pass 
                    ADD429=self.match(self.input, ADD, self.FOLLOW_ADD_in_alter_table_stmt3711)

                    ADD429_tree = self._adaptor.createWithPayload(ADD429)
                    self._adaptor.addChild(root_0, ADD429_tree)

                    # SQLite.g:476:104: ( COLUMN )?
                    alt156 = 2
                    LA156_0 = self.input.LA(1)

                    if (LA156_0 == COLUMN) :
                        alt156 = 1
                    if alt156 == 1:
                        # SQLite.g:476:105: COLUMN
                        pass 
                        COLUMN430=self.match(self.input, COLUMN, self.FOLLOW_COLUMN_in_alter_table_stmt3714)

                        COLUMN430_tree = self._adaptor.createWithPayload(COLUMN430)
                        self._adaptor.addChild(root_0, COLUMN430_tree)




                    self._state.following.append(self.FOLLOW_column_def_in_alter_table_stmt3718)
                    column_def431 = self.column_def()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, column_def431.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "alter_table_stmt"

    class create_view_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.create_view_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "create_view_stmt"
    # SQLite.g:479:1: create_view_stmt : CREATE ( TEMPORARY )? VIEW ( IF NOT EXISTS )? (database_name= id DOT )? view_name= id AS t= select_stmt -> ^( CREATE_VIEW ^( OPTIONS ( TEMPORARY )? ( EXISTS )? ) ^( $view_name ( $database_name)? ) ^( STATEMENT $t) ) ;
    def create_view_stmt(self, ):

        retval = self.create_view_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CREATE432 = None
        TEMPORARY433 = None
        VIEW434 = None
        IF435 = None
        NOT436 = None
        EXISTS437 = None
        DOT438 = None
        AS439 = None
        database_name = None

        view_name = None

        t = None


        CREATE432_tree = None
        TEMPORARY433_tree = None
        VIEW434_tree = None
        IF435_tree = None
        NOT436_tree = None
        EXISTS437_tree = None
        DOT438_tree = None
        AS439_tree = None
        stream_AS = RewriteRuleTokenStream(self._adaptor, "token AS")
        stream_CREATE = RewriteRuleTokenStream(self._adaptor, "token CREATE")
        stream_VIEW = RewriteRuleTokenStream(self._adaptor, "token VIEW")
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_EXISTS = RewriteRuleTokenStream(self._adaptor, "token EXISTS")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_TEMPORARY = RewriteRuleTokenStream(self._adaptor, "token TEMPORARY")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_select_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule select_stmt")
        try:
            try:
                # SQLite.g:479:17: ( CREATE ( TEMPORARY )? VIEW ( IF NOT EXISTS )? (database_name= id DOT )? view_name= id AS t= select_stmt -> ^( CREATE_VIEW ^( OPTIONS ( TEMPORARY )? ( EXISTS )? ) ^( $view_name ( $database_name)? ) ^( STATEMENT $t) ) )
                # SQLite.g:479:19: CREATE ( TEMPORARY )? VIEW ( IF NOT EXISTS )? (database_name= id DOT )? view_name= id AS t= select_stmt
                pass 
                CREATE432=self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_view_stmt3727) 
                stream_CREATE.add(CREATE432)
                # SQLite.g:479:26: ( TEMPORARY )?
                alt158 = 2
                LA158_0 = self.input.LA(1)

                if (LA158_0 == TEMPORARY) :
                    alt158 = 1
                if alt158 == 1:
                    # SQLite.g:479:26: TEMPORARY
                    pass 
                    TEMPORARY433=self.match(self.input, TEMPORARY, self.FOLLOW_TEMPORARY_in_create_view_stmt3729) 
                    stream_TEMPORARY.add(TEMPORARY433)



                VIEW434=self.match(self.input, VIEW, self.FOLLOW_VIEW_in_create_view_stmt3732) 
                stream_VIEW.add(VIEW434)
                # SQLite.g:479:42: ( IF NOT EXISTS )?
                alt159 = 2
                LA159_0 = self.input.LA(1)

                if (LA159_0 == IF) :
                    LA159_1 = self.input.LA(2)

                    if (LA159_1 == NOT) :
                        alt159 = 1
                if alt159 == 1:
                    # SQLite.g:479:43: IF NOT EXISTS
                    pass 
                    IF435=self.match(self.input, IF, self.FOLLOW_IF_in_create_view_stmt3735) 
                    stream_IF.add(IF435)
                    NOT436=self.match(self.input, NOT, self.FOLLOW_NOT_in_create_view_stmt3737) 
                    stream_NOT.add(NOT436)
                    EXISTS437=self.match(self.input, EXISTS, self.FOLLOW_EXISTS_in_create_view_stmt3739) 
                    stream_EXISTS.add(EXISTS437)



                # SQLite.g:479:59: (database_name= id DOT )?
                alt160 = 2
                LA160_0 = self.input.LA(1)

                if (LA160_0 == ID or LA160_0 == STRING) :
                    LA160_1 = self.input.LA(2)

                    if (LA160_1 == DOT) :
                        alt160 = 1
                elif ((EXPLAIN <= LA160_0 <= PLAN) or (INDEXED <= LA160_0 <= BY) or (OR <= LA160_0 <= ESCAPE) or (IS <= LA160_0 <= BETWEEN) or LA160_0 == COLLATE or (DISTINCT <= LA160_0 <= THEN) or (CURRENT_TIME <= LA160_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA160_0 <= ROW)) :
                    LA160_2 = self.input.LA(2)

                    if (LA160_2 == DOT) :
                        alt160 = 1
                if alt160 == 1:
                    # SQLite.g:479:60: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_create_view_stmt3746)
                    database_name = self.id()

                    self._state.following.pop()
                    stream_id.add(database_name.tree)
                    DOT438=self.match(self.input, DOT, self.FOLLOW_DOT_in_create_view_stmt3748) 
                    stream_DOT.add(DOT438)



                self._state.following.append(self.FOLLOW_id_in_create_view_stmt3754)
                view_name = self.id()

                self._state.following.pop()
                stream_id.add(view_name.tree)
                AS439=self.match(self.input, AS, self.FOLLOW_AS_in_create_view_stmt3756) 
                stream_AS.add(AS439)
                self._state.following.append(self.FOLLOW_select_stmt_in_create_view_stmt3760)
                t = self.select_stmt()

                self._state.following.pop()
                stream_select_stmt.add(t.tree)

                # AST Rewrite
                # elements: EXISTS, t, database_name, view_name, TEMPORARY
                # token labels: 
                # rule labels: view_name, database_name, retval, t
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if view_name is not None:
                    stream_view_name = RewriteRuleSubtreeStream(self._adaptor, "rule view_name", view_name.tree)
                else:
                    stream_view_name = RewriteRuleSubtreeStream(self._adaptor, "token view_name", None)


                if database_name is not None:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "rule database_name", database_name.tree)
                else:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "token database_name", None)


                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if t is not None:
                    stream_t = RewriteRuleSubtreeStream(self._adaptor, "rule t", t.tree)
                else:
                    stream_t = RewriteRuleSubtreeStream(self._adaptor, "token t", None)


                root_0 = self._adaptor.nil()
                # 480:1: -> ^( CREATE_VIEW ^( OPTIONS ( TEMPORARY )? ( EXISTS )? ) ^( $view_name ( $database_name)? ) ^( STATEMENT $t) )
                # SQLite.g:480:4: ^( CREATE_VIEW ^( OPTIONS ( TEMPORARY )? ( EXISTS )? ) ^( $view_name ( $database_name)? ) ^( STATEMENT $t) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CREATE_VIEW, "CREATE_VIEW"), root_1)

                # SQLite.g:480:18: ^( OPTIONS ( TEMPORARY )? ( EXISTS )? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTIONS, "OPTIONS"), root_2)

                # SQLite.g:480:28: ( TEMPORARY )?
                if stream_TEMPORARY.hasNext():
                    self._adaptor.addChild(root_2, stream_TEMPORARY.nextNode())


                stream_TEMPORARY.reset();
                # SQLite.g:480:39: ( EXISTS )?
                if stream_EXISTS.hasNext():
                    self._adaptor.addChild(root_2, stream_EXISTS.nextNode())


                stream_EXISTS.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:480:48: ^( $view_name ( $database_name)? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(stream_view_name.nextNode(), root_2)

                # SQLite.g:480:61: ( $database_name)?
                if stream_database_name.hasNext():
                    self._adaptor.addChild(root_2, stream_database_name.nextTree())


                stream_database_name.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:480:78: ^( STATEMENT $t)
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(STATEMENT, "STATEMENT"), root_2)

                self._adaptor.addChild(root_2, stream_t.nextTree())

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "create_view_stmt"

    class drop_view_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.drop_view_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "drop_view_stmt"
    # SQLite.g:484:1: drop_view_stmt : DROP VIEW ( IF EXISTS )? (database_name= id DOT )? view_name= id ;
    def drop_view_stmt(self, ):

        retval = self.drop_view_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DROP440 = None
        VIEW441 = None
        IF442 = None
        EXISTS443 = None
        DOT444 = None
        database_name = None

        view_name = None


        DROP440_tree = None
        VIEW441_tree = None
        IF442_tree = None
        EXISTS443_tree = None
        DOT444_tree = None

        try:
            try:
                # SQLite.g:484:15: ( DROP VIEW ( IF EXISTS )? (database_name= id DOT )? view_name= id )
                # SQLite.g:484:17: DROP VIEW ( IF EXISTS )? (database_name= id DOT )? view_name= id
                pass 
                root_0 = self._adaptor.nil()

                DROP440=self.match(self.input, DROP, self.FOLLOW_DROP_in_drop_view_stmt3801)

                DROP440_tree = self._adaptor.createWithPayload(DROP440)
                self._adaptor.addChild(root_0, DROP440_tree)

                VIEW441=self.match(self.input, VIEW, self.FOLLOW_VIEW_in_drop_view_stmt3803)

                VIEW441_tree = self._adaptor.createWithPayload(VIEW441)
                self._adaptor.addChild(root_0, VIEW441_tree)

                # SQLite.g:484:27: ( IF EXISTS )?
                alt161 = 2
                LA161_0 = self.input.LA(1)

                if (LA161_0 == IF) :
                    LA161_1 = self.input.LA(2)

                    if (LA161_1 == EXISTS) :
                        alt161 = 1
                if alt161 == 1:
                    # SQLite.g:484:28: IF EXISTS
                    pass 
                    IF442=self.match(self.input, IF, self.FOLLOW_IF_in_drop_view_stmt3806)

                    IF442_tree = self._adaptor.createWithPayload(IF442)
                    self._adaptor.addChild(root_0, IF442_tree)

                    EXISTS443=self.match(self.input, EXISTS, self.FOLLOW_EXISTS_in_drop_view_stmt3808)

                    EXISTS443_tree = self._adaptor.createWithPayload(EXISTS443)
                    self._adaptor.addChild(root_0, EXISTS443_tree)




                # SQLite.g:484:40: (database_name= id DOT )?
                alt162 = 2
                LA162_0 = self.input.LA(1)

                if (LA162_0 == ID or LA162_0 == STRING) :
                    LA162_1 = self.input.LA(2)

                    if (LA162_1 == DOT) :
                        alt162 = 1
                elif ((EXPLAIN <= LA162_0 <= PLAN) or (INDEXED <= LA162_0 <= BY) or (OR <= LA162_0 <= ESCAPE) or (IS <= LA162_0 <= BETWEEN) or LA162_0 == COLLATE or (DISTINCT <= LA162_0 <= THEN) or (CURRENT_TIME <= LA162_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA162_0 <= ROW)) :
                    LA162_2 = self.input.LA(2)

                    if (LA162_2 == DOT) :
                        alt162 = 1
                if alt162 == 1:
                    # SQLite.g:484:41: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_drop_view_stmt3815)
                    database_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, database_name.tree)
                    DOT444=self.match(self.input, DOT, self.FOLLOW_DOT_in_drop_view_stmt3817)

                    DOT444_tree = self._adaptor.createWithPayload(DOT444)
                    self._adaptor.addChild(root_0, DOT444_tree)




                self._state.following.append(self.FOLLOW_id_in_drop_view_stmt3823)
                view_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, view_name.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "drop_view_stmt"

    class create_index_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.create_index_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "create_index_stmt"
    # SQLite.g:487:1: create_index_stmt : CREATE ( UNIQUE )? INDEX ( IF NOT EXISTS )? (database_name= id DOT )? index_name= id ON table_name= id LPAREN columns+= indexed_column ( COMMA columns+= indexed_column )* RPAREN -> ^( CREATE_INDEX ^( OPTIONS ( UNIQUE )? ( EXISTS )? ) ^( $index_name ( $database_name)? ) $table_name ( ^( COLUMNS ( $columns)+ ) )? ) ;
    def create_index_stmt(self, ):

        retval = self.create_index_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CREATE445 = None
        UNIQUE446 = None
        INDEX447 = None
        IF448 = None
        NOT449 = None
        EXISTS450 = None
        DOT451 = None
        ON452 = None
        LPAREN453 = None
        COMMA454 = None
        RPAREN455 = None
        list_columns = None
        database_name = None

        index_name = None

        table_name = None

        columns = None

        columns = None
        CREATE445_tree = None
        UNIQUE446_tree = None
        INDEX447_tree = None
        IF448_tree = None
        NOT449_tree = None
        EXISTS450_tree = None
        DOT451_tree = None
        ON452_tree = None
        LPAREN453_tree = None
        COMMA454_tree = None
        RPAREN455_tree = None
        stream_INDEX = RewriteRuleTokenStream(self._adaptor, "token INDEX")
        stream_ON = RewriteRuleTokenStream(self._adaptor, "token ON")
        stream_UNIQUE = RewriteRuleTokenStream(self._adaptor, "token UNIQUE")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_CREATE = RewriteRuleTokenStream(self._adaptor, "token CREATE")
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_EXISTS = RewriteRuleTokenStream(self._adaptor, "token EXISTS")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_indexed_column = RewriteRuleSubtreeStream(self._adaptor, "rule indexed_column")
        try:
            try:
                # SQLite.g:487:18: ( CREATE ( UNIQUE )? INDEX ( IF NOT EXISTS )? (database_name= id DOT )? index_name= id ON table_name= id LPAREN columns+= indexed_column ( COMMA columns+= indexed_column )* RPAREN -> ^( CREATE_INDEX ^( OPTIONS ( UNIQUE )? ( EXISTS )? ) ^( $index_name ( $database_name)? ) $table_name ( ^( COLUMNS ( $columns)+ ) )? ) )
                # SQLite.g:487:20: CREATE ( UNIQUE )? INDEX ( IF NOT EXISTS )? (database_name= id DOT )? index_name= id ON table_name= id LPAREN columns+= indexed_column ( COMMA columns+= indexed_column )* RPAREN
                pass 
                CREATE445=self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_index_stmt3831) 
                stream_CREATE.add(CREATE445)
                # SQLite.g:487:27: ( UNIQUE )?
                alt163 = 2
                LA163_0 = self.input.LA(1)

                if (LA163_0 == UNIQUE) :
                    alt163 = 1
                if alt163 == 1:
                    # SQLite.g:487:28: UNIQUE
                    pass 
                    UNIQUE446=self.match(self.input, UNIQUE, self.FOLLOW_UNIQUE_in_create_index_stmt3834) 
                    stream_UNIQUE.add(UNIQUE446)



                INDEX447=self.match(self.input, INDEX, self.FOLLOW_INDEX_in_create_index_stmt3838) 
                stream_INDEX.add(INDEX447)
                # SQLite.g:487:43: ( IF NOT EXISTS )?
                alt164 = 2
                LA164_0 = self.input.LA(1)

                if (LA164_0 == IF) :
                    LA164_1 = self.input.LA(2)

                    if (LA164_1 == NOT) :
                        alt164 = 1
                if alt164 == 1:
                    # SQLite.g:487:44: IF NOT EXISTS
                    pass 
                    IF448=self.match(self.input, IF, self.FOLLOW_IF_in_create_index_stmt3841) 
                    stream_IF.add(IF448)
                    NOT449=self.match(self.input, NOT, self.FOLLOW_NOT_in_create_index_stmt3843) 
                    stream_NOT.add(NOT449)
                    EXISTS450=self.match(self.input, EXISTS, self.FOLLOW_EXISTS_in_create_index_stmt3845) 
                    stream_EXISTS.add(EXISTS450)



                # SQLite.g:487:60: (database_name= id DOT )?
                alt165 = 2
                LA165_0 = self.input.LA(1)

                if (LA165_0 == ID or LA165_0 == STRING) :
                    LA165_1 = self.input.LA(2)

                    if (LA165_1 == DOT) :
                        alt165 = 1
                elif ((EXPLAIN <= LA165_0 <= PLAN) or (INDEXED <= LA165_0 <= BY) or (OR <= LA165_0 <= ESCAPE) or (IS <= LA165_0 <= BETWEEN) or LA165_0 == COLLATE or (DISTINCT <= LA165_0 <= THEN) or (CURRENT_TIME <= LA165_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA165_0 <= ROW)) :
                    LA165_2 = self.input.LA(2)

                    if (LA165_2 == DOT) :
                        alt165 = 1
                if alt165 == 1:
                    # SQLite.g:487:61: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_create_index_stmt3852)
                    database_name = self.id()

                    self._state.following.pop()
                    stream_id.add(database_name.tree)
                    DOT451=self.match(self.input, DOT, self.FOLLOW_DOT_in_create_index_stmt3854) 
                    stream_DOT.add(DOT451)



                self._state.following.append(self.FOLLOW_id_in_create_index_stmt3860)
                index_name = self.id()

                self._state.following.pop()
                stream_id.add(index_name.tree)
                ON452=self.match(self.input, ON, self.FOLLOW_ON_in_create_index_stmt3864) 
                stream_ON.add(ON452)
                self._state.following.append(self.FOLLOW_id_in_create_index_stmt3868)
                table_name = self.id()

                self._state.following.pop()
                stream_id.add(table_name.tree)
                LPAREN453=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_create_index_stmt3870) 
                stream_LPAREN.add(LPAREN453)
                self._state.following.append(self.FOLLOW_indexed_column_in_create_index_stmt3874)
                columns = self.indexed_column()

                self._state.following.pop()
                stream_indexed_column.add(columns.tree)
                if list_columns is None:
                    list_columns = []
                list_columns.append(columns.tree)

                # SQLite.g:488:51: ( COMMA columns+= indexed_column )*
                while True: #loop166
                    alt166 = 2
                    LA166_0 = self.input.LA(1)

                    if (LA166_0 == COMMA) :
                        alt166 = 1


                    if alt166 == 1:
                        # SQLite.g:488:52: COMMA columns+= indexed_column
                        pass 
                        COMMA454=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_create_index_stmt3877) 
                        stream_COMMA.add(COMMA454)
                        self._state.following.append(self.FOLLOW_indexed_column_in_create_index_stmt3881)
                        columns = self.indexed_column()

                        self._state.following.pop()
                        stream_indexed_column.add(columns.tree)
                        if list_columns is None:
                            list_columns = []
                        list_columns.append(columns.tree)



                    else:
                        break #loop166
                RPAREN455=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_create_index_stmt3885) 
                stream_RPAREN.add(RPAREN455)

                # AST Rewrite
                # elements: index_name, columns, database_name, UNIQUE, table_name, EXISTS
                # token labels: 
                # rule labels: database_name, index_name, retval, table_name
                # token list labels: 
                # rule list labels: columns
                # wildcard labels: 

                retval.tree = root_0

                if database_name is not None:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "rule database_name", database_name.tree)
                else:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "token database_name", None)


                if index_name is not None:
                    stream_index_name = RewriteRuleSubtreeStream(self._adaptor, "rule index_name", index_name.tree)
                else:
                    stream_index_name = RewriteRuleSubtreeStream(self._adaptor, "token index_name", None)


                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if table_name is not None:
                    stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "rule table_name", table_name.tree)
                else:
                    stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "token table_name", None)

                stream_columns = RewriteRuleSubtreeStream(self._adaptor, "token columns", list_columns)
                root_0 = self._adaptor.nil()
                # 489:1: -> ^( CREATE_INDEX ^( OPTIONS ( UNIQUE )? ( EXISTS )? ) ^( $index_name ( $database_name)? ) $table_name ( ^( COLUMNS ( $columns)+ ) )? )
                # SQLite.g:489:4: ^( CREATE_INDEX ^( OPTIONS ( UNIQUE )? ( EXISTS )? ) ^( $index_name ( $database_name)? ) $table_name ( ^( COLUMNS ( $columns)+ ) )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CREATE_INDEX, "CREATE_INDEX"), root_1)

                # SQLite.g:489:19: ^( OPTIONS ( UNIQUE )? ( EXISTS )? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTIONS, "OPTIONS"), root_2)

                # SQLite.g:489:29: ( UNIQUE )?
                if stream_UNIQUE.hasNext():
                    self._adaptor.addChild(root_2, stream_UNIQUE.nextNode())


                stream_UNIQUE.reset();
                # SQLite.g:489:37: ( EXISTS )?
                if stream_EXISTS.hasNext():
                    self._adaptor.addChild(root_2, stream_EXISTS.nextNode())


                stream_EXISTS.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:489:46: ^( $index_name ( $database_name)? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(stream_index_name.nextNode(), root_2)

                # SQLite.g:489:60: ( $database_name)?
                if stream_database_name.hasNext():
                    self._adaptor.addChild(root_2, stream_database_name.nextTree())


                stream_database_name.reset();

                self._adaptor.addChild(root_1, root_2)
                self._adaptor.addChild(root_1, stream_table_name.nextTree())
                # SQLite.g:489:89: ( ^( COLUMNS ( $columns)+ ) )?
                if stream_columns.hasNext():
                    # SQLite.g:489:89: ^( COLUMNS ( $columns)+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(COLUMNS, "COLUMNS"), root_2)

                    # SQLite.g:489:99: ( $columns)+
                    if not (stream_columns.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_columns.hasNext():
                        self._adaptor.addChild(root_2, stream_columns.nextTree())


                    stream_columns.reset()

                    self._adaptor.addChild(root_1, root_2)


                stream_columns.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "create_index_stmt"

    class indexed_column_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.indexed_column_return, self).__init__()

            self.tree = None




    # $ANTLR start "indexed_column"
    # SQLite.g:491:1: indexed_column : column_name= id ( COLLATE collation_name= id )? ( ASC | DESC )? -> ^( $column_name ( ^( COLLATE $collation_name) )? ( ASC )? ( DESC )? ) ;
    def indexed_column(self, ):

        retval = self.indexed_column_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLLATE456 = None
        ASC457 = None
        DESC458 = None
        column_name = None

        collation_name = None


        COLLATE456_tree = None
        ASC457_tree = None
        DESC458_tree = None
        stream_ASC = RewriteRuleTokenStream(self._adaptor, "token ASC")
        stream_DESC = RewriteRuleTokenStream(self._adaptor, "token DESC")
        stream_COLLATE = RewriteRuleTokenStream(self._adaptor, "token COLLATE")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        try:
            try:
                # SQLite.g:491:15: (column_name= id ( COLLATE collation_name= id )? ( ASC | DESC )? -> ^( $column_name ( ^( COLLATE $collation_name) )? ( ASC )? ( DESC )? ) )
                # SQLite.g:491:17: column_name= id ( COLLATE collation_name= id )? ( ASC | DESC )?
                pass 
                self._state.following.append(self.FOLLOW_id_in_indexed_column3931)
                column_name = self.id()

                self._state.following.pop()
                stream_id.add(column_name.tree)
                # SQLite.g:491:32: ( COLLATE collation_name= id )?
                alt167 = 2
                LA167_0 = self.input.LA(1)

                if (LA167_0 == COLLATE) :
                    alt167 = 1
                if alt167 == 1:
                    # SQLite.g:491:33: COLLATE collation_name= id
                    pass 
                    COLLATE456=self.match(self.input, COLLATE, self.FOLLOW_COLLATE_in_indexed_column3934) 
                    stream_COLLATE.add(COLLATE456)
                    self._state.following.append(self.FOLLOW_id_in_indexed_column3938)
                    collation_name = self.id()

                    self._state.following.pop()
                    stream_id.add(collation_name.tree)



                # SQLite.g:491:61: ( ASC | DESC )?
                alt168 = 3
                LA168_0 = self.input.LA(1)

                if (LA168_0 == ASC) :
                    alt168 = 1
                elif (LA168_0 == DESC) :
                    alt168 = 2
                if alt168 == 1:
                    # SQLite.g:491:62: ASC
                    pass 
                    ASC457=self.match(self.input, ASC, self.FOLLOW_ASC_in_indexed_column3943) 
                    stream_ASC.add(ASC457)


                elif alt168 == 2:
                    # SQLite.g:491:68: DESC
                    pass 
                    DESC458=self.match(self.input, DESC, self.FOLLOW_DESC_in_indexed_column3947) 
                    stream_DESC.add(DESC458)




                # AST Rewrite
                # elements: DESC, collation_name, column_name, COLLATE, ASC
                # token labels: 
                # rule labels: retval, collation_name, column_name
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if collation_name is not None:
                    stream_collation_name = RewriteRuleSubtreeStream(self._adaptor, "rule collation_name", collation_name.tree)
                else:
                    stream_collation_name = RewriteRuleSubtreeStream(self._adaptor, "token collation_name", None)


                if column_name is not None:
                    stream_column_name = RewriteRuleSubtreeStream(self._adaptor, "rule column_name", column_name.tree)
                else:
                    stream_column_name = RewriteRuleSubtreeStream(self._adaptor, "token column_name", None)


                root_0 = self._adaptor.nil()
                # 492:1: -> ^( $column_name ( ^( COLLATE $collation_name) )? ( ASC )? ( DESC )? )
                # SQLite.g:492:4: ^( $column_name ( ^( COLLATE $collation_name) )? ( ASC )? ( DESC )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_column_name.nextNode(), root_1)

                # SQLite.g:492:19: ( ^( COLLATE $collation_name) )?
                if stream_collation_name.hasNext() or stream_COLLATE.hasNext():
                    # SQLite.g:492:19: ^( COLLATE $collation_name)
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_COLLATE.nextNode(), root_2)

                    self._adaptor.addChild(root_2, stream_collation_name.nextTree())

                    self._adaptor.addChild(root_1, root_2)


                stream_collation_name.reset();
                stream_COLLATE.reset();
                # SQLite.g:492:47: ( ASC )?
                if stream_ASC.hasNext():
                    self._adaptor.addChild(root_1, stream_ASC.nextNode())


                stream_ASC.reset();
                # SQLite.g:492:52: ( DESC )?
                if stream_DESC.hasNext():
                    self._adaptor.addChild(root_1, stream_DESC.nextNode())


                stream_DESC.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "indexed_column"

    class drop_index_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.drop_index_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "drop_index_stmt"
    # SQLite.g:495:1: drop_index_stmt : DROP INDEX ( IF EXISTS )? (database_name= id DOT )? index_name= id -> ^( DROP_INDEX ^( OPTIONS ( EXISTS )? ) ^( $index_name ( $database_name)? ) ) ;
    def drop_index_stmt(self, ):

        retval = self.drop_index_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DROP459 = None
        INDEX460 = None
        IF461 = None
        EXISTS462 = None
        DOT463 = None
        database_name = None

        index_name = None


        DROP459_tree = None
        INDEX460_tree = None
        IF461_tree = None
        EXISTS462_tree = None
        DOT463_tree = None
        stream_INDEX = RewriteRuleTokenStream(self._adaptor, "token INDEX")
        stream_EXISTS = RewriteRuleTokenStream(self._adaptor, "token EXISTS")
        stream_DROP = RewriteRuleTokenStream(self._adaptor, "token DROP")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        try:
            try:
                # SQLite.g:495:16: ( DROP INDEX ( IF EXISTS )? (database_name= id DOT )? index_name= id -> ^( DROP_INDEX ^( OPTIONS ( EXISTS )? ) ^( $index_name ( $database_name)? ) ) )
                # SQLite.g:495:18: DROP INDEX ( IF EXISTS )? (database_name= id DOT )? index_name= id
                pass 
                DROP459=self.match(self.input, DROP, self.FOLLOW_DROP_in_drop_index_stmt3978) 
                stream_DROP.add(DROP459)
                INDEX460=self.match(self.input, INDEX, self.FOLLOW_INDEX_in_drop_index_stmt3980) 
                stream_INDEX.add(INDEX460)
                # SQLite.g:495:29: ( IF EXISTS )?
                alt169 = 2
                LA169_0 = self.input.LA(1)

                if (LA169_0 == IF) :
                    LA169_1 = self.input.LA(2)

                    if (LA169_1 == EXISTS) :
                        alt169 = 1
                if alt169 == 1:
                    # SQLite.g:495:30: IF EXISTS
                    pass 
                    IF461=self.match(self.input, IF, self.FOLLOW_IF_in_drop_index_stmt3983) 
                    stream_IF.add(IF461)
                    EXISTS462=self.match(self.input, EXISTS, self.FOLLOW_EXISTS_in_drop_index_stmt3985) 
                    stream_EXISTS.add(EXISTS462)



                # SQLite.g:495:42: (database_name= id DOT )?
                alt170 = 2
                LA170_0 = self.input.LA(1)

                if (LA170_0 == ID or LA170_0 == STRING) :
                    LA170_1 = self.input.LA(2)

                    if (LA170_1 == DOT) :
                        alt170 = 1
                elif ((EXPLAIN <= LA170_0 <= PLAN) or (INDEXED <= LA170_0 <= BY) or (OR <= LA170_0 <= ESCAPE) or (IS <= LA170_0 <= BETWEEN) or LA170_0 == COLLATE or (DISTINCT <= LA170_0 <= THEN) or (CURRENT_TIME <= LA170_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA170_0 <= ROW)) :
                    LA170_2 = self.input.LA(2)

                    if (LA170_2 == DOT) :
                        alt170 = 1
                if alt170 == 1:
                    # SQLite.g:495:43: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_drop_index_stmt3992)
                    database_name = self.id()

                    self._state.following.pop()
                    stream_id.add(database_name.tree)
                    DOT463=self.match(self.input, DOT, self.FOLLOW_DOT_in_drop_index_stmt3994) 
                    stream_DOT.add(DOT463)



                self._state.following.append(self.FOLLOW_id_in_drop_index_stmt4000)
                index_name = self.id()

                self._state.following.pop()
                stream_id.add(index_name.tree)

                # AST Rewrite
                # elements: database_name, EXISTS, index_name
                # token labels: 
                # rule labels: index_name, database_name, retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if index_name is not None:
                    stream_index_name = RewriteRuleSubtreeStream(self._adaptor, "rule index_name", index_name.tree)
                else:
                    stream_index_name = RewriteRuleSubtreeStream(self._adaptor, "token index_name", None)


                if database_name is not None:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "rule database_name", database_name.tree)
                else:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "token database_name", None)


                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 496:1: -> ^( DROP_INDEX ^( OPTIONS ( EXISTS )? ) ^( $index_name ( $database_name)? ) )
                # SQLite.g:496:4: ^( DROP_INDEX ^( OPTIONS ( EXISTS )? ) ^( $index_name ( $database_name)? ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(DROP_INDEX, "DROP_INDEX"), root_1)

                # SQLite.g:496:17: ^( OPTIONS ( EXISTS )? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTIONS, "OPTIONS"), root_2)

                # SQLite.g:496:27: ( EXISTS )?
                if stream_EXISTS.hasNext():
                    self._adaptor.addChild(root_2, stream_EXISTS.nextNode())


                stream_EXISTS.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:496:36: ^( $index_name ( $database_name)? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(stream_index_name.nextNode(), root_2)

                # SQLite.g:496:50: ( $database_name)?
                if stream_database_name.hasNext():
                    self._adaptor.addChild(root_2, stream_database_name.nextTree())


                stream_database_name.reset();

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "drop_index_stmt"

    class create_trigger_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.create_trigger_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "create_trigger_stmt"
    # SQLite.g:499:1: create_trigger_stmt : CREATE ( TEMPORARY )? TRIGGER ( IF NOT EXISTS )? (database_name= id DOT )? trigger_name= id ( BEFORE | AFTER | INSTEAD OF )? ( DELETE | INSERT | UPDATE ( OF column_names+= id ( COMMA column_names+= id )* )? ) ON table_name= id ( FOR EACH ROW )? ( WHEN expr )? BEGIN ( ( update_stmt | insert_stmt | delete_stmt | select_stmt ) SEMI )+ END -> ^( CREATE_TRIGGER ^( OPTIONS ( TEMPORARY )? ) ^( $trigger_name $table_name ( $database_name)? ) ) ;
    def create_trigger_stmt(self, ):

        retval = self.create_trigger_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CREATE464 = None
        TEMPORARY465 = None
        TRIGGER466 = None
        IF467 = None
        NOT468 = None
        EXISTS469 = None
        DOT470 = None
        BEFORE471 = None
        AFTER472 = None
        INSTEAD473 = None
        OF474 = None
        DELETE475 = None
        INSERT476 = None
        UPDATE477 = None
        OF478 = None
        COMMA479 = None
        ON480 = None
        FOR481 = None
        EACH482 = None
        ROW483 = None
        WHEN484 = None
        BEGIN486 = None
        SEMI491 = None
        END492 = None
        list_column_names = None
        database_name = None

        trigger_name = None

        table_name = None

        expr485 = None

        update_stmt487 = None

        insert_stmt488 = None

        delete_stmt489 = None

        select_stmt490 = None

        column_names = None

        column_names = None
        CREATE464_tree = None
        TEMPORARY465_tree = None
        TRIGGER466_tree = None
        IF467_tree = None
        NOT468_tree = None
        EXISTS469_tree = None
        DOT470_tree = None
        BEFORE471_tree = None
        AFTER472_tree = None
        INSTEAD473_tree = None
        OF474_tree = None
        DELETE475_tree = None
        INSERT476_tree = None
        UPDATE477_tree = None
        OF478_tree = None
        COMMA479_tree = None
        ON480_tree = None
        FOR481_tree = None
        EACH482_tree = None
        ROW483_tree = None
        WHEN484_tree = None
        BEGIN486_tree = None
        SEMI491_tree = None
        END492_tree = None
        stream_CREATE = RewriteRuleTokenStream(self._adaptor, "token CREATE")
        stream_INSERT = RewriteRuleTokenStream(self._adaptor, "token INSERT")
        stream_ROW = RewriteRuleTokenStream(self._adaptor, "token ROW")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_WHEN = RewriteRuleTokenStream(self._adaptor, "token WHEN")
        stream_BEGIN = RewriteRuleTokenStream(self._adaptor, "token BEGIN")
        stream_TRIGGER = RewriteRuleTokenStream(self._adaptor, "token TRIGGER")
        stream_ON = RewriteRuleTokenStream(self._adaptor, "token ON")
        stream_UPDATE = RewriteRuleTokenStream(self._adaptor, "token UPDATE")
        stream_FOR = RewriteRuleTokenStream(self._adaptor, "token FOR")
        stream_BEFORE = RewriteRuleTokenStream(self._adaptor, "token BEFORE")
        stream_DELETE = RewriteRuleTokenStream(self._adaptor, "token DELETE")
        stream_EXISTS = RewriteRuleTokenStream(self._adaptor, "token EXISTS")
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_EACH = RewriteRuleTokenStream(self._adaptor, "token EACH")
        stream_AFTER = RewriteRuleTokenStream(self._adaptor, "token AFTER")
        stream_INSTEAD = RewriteRuleTokenStream(self._adaptor, "token INSTEAD")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_END = RewriteRuleTokenStream(self._adaptor, "token END")
        stream_OF = RewriteRuleTokenStream(self._adaptor, "token OF")
        stream_TEMPORARY = RewriteRuleTokenStream(self._adaptor, "token TEMPORARY")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_id = RewriteRuleSubtreeStream(self._adaptor, "rule id")
        stream_insert_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule insert_stmt")
        stream_select_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule select_stmt")
        stream_delete_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule delete_stmt")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_update_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule update_stmt")
        try:
            try:
                # SQLite.g:499:20: ( CREATE ( TEMPORARY )? TRIGGER ( IF NOT EXISTS )? (database_name= id DOT )? trigger_name= id ( BEFORE | AFTER | INSTEAD OF )? ( DELETE | INSERT | UPDATE ( OF column_names+= id ( COMMA column_names+= id )* )? ) ON table_name= id ( FOR EACH ROW )? ( WHEN expr )? BEGIN ( ( update_stmt | insert_stmt | delete_stmt | select_stmt ) SEMI )+ END -> ^( CREATE_TRIGGER ^( OPTIONS ( TEMPORARY )? ) ^( $trigger_name $table_name ( $database_name)? ) ) )
                # SQLite.g:499:22: CREATE ( TEMPORARY )? TRIGGER ( IF NOT EXISTS )? (database_name= id DOT )? trigger_name= id ( BEFORE | AFTER | INSTEAD OF )? ( DELETE | INSERT | UPDATE ( OF column_names+= id ( COMMA column_names+= id )* )? ) ON table_name= id ( FOR EACH ROW )? ( WHEN expr )? BEGIN ( ( update_stmt | insert_stmt | delete_stmt | select_stmt ) SEMI )+ END
                pass 
                CREATE464=self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_trigger_stmt4030) 
                stream_CREATE.add(CREATE464)
                # SQLite.g:499:29: ( TEMPORARY )?
                alt171 = 2
                LA171_0 = self.input.LA(1)

                if (LA171_0 == TEMPORARY) :
                    alt171 = 1
                if alt171 == 1:
                    # SQLite.g:499:29: TEMPORARY
                    pass 
                    TEMPORARY465=self.match(self.input, TEMPORARY, self.FOLLOW_TEMPORARY_in_create_trigger_stmt4032) 
                    stream_TEMPORARY.add(TEMPORARY465)



                TRIGGER466=self.match(self.input, TRIGGER, self.FOLLOW_TRIGGER_in_create_trigger_stmt4035) 
                stream_TRIGGER.add(TRIGGER466)
                # SQLite.g:499:48: ( IF NOT EXISTS )?
                alt172 = 2
                alt172 = self.dfa172.predict(self.input)
                if alt172 == 1:
                    # SQLite.g:499:49: IF NOT EXISTS
                    pass 
                    IF467=self.match(self.input, IF, self.FOLLOW_IF_in_create_trigger_stmt4038) 
                    stream_IF.add(IF467)
                    NOT468=self.match(self.input, NOT, self.FOLLOW_NOT_in_create_trigger_stmt4040) 
                    stream_NOT.add(NOT468)
                    EXISTS469=self.match(self.input, EXISTS, self.FOLLOW_EXISTS_in_create_trigger_stmt4042) 
                    stream_EXISTS.add(EXISTS469)



                # SQLite.g:499:65: (database_name= id DOT )?
                alt173 = 2
                alt173 = self.dfa173.predict(self.input)
                if alt173 == 1:
                    # SQLite.g:499:66: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_create_trigger_stmt4049)
                    database_name = self.id()

                    self._state.following.pop()
                    stream_id.add(database_name.tree)
                    DOT470=self.match(self.input, DOT, self.FOLLOW_DOT_in_create_trigger_stmt4051) 
                    stream_DOT.add(DOT470)



                self._state.following.append(self.FOLLOW_id_in_create_trigger_stmt4057)
                trigger_name = self.id()

                self._state.following.pop()
                stream_id.add(trigger_name.tree)
                # SQLite.g:500:3: ( BEFORE | AFTER | INSTEAD OF )?
                alt174 = 4
                LA174 = self.input.LA(1)
                if LA174 == BEFORE:
                    alt174 = 1
                elif LA174 == AFTER:
                    alt174 = 2
                elif LA174 == INSTEAD:
                    alt174 = 3
                if alt174 == 1:
                    # SQLite.g:500:4: BEFORE
                    pass 
                    BEFORE471=self.match(self.input, BEFORE, self.FOLLOW_BEFORE_in_create_trigger_stmt4062) 
                    stream_BEFORE.add(BEFORE471)


                elif alt174 == 2:
                    # SQLite.g:500:13: AFTER
                    pass 
                    AFTER472=self.match(self.input, AFTER, self.FOLLOW_AFTER_in_create_trigger_stmt4066) 
                    stream_AFTER.add(AFTER472)


                elif alt174 == 3:
                    # SQLite.g:500:21: INSTEAD OF
                    pass 
                    INSTEAD473=self.match(self.input, INSTEAD, self.FOLLOW_INSTEAD_in_create_trigger_stmt4070) 
                    stream_INSTEAD.add(INSTEAD473)
                    OF474=self.match(self.input, OF, self.FOLLOW_OF_in_create_trigger_stmt4072) 
                    stream_OF.add(OF474)



                # SQLite.g:500:34: ( DELETE | INSERT | UPDATE ( OF column_names+= id ( COMMA column_names+= id )* )? )
                alt177 = 3
                LA177 = self.input.LA(1)
                if LA177 == DELETE:
                    alt177 = 1
                elif LA177 == INSERT:
                    alt177 = 2
                elif LA177 == UPDATE:
                    alt177 = 3
                else:
                    nvae = NoViableAltException("", 177, 0, self.input)

                    raise nvae

                if alt177 == 1:
                    # SQLite.g:500:35: DELETE
                    pass 
                    DELETE475=self.match(self.input, DELETE, self.FOLLOW_DELETE_in_create_trigger_stmt4077) 
                    stream_DELETE.add(DELETE475)


                elif alt177 == 2:
                    # SQLite.g:500:44: INSERT
                    pass 
                    INSERT476=self.match(self.input, INSERT, self.FOLLOW_INSERT_in_create_trigger_stmt4081) 
                    stream_INSERT.add(INSERT476)


                elif alt177 == 3:
                    # SQLite.g:500:53: UPDATE ( OF column_names+= id ( COMMA column_names+= id )* )?
                    pass 
                    UPDATE477=self.match(self.input, UPDATE, self.FOLLOW_UPDATE_in_create_trigger_stmt4085) 
                    stream_UPDATE.add(UPDATE477)
                    # SQLite.g:500:60: ( OF column_names+= id ( COMMA column_names+= id )* )?
                    alt176 = 2
                    LA176_0 = self.input.LA(1)

                    if (LA176_0 == OF) :
                        alt176 = 1
                    if alt176 == 1:
                        # SQLite.g:500:61: OF column_names+= id ( COMMA column_names+= id )*
                        pass 
                        OF478=self.match(self.input, OF, self.FOLLOW_OF_in_create_trigger_stmt4088) 
                        stream_OF.add(OF478)
                        self._state.following.append(self.FOLLOW_id_in_create_trigger_stmt4092)
                        column_names = self.id()

                        self._state.following.pop()
                        stream_id.add(column_names.tree)
                        if list_column_names is None:
                            list_column_names = []
                        list_column_names.append(column_names.tree)

                        # SQLite.g:500:81: ( COMMA column_names+= id )*
                        while True: #loop175
                            alt175 = 2
                            LA175_0 = self.input.LA(1)

                            if (LA175_0 == COMMA) :
                                alt175 = 1


                            if alt175 == 1:
                                # SQLite.g:500:82: COMMA column_names+= id
                                pass 
                                COMMA479=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_create_trigger_stmt4095) 
                                stream_COMMA.add(COMMA479)
                                self._state.following.append(self.FOLLOW_id_in_create_trigger_stmt4099)
                                column_names = self.id()

                                self._state.following.pop()
                                stream_id.add(column_names.tree)
                                if list_column_names is None:
                                    list_column_names = []
                                list_column_names.append(column_names.tree)



                            else:
                                break #loop175






                ON480=self.match(self.input, ON, self.FOLLOW_ON_in_create_trigger_stmt4108) 
                stream_ON.add(ON480)
                self._state.following.append(self.FOLLOW_id_in_create_trigger_stmt4112)
                table_name = self.id()

                self._state.following.pop()
                stream_id.add(table_name.tree)
                # SQLite.g:501:20: ( FOR EACH ROW )?
                alt178 = 2
                LA178_0 = self.input.LA(1)

                if (LA178_0 == FOR) :
                    alt178 = 1
                if alt178 == 1:
                    # SQLite.g:501:21: FOR EACH ROW
                    pass 
                    FOR481=self.match(self.input, FOR, self.FOLLOW_FOR_in_create_trigger_stmt4115) 
                    stream_FOR.add(FOR481)
                    EACH482=self.match(self.input, EACH, self.FOLLOW_EACH_in_create_trigger_stmt4117) 
                    stream_EACH.add(EACH482)
                    ROW483=self.match(self.input, ROW, self.FOLLOW_ROW_in_create_trigger_stmt4119) 
                    stream_ROW.add(ROW483)



                # SQLite.g:501:36: ( WHEN expr )?
                alt179 = 2
                LA179_0 = self.input.LA(1)

                if (LA179_0 == WHEN) :
                    alt179 = 1
                if alt179 == 1:
                    # SQLite.g:501:37: WHEN expr
                    pass 
                    WHEN484=self.match(self.input, WHEN, self.FOLLOW_WHEN_in_create_trigger_stmt4124) 
                    stream_WHEN.add(WHEN484)
                    self._state.following.append(self.FOLLOW_expr_in_create_trigger_stmt4126)
                    expr485 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr485.tree)



                BEGIN486=self.match(self.input, BEGIN, self.FOLLOW_BEGIN_in_create_trigger_stmt4132) 
                stream_BEGIN.add(BEGIN486)
                # SQLite.g:502:9: ( ( update_stmt | insert_stmt | delete_stmt | select_stmt ) SEMI )+
                cnt181 = 0
                while True: #loop181
                    alt181 = 2
                    LA181_0 = self.input.LA(1)

                    if (LA181_0 == REPLACE or LA181_0 == SELECT or LA181_0 == INSERT or LA181_0 == UPDATE or LA181_0 == DELETE) :
                        alt181 = 1


                    if alt181 == 1:
                        # SQLite.g:502:10: ( update_stmt | insert_stmt | delete_stmt | select_stmt ) SEMI
                        pass 
                        # SQLite.g:502:10: ( update_stmt | insert_stmt | delete_stmt | select_stmt )
                        alt180 = 4
                        LA180 = self.input.LA(1)
                        if LA180 == UPDATE:
                            alt180 = 1
                        elif LA180 == REPLACE or LA180 == INSERT:
                            alt180 = 2
                        elif LA180 == DELETE:
                            alt180 = 3
                        elif LA180 == SELECT:
                            alt180 = 4
                        else:
                            nvae = NoViableAltException("", 180, 0, self.input)

                            raise nvae

                        if alt180 == 1:
                            # SQLite.g:502:11: update_stmt
                            pass 
                            self._state.following.append(self.FOLLOW_update_stmt_in_create_trigger_stmt4136)
                            update_stmt487 = self.update_stmt()

                            self._state.following.pop()
                            stream_update_stmt.add(update_stmt487.tree)


                        elif alt180 == 2:
                            # SQLite.g:502:25: insert_stmt
                            pass 
                            self._state.following.append(self.FOLLOW_insert_stmt_in_create_trigger_stmt4140)
                            insert_stmt488 = self.insert_stmt()

                            self._state.following.pop()
                            stream_insert_stmt.add(insert_stmt488.tree)


                        elif alt180 == 3:
                            # SQLite.g:502:39: delete_stmt
                            pass 
                            self._state.following.append(self.FOLLOW_delete_stmt_in_create_trigger_stmt4144)
                            delete_stmt489 = self.delete_stmt()

                            self._state.following.pop()
                            stream_delete_stmt.add(delete_stmt489.tree)


                        elif alt180 == 4:
                            # SQLite.g:502:53: select_stmt
                            pass 
                            self._state.following.append(self.FOLLOW_select_stmt_in_create_trigger_stmt4148)
                            select_stmt490 = self.select_stmt()

                            self._state.following.pop()
                            stream_select_stmt.add(select_stmt490.tree)



                        SEMI491=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_create_trigger_stmt4151) 
                        stream_SEMI.add(SEMI491)


                    else:
                        if cnt181 >= 1:
                            break #loop181

                        eee = EarlyExitException(181, self.input)
                        raise eee

                    cnt181 += 1
                END492=self.match(self.input, END, self.FOLLOW_END_in_create_trigger_stmt4155) 
                stream_END.add(END492)

                # AST Rewrite
                # elements: TEMPORARY, database_name, table_name, trigger_name
                # token labels: 
                # rule labels: database_name, retval, table_name, trigger_name
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if database_name is not None:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "rule database_name", database_name.tree)
                else:
                    stream_database_name = RewriteRuleSubtreeStream(self._adaptor, "token database_name", None)


                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if table_name is not None:
                    stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "rule table_name", table_name.tree)
                else:
                    stream_table_name = RewriteRuleSubtreeStream(self._adaptor, "token table_name", None)


                if trigger_name is not None:
                    stream_trigger_name = RewriteRuleSubtreeStream(self._adaptor, "rule trigger_name", trigger_name.tree)
                else:
                    stream_trigger_name = RewriteRuleSubtreeStream(self._adaptor, "token trigger_name", None)


                root_0 = self._adaptor.nil()
                # 503:1: -> ^( CREATE_TRIGGER ^( OPTIONS ( TEMPORARY )? ) ^( $trigger_name $table_name ( $database_name)? ) )
                # SQLite.g:503:4: ^( CREATE_TRIGGER ^( OPTIONS ( TEMPORARY )? ) ^( $trigger_name $table_name ( $database_name)? ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CREATE_TRIGGER, "CREATE_TRIGGER"), root_1)

                # SQLite.g:503:21: ^( OPTIONS ( TEMPORARY )? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTIONS, "OPTIONS"), root_2)

                # SQLite.g:503:31: ( TEMPORARY )?
                if stream_TEMPORARY.hasNext():
                    self._adaptor.addChild(root_2, stream_TEMPORARY.nextNode())


                stream_TEMPORARY.reset();

                self._adaptor.addChild(root_1, root_2)
                # SQLite.g:503:43: ^( $trigger_name $table_name ( $database_name)? )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(stream_trigger_name.nextNode(), root_2)

                self._adaptor.addChild(root_2, stream_table_name.nextTree())
                # SQLite.g:503:71: ( $database_name)?
                if stream_database_name.hasNext():
                    self._adaptor.addChild(root_2, stream_database_name.nextTree())


                stream_database_name.reset();

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "create_trigger_stmt"

    class drop_trigger_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.drop_trigger_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "drop_trigger_stmt"
    # SQLite.g:506:1: drop_trigger_stmt : DROP TRIGGER ( IF EXISTS )? (database_name= id DOT )? trigger_name= id ;
    def drop_trigger_stmt(self, ):

        retval = self.drop_trigger_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DROP493 = None
        TRIGGER494 = None
        IF495 = None
        EXISTS496 = None
        DOT497 = None
        database_name = None

        trigger_name = None


        DROP493_tree = None
        TRIGGER494_tree = None
        IF495_tree = None
        EXISTS496_tree = None
        DOT497_tree = None

        try:
            try:
                # SQLite.g:506:18: ( DROP TRIGGER ( IF EXISTS )? (database_name= id DOT )? trigger_name= id )
                # SQLite.g:506:20: DROP TRIGGER ( IF EXISTS )? (database_name= id DOT )? trigger_name= id
                pass 
                root_0 = self._adaptor.nil()

                DROP493=self.match(self.input, DROP, self.FOLLOW_DROP_in_drop_trigger_stmt4188)

                DROP493_tree = self._adaptor.createWithPayload(DROP493)
                self._adaptor.addChild(root_0, DROP493_tree)

                TRIGGER494=self.match(self.input, TRIGGER, self.FOLLOW_TRIGGER_in_drop_trigger_stmt4190)

                TRIGGER494_tree = self._adaptor.createWithPayload(TRIGGER494)
                self._adaptor.addChild(root_0, TRIGGER494_tree)

                # SQLite.g:506:33: ( IF EXISTS )?
                alt182 = 2
                LA182_0 = self.input.LA(1)

                if (LA182_0 == IF) :
                    LA182_1 = self.input.LA(2)

                    if (LA182_1 == EXISTS) :
                        alt182 = 1
                if alt182 == 1:
                    # SQLite.g:506:34: IF EXISTS
                    pass 
                    IF495=self.match(self.input, IF, self.FOLLOW_IF_in_drop_trigger_stmt4193)

                    IF495_tree = self._adaptor.createWithPayload(IF495)
                    self._adaptor.addChild(root_0, IF495_tree)

                    EXISTS496=self.match(self.input, EXISTS, self.FOLLOW_EXISTS_in_drop_trigger_stmt4195)

                    EXISTS496_tree = self._adaptor.createWithPayload(EXISTS496)
                    self._adaptor.addChild(root_0, EXISTS496_tree)




                # SQLite.g:506:46: (database_name= id DOT )?
                alt183 = 2
                LA183_0 = self.input.LA(1)

                if (LA183_0 == ID or LA183_0 == STRING) :
                    LA183_1 = self.input.LA(2)

                    if (LA183_1 == DOT) :
                        alt183 = 1
                elif ((EXPLAIN <= LA183_0 <= PLAN) or (INDEXED <= LA183_0 <= BY) or (OR <= LA183_0 <= ESCAPE) or (IS <= LA183_0 <= BETWEEN) or LA183_0 == COLLATE or (DISTINCT <= LA183_0 <= THEN) or (CURRENT_TIME <= LA183_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA183_0 <= ROW)) :
                    LA183_2 = self.input.LA(2)

                    if (LA183_2 == DOT) :
                        alt183 = 1
                if alt183 == 1:
                    # SQLite.g:506:47: database_name= id DOT
                    pass 
                    self._state.following.append(self.FOLLOW_id_in_drop_trigger_stmt4202)
                    database_name = self.id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, database_name.tree)
                    DOT497=self.match(self.input, DOT, self.FOLLOW_DOT_in_drop_trigger_stmt4204)

                    DOT497_tree = self._adaptor.createWithPayload(DOT497)
                    self._adaptor.addChild(root_0, DOT497_tree)




                self._state.following.append(self.FOLLOW_id_in_drop_trigger_stmt4210)
                trigger_name = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, trigger_name.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "drop_trigger_stmt"

    class id_core_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.id_core_return, self).__init__()

            self.tree = None




    # $ANTLR start "id_core"
    # SQLite.g:509:1: id_core : str= ( ID | STRING ) ;
    def id_core(self, ):

        retval = self.id_core_return()
        retval.start = self.input.LT(1)

        root_0 = None

        str = None

        str_tree = None

        try:
            try:
                # SQLite.g:509:8: (str= ( ID | STRING ) )
                # SQLite.g:509:10: str= ( ID | STRING )
                pass 
                root_0 = self._adaptor.nil()

                str = self.input.LT(1)
                if self.input.LA(1) == ID or self.input.LA(1) == STRING:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(str))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse


                #action start
                str.setText(self.unquoteId(str.text));
                #action end



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "id_core"

    class id_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.id_return, self).__init__()

            self.tree = None




    # $ANTLR start "id"
    # SQLite.g:513:1: id : ( id_core | keyword );
    def id(self, ):

        retval = self.id_return()
        retval.start = self.input.LT(1)

        root_0 = None

        id_core498 = None

        keyword499 = None



        try:
            try:
                # SQLite.g:513:3: ( id_core | keyword )
                alt184 = 2
                LA184_0 = self.input.LA(1)

                if (LA184_0 == ID or LA184_0 == STRING) :
                    alt184 = 1
                elif ((EXPLAIN <= LA184_0 <= PLAN) or (INDEXED <= LA184_0 <= BY) or (OR <= LA184_0 <= ESCAPE) or (IS <= LA184_0 <= BETWEEN) or LA184_0 == COLLATE or (DISTINCT <= LA184_0 <= THEN) or (CURRENT_TIME <= LA184_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA184_0 <= ROW)) :
                    alt184 = 2
                else:
                    nvae = NoViableAltException("", 184, 0, self.input)

                    raise nvae

                if alt184 == 1:
                    # SQLite.g:513:5: id_core
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_id_core_in_id4239)
                    id_core498 = self.id_core()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, id_core498.tree)


                elif alt184 == 2:
                    # SQLite.g:513:15: keyword
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_keyword_in_id4243)
                    keyword499 = self.keyword()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, keyword499.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "id"

    class keyword_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.keyword_return, self).__init__()

            self.tree = None




    # $ANTLR start "keyword"
    # SQLite.g:515:1: keyword : ( ABORT | ADD | AFTER | ALL | ALTER | ANALYZE | AND | AS | ASC | ATTACH | AUTOINCREMENT | BEFORE | BEGIN | BETWEEN | BY | CASCADE | CASE | CAST | CHECK | COLLATE | COLUMN | COMMIT | CONFLICT | CONSTRAINT | CREATE | CROSS | CURRENT_TIME | CURRENT_DATE | CURRENT_TIMESTAMP | DATABASE | DEFAULT | DEFERRABLE | DEFERRED | DELETE | DESC | DETACH | DISTINCT | DROP | EACH | ELSE | END | ESCAPE | EXCEPT | EXCLUSIVE | EXISTS | EXPLAIN | FAIL | FOR | FOREIGN | FROM | GROUP | HAVING | IF | IGNORE | IMMEDIATE | INDEX | INDEXED | INITIALLY | INNER | INSERT | INSTEAD | INTERSECT | INTO | IS | JOIN | KEY | LEFT | LIMIT | NATURAL | NULL | OF | OFFSET | ON | OR | ORDER | OUTER | PLAN | PRAGMA | PRIMARY | QUERY | RAISE | REFERENCES | REINDEX | RELEASE | RENAME | REPLACE | RESTRICT | ROLLBACK | ROW | SAVEPOINT | SELECT | SET | TABLE | TEMPORARY | THEN | TO | TRANSACTION | TRIGGER | UNION | UNIQUE | UPDATE | USING | VACUUM | VALUES | VIEW | VIRTUAL | WHEN | WHERE ) ;
    def keyword(self, ):

        retval = self.keyword_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set500 = None

        set500_tree = None

        try:
            try:
                # SQLite.g:515:8: ( ( ABORT | ADD | AFTER | ALL | ALTER | ANALYZE | AND | AS | ASC | ATTACH | AUTOINCREMENT | BEFORE | BEGIN | BETWEEN | BY | CASCADE | CASE | CAST | CHECK | COLLATE | COLUMN | COMMIT | CONFLICT | CONSTRAINT | CREATE | CROSS | CURRENT_TIME | CURRENT_DATE | CURRENT_TIMESTAMP | DATABASE | DEFAULT | DEFERRABLE | DEFERRED | DELETE | DESC | DETACH | DISTINCT | DROP | EACH | ELSE | END | ESCAPE | EXCEPT | EXCLUSIVE | EXISTS | EXPLAIN | FAIL | FOR | FOREIGN | FROM | GROUP | HAVING | IF | IGNORE | IMMEDIATE | INDEX | INDEXED | INITIALLY | INNER | INSERT | INSTEAD | INTERSECT | INTO | IS | JOIN | KEY | LEFT | LIMIT | NATURAL | NULL | OF | OFFSET | ON | OR | ORDER | OUTER | PLAN | PRAGMA | PRIMARY | QUERY | RAISE | REFERENCES | REINDEX | RELEASE | RENAME | REPLACE | RESTRICT | ROLLBACK | ROW | SAVEPOINT | SELECT | SET | TABLE | TEMPORARY | THEN | TO | TRANSACTION | TRIGGER | UNION | UNIQUE | UPDATE | USING | VACUUM | VALUES | VIEW | VIRTUAL | WHEN | WHERE ) )
                # SQLite.g:515:10: ( ABORT | ADD | AFTER | ALL | ALTER | ANALYZE | AND | AS | ASC | ATTACH | AUTOINCREMENT | BEFORE | BEGIN | BETWEEN | BY | CASCADE | CASE | CAST | CHECK | COLLATE | COLUMN | COMMIT | CONFLICT | CONSTRAINT | CREATE | CROSS | CURRENT_TIME | CURRENT_DATE | CURRENT_TIMESTAMP | DATABASE | DEFAULT | DEFERRABLE | DEFERRED | DELETE | DESC | DETACH | DISTINCT | DROP | EACH | ELSE | END | ESCAPE | EXCEPT | EXCLUSIVE | EXISTS | EXPLAIN | FAIL | FOR | FOREIGN | FROM | GROUP | HAVING | IF | IGNORE | IMMEDIATE | INDEX | INDEXED | INITIALLY | INNER | INSERT | INSTEAD | INTERSECT | INTO | IS | JOIN | KEY | LEFT | LIMIT | NATURAL | NULL | OF | OFFSET | ON | OR | ORDER | OUTER | PLAN | PRAGMA | PRIMARY | QUERY | RAISE | REFERENCES | REINDEX | RELEASE | RENAME | REPLACE | RESTRICT | ROLLBACK | ROW | SAVEPOINT | SELECT | SET | TABLE | TEMPORARY | THEN | TO | TRANSACTION | TRIGGER | UNION | UNIQUE | UPDATE | USING | VACUUM | VALUES | VIEW | VIRTUAL | WHEN | WHERE )
                pass 
                root_0 = self._adaptor.nil()

                set500 = self.input.LT(1)
                if (EXPLAIN <= self.input.LA(1) <= PLAN) or (INDEXED <= self.input.LA(1) <= BY) or (OR <= self.input.LA(1) <= ESCAPE) or (IS <= self.input.LA(1) <= BETWEEN) or self.input.LA(1) == COLLATE or (DISTINCT <= self.input.LA(1) <= THEN) or (CURRENT_TIME <= self.input.LA(1) <= CURRENT_TIMESTAMP) or (RAISE <= self.input.LA(1) <= ROW):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set500))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "keyword"

    class id_column_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.id_column_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "id_column_def"
    # SQLite.g:634:1: id_column_def : ( id_core | keyword_column_def );
    def id_column_def(self, ):

        retval = self.id_column_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        id_core501 = None

        keyword_column_def502 = None



        try:
            try:
                # SQLite.g:634:14: ( id_core | keyword_column_def )
                alt185 = 2
                LA185_0 = self.input.LA(1)

                if (LA185_0 == ID or LA185_0 == STRING) :
                    alt185 = 1
                elif ((EXPLAIN <= LA185_0 <= PLAN) or (INDEXED <= LA185_0 <= IN) or (ISNULL <= LA185_0 <= BETWEEN) or (LIKE <= LA185_0 <= MATCH) or LA185_0 == COLLATE or (DISTINCT <= LA185_0 <= THEN) or (CURRENT_TIME <= LA185_0 <= CURRENT_TIMESTAMP) or (RAISE <= LA185_0 <= EXISTS) or (PRIMARY <= LA185_0 <= ADD) or (VIEW <= LA185_0 <= ROW)) :
                    alt185 = 2
                else:
                    nvae = NoViableAltException("", 185, 0, self.input)

                    raise nvae

                if alt185 == 1:
                    # SQLite.g:634:16: id_core
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_id_core_in_id_column_def4917)
                    id_core501 = self.id_core()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, id_core501.tree)


                elif alt185 == 2:
                    # SQLite.g:634:26: keyword_column_def
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_keyword_column_def_in_id_column_def4921)
                    keyword_column_def502 = self.keyword_column_def()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, keyword_column_def502.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "id_column_def"

    class keyword_column_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(SQLiteParser.keyword_column_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "keyword_column_def"
    # SQLite.g:636:1: keyword_column_def : ( ABORT | ADD | AFTER | ALL | ALTER | ANALYZE | AND | AS | ASC | ATTACH | AUTOINCREMENT | BEFORE | BEGIN | BETWEEN | BY | CASCADE | CASE | CAST | CHECK | COLLATE | COMMIT | CONFLICT | CREATE | CROSS | CURRENT_TIME | CURRENT_DATE | CURRENT_TIMESTAMP | DATABASE | DEFAULT | DEFERRABLE | DEFERRED | DELETE | DESC | DETACH | DISTINCT | DROP | EACH | ELSE | END | ESCAPE | EXCEPT | EXCLUSIVE | EXISTS | EXPLAIN | FAIL | FOR | FOREIGN | FROM | GLOB | GROUP | HAVING | IF | IGNORE | IMMEDIATE | IN | INDEX | INDEXED | INITIALLY | INNER | INSERT | INSTEAD | INTERSECT | INTO | IS | ISNULL | JOIN | KEY | LEFT | LIKE | LIMIT | MATCH | NATURAL | NOT | NOTNULL | NULL | OF | OFFSET | ON | OR | ORDER | OUTER | PLAN | PRAGMA | PRIMARY | QUERY | RAISE | REFERENCES | REGEXP | REINDEX | RELEASE | RENAME | REPLACE | RESTRICT | ROLLBACK | ROW | SAVEPOINT | SELECT | SET | TABLE | TEMPORARY | THEN | TO | TRANSACTION | TRIGGER | UNION | UNIQUE | UPDATE | USING | VACUUM | VALUES | VIEW | VIRTUAL | WHEN | WHERE ) ;
    def keyword_column_def(self, ):

        retval = self.keyword_column_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set503 = None

        set503_tree = None

        try:
            try:
                # SQLite.g:636:19: ( ( ABORT | ADD | AFTER | ALL | ALTER | ANALYZE | AND | AS | ASC | ATTACH | AUTOINCREMENT | BEFORE | BEGIN | BETWEEN | BY | CASCADE | CASE | CAST | CHECK | COLLATE | COMMIT | CONFLICT | CREATE | CROSS | CURRENT_TIME | CURRENT_DATE | CURRENT_TIMESTAMP | DATABASE | DEFAULT | DEFERRABLE | DEFERRED | DELETE | DESC | DETACH | DISTINCT | DROP | EACH | ELSE | END | ESCAPE | EXCEPT | EXCLUSIVE | EXISTS | EXPLAIN | FAIL | FOR | FOREIGN | FROM | GLOB | GROUP | HAVING | IF | IGNORE | IMMEDIATE | IN | INDEX | INDEXED | INITIALLY | INNER | INSERT | INSTEAD | INTERSECT | INTO | IS | ISNULL | JOIN | KEY | LEFT | LIKE | LIMIT | MATCH | NATURAL | NOT | NOTNULL | NULL | OF | OFFSET | ON | OR | ORDER | OUTER | PLAN | PRAGMA | PRIMARY | QUERY | RAISE | REFERENCES | REGEXP | REINDEX | RELEASE | RENAME | REPLACE | RESTRICT | ROLLBACK | ROW | SAVEPOINT | SELECT | SET | TABLE | TEMPORARY | THEN | TO | TRANSACTION | TRIGGER | UNION | UNIQUE | UPDATE | USING | VACUUM | VALUES | VIEW | VIRTUAL | WHEN | WHERE ) )
                # SQLite.g:636:21: ( ABORT | ADD | AFTER | ALL | ALTER | ANALYZE | AND | AS | ASC | ATTACH | AUTOINCREMENT | BEFORE | BEGIN | BETWEEN | BY | CASCADE | CASE | CAST | CHECK | COLLATE | COMMIT | CONFLICT | CREATE | CROSS | CURRENT_TIME | CURRENT_DATE | CURRENT_TIMESTAMP | DATABASE | DEFAULT | DEFERRABLE | DEFERRED | DELETE | DESC | DETACH | DISTINCT | DROP | EACH | ELSE | END | ESCAPE | EXCEPT | EXCLUSIVE | EXISTS | EXPLAIN | FAIL | FOR | FOREIGN | FROM | GLOB | GROUP | HAVING | IF | IGNORE | IMMEDIATE | IN | INDEX | INDEXED | INITIALLY | INNER | INSERT | INSTEAD | INTERSECT | INTO | IS | ISNULL | JOIN | KEY | LEFT | LIKE | LIMIT | MATCH | NATURAL | NOT | NOTNULL | NULL | OF | OFFSET | ON | OR | ORDER | OUTER | PLAN | PRAGMA | PRIMARY | QUERY | RAISE | REFERENCES | REGEXP | REINDEX | RELEASE | RENAME | REPLACE | RESTRICT | ROLLBACK | ROW | SAVEPOINT | SELECT | SET | TABLE | TEMPORARY | THEN | TO | TRANSACTION | TRIGGER | UNION | UNIQUE | UPDATE | USING | VACUUM | VALUES | VIEW | VIRTUAL | WHEN | WHERE )
                pass 
                root_0 = self._adaptor.nil()

                set503 = self.input.LT(1)
                if (EXPLAIN <= self.input.LA(1) <= PLAN) or (INDEXED <= self.input.LA(1) <= IN) or (ISNULL <= self.input.LA(1) <= BETWEEN) or (LIKE <= self.input.LA(1) <= MATCH) or self.input.LA(1) == COLLATE or (DISTINCT <= self.input.LA(1) <= THEN) or (CURRENT_TIME <= self.input.LA(1) <= CURRENT_TIMESTAMP) or (RAISE <= self.input.LA(1) <= EXISTS) or (PRIMARY <= self.input.LA(1) <= ADD) or (VIEW <= self.input.LA(1) <= ROW):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set503))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "keyword_column_def"


    # Delegated rules


    # lookup tables for DFA #1

    DFA1_eot = DFA.unpack(
        u"\26\uffff"
        )

    DFA1_eof = DFA.unpack(
        u"\1\1\25\uffff"
        )

    DFA1_min = DFA.unpack(
        u"\1\45\25\uffff"
        )

    DFA1_max = DFA.unpack(
        u"\1\u00aa\25\uffff"
        )

    DFA1_accept = DFA.unpack(
        u"\1\uffff\1\2\1\1\23\uffff"
        )

    DFA1_special = DFA.unpack(
        u"\26\uffff"
        )

            
    DFA1_transition = [
        DFA.unpack(u"\1\2\60\uffff\1\2\16\uffff\1\2\2\uffff\2\2\1\uffff\5"
        u"\2\11\uffff\1\2\14\uffff\1\2\3\uffff\1\2\1\uffff\2\2\4\uffff\1"
        u"\2\1\uffff\2\2\1\uffff\1\2\21\uffff\2\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #1

    class DFA1(DFA):
        pass


    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\25\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\25\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\1\45\24\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\u00aa\24\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\22\uffff"
        )

    DFA5_special = DFA.unpack(
        u"\25\uffff"
        )

            
    DFA5_transition = [
        DFA.unpack(u"\1\1\60\uffff\1\2\16\uffff\1\2\2\uffff\2\2\1\uffff\5"
        u"\2\11\uffff\1\2\14\uffff\1\2\3\uffff\1\2\1\uffff\2\2\4\uffff\1"
        u"\2\1\uffff\2\2\1\uffff\1\2\21\uffff\2\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    class DFA5(DFA):
        pass


    # lookup tables for DFA #4

    DFA4_eot = DFA.unpack(
        u"\25\uffff"
        )

    DFA4_eof = DFA.unpack(
        u"\25\uffff"
        )

    DFA4_min = DFA.unpack(
        u"\1\46\24\uffff"
        )

    DFA4_max = DFA.unpack(
        u"\1\u00aa\24\uffff"
        )

    DFA4_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\22\uffff"
        )

    DFA4_special = DFA.unpack(
        u"\25\uffff"
        )

            
    DFA4_transition = [
        DFA.unpack(u"\1\1\57\uffff\1\2\16\uffff\1\2\2\uffff\2\2\1\uffff\5"
        u"\2\11\uffff\1\2\14\uffff\1\2\3\uffff\1\2\1\uffff\2\2\4\uffff\1"
        u"\2\1\uffff\2\2\1\uffff\1\2\21\uffff\2\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #4

    class DFA4(DFA):
        pass


    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\42\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\42\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\126\20\uffff\1\u0098\1\u0099\4\uffff\1\u0099\12\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\1\u00aa\20\uffff\2\u00b0\4\uffff\1\u00b0\12\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\uffff\1\11\1\12\1\13"
        u"\1\14\1\15\1\16\1\17\2\uffff\1\23\1\20\1\26\2\uffff\1\24\1\21\1"
        u"\30\1\22\1\25\1\27\1\31\3\uffff"
        )

    DFA6_special = DFA.unpack(
        u"\42\uffff"
        )

            
    DFA6_transition = [
        DFA.unpack(u"\1\15\16\uffff\1\16\2\uffff\1\1\1\2\1\uffff\1\3\1\4"
        u"\1\5\1\6\1\10\11\uffff\1\7\14\uffff\1\10\3\uffff\1\12\1\uffff\1"
        u"\13\1\14\4\uffff\1\15\1\uffff\1\17\1\20\1\uffff\1\21\21\uffff\1"
        u"\22\1\23"),
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
        DFA.unpack(u"\1\24\1\31\1\27\6\uffff\1\25\14\uffff\1\30\1\25\1\32"),
        DFA.unpack(u"\1\33\24\uffff\1\34\1\35\1\36"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\24\uffff\1\30\1\uffff\1\32"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #6

    class DFA6(DFA):
        pass


    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\25\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\1\uffff\2\4\22\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\1\45\2\44\22\uffff"
        )

    DFA8_max = DFA.unpack(
        u"\1\u00b7\2\u008b\22\uffff"
        )

    DFA8_accept = DFA.unpack(
        u"\3\uffff\1\1\1\2\20\uffff"
        )

    DFA8_special = DFA.unpack(
        u"\25\uffff"
        )

            
    DFA8_transition = [
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\1"
        u"\2\1\1\10\2\2\uffff\1\1\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\1\4\3\uffff\1\3\1\4\1\uffff\1\4\106\uffff\2\4\7\uffff"
        u"\1\4\17\uffff\1\4"),
        DFA.unpack(u"\1\4\3\uffff\1\3\1\4\1\uffff\1\4\106\uffff\2\4\7\uffff"
        u"\1\4\17\uffff\1\4"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #8

    class DFA8(DFA):
        pass


    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\142\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\1\1\34\uffff\1\1\104\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\44\34\uffff\1\44\21\uffff\1\45\2\uffff\1\45\6\50\51\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\1\u00b7\34\uffff\1\u00b7\21\uffff\1\u00b7\2\uffff\1\u00b7\1\52"
        u"\3\171\1\52\1\131\51\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\1\uffff\1\2\35\uffff\1\1\102\uffff"
        )

    DFA10_special = DFA.unpack(
        u"\142\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\4\1\1\uffff\2\1\1\uffff\1\35\2\1\2\uffff\2\1\3\uffff"
        u"\3\1\26\uffff\12\1\2\uffff\1\1\1\uffff\3\1\3\uffff\125\1"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\1\3\37\1\uffff\6\37\1\uffff\1\37\2\1\3\uffff\3\37"
        u"\17\uffff\2\37\4\uffff\44\37\1\67\1\70\1\37\1\64\1\37\1\65\1\66"
        u"\1\37\1\57\1\62\1\63\73\37"),
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
        DFA.unpack(u"\3\1\1\37\2\1\1\uffff\3\1\1\uffff\1\1\5\uffff\3\1\26"
        u"\uffff\12\1\2\uffff\1\1\1\uffff\3\1\3\uffff\125\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\1\1\37\6\1\1\uffff\1\1\5\uffff\3\1\17\uffff\2\1"
        u"\4\uffff\152\1"),
        DFA.unpack(u"\1\37\1\uffff\1\1"),
        DFA.unpack(u"\1\37\115\uffff\1\1\2\uffff\1\1"),
        DFA.unpack(u"\1\37\120\uffff\1\1"),
        DFA.unpack(u"\1\37\120\uffff\1\1"),
        DFA.unpack(u"\1\37\1\uffff\1\1"),
        DFA.unpack(u"\1\37\60\uffff\1\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


    # lookup tables for DFA #11

    DFA11_eot = DFA.unpack(
        u"\143\uffff"
        )

    DFA11_eof = DFA.unpack(
        u"\1\1\35\uffff\1\1\104\uffff"
        )

    DFA11_min = DFA.unpack(
        u"\1\44\35\uffff\1\44\21\uffff\1\45\2\uffff\1\45\6\50\51\uffff"
        )

    DFA11_max = DFA.unpack(
        u"\1\u00b7\35\uffff\1\u00b7\21\uffff\1\u00b7\2\uffff\1\u00b7\1\52"
        u"\3\171\1\52\1\131\51\uffff"
        )

    DFA11_accept = DFA.unpack(
        u"\1\uffff\1\2\36\uffff\1\1\102\uffff"
        )

    DFA11_special = DFA.unpack(
        u"\143\uffff"
        )

            
    DFA11_transition = [
        DFA.unpack(u"\4\1\1\uffff\2\1\1\uffff\1\1\1\36\1\1\2\uffff\2\1\3"
        u"\uffff\3\1\26\uffff\12\1\2\uffff\1\1\1\uffff\3\1\3\uffff\125\1"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\1\3\40\1\uffff\6\40\1\uffff\1\40\2\1\3\uffff\3\40"
        u"\17\uffff\2\40\4\uffff\44\40\1\70\1\71\1\40\1\65\1\40\1\66\1\67"
        u"\1\40\1\60\1\63\1\64\73\40"),
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
        DFA.unpack(u"\3\1\1\40\2\1\1\uffff\3\1\1\uffff\1\1\5\uffff\3\1\26"
        u"\uffff\12\1\2\uffff\1\1\1\uffff\3\1\3\uffff\125\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\1\1\40\6\1\1\uffff\1\1\5\uffff\3\1\17\uffff\2\1"
        u"\4\uffff\152\1"),
        DFA.unpack(u"\1\40\1\uffff\1\1"),
        DFA.unpack(u"\1\40\115\uffff\1\1\2\uffff\1\1"),
        DFA.unpack(u"\1\40\120\uffff\1\1"),
        DFA.unpack(u"\1\40\120\uffff\1\1"),
        DFA.unpack(u"\1\40\1\uffff\1\1"),
        DFA.unpack(u"\1\40\60\uffff\1\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #11

    class DFA11(DFA):
        pass


    # lookup tables for DFA #12

    DFA12_eot = DFA.unpack(
        u"\172\uffff"
        )

    DFA12_eof = DFA.unpack(
        u"\1\12\6\uffff\2\12\161\uffff"
        )

    DFA12_min = DFA.unpack(
        u"\1\44\6\uffff\2\44\57\uffff\2\45\6\50\72\uffff"
        )

    DFA12_max = DFA.unpack(
        u"\1\u00b7\6\uffff\1\174\1\u00b7\57\uffff\2\u00b7\1\52\3\171\1\52"
        u"\1\131\72\uffff"
        )

    DFA12_accept = DFA.unpack(
        u"\1\uffff\1\1\10\uffff\1\2\157\uffff"
        )

    DFA12_special = DFA.unpack(
        u"\172\uffff"
        )

            
    DFA12_transition = [
        DFA.unpack(u"\4\12\1\uffff\2\12\1\1\3\12\1\1\1\uffff\2\12\3\1\1\7"
        u"\1\12\1\10\7\1\17\uffff\12\12\2\uffff\1\12\1\uffff\3\12\3\uffff"
        u"\125\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\6\uffff\1\1\5\uffff\2\12\4\uffff\1\1\72\uffff"
        u"\2\12\1\uffff\1\12\1\uffff\2\12\1\uffff\3\12"),
        DFA.unpack(u"\1\12\3\1\1\uffff\6\1\1\uffff\1\1\2\12\3\uffff\3\1"
        u"\17\uffff\2\1\4\uffff\44\1\1\76\1\77\1\1\1\73\1\1\1\74\1\75\1\1"
        u"\1\70\1\71\1\72\73\1"),
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
        DFA.unpack(u""),
        DFA.unpack(u"\3\12\1\1\2\12\1\uffff\3\12\1\uffff\1\12\5\uffff\3"
        u"\12\26\uffff\12\12\2\uffff\1\12\1\uffff\3\12\3\uffff\125\12"),
        DFA.unpack(u"\3\12\1\1\6\12\1\uffff\1\12\5\uffff\3\12\17\uffff\2"
        u"\12\4\uffff\152\12"),
        DFA.unpack(u"\1\1\1\uffff\1\12"),
        DFA.unpack(u"\1\1\115\uffff\1\12\2\uffff\1\12"),
        DFA.unpack(u"\1\1\120\uffff\1\12"),
        DFA.unpack(u"\1\1\120\uffff\1\12"),
        DFA.unpack(u"\1\1\1\uffff\1\12"),
        DFA.unpack(u"\1\1\60\uffff\1\12"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #12

    class DFA12(DFA):
        pass


    # lookup tables for DFA #26

    DFA26_eot = DFA.unpack(
        u"\u00a3\uffff"
        )

    DFA26_eof = DFA.unpack(
        u"\u00a3\uffff"
        )

    DFA26_min = DFA.unpack(
        u"\1\53\1\57\1\uffff\2\45\2\uffff\1\53\3\uffff\1\45\3\uffff\1\45"
        u"\2\uffff\1\45\22\uffff\2\45\22\uffff\1\45\3\uffff\1\45\145\uffff"
        )

    DFA26_max = DFA.unpack(
        u"\2\77\1\uffff\2\u00b7\2\uffff\1\67\3\uffff\1\u00b7\3\uffff\1\u00b7"
        u"\2\uffff\1\u00b7\22\uffff\2\u00b7\22\uffff\1\u00b7\3\uffff\1\u00b7"
        u"\145\uffff"
        )

    DFA26_accept = DFA.unpack(
        u"\2\uffff\1\1\2\uffff\1\6\2\uffff\1\10\1\11\4\uffff\1\5\1\uffff"
        u"\1\3\30\uffff\1\2\22\uffff\1\4\24\uffff\1\6\1\7\40\uffff\1\2\57"
        u"\uffff"
        )

    DFA26_special = DFA.unpack(
        u"\u00a3\uffff"
        )

            
    DFA26_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\3\3\uffff\1\4\2\5\1\7\1\uffff\1\10\3"
        u"\11\4\2"),
        DFA.unpack(u"\1\13\3\uffff\1\16\3\uffff\1\5\1\10\3\uffff\4\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\3\20\1\uffff\2\20\1\uffff\3\20\1\uffff\1\17\5\uffff"
        u"\3\20\26\uffff\12\20\2\uffff\1\20\1\uffff\3\20\3\uffff\125\20"),
        DFA.unpack(u"\3\11\1\uffff\6\11\1\uffff\1\22\5\uffff\3\11\17\uffff"
        u"\2\11\4\uffff\152\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\45\13\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\20\1\uffff\2\20\1\uffff\3\20\1\uffff\1\46\5\uffff"
        u"\3\20\26\uffff\12\20\2\uffff\1\20\1\uffff\3\20\3\uffff\125\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\51\1\uffff\6\51\1\uffff\1\51\1\uffff\1\74\3\uffff"
        u"\3\51\17\uffff\2\51\4\uffff\53\51\1\71\76\51"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\11\1\uffff\6\11\1\uffff\1\11\1\uffff\1\16\3\uffff"
        u"\3\11\17\uffff\2\11\4\uffff\53\11\1\75\76\11"),
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
        DFA.unpack(u"\3\122\1\uffff\6\122\1\uffff\1\122\5\uffff\1\122\1"
        u"\121\1\122\17\uffff\2\122\4\uffff\152\122"),
        DFA.unpack(u"\3\51\1\uffff\6\51\1\uffff\1\51\1\uffff\1\74\3\uffff"
        u"\3\51\17\uffff\2\51\4\uffff\53\51\1\163\76\51"),
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
        DFA.unpack(u"\3\74\1\51\6\74\1\uffff\1\74\5\uffff\3\74\17\uffff"
        u"\3\74\3\uffff\152\74"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\16\1\11\6\16\1\uffff\1\16\5\uffff\3\16\17\uffff"
        u"\3\16\3\uffff\152\16"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #26

    class DFA26(DFA):
        pass


    # lookup tables for DFA #14

    DFA14_eot = DFA.unpack(
        u"\144\uffff"
        )

    DFA14_eof = DFA.unpack(
        u"\2\2\142\uffff"
        )

    DFA14_min = DFA.unpack(
        u"\2\44\57\uffff\1\45\2\uffff\1\45\6\50\51\uffff"
        )

    DFA14_max = DFA.unpack(
        u"\2\u00b7\57\uffff\1\u00b7\2\uffff\1\u00b7\1\52\3\171\1\52\1\131"
        u"\51\uffff"
        )

    DFA14_accept = DFA.unpack(
        u"\2\uffff\1\2\36\uffff\1\1\102\uffff"
        )

    DFA14_special = DFA.unpack(
        u"\144\uffff"
        )

            
    DFA14_transition = [
        DFA.unpack(u"\4\2\1\uffff\2\2\1\uffff\2\2\1\1\2\uffff\2\2\3\uffff"
        u"\3\2\26\uffff\12\2\2\uffff\1\2\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\1\2\3\41\1\uffff\6\41\1\uffff\1\41\2\2\3\uffff\3\41"
        u"\17\uffff\2\41\4\uffff\44\41\1\71\1\72\1\41\1\66\1\41\1\67\1\70"
        u"\1\41\1\61\1\64\1\65\73\41"),
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
        DFA.unpack(u""),
        DFA.unpack(u"\3\2\1\41\2\2\1\uffff\3\2\1\uffff\1\2\5\uffff\3\2\26"
        u"\uffff\12\2\2\uffff\1\2\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\2\1\41\6\2\1\uffff\1\2\5\uffff\3\2\17\uffff\2\2"
        u"\4\uffff\152\2"),
        DFA.unpack(u"\1\41\1\uffff\1\2"),
        DFA.unpack(u"\1\41\115\uffff\1\2\2\uffff\1\2"),
        DFA.unpack(u"\1\41\120\uffff\1\2"),
        DFA.unpack(u"\1\41\120\uffff\1\2"),
        DFA.unpack(u"\1\41\1\uffff\1\2"),
        DFA.unpack(u"\1\41\60\uffff\1\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #14

    class DFA14(DFA):
        pass


    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\103\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\1\uffff\2\4\100\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\1\45\2\44\100\uffff"
        )

    DFA18_max = DFA.unpack(
        u"\3\u00b7\100\uffff"
        )

    DFA18_accept = DFA.unpack(
        u"\3\uffff\1\1\1\2\76\uffff"
        )

    DFA18_special = DFA.unpack(
        u"\103\uffff"
        )

            
    DFA18_transition = [
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\1"
        u"\2\1\1\10\2\2\uffff\1\1\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\4\4\1\3\2\4\1\uffff\3\4\2\uffff\2\4\3\uffff\3\4\26"
        u"\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u"\4\4\1\3\2\4\1\uffff\3\4\2\uffff\2\4\3\uffff\3\4\26"
        u"\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #18

    class DFA18(DFA):
        pass


    # lookup tables for DFA #25

    DFA25_eot = DFA.unpack(
        u"\41\uffff"
        )

    DFA25_eof = DFA.unpack(
        u"\1\1\40\uffff"
        )

    DFA25_min = DFA.unpack(
        u"\1\44\40\uffff"
        )

    DFA25_max = DFA.unpack(
        u"\1\u00b7\40\uffff"
        )

    DFA25_accept = DFA.unpack(
        u"\1\uffff\1\2\36\uffff\1\1"
        )

    DFA25_special = DFA.unpack(
        u"\41\uffff"
        )

            
    DFA25_transition = [
        DFA.unpack(u"\4\1\1\uffff\2\1\1\uffff\3\1\2\uffff\2\1\1\40\2\uffff"
        u"\3\1\3\40\23\uffff\12\1\2\uffff\1\1\1\uffff\3\1\3\uffff\125\1"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #25

    class DFA25(DFA):
        pass


    # lookup tables for DFA #27

    DFA27_eot = DFA.unpack(
        u"\53\uffff"
        )

    DFA27_eof = DFA.unpack(
        u"\1\1\52\uffff"
        )

    DFA27_min = DFA.unpack(
        u"\1\44\52\uffff"
        )

    DFA27_max = DFA.unpack(
        u"\1\u00b7\52\uffff"
        )

    DFA27_accept = DFA.unpack(
        u"\1\uffff\1\2\50\uffff\1\1"
        )

    DFA27_special = DFA.unpack(
        u"\53\uffff"
        )

            
    DFA27_transition = [
        DFA.unpack(u"\4\1\1\uffff\7\1\1\uffff\17\1\4\52\13\uffff\12\1\2\uffff"
        u"\1\1\1\uffff\3\1\3\uffff\125\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #27

    class DFA27(DFA):
        pass


    # lookup tables for DFA #28

    DFA28_eot = DFA.unpack(
        u"\54\uffff"
        )

    DFA28_eof = DFA.unpack(
        u"\1\1\53\uffff"
        )

    DFA28_min = DFA.unpack(
        u"\1\44\53\uffff"
        )

    DFA28_max = DFA.unpack(
        u"\1\u00b7\53\uffff"
        )

    DFA28_accept = DFA.unpack(
        u"\1\uffff\1\2\51\uffff\1\1"
        )

    DFA28_special = DFA.unpack(
        u"\54\uffff"
        )

            
    DFA28_transition = [
        DFA.unpack(u"\4\1\1\uffff\7\1\1\uffff\23\1\4\53\7\uffff\12\1\2\uffff"
        u"\1\1\1\uffff\3\1\3\uffff\125\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #28

    class DFA28(DFA):
        pass


    # lookup tables for DFA #29

    DFA29_eot = DFA.unpack(
        u"\55\uffff"
        )

    DFA29_eof = DFA.unpack(
        u"\1\1\54\uffff"
        )

    DFA29_min = DFA.unpack(
        u"\1\44\54\uffff"
        )

    DFA29_max = DFA.unpack(
        u"\1\u00b7\54\uffff"
        )

    DFA29_accept = DFA.unpack(
        u"\1\uffff\1\2\52\uffff\1\1"
        )

    DFA29_special = DFA.unpack(
        u"\55\uffff"
        )

            
    DFA29_transition = [
        DFA.unpack(u"\4\1\1\uffff\7\1\1\uffff\27\1\2\54\5\uffff\12\1\2\uffff"
        u"\1\1\1\uffff\3\1\3\uffff\125\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #29

    class DFA29(DFA):
        pass


    # lookup tables for DFA #30

    DFA30_eot = DFA.unpack(
        u"\56\uffff"
        )

    DFA30_eof = DFA.unpack(
        u"\1\1\55\uffff"
        )

    DFA30_min = DFA.unpack(
        u"\1\44\55\uffff"
        )

    DFA30_max = DFA.unpack(
        u"\1\u00b7\55\uffff"
        )

    DFA30_accept = DFA.unpack(
        u"\1\uffff\1\2\53\uffff\1\1"
        )

    DFA30_special = DFA.unpack(
        u"\56\uffff"
        )

            
    DFA30_transition = [
        DFA.unpack(u"\4\1\1\uffff\7\1\1\uffff\31\1\3\55\2\uffff\12\1\2\uffff"
        u"\1\1\1\uffff\3\1\3\uffff\125\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #30

    class DFA30(DFA):
        pass


    # lookup tables for DFA #31

    DFA31_eot = DFA.unpack(
        u"\57\uffff"
        )

    DFA31_eof = DFA.unpack(
        u"\1\1\56\uffff"
        )

    DFA31_min = DFA.unpack(
        u"\1\44\56\uffff"
        )

    DFA31_max = DFA.unpack(
        u"\1\u00b7\56\uffff"
        )

    DFA31_accept = DFA.unpack(
        u"\1\uffff\1\2\54\uffff\1\1"
        )

    DFA31_special = DFA.unpack(
        u"\57\uffff"
        )

            
    DFA31_transition = [
        DFA.unpack(u"\4\1\1\uffff\7\1\1\uffff\34\1\1\56\1\uffff\12\1\2\uffff"
        u"\1\1\1\uffff\3\1\3\uffff\125\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #31

    class DFA31(DFA):
        pass


    # lookup tables for DFA #32

    DFA32_eot = DFA.unpack(
        u"\23\uffff"
        )

    DFA32_eof = DFA.unpack(
        u"\23\uffff"
        )

    DFA32_min = DFA.unpack(
        u"\1\45\22\uffff"
        )

    DFA32_max = DFA.unpack(
        u"\1\u00b7\22\uffff"
        )

    DFA32_accept = DFA.unpack(
        u"\1\uffff\1\1\20\uffff\1\2"
        )

    DFA32_special = DFA.unpack(
        u"\23\uffff"
        )

            
    DFA32_transition = [
        DFA.unpack(u"\3\1\1\uffff\2\1\1\22\3\1\1\uffff\1\1\5\uffff\3\1\17"
        u"\uffff\2\22\4\uffff\1\22\151\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #32

    class DFA32(DFA):
        pass


    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack(
        u"\75\uffff"
        )

    DFA33_eof = DFA.unpack(
        u"\2\2\73\uffff"
        )

    DFA33_min = DFA.unpack(
        u"\2\44\73\uffff"
        )

    DFA33_max = DFA.unpack(
        u"\1\u00b7\1\174\73\uffff"
        )

    DFA33_accept = DFA.unpack(
        u"\2\uffff\1\2\55\uffff\1\1\14\uffff"
        )

    DFA33_special = DFA.unpack(
        u"\75\uffff"
        )

            
    DFA33_transition = [
        DFA.unpack(u"\4\2\1\uffff\7\2\1\uffff\35\2\1\uffff\1\1\11\2\2\uffff"
        u"\1\2\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\1\2\14\uffff\2\2\35\uffff\1\60\41\uffff\2\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\3\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #33

    class DFA33(DFA):
        pass


    # lookup tables for DFA #42

    DFA42_eot = DFA.unpack(
        u"\u014b\uffff"
        )

    DFA42_eof = DFA.unpack(
        u"\3\uffff\1\1\1\uffff\4\1\3\uffff\1\21\u013e\uffff"
        )

    DFA42_min = DFA.unpack(
        u"\1\45\2\uffff\1\44\1\uffff\4\44\3\uffff\1\44\1\50\1\uffff\1\45"
        u"\1\50\u013a\uffff"
        )

    DFA42_max = DFA.unpack(
        u"\1\u00b7\2\uffff\1\u00b7\1\uffff\4\u00b7\3\uffff\1\u00b7\1\60\1"
        u"\uffff\1\u00b7\1\60\u013a\uffff"
        )

    DFA42_accept = DFA.unpack(
        u"\1\uffff\1\1\7\uffff\1\2\4\uffff\1\5\2\uffff\1\3\u00f0\uffff\1"
        u"\4\60\uffff\1\6\2\uffff\1\7\22\uffff\1\10\1\uffff"
        )

    DFA42_special = DFA.unpack(
        u"\u014b\uffff"
        )

            
    DFA42_transition = [
        DFA.unpack(u"\3\21\1\uffff\2\21\1\uffff\3\21\1\uffff\1\16\5\uffff"
        u"\1\21\1\5\1\21\26\uffff\1\21\1\14\1\21\1\15\1\21\1\17\4\21\2\1"
        u"\1\3\1\1\1\6\1\7\1\10\3\11\1\20\124\21"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\4\1\1\21\7\1\1\uffff\35\1\1\uffff\12\1\2\uffff\1\1"
        u"\1\uffff\3\1\3\uffff\125\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\4\1\1\21\7\1\1\uffff\35\1\1\uffff\12\1\2\uffff\1\1"
        u"\1\uffff\3\1\3\uffff\125\1"),
        DFA.unpack(u"\4\1\1\21\7\1\1\uffff\35\1\1\uffff\12\1\2\uffff\1\1"
        u"\1\uffff\3\1\3\uffff\125\1"),
        DFA.unpack(u"\4\1\1\21\7\1\1\uffff\35\1\1\uffff\12\1\2\uffff\1\1"
        u"\1\uffff\3\1\3\uffff\125\1"),
        DFA.unpack(u"\4\1\1\21\7\1\1\uffff\35\1\1\uffff\12\1\2\uffff\1\1"
        u"\1\uffff\3\1\3\uffff\125\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\14\21\1\u0102\35\21\1\uffff\12\21\2\uffff\1\21\1\uffff"
        u"\3\21\3\uffff\125\21"),
        DFA.unpack(u"\1\21\7\uffff\1\u0133"),
        DFA.unpack(u""),
        DFA.unpack(u"\3\u0136\1\21\6\u0136\1\uffff\1\u0136\5\uffff\3\u0136"
        u"\17\uffff\2\u0136\4\uffff\152\u0136"),
        DFA.unpack(u"\1\21\7\uffff\1\u0149"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #42

    class DFA42(DFA):
        pass


    # lookup tables for DFA #35

    DFA35_eot = DFA.unpack(
        u"\64\uffff"
        )

    DFA35_eof = DFA.unpack(
        u"\1\uffff\1\5\62\uffff"
        )

    DFA35_min = DFA.unpack(
        u"\1\45\1\44\62\uffff"
        )

    DFA35_max = DFA.unpack(
        u"\2\u00b7\62\uffff"
        )

    DFA35_accept = DFA.unpack(
        u"\2\uffff\1\1\2\uffff\1\2\56\uffff"
        )

    DFA35_special = DFA.unpack(
        u"\64\uffff"
        )

            
    DFA35_transition = [
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\1"
        u"\2\1\1\10\2\2\uffff\1\2\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\4\5\1\2\7\5\1\uffff\35\5\1\uffff\12\5\2\uffff\1\5"
        u"\1\uffff\3\5\3\uffff\125\5"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #35

    class DFA35(DFA):
        pass


    # lookup tables for DFA #34

    DFA34_eot = DFA.unpack(
        u"\153\uffff"
        )

    DFA34_eof = DFA.unpack(
        u"\5\uffff\1\14\2\uffff\1\14\142\uffff"
        )

    DFA34_min = DFA.unpack(
        u"\1\45\2\50\2\45\1\44\2\uffff\1\44\142\uffff"
        )

    DFA34_max = DFA.unpack(
        u"\1\u00b7\2\50\3\u00b7\2\uffff\1\u00b7\142\uffff"
        )

    DFA34_accept = DFA.unpack(
        u"\6\uffff\1\1\5\uffff\1\2\136\uffff"
        )

    DFA34_special = DFA.unpack(
        u"\153\uffff"
        )

            
    DFA34_transition = [
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\1"
        u"\2\1\1\10\2\2\uffff\1\1\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4"),
        DFA.unpack(u"\3\6\1\uffff\2\6\1\uffff\3\6\7\uffff\3\6\26\uffff\1"
        u"\6\1\5\10\6\2\uffff\1\6\1\uffff\3\6\3\uffff\125\6"),
        DFA.unpack(u"\3\6\1\uffff\2\6\1\uffff\3\6\7\uffff\3\6\26\uffff\1"
        u"\6\1\10\10\6\2\uffff\1\6\1\uffff\3\6\3\uffff\125\6"),
        DFA.unpack(u"\4\14\1\6\7\14\1\uffff\35\14\1\uffff\12\14\2\uffff"
        u"\1\14\1\uffff\3\14\3\uffff\125\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\4\14\1\6\7\14\1\uffff\35\14\1\uffff\12\14\2\uffff"
        u"\1\14\1\uffff\3\14\3\uffff\125\14"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #34

    class DFA34(DFA):
        pass


    # lookup tables for DFA #38

    DFA38_eot = DFA.unpack(
        u"\26\uffff"
        )

    DFA38_eof = DFA.unpack(
        u"\26\uffff"
        )

    DFA38_min = DFA.unpack(
        u"\1\45\25\uffff"
        )

    DFA38_max = DFA.unpack(
        u"\1\u00b7\25\uffff"
        )

    DFA38_accept = DFA.unpack(
        u"\1\uffff\1\1\22\uffff\1\2\1\3"
        )

    DFA38_special = DFA.unpack(
        u"\26\uffff"
        )

            
    DFA38_transition = [
        DFA.unpack(u"\3\1\1\uffff\6\1\1\uffff\1\1\1\uffff\1\25\3\uffff\3"
        u"\1\17\uffff\2\1\1\24\3\uffff\152\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #38

    class DFA38(DFA):
        pass


    # lookup tables for DFA #36

    DFA36_eot = DFA.unpack(
        u"\47\uffff"
        )

    DFA36_eof = DFA.unpack(
        u"\47\uffff"
        )

    DFA36_min = DFA.unpack(
        u"\2\45\45\uffff"
        )

    DFA36_max = DFA.unpack(
        u"\2\u00b7\45\uffff"
        )

    DFA36_accept = DFA.unpack(
        u"\2\uffff\1\2\22\uffff\1\1\21\uffff"
        )

    DFA36_special = DFA.unpack(
        u"\47\uffff"
        )

            
    DFA36_transition = [
        DFA.unpack(u"\3\2\1\uffff\6\2\1\uffff\1\2\5\uffff\3\2\17\uffff\2"
        u"\2\4\uffff\3\2\1\1\146\2"),
        DFA.unpack(u"\3\25\1\2\6\25\1\uffff\1\25\5\uffff\3\25\17\uffff\2"
        u"\25\4\uffff\152\25"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #36

    class DFA36(DFA):
        pass


    # lookup tables for DFA #39

    DFA39_eot = DFA.unpack(
        u"\47\uffff"
        )

    DFA39_eof = DFA.unpack(
        u"\47\uffff"
        )

    DFA39_min = DFA.unpack(
        u"\1\45\20\uffff\1\45\25\uffff"
        )

    DFA39_max = DFA.unpack(
        u"\1\u00b7\20\uffff\1\u00b7\25\uffff"
        )

    DFA39_accept = DFA.unpack(
        u"\1\uffff\1\1\22\uffff\1\2\22\uffff"
        )

    DFA39_special = DFA.unpack(
        u"\47\uffff"
        )

            
    DFA39_transition = [
        DFA.unpack(u"\3\1\1\uffff\6\1\1\uffff\1\1\5\uffff\3\1\17\uffff\2"
        u"\1\4\uffff\11\1\1\21\140\1"),
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
        DFA.unpack(u"\3\24\1\1\6\24\1\uffff\1\24\5\uffff\3\24\17\uffff\2"
        u"\24\4\uffff\152\24"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #39

    class DFA39(DFA):
        pass


    # lookup tables for DFA #44

    DFA44_eot = DFA.unpack(
        u"\64\uffff"
        )

    DFA44_eof = DFA.unpack(
        u"\1\uffff\1\5\62\uffff"
        )

    DFA44_min = DFA.unpack(
        u"\1\140\1\44\62\uffff"
        )

    DFA44_max = DFA.unpack(
        u"\1\142\1\u00b7\62\uffff"
        )

    DFA44_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\2\1\1\56\uffff"
        )

    DFA44_special = DFA.unpack(
        u"\64\uffff"
        )

            
    DFA44_transition = [
        DFA.unpack(u"\1\1\1\2\1\3"),
        DFA.unpack(u"\4\5\1\uffff\7\5\1\uffff\35\5\1\uffff\12\5\1\4\1\uffff"
        u"\1\5\1\uffff\3\5\3\uffff\125\5"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #44

    class DFA44(DFA):
        pass


    # lookup tables for DFA #46

    DFA46_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA46_eof = DFA.unpack(
        u"\1\1\20\uffff"
        )

    DFA46_min = DFA.unpack(
        u"\1\44\20\uffff"
        )

    DFA46_max = DFA.unpack(
        u"\1\u00a4\20\uffff"
        )

    DFA46_accept = DFA.unpack(
        u"\1\uffff\1\2\16\uffff\1\1"
        )

    DFA46_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA46_transition = [
        DFA.unpack(u"\1\1\6\uffff\1\1\4\uffff\3\1\4\uffff\1\1\27\uffff\1"
        u"\1\1\20\70\uffff\1\1\23\uffff\2\1\2\uffff\4\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #46

    class DFA46(DFA):
        pass


    # lookup tables for DFA #48

    DFA48_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA48_eof = DFA.unpack(
        u"\1\2\17\uffff"
        )

    DFA48_min = DFA.unpack(
        u"\1\44\17\uffff"
        )

    DFA48_max = DFA.unpack(
        u"\1\u00a4\17\uffff"
        )

    DFA48_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\15\uffff"
        )

    DFA48_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA48_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\2\4\uffff\1\1\2\2\4\uffff\1\2\27\uffff"
        u"\1\2\71\uffff\1\2\23\uffff\2\2\2\uffff\4\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #48

    class DFA48(DFA):
        pass


    # lookup tables for DFA #50

    DFA50_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA50_eof = DFA.unpack(
        u"\1\uffff\2\4\12\uffff"
        )

    DFA50_min = DFA.unpack(
        u"\1\45\2\44\12\uffff"
        )

    DFA50_max = DFA.unpack(
        u"\1\u00b7\2\63\12\uffff"
        )

    DFA50_accept = DFA.unpack(
        u"\3\uffff\1\1\1\2\10\uffff"
        )

    DFA50_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA50_transition = [
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\1"
        u"\2\1\1\10\2\2\uffff\1\1\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\1\4\3\uffff\1\3\7\uffff\1\4\2\uffff\1\4"),
        DFA.unpack(u"\1\4\3\uffff\1\3\7\uffff\1\4\2\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #50

    class DFA50(DFA):
        pass


    # lookup tables for DFA #53

    DFA53_eot = DFA.unpack(
        u"\16\uffff"
        )

    DFA53_eof = DFA.unpack(
        u"\10\uffff\1\2\5\uffff"
        )

    DFA53_min = DFA.unpack(
        u"\2\45\3\uffff\1\45\2\uffff\1\44\5\uffff"
        )

    DFA53_max = DFA.unpack(
        u"\2\u00b7\3\uffff\1\u00b7\2\uffff\1\u00b7\5\uffff"
        )

    DFA53_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1\11\uffff"
        )

    DFA53_special = DFA.unpack(
        u"\16\uffff"
        )

            
    DFA53_transition = [
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\12"
        u"\2\2\uffff\1\2\1\uffff\3\2\3\uffff\7\2\1\1\115\2"),
        DFA.unpack(u"\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\26\uffff\4"
        u"\4\1\5\5\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\4"
        u"\2\1\10\5\2\2\uffff\1\2\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\26\uffff"
        u"\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #53

    class DFA53(DFA):
        pass


    # lookup tables for DFA #55

    DFA55_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA55_eof = DFA.unpack(
        u"\1\3\2\5\10\uffff"
        )

    DFA55_min = DFA.unpack(
        u"\3\44\10\uffff"
        )

    DFA55_max = DFA.unpack(
        u"\1\u00b7\2\50\10\uffff"
        )

    DFA55_accept = DFA.unpack(
        u"\3\uffff\1\3\1\uffff\1\1\1\uffff\1\2\3\uffff"
        )

    DFA55_special = DFA.unpack(
        u"\13\uffff"
        )

            
    DFA55_transition = [
        DFA.unpack(u"\1\3\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff"
        u"\1\2\1\1\10\2\2\uffff\1\1\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\1\5\3\uffff\1\7"),
        DFA.unpack(u"\1\5\3\uffff\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #55

    class DFA55(DFA):
        pass


    # lookup tables for DFA #57

    DFA57_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA57_eof = DFA.unpack(
        u"\1\3\14\uffff"
        )

    DFA57_min = DFA.unpack(
        u"\1\44\14\uffff"
        )

    DFA57_max = DFA.unpack(
        u"\1\175\14\uffff"
        )

    DFA57_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\11\uffff"
        )

    DFA57_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA57_transition = [
        DFA.unpack(u"\1\3\14\uffff\2\3\75\uffff\1\1\1\2\2\3\1\uffff\1\3\1"
        u"\uffff\2\3\4\uffff\1\3"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #57

    class DFA57(DFA):
        pass


    # lookup tables for DFA #69

    DFA69_eot = DFA.unpack(
        u"\76\uffff"
        )

    DFA69_eof = DFA.unpack(
        u"\76\uffff"
        )

    DFA69_min = DFA.unpack(
        u"\3\45\73\uffff"
        )

    DFA69_max = DFA.unpack(
        u"\3\u00b7\73\uffff"
        )

    DFA69_accept = DFA.unpack(
        u"\3\uffff\1\3\23\uffff\1\1\23\uffff\1\2\22\uffff"
        )

    DFA69_special = DFA.unpack(
        u"\76\uffff"
        )

            
    DFA69_transition = [
        DFA.unpack(u"\3\3\1\uffff\6\3\1\uffff\1\3\5\uffff\3\3\17\uffff\3"
        u"\3\3\uffff\3\3\1\2\44\3\1\1\101\3"),
        DFA.unpack(u"\3\27\1\3\6\27\1\uffff\1\27\5\uffff\3\27\17\uffff\3"
        u"\27\3\uffff\152\27"),
        DFA.unpack(u"\3\53\1\3\6\53\1\uffff\1\53\5\uffff\3\53\17\uffff\3"
        u"\53\3\uffff\152\53"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #69

    class DFA69(DFA):
        pass


    # lookup tables for DFA #70

    DFA70_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA70_eof = DFA.unpack(
        u"\1\1\14\uffff"
        )

    DFA70_min = DFA.unpack(
        u"\1\44\14\uffff"
        )

    DFA70_max = DFA.unpack(
        u"\1\174\14\uffff"
        )

    DFA70_accept = DFA.unpack(
        u"\1\uffff\1\2\12\uffff\1\1"
        )

    DFA70_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA70_transition = [
        DFA.unpack(u"\1\1\14\uffff\1\14\1\1\77\uffff\2\1\1\uffff\1\1\1\uffff"
        u"\2\1\1\uffff\3\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #70

    class DFA70(DFA):
        pass


    # lookup tables for DFA #71

    DFA71_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA71_eof = DFA.unpack(
        u"\1\2\13\uffff"
        )

    DFA71_min = DFA.unpack(
        u"\1\44\13\uffff"
        )

    DFA71_max = DFA.unpack(
        u"\1\174\13\uffff"
        )

    DFA71_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\11\uffff"
        )

    DFA71_special = DFA.unpack(
        u"\14\uffff"
        )

            
    DFA71_transition = [
        DFA.unpack(u"\1\2\15\uffff\1\2\77\uffff\2\2\1\uffff\1\2\1\uffff\2"
        u"\2\1\uffff\1\1\2\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #71

    class DFA71(DFA):
        pass


    # lookup tables for DFA #72

    DFA72_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA72_eof = DFA.unpack(
        u"\1\2\12\uffff"
        )

    DFA72_min = DFA.unpack(
        u"\1\44\12\uffff"
        )

    DFA72_max = DFA.unpack(
        u"\1\174\12\uffff"
        )

    DFA72_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\10\uffff"
        )

    DFA72_special = DFA.unpack(
        u"\13\uffff"
        )

            
    DFA72_transition = [
        DFA.unpack(u"\1\2\15\uffff\1\2\77\uffff\2\2\1\uffff\1\2\1\uffff\2"
        u"\2\2\uffff\1\1\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #72

    class DFA72(DFA):
        pass


    # lookup tables for DFA #75

    DFA75_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA75_eof = DFA.unpack(
        u"\1\2\11\uffff"
        )

    DFA75_min = DFA.unpack(
        u"\1\44\11\uffff"
        )

    DFA75_max = DFA.unpack(
        u"\1\174\11\uffff"
        )

    DFA75_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\7\uffff"
        )

    DFA75_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA75_transition = [
        DFA.unpack(u"\1\2\15\uffff\1\2\77\uffff\2\2\1\uffff\1\2\1\uffff\2"
        u"\2\3\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #75

    class DFA75(DFA):
        pass


    # lookup tables for DFA #73

    DFA73_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA73_eof = DFA.unpack(
        u"\1\1\12\uffff"
        )

    DFA73_min = DFA.unpack(
        u"\1\44\12\uffff"
        )

    DFA73_max = DFA.unpack(
        u"\1\175\12\uffff"
        )

    DFA73_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA73_special = DFA.unpack(
        u"\13\uffff"
        )

            
    DFA73_transition = [
        DFA.unpack(u"\1\1\14\uffff\1\12\1\1\77\uffff\2\1\1\uffff\1\1\1\uffff"
        u"\2\1\4\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #73

    class DFA73(DFA):
        pass


    # lookup tables for DFA #74

    DFA74_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA74_eof = DFA.unpack(
        u"\1\2\11\uffff"
        )

    DFA74_min = DFA.unpack(
        u"\1\44\11\uffff"
        )

    DFA74_max = DFA.unpack(
        u"\1\175\11\uffff"
        )

    DFA74_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\7\uffff"
        )

    DFA74_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA74_transition = [
        DFA.unpack(u"\1\2\15\uffff\1\2\77\uffff\2\2\1\uffff\1\2\1\uffff\2"
        u"\2\4\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #74

    class DFA74(DFA):
        pass


    # lookup tables for DFA #78

    DFA78_eot = DFA.unpack(
        u"\u011c\uffff"
        )

    DFA78_eof = DFA.unpack(
        u"\2\uffff\2\4\2\uffff\1\4\1\uffff\3\4\u0111\uffff"
        )

    DFA78_min = DFA.unpack(
        u"\1\45\1\uffff\2\44\2\uffff\1\44\1\uffff\3\44\1\50\4\uffff\1\45"
        u"\2\50\1\uffff\1\45\40\uffff\1\45\41\uffff\1\45\40\uffff\1\45\100"
        u"\uffff\1\45\40\uffff\1\45\1\uffff\2\45\24\uffff\2\45\50\uffff"
        )

    DFA78_max = DFA.unpack(
        u"\1\u00b7\1\uffff\2\u00b7\2\uffff\1\u00b7\1\uffff\3\u00b7\1\60\4"
        u"\uffff\1\u00b7\1\60\1\50\1\uffff\1\u00b7\40\uffff\1\u00b7\41\uffff"
        u"\1\u00b7\40\uffff\1\u00b7\100\uffff\1\u00b7\40\uffff\1\u00b7\1"
        u"\uffff\2\u00b7\24\uffff\2\u00b7\50\uffff"
        )

    DFA78_accept = DFA.unpack(
        u"\1\uffff\1\1\2\uffff\1\3\u00ef\uffff\1\2\47\uffff"
        )

    DFA78_special = DFA.unpack(
        u"\u011c\uffff"
        )

            
    DFA78_transition = [
        DFA.unpack(u"\3\22\1\uffff\2\22\1\4\3\22\1\uffff\1\4\5\uffff\1\22"
        u"\1\3\1\22\17\uffff\2\4\1\1\3\uffff\1\4\1\22\1\6\1\22\1\13\1\22"
        u"\1\20\4\22\2\4\1\2\1\4\1\10\1\11\1\12\3\4\1\21\124\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\4\4\1\24\7\4\1\uffff\35\4\1\uffff\12\4\2\uffff\1\4"
        u"\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u"\4\4\1\65\7\4\1\uffff\35\4\1\uffff\12\4\2\uffff\1\4"
        u"\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\4\4\1\127\45\4\1\uffff\12\4\2\uffff\1\4\1\uffff\3"
        u"\4\3\uffff\125\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\4\4\1\170\7\4\1\uffff\35\4\1\uffff\12\4\2\uffff\1"
        u"\4\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u"\4\4\1\u00b9\7\4\1\uffff\35\4\1\uffff\12\4\2\uffff"
        u"\1\4\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u"\4\4\1\u00da\7\4\1\uffff\35\4\1\uffff\12\4\2\uffff"
        u"\1\4\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u"\1\u00dc\7\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\4\1\u00dd\6\4\1\uffff\1\4\5\uffff\3\4\17\uffff\2"
        u"\4\4\uffff\152\4"),
        DFA.unpack(u"\1\u00f2\7\uffff\1\4"),
        DFA.unpack(u"\1\u00f3"),
        DFA.unpack(u""),
        DFA.unpack(u"\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\21\uffff\1"
        u"\u00f4\4\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\21\uffff\1"
        u"\u00f4\4\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
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
        DFA.unpack(u"\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\21\uffff\1"
        u"\u00f4\4\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\21\uffff\1"
        u"\u00f4\4\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
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
        DFA.unpack(u"\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\21\uffff\1"
        u"\u00f4\4\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\21\uffff\1"
        u"\u00f4\4\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\21\uffff\1"
        u"\u00f4\4\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u"\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\21\uffff\1"
        u"\u00f4\4\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
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
        DFA.unpack(u"\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\21\uffff\1"
        u"\u00f4\4\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u"\3\4\1\uffff\2\4\1\uffff\3\4\7\uffff\3\4\21\uffff\1"
        u"\u00f4\4\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #78

    class DFA78(DFA):
        pass


    # lookup tables for DFA #77

    DFA77_eot = DFA.unpack(
        u"\u00d7\uffff"
        )

    DFA77_eof = DFA.unpack(
        u"\1\4\2\uffff\1\1\1\uffff\7\1\u00cb\uffff"
        )

    DFA77_min = DFA.unpack(
        u"\1\44\2\uffff\1\44\1\uffff\7\44\5\uffff\1\45\3\uffff\1\45\6\50"
        u"\24\uffff\1\45\2\uffff\1\45\6\50\u009d\uffff"
        )

    DFA77_max = DFA.unpack(
        u"\1\u00b7\2\uffff\1\u00b7\1\uffff\1\u00b7\6\174\5\uffff\1\u00b7"
        u"\3\uffff\1\u00b7\1\52\3\171\1\52\1\131\24\uffff\1\u00b7\2\uffff"
        u"\1\u00b7\1\52\3\171\1\52\1\131\u009d\uffff"
        )

    DFA77_accept = DFA.unpack(
        u"\1\uffff\1\1\2\uffff\1\2\u00d2\uffff"
        )

    DFA77_special = DFA.unpack(
        u"\u00d7\uffff"
        )

            
    DFA77_transition = [
        DFA.unpack(u"\1\4\3\1\1\uffff\2\1\1\uffff\3\1\2\uffff\2\4\3\uffff"
        u"\3\1\26\uffff\12\1\2\uffff\1\1\1\uffff\3\1\3\uffff\17\1\1\12\1"
        u"\13\1\1\1\7\1\1\1\10\1\11\1\1\1\3\1\5\1\6\73\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\1\3\4\1\uffff\2\4\1\uffff\3\4\1\uffff\1\4\2\1\3"
        u"\uffff\3\4\26\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\17\4\1"
        u"\32\1\33\1\4\1\27\1\4\1\30\1\31\1\4\1\21\1\25\1\26\73\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\1\3\4\1\uffff\6\4\1\uffff\1\4\2\1\3\uffff\3\4\17"
        u"\uffff\2\4\4\uffff\44\4\1\70\1\71\1\4\1\65\1\4\1\66\1\67\1\4\1"
        u"\60\1\63\1\64\73\4"),
        DFA.unpack(u"\1\1\5\uffff\1\4\6\uffff\2\1\77\uffff\2\1\1\uffff\1"
        u"\1\1\uffff\2\1\1\uffff\3\1"),
        DFA.unpack(u"\1\1\14\uffff\2\1\77\uffff\2\1\1\uffff\1\1\1\4\2\1"
        u"\1\4\3\1"),
        DFA.unpack(u"\1\1\14\uffff\2\1\77\uffff\2\1\1\uffff\1\1\1\uffff"
        u"\2\1\1\4\3\1"),
        DFA.unpack(u"\1\1\14\uffff\2\1\77\uffff\2\1\1\uffff\1\1\1\uffff"
        u"\2\1\1\4\3\1"),
        DFA.unpack(u"\1\1\5\uffff\1\4\6\uffff\2\1\77\uffff\2\1\1\uffff\1"
        u"\1\1\uffff\2\1\1\uffff\3\1"),
        DFA.unpack(u"\1\1\14\uffff\2\1\46\uffff\1\4\30\uffff\2\1\1\uffff"
        u"\1\1\1\uffff\2\1\1\uffff\3\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\1\1\4\2\1\1\uffff\3\1\1\uffff\1\1\5\uffff\3\1\26"
        u"\uffff\12\1\2\uffff\1\1\1\uffff\3\1\3\uffff\125\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\1\1\4\6\1\1\uffff\1\1\5\uffff\3\1\17\uffff\2\1\4"
        u"\uffff\152\1"),
        DFA.unpack(u"\1\4\1\uffff\1\1"),
        DFA.unpack(u"\1\4\115\uffff\1\1\2\uffff\1\1"),
        DFA.unpack(u"\1\4\120\uffff\1\1"),
        DFA.unpack(u"\1\4\120\uffff\1\1"),
        DFA.unpack(u"\1\4\1\uffff\1\1"),
        DFA.unpack(u"\1\4\60\uffff\1\1"),
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
        DFA.unpack(u"\3\1\1\4\2\1\1\uffff\3\1\1\uffff\1\1\5\uffff\3\1\26"
        u"\uffff\12\1\2\uffff\1\1\1\uffff\3\1\3\uffff\125\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\1\1\4\6\1\1\uffff\1\1\5\uffff\3\1\17\uffff\2\1\4"
        u"\uffff\152\1"),
        DFA.unpack(u"\1\4\1\uffff\1\1"),
        DFA.unpack(u"\1\4\115\uffff\1\1\2\uffff\1\1"),
        DFA.unpack(u"\1\4\120\uffff\1\1"),
        DFA.unpack(u"\1\4\120\uffff\1\1"),
        DFA.unpack(u"\1\4\1\uffff\1\1"),
        DFA.unpack(u"\1\4\60\uffff\1\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #77

    class DFA77(DFA):
        pass


    # lookup tables for DFA #76

    DFA76_eot = DFA.unpack(
        u"\u00d9\uffff"
        )

    DFA76_eof = DFA.unpack(
        u"\1\uffff\1\2\3\uffff\1\4\1\uffff\7\4\u00cb\uffff"
        )

    DFA76_min = DFA.unpack(
        u"\1\45\1\44\3\uffff\1\44\1\uffff\7\44\5\uffff\1\45\3\uffff\1\45"
        u"\6\50\24\uffff\1\45\2\uffff\1\45\6\50\u009d\uffff"
        )

    DFA76_max = DFA.unpack(
        u"\2\u00b7\3\uffff\1\u00b7\1\uffff\1\u00b7\6\174\5\uffff\1\u00b7"
        u"\3\uffff\1\u00b7\1\52\3\171\1\52\1\131\24\uffff\1\u00b7\2\uffff"
        u"\1\u00b7\1\52\3\171\1\52\1\131\u009d\uffff"
        )

    DFA76_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1\u00d4\uffff"
        )

    DFA76_special = DFA.unpack(
        u"\u00d9\uffff"
        )

            
    DFA76_transition = [
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\4"
        u"\2\1\1\5\2\2\uffff\1\2\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\1\2\3\4\1\uffff\2\4\1\uffff\3\4\2\uffff\2\2\3\uffff"
        u"\3\4\26\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\17\4\1\14\1"
        u"\15\1\4\1\11\1\4\1\12\1\13\1\4\1\5\1\7\1\10\73\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\1\uffff\2\2\1\uffff\3\2\1\uffff\1\2\2\4\3"
        u"\uffff\3\2\26\uffff\12\2\2\uffff\1\2\1\uffff\3\2\3\uffff\17\2\1"
        u"\34\1\35\1\2\1\31\1\2\1\32\1\33\1\2\1\23\1\27\1\30\73\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\1\uffff\6\2\1\uffff\1\2\2\4\3\uffff\3\2\17"
        u"\uffff\2\2\4\uffff\44\2\1\72\1\73\1\2\1\67\1\2\1\70\1\71\1\2\1"
        u"\62\1\65\1\66\73\2"),
        DFA.unpack(u"\1\4\5\uffff\1\2\6\uffff\2\4\77\uffff\2\4\1\uffff\1"
        u"\4\1\uffff\2\4\1\uffff\3\4"),
        DFA.unpack(u"\1\4\14\uffff\2\4\77\uffff\2\4\1\uffff\1\4\1\2\2\4"
        u"\1\2\3\4"),
        DFA.unpack(u"\1\4\14\uffff\2\4\77\uffff\2\4\1\uffff\1\4\1\uffff"
        u"\2\4\1\2\3\4"),
        DFA.unpack(u"\1\4\14\uffff\2\4\77\uffff\2\4\1\uffff\1\4\1\uffff"
        u"\2\4\1\2\3\4"),
        DFA.unpack(u"\1\4\5\uffff\1\2\6\uffff\2\4\77\uffff\2\4\1\uffff\1"
        u"\4\1\uffff\2\4\1\uffff\3\4"),
        DFA.unpack(u"\1\4\14\uffff\2\4\46\uffff\1\2\30\uffff\2\4\1\uffff"
        u"\1\4\1\uffff\2\4\1\uffff\3\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\4\1\2\2\4\1\uffff\3\4\1\uffff\1\4\5\uffff\3\4\26"
        u"\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\4\1\2\6\4\1\uffff\1\4\5\uffff\3\4\17\uffff\2\4\4"
        u"\uffff\152\4"),
        DFA.unpack(u"\1\2\1\uffff\1\4"),
        DFA.unpack(u"\1\2\115\uffff\1\4\2\uffff\1\4"),
        DFA.unpack(u"\1\2\120\uffff\1\4"),
        DFA.unpack(u"\1\2\120\uffff\1\4"),
        DFA.unpack(u"\1\2\1\uffff\1\4"),
        DFA.unpack(u"\1\2\60\uffff\1\4"),
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
        DFA.unpack(u"\3\4\1\2\2\4\1\uffff\3\4\1\uffff\1\4\5\uffff\3\4\26"
        u"\uffff\12\4\2\uffff\1\4\1\uffff\3\4\3\uffff\125\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\4\1\2\6\4\1\uffff\1\4\5\uffff\3\4\17\uffff\2\4\4"
        u"\uffff\152\4"),
        DFA.unpack(u"\1\2\1\uffff\1\4"),
        DFA.unpack(u"\1\2\115\uffff\1\4\2\uffff\1\4"),
        DFA.unpack(u"\1\2\120\uffff\1\4"),
        DFA.unpack(u"\1\2\120\uffff\1\4"),
        DFA.unpack(u"\1\2\1\uffff\1\4"),
        DFA.unpack(u"\1\2\60\uffff\1\4"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #76

    class DFA76(DFA):
        pass


    # lookup tables for DFA #80

    DFA80_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA80_eof = DFA.unpack(
        u"\1\1\21\uffff"
        )

    DFA80_min = DFA.unpack(
        u"\1\44\21\uffff"
        )

    DFA80_max = DFA.unpack(
        u"\1\u0083\21\uffff"
        )

    DFA80_accept = DFA.unpack(
        u"\1\uffff\1\2\11\uffff\1\1\6\uffff"
        )

    DFA80_special = DFA.unpack(
        u"\22\uffff"
        )

            
    DFA80_transition = [
        DFA.unpack(u"\1\1\14\uffff\1\13\1\1\77\uffff\2\1\1\uffff\1\1\1\uffff"
        u"\2\1\2\uffff\2\1\1\uffff\6\13"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #80

    class DFA80(DFA):
        pass


    # lookup tables for DFA #79

    DFA79_eot = DFA.unpack(
        u"\24\uffff"
        )

    DFA79_eof = DFA.unpack(
        u"\1\3\23\uffff"
        )

    DFA79_min = DFA.unpack(
        u"\1\44\23\uffff"
        )

    DFA79_max = DFA.unpack(
        u"\1\u0085\23\uffff"
        )

    DFA79_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2\20\uffff"
        )

    DFA79_special = DFA.unpack(
        u"\24\uffff"
        )

            
    DFA79_transition = [
        DFA.unpack(u"\1\3\14\uffff\2\3\77\uffff\2\3\1\uffff\1\3\1\uffff\2"
        u"\3\2\uffff\2\3\1\uffff\6\3\2\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #79

    class DFA79(DFA):
        pass


    # lookup tables for DFA #87

    DFA87_eot = DFA.unpack(
        u"\40\uffff"
        )

    DFA87_eof = DFA.unpack(
        u"\40\uffff"
        )

    DFA87_min = DFA.unpack(
        u"\1\45\3\uffff\1\45\1\uffff\1\45\31\uffff"
        )

    DFA87_max = DFA.unpack(
        u"\1\u00b7\3\uffff\1\u00b7\1\uffff\1\u00b7\31\uffff"
        )

    DFA87_accept = DFA.unpack(
        u"\1\uffff\1\1\3\uffff\1\3\5\uffff\1\2\24\uffff"
        )

    DFA87_special = DFA.unpack(
        u"\40\uffff"
        )

            
    DFA87_transition = [
        DFA.unpack(u"\3\1\1\uffff\2\1\1\uffff\3\1\1\uffff\1\4\5\uffff\3\1"
        u"\26\uffff\12\1\2\uffff\1\1\1\uffff\3\1\3\uffff\125\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\5\1\uffff\2\5\1\uffff\3\5\1\uffff\1\5\5\uffff\3"
        u"\5\26\uffff\12\5\2\uffff\1\5\1\uffff\3\5\3\uffff\26\5\1\6\76\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\3\13\1\5\6\13\1\uffff\1\13\5\uffff\3\13\17\uffff\3"
        u"\13\3\uffff\152\13"),
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
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #87

    class DFA87(DFA):
        pass


    # lookup tables for DFA #81

    DFA81_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA81_eof = DFA.unpack(
        u"\1\uffff\1\4\32\uffff"
        )

    DFA81_min = DFA.unpack(
        u"\1\45\1\44\32\uffff"
        )

    DFA81_max = DFA.unpack(
        u"\1\u00b7\1\u0085\32\uffff"
        )

    DFA81_accept = DFA.unpack(
        u"\2\uffff\1\1\1\uffff\1\2\27\uffff"
        )

    DFA81_special = DFA.unpack(
        u"\34\uffff"
        )

            
    DFA81_transition = [
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\1"
        u"\2\1\1\10\2\2\uffff\1\2\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\1\4\3\uffff\1\2\1\4\1\uffff\1\4\5\uffff\2\4\35\uffff"
        u"\1\4\2\uffff\1\4\36\uffff\2\4\1\uffff\1\4\1\uffff\2\4\2\uffff\2"
        u"\4\1\uffff\10\4"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #81

    class DFA81(DFA):
        pass


    # lookup tables for DFA #83

    DFA83_eot = DFA.unpack(
        u"\30\uffff"
        )

    DFA83_eof = DFA.unpack(
        u"\1\3\27\uffff"
        )

    DFA83_min = DFA.unpack(
        u"\1\44\27\uffff"
        )

    DFA83_max = DFA.unpack(
        u"\1\u0085\27\uffff"
        )

    DFA83_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2\24\uffff"
        )

    DFA83_special = DFA.unpack(
        u"\30\uffff"
        )

            
    DFA83_transition = [
        DFA.unpack(u"\1\3\4\uffff\1\3\1\uffff\1\3\5\uffff\2\3\35\uffff\1"
        u"\1\2\uffff\1\1\36\uffff\2\3\1\uffff\1\3\1\uffff\2\3\2\uffff\2\3"
        u"\1\uffff\10\3"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #83

    class DFA83(DFA):
        pass


    # lookup tables for DFA #84

    DFA84_eot = DFA.unpack(
        u"\26\uffff"
        )

    DFA84_eof = DFA.unpack(
        u"\1\3\25\uffff"
        )

    DFA84_min = DFA.unpack(
        u"\1\44\25\uffff"
        )

    DFA84_max = DFA.unpack(
        u"\1\u0085\25\uffff"
        )

    DFA84_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\22\uffff"
        )

    DFA84_special = DFA.unpack(
        u"\26\uffff"
        )

            
    DFA84_transition = [
        DFA.unpack(u"\1\3\4\uffff\1\1\1\uffff\1\2\5\uffff\2\3\77\uffff\2"
        u"\3\1\uffff\1\3\1\uffff\2\3\2\uffff\2\3\1\uffff\10\3"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #84

    class DFA84(DFA):
        pass


    # lookup tables for DFA #86

    DFA86_eot = DFA.unpack(
        u"\26\uffff"
        )

    DFA86_eof = DFA.unpack(
        u"\1\3\25\uffff"
        )

    DFA86_min = DFA.unpack(
        u"\1\44\25\uffff"
        )

    DFA86_max = DFA.unpack(
        u"\1\u0085\25\uffff"
        )

    DFA86_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2\22\uffff"
        )

    DFA86_special = DFA.unpack(
        u"\26\uffff"
        )

            
    DFA86_transition = [
        DFA.unpack(u"\1\3\14\uffff\2\3\35\uffff\1\1\2\uffff\1\1\36\uffff"
        u"\2\3\1\uffff\1\3\1\uffff\2\3\2\uffff\2\3\1\uffff\10\3"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #86

    class DFA86(DFA):
        pass


    # lookup tables for DFA #97

    DFA97_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA97_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA97_min = DFA.unpack(
        u"\1\45\2\50\12\uffff"
        )

    DFA97_max = DFA.unpack(
        u"\1\u00b7\2\u0089\12\uffff"
        )

    DFA97_accept = DFA.unpack(
        u"\3\uffff\1\1\1\2\10\uffff"
        )

    DFA97_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA97_transition = [
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\1"
        u"\2\1\1\10\2\2\uffff\1\1\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\1\3\7\uffff\1\4\110\uffff\1\4\16\uffff\2\4"),
        DFA.unpack(u"\1\3\7\uffff\1\4\110\uffff\1\4\16\uffff\2\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #97

    class DFA97(DFA):
        pass


    # lookup tables for DFA #122

    DFA122_eot = DFA.unpack(
        u"\107\uffff"
        )

    DFA122_eof = DFA.unpack(
        u"\107\uffff"
        )

    DFA122_min = DFA.unpack(
        u"\1\61\1\45\7\uffff\4\53\72\uffff"
        )

    DFA122_max = DFA.unpack(
        u"\1\u00a3\1\u00b7\7\uffff\4\u00a4\72\uffff"
        )

    DFA122_accept = DFA.unpack(
        u"\2\uffff\1\2\12\uffff\1\1\71\uffff"
        )

    DFA122_special = DFA.unpack(
        u"\107\uffff"
        )

            
    DFA122_transition = [
        DFA.unpack(u"\1\1\1\2\152\uffff\2\2\2\uffff\3\2"),
        DFA.unpack(u"\3\15\1\uffff\7\15\4\uffff\5\15\3\uffff\4\15\17\uffff"
        u"\12\15\2\uffff\1\15\1\uffff\3\15\3\uffff\72\15\1\2\1\11\2\15\1"
        u"\12\1\13\1\14\11\15\1\uffff\12\15"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\15\5\uffff\2\15\4\uffff\1\15\27\uffff\2\15\70\uffff"
        u"\1\15\23\uffff\2\15\1\2\1\uffff\4\15"),
        DFA.unpack(u"\1\15\4\uffff\1\2\2\15\4\uffff\1\15\27\uffff\2\15\70"
        u"\uffff\1\15\23\uffff\2\15\2\uffff\4\15"),
        DFA.unpack(u"\1\15\4\uffff\1\2\2\15\4\uffff\1\15\27\uffff\2\15\70"
        u"\uffff\1\15\23\uffff\2\15\2\uffff\4\15"),
        DFA.unpack(u"\1\15\5\uffff\2\15\4\uffff\1\15\27\uffff\2\15\70\uffff"
        u"\1\15\23\uffff\2\15\1\2\1\uffff\4\15"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #122

    class DFA122(DFA):
        pass


    # lookup tables for DFA #126

    DFA126_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA126_eof = DFA.unpack(
        u"\1\2\17\uffff"
        )

    DFA126_min = DFA.unpack(
        u"\1\44\17\uffff"
        )

    DFA126_max = DFA.unpack(
        u"\1\u00a4\17\uffff"
        )

    DFA126_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\15\uffff"
        )

    DFA126_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA126_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\2\5\uffff\2\2\4\uffff\1\2\27\uffff\1"
        u"\2\1\1\70\uffff\1\2\23\uffff\2\2\2\uffff\4\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #126

    class DFA126(DFA):
        pass


    # lookup tables for DFA #127

    DFA127_eot = DFA.unpack(
        u"\u0179\uffff"
        )

    DFA127_eof = DFA.unpack(
        u"\1\1\4\uffff\1\12\13\uffff\1\12\22\uffff\1\12\10\uffff\1\12\u014b"
        u"\uffff"
        )

    DFA127_min = DFA.unpack(
        u"\1\44\2\uffff\1\45\1\u009f\1\44\1\60\10\uffff\2\53\1\44\20\uffff"
        u"\1\45\1\u009f\1\44\1\60\6\uffff\1\u009f\1\44\1\60\30\uffff\2\53"
        u"\1\50\1\53\4\50\1\53\2\45\2\50\2\45\2\50\1\45\u0120\uffff"
        )

    DFA127_max = DFA.unpack(
        u"\1\u00a4\2\uffff\1\u00b7\1\u009f\1\u00a4\1\60\10\uffff\3\u00a4"
        u"\20\uffff\1\u00b7\1\u009f\1\u00a4\1\60\6\uffff\1\u009f\1\u00a4"
        u"\1\60\30\uffff\10\117\1\131\2\u00b7\1\117\1\60\2\u00b7\1\60\1\50"
        u"\1\u00b7\u0120\uffff"
        )

    DFA127_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1\116\uffff\1\1\20\uffff\2\1\20\uffff\u00fd"
        u"\1"
        )

    DFA127_special = DFA.unpack(
        u"\u0179\uffff"
        )

            
    DFA127_transition = [
        DFA.unpack(u"\1\1\6\uffff\1\12\5\uffff\2\1\4\uffff\1\12\27\uffff"
        u"\1\12\71\uffff\1\12\23\uffff\1\3\1\4\2\uffff\1\5\1\6\1\1\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\20\1\uffff\2\20\1\uffff\3\20\7\uffff\3\20\26\uffff"
        u"\1\20\1\17\10\20\2\uffff\1\17\1\uffff\3\20\3\uffff\125\20"),
        DFA.unpack(u"\1\21"),
        DFA.unpack(u"\1\12\6\uffff\1\12\4\uffff\1\1\2\12\4\uffff\1\12\27"
        u"\uffff\1\12\64\uffff\1\12\4\uffff\1\12\23\uffff\2\12\2\uffff\4"
        u"\12"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\13\uffff\1\12\27\uffff\1\12\71\uffff\1\12\24"
        u"\uffff\1\43\2\uffff\1\44\1\45\1\1\1\12"),
        DFA.unpack(u"\1\12\13\uffff\1\12\27\uffff\1\12\71\uffff\1\12\24"
        u"\uffff\1\54\2\uffff\1\55\1\56\1\1\1\12"),
        DFA.unpack(u"\1\12\6\uffff\1\12\4\uffff\1\1\2\12\4\uffff\1\12\27"
        u"\uffff\1\12\40\uffff\2\12\22\uffff\1\12\4\uffff\1\12\23\uffff\2"
        u"\12\1\uffff\5\12"),
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
        DFA.unpack(u"\3\127\1\uffff\2\127\1\130\3\127\1\uffff\1\124\5\uffff"
        u"\1\127\1\113\1\127\17\uffff\2\130\4\uffff\1\130\1\127\1\122\1\127"
        u"\1\123\1\127\1\125\4\127\1\107\1\110\1\111\1\112\1\114\1\115\1"
        u"\116\1\117\1\120\1\121\1\126\124\127"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\12\6\uffff\1\12\4\uffff\1\1\2\12\4\uffff\1\12\27"
        u"\uffff\1\12\64\uffff\1\12\4\uffff\1\12\23\uffff\2\12\2\uffff\4"
        u"\12"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\1\12\6\uffff\1\12\4\uffff\1\1\2\12\4\uffff\1\12\27"
        u"\uffff\1\12\64\uffff\1\12\4\uffff\1\12\23\uffff\2\12\2\uffff\4"
        u"\12"),
        DFA.unpack(u"\1\174"),
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
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0083\1\u008d\1\u008c\1\uffff\1\u0085\2\uffff\1"
        u"\u008e\1\u0086\1\u0087\1\u0088\1\u0089\1\uffff\1\u008a\3\u008b"
        u"\4\u0084\4\u0082\4\u0081\2\u0080\3\177\1\176\1\uffff\1\175"),
        DFA.unpack(u"\1\u0095\1\u009f\1\u009e\1\uffff\1\u0097\2\uffff\1"
        u"\u00a0\1\u0098\1\u0099\1\u009a\1\u009b\1\uffff\1\u009c\3\u009d"
        u"\4\u0096\4\u0094\4\u0093\2\u0092\3\u0091\1\u0090\1\uffff\1\u008f"),
        DFA.unpack(u"\1\u00a1\2\uffff\1\u00a8\1\u00b2\1\u00b1\1\uffff\1"
        u"\u00aa\2\uffff\1\u00b3\1\u00ab\1\u00ac\1\u00ad\1\u00ae\1\uffff"
        u"\1\u00af\3\u00b0\4\u00a9\4\u00a7\4\u00a6\2\u00a5\3\u00a4\1\u00a3"
        u"\1\uffff\1\u00a2"),
        DFA.unpack(u"\1\u00ba\1\u00c4\1\u00c3\1\uffff\1\u00bc\2\uffff\1"
        u"\u00c5\1\u00bd\1\u00be\1\u00bf\1\u00c0\1\uffff\1\u00c1\3\u00c2"
        u"\4\u00bb\4\u00b9\4\u00b8\2\u00b7\3\u00b6\1\u00b5\1\uffff\1\u00b4"),
        DFA.unpack(u"\1\u00c6\2\uffff\1\u00cd\1\u00d7\1\u00d6\1\uffff\1"
        u"\u00cf\2\uffff\1\u00d8\1\u00d0\1\u00d1\1\u00d2\1\u00d3\1\uffff"
        u"\1\u00d4\3\u00d5\4\u00ce\4\u00cc\4\u00cb\2\u00ca\3\u00c9\1\u00c8"
        u"\1\uffff\1\u00c7"),
        DFA.unpack(u"\1\u00d9\2\uffff\1\u00e0\1\u00ea\1\u00e9\1\uffff\1"
        u"\u00e2\2\uffff\1\u00eb\1\u00e3\1\u00e4\1\u00e5\1\u00e6\1\uffff"
        u"\1\u00e7\3\u00e8\4\u00e1\4\u00df\4\u00de\2\u00dd\3\u00dc\1\u00db"
        u"\1\uffff\1\u00da"),
        DFA.unpack(u"\1\u00ec\2\uffff\1\u00f3\1\u00fd\1\u00fc\1\uffff\1"
        u"\u00f5\2\uffff\1\u00fe\1\u00f6\1\u00f7\1\u00f8\1\u00f9\1\uffff"
        u"\1\u00fa\3\u00fb\4\u00f4\4\u00f2\4\u00f1\2\u00f0\3\u00ef\1\u00ee"
        u"\1\uffff\1\u00ed"),
        DFA.unpack(u"\1\u00ff\2\uffff\1\u0106\1\u0110\1\u010f\1\uffff\1"
        u"\u0108\2\uffff\1\u0111\1\u0109\1\u010a\1\u010b\1\u010c\1\uffff"
        u"\1\u010d\3\u010e\4\u0107\4\u0105\4\u0104\2\u0103\3\u0102\1\u0101"
        u"\1\uffff\1\u0100"),
        DFA.unpack(u"\1\u0119\1\u0123\1\u0122\1\uffff\1\u011b\2\uffff\1"
        u"\u0124\1\u011c\1\u011d\1\u011e\1\u011f\1\uffff\1\u0120\3\u0121"
        u"\4\u011a\4\u0118\4\u0117\2\u0116\3\u0115\1\u0114\1\uffff\1\u0113"
        u"\11\uffff\1\u0112"),
        DFA.unpack(u"\3\u0126\1\uffff\2\u0126\1\uffff\3\u0126\7\uffff\3"
        u"\u0126\26\uffff\1\u0126\1\u0125\10\u0126\2\uffff\1\u0125\1\uffff"
        u"\3\u0126\3\uffff\125\u0126"),
        DFA.unpack(u"\3\u0128\1\uffff\2\u0128\1\uffff\3\u0128\7\uffff\3"
        u"\u0128\26\uffff\1\u0128\1\u0127\10\u0128\2\uffff\1\u0127\1\uffff"
        u"\3\u0128\3\uffff\125\u0128"),
        DFA.unpack(u"\1\u012a\2\uffff\1\u0131\1\u013b\1\u013a\1\uffff\1"
        u"\u0133\1\u0129\1\uffff\1\u013c\1\u0134\1\u0135\1\u0136\1\u0137"
        u"\1\uffff\1\u0138\3\u0139\4\u0132\4\u0130\4\u012f\2\u012e\3\u012d"
        u"\1\u012c\1\uffff\1\u012b"),
        DFA.unpack(u"\1\u013e\7\uffff\1\u013d"),
        DFA.unpack(u"\3\u014f\1\uffff\2\u014f\1\u0150\3\u014f\1\uffff\1"
        u"\u014c\5\uffff\1\u014f\1\u0143\1\u014f\17\uffff\2\u0150\4\uffff"
        u"\1\u0150\1\u014f\1\u014a\1\u014f\1\u014b\1\u014f\1\u014d\4\u014f"
        u"\1\u013f\1\u0140\1\u0141\1\u0142\1\u0144\1\u0145\1\u0146\1\u0147"
        u"\1\u0148\1\u0149\1\u014e\124\u014f"),
        DFA.unpack(u"\3\u0164\1\u0151\2\u0164\1\u0163\3\u0164\1\uffff\1"
        u"\u015f\5\uffff\1\u0164\1\u0156\1\u0164\17\uffff\2\u0163\4\uffff"
        u"\1\u0163\1\u0164\1\u015d\1\u0164\1\u015e\1\u0164\1\u0160\2\u0164"
        u"\1\u0162\1\u0164\1\u0152\1\u0153\1\u0154\1\u0155\1\u0157\1\u0158"
        u"\1\u0159\1\u015a\1\u015b\1\u015c\1\u0161\124\u0164"),
        DFA.unpack(u"\1\u0166\7\uffff\1\u0165"),
        DFA.unpack(u"\1\u0167"),
        DFA.unpack(u"\3\u0178\1\uffff\2\u0178\1\uffff\3\u0178\1\uffff\1"
        u"\u0175\5\uffff\1\u0178\1\u016c\1\u0178\26\uffff\1\u0178\1\u0173"
        u"\1\u0178\1\u0174\1\u0178\1\u0176\4\u0178\1\u0168\1\u0169\1\u016a"
        u"\1\u016b\1\u016d\1\u016e\1\u016f\1\u0170\1\u0171\1\u0172\1\u0177"
        u"\124\u0178"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #127

    class DFA127(DFA):
        pass


    # lookup tables for DFA #128

    DFA128_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA128_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA128_min = DFA.unpack(
        u"\1\53\11\uffff"
        )

    DFA128_max = DFA.unpack(
        u"\1\u00a4\11\uffff"
        )

    DFA128_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\7\uffff"
        )

    DFA128_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA128_transition = [
        DFA.unpack(u"\1\2\13\uffff\1\2\27\uffff\1\2\71\uffff\1\2\23\uffff"
        u"\1\1\1\2\2\uffff\2\2\1\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #128

    class DFA128(DFA):
        pass


    # lookup tables for DFA #130

    DFA130_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA130_eof = DFA.unpack(
        u"\1\2\21\uffff"
        )

    DFA130_min = DFA.unpack(
        u"\1\44\21\uffff"
        )

    DFA130_max = DFA.unpack(
        u"\1\u00a4\21\uffff"
        )

    DFA130_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\17\uffff"
        )

    DFA130_special = DFA.unpack(
        u"\22\uffff"
        )

            
    DFA130_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\2\5\uffff\2\2\4\uffff\1\2\27\uffff\1"
        u"\2\40\uffff\2\1\22\uffff\1\2\4\uffff\1\2\23\uffff\2\2\1\uffff\5"
        u"\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #130

    class DFA130(DFA):
        pass


    # lookup tables for DFA #131

    DFA131_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA131_eof = DFA.unpack(
        u"\1\2\20\uffff"
        )

    DFA131_min = DFA.unpack(
        u"\1\44\20\uffff"
        )

    DFA131_max = DFA.unpack(
        u"\1\u00a4\20\uffff"
        )

    DFA131_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\16\uffff"
        )

    DFA131_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA131_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\2\5\uffff\2\2\4\uffff\1\2\27\uffff\1"
        u"\2\64\uffff\1\1\4\uffff\1\2\23\uffff\2\2\1\uffff\5\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #131

    class DFA131(DFA):
        pass


    # lookup tables for DFA #132

    DFA132_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA132_eof = DFA.unpack(
        u"\1\2\17\uffff"
        )

    DFA132_min = DFA.unpack(
        u"\1\44\17\uffff"
        )

    DFA132_max = DFA.unpack(
        u"\1\u00a4\17\uffff"
        )

    DFA132_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\15\uffff"
        )

    DFA132_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA132_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\2\5\uffff\2\2\4\uffff\1\2\27\uffff\1"
        u"\2\71\uffff\1\2\23\uffff\2\2\1\uffff\1\1\4\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #132

    class DFA132(DFA):
        pass


    # lookup tables for DFA #133

    DFA133_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA133_eof = DFA.unpack(
        u"\1\2\17\uffff"
        )

    DFA133_min = DFA.unpack(
        u"\1\44\17\uffff"
        )

    DFA133_max = DFA.unpack(
        u"\1\u00a4\17\uffff"
        )

    DFA133_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\15\uffff"
        )

    DFA133_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA133_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\2\5\uffff\2\2\4\uffff\1\2\27\uffff\1"
        u"\2\64\uffff\1\1\4\uffff\1\2\23\uffff\2\2\2\uffff\4\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #133

    class DFA133(DFA):
        pass


    # lookup tables for DFA #134

    DFA134_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA134_eof = DFA.unpack(
        u"\1\2\17\uffff"
        )

    DFA134_min = DFA.unpack(
        u"\1\44\17\uffff"
        )

    DFA134_max = DFA.unpack(
        u"\1\u00a4\17\uffff"
        )

    DFA134_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\15\uffff"
        )

    DFA134_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA134_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\2\5\uffff\2\2\4\uffff\1\2\27\uffff\1"
        u"\2\64\uffff\1\1\4\uffff\1\2\23\uffff\2\2\2\uffff\4\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #134

    class DFA134(DFA):
        pass


    # lookup tables for DFA #135

    DFA135_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA135_eof = DFA.unpack(
        u"\1\2\17\uffff"
        )

    DFA135_min = DFA.unpack(
        u"\1\44\17\uffff"
        )

    DFA135_max = DFA.unpack(
        u"\1\u00a4\17\uffff"
        )

    DFA135_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\15\uffff"
        )

    DFA135_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA135_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\2\5\uffff\2\2\4\uffff\1\2\27\uffff\1"
        u"\2\64\uffff\1\1\4\uffff\1\2\23\uffff\2\2\2\uffff\4\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #135

    class DFA135(DFA):
        pass


    # lookup tables for DFA #137

    DFA137_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA137_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA137_min = DFA.unpack(
        u"\1\60\12\uffff"
        )

    DFA137_max = DFA.unpack(
        u"\1\137\12\uffff"
        )

    DFA137_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\7\uffff\1\3"
        )

    DFA137_special = DFA.unpack(
        u"\13\uffff"
        )

            
    DFA137_transition = [
        DFA.unpack(u"\1\12\6\uffff\1\2\20\uffff\2\1\17\uffff\7\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #137

    class DFA137(DFA):
        pass


    # lookup tables for DFA #146

    DFA146_eot = DFA.unpack(
        u"\23\uffff"
        )

    DFA146_eof = DFA.unpack(
        u"\1\2\22\uffff"
        )

    DFA146_min = DFA.unpack(
        u"\1\44\22\uffff"
        )

    DFA146_max = DFA.unpack(
        u"\1\u00a7\22\uffff"
        )

    DFA146_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\20\uffff"
        )

    DFA146_special = DFA.unpack(
        u"\23\uffff"
        )

            
    DFA146_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\2\4\uffff\1\1\2\2\4\uffff\1\2\7\uffff"
        u"\1\2\17\uffff\1\2\64\uffff\1\2\4\uffff\1\2\23\uffff\2\2\2\uffff"
        u"\4\2\2\uffff\1\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #146

    class DFA146(DFA):
        pass


    # lookup tables for DFA #147

    DFA147_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA147_eof = DFA.unpack(
        u"\1\1\21\uffff"
        )

    DFA147_min = DFA.unpack(
        u"\1\44\21\uffff"
        )

    DFA147_max = DFA.unpack(
        u"\1\u00a7\21\uffff"
        )

    DFA147_accept = DFA.unpack(
        u"\1\uffff\1\2\16\uffff\1\1\1\uffff"
        )

    DFA147_special = DFA.unpack(
        u"\22\uffff"
        )

            
    DFA147_transition = [
        DFA.unpack(u"\1\1\6\uffff\1\1\5\uffff\2\1\4\uffff\1\1\7\uffff\1\20"
        u"\17\uffff\1\1\64\uffff\1\20\4\uffff\1\1\23\uffff\2\1\2\uffff\4"
        u"\1\2\uffff\1\1"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #147

    class DFA147(DFA):
        pass


    # lookup tables for DFA #148

    DFA148_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA148_eof = DFA.unpack(
        u"\1\3\21\uffff"
        )

    DFA148_min = DFA.unpack(
        u"\1\44\1\67\20\uffff"
        )

    DFA148_max = DFA.unpack(
        u"\2\u00a7\20\uffff"
        )

    DFA148_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\16\uffff"
        )

    DFA148_special = DFA.unpack(
        u"\22\uffff"
        )

            
    DFA148_transition = [
        DFA.unpack(u"\1\3\6\uffff\1\1\5\uffff\2\3\4\uffff\1\3\27\uffff\1"
        u"\3\71\uffff\1\3\23\uffff\2\3\2\uffff\4\3\2\uffff\1\2"),
        DFA.unpack(u"\1\3\157\uffff\1\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #148

    class DFA148(DFA):
        pass


    # lookup tables for DFA #152

    DFA152_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA152_eof = DFA.unpack(
        u"\1\2\21\uffff"
        )

    DFA152_min = DFA.unpack(
        u"\1\44\1\u008e\20\uffff"
        )

    DFA152_max = DFA.unpack(
        u"\1\u00a8\1\u008f\20\uffff"
        )

    DFA152_accept = DFA.unpack(
        u"\2\uffff\1\3\15\uffff\1\1\1\2"
        )

    DFA152_special = DFA.unpack(
        u"\22\uffff"
        )

            
    DFA152_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\2\5\uffff\2\2\4\uffff\1\2\27\uffff\1"
        u"\2\71\uffff\1\2\23\uffff\2\2\2\uffff\4\2\3\uffff\1\1"),
        DFA.unpack(u"\1\20\1\21"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #152

    class DFA152(DFA):
        pass


    # lookup tables for DFA #172

    DFA172_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA172_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA172_min = DFA.unpack(
        u"\1\45\1\50\12\uffff"
        )

    DFA172_max = DFA.unpack(
        u"\1\u00b7\1\u00b3\12\uffff"
        )

    DFA172_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1\7\uffff"
        )

    DFA172_special = DFA.unpack(
        u"\14\uffff"
        )

            
    DFA172_transition = [
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\12"
        u"\2\2\uffff\1\2\1\uffff\3\2\3\uffff\70\2\1\1\34\2"),
        DFA.unpack(u"\1\2\2\uffff\1\4\132\uffff\1\2\3\uffff\1\2\1\uffff"
        u"\1\2\44\uffff\3\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #172

    class DFA172(DFA):
        pass


    # lookup tables for DFA #173

    DFA173_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA173_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA173_min = DFA.unpack(
        u"\1\45\2\50\16\uffff"
        )

    DFA173_max = DFA.unpack(
        u"\1\u00b7\2\u00b3\16\uffff"
        )

    DFA173_accept = DFA.unpack(
        u"\3\uffff\1\2\5\uffff\1\1\7\uffff"
        )

    DFA173_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA173_transition = [
        DFA.unpack(u"\3\2\1\uffff\2\2\1\uffff\3\2\7\uffff\3\2\26\uffff\1"
        u"\2\1\1\10\2\2\uffff\1\1\1\uffff\3\2\3\uffff\125\2"),
        DFA.unpack(u"\1\11\135\uffff\1\3\3\uffff\1\3\1\uffff\1\3\44\uffff"
        u"\3\3"),
        DFA.unpack(u"\1\11\135\uffff\1\3\3\uffff\1\3\1\uffff\1\3\44\uffff"
        u"\3\3"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #173

    class DFA173(DFA):
        pass


 

    FOLLOW_sql_stmt_in_sql_stmt_list223 = frozenset([36])
    FOLLOW_SEMI_in_sql_stmt_list226 = frozenset([37, 86, 101, 104, 105, 107, 108, 109, 110, 111, 121, 134, 138, 140, 141, 146, 148, 149, 151, 169, 170])
    FOLLOW_sql_stmt_in_sql_stmt_list230 = frozenset([36])
    FOLLOW_SEMI_in_sql_stmt_list232 = frozenset([37, 86, 101, 104, 105, 107, 108, 109, 110, 111, 121, 134, 138, 140, 141, 146, 148, 149, 151, 169, 170])
    FOLLOW_EOF_in_sql_stmt_list240 = frozenset([1])
    FOLLOW_sql_stmt_in_sql_stmt_itself248 = frozenset([36])
    FOLLOW_SEMI_in_sql_stmt_itself251 = frozenset([])
    FOLLOW_EOF_in_sql_stmt_itself256 = frozenset([1])
    FOLLOW_EXPLAIN_in_sql_stmt265 = frozenset([37, 38, 86, 101, 104, 105, 107, 108, 109, 110, 111, 121, 134, 138, 140, 141, 146, 148, 149, 151, 169, 170])
    FOLLOW_QUERY_in_sql_stmt268 = frozenset([39])
    FOLLOW_PLAN_in_sql_stmt270 = frozenset([37, 86, 101, 104, 105, 107, 108, 109, 110, 111, 121, 134, 138, 140, 141, 146, 148, 149, 151, 169, 170])
    FOLLOW_sql_stmt_core_in_sql_stmt276 = frozenset([1])
    FOLLOW_pragma_stmt_in_sql_stmt_core286 = frozenset([1])
    FOLLOW_attach_stmt_in_sql_stmt_core292 = frozenset([1])
    FOLLOW_detach_stmt_in_sql_stmt_core298 = frozenset([1])
    FOLLOW_analyze_stmt_in_sql_stmt_core304 = frozenset([1])
    FOLLOW_reindex_stmt_in_sql_stmt_core310 = frozenset([1])
    FOLLOW_vacuum_stmt_in_sql_stmt_core316 = frozenset([1])
    FOLLOW_select_stmt_in_sql_stmt_core323 = frozenset([1])
    FOLLOW_insert_stmt_in_sql_stmt_core329 = frozenset([1])
    FOLLOW_update_stmt_in_sql_stmt_core335 = frozenset([1])
    FOLLOW_delete_stmt_in_sql_stmt_core341 = frozenset([1])
    FOLLOW_begin_stmt_in_sql_stmt_core347 = frozenset([1])
    FOLLOW_commit_stmt_in_sql_stmt_core353 = frozenset([1])
    FOLLOW_rollback_stmt_in_sql_stmt_core359 = frozenset([1])
    FOLLOW_savepoint_stmt_in_sql_stmt_core365 = frozenset([1])
    FOLLOW_release_stmt_in_sql_stmt_core371 = frozenset([1])
    FOLLOW_create_virtual_table_stmt_in_sql_stmt_core378 = frozenset([1])
    FOLLOW_create_table_stmt_in_sql_stmt_core384 = frozenset([1])
    FOLLOW_drop_table_stmt_in_sql_stmt_core390 = frozenset([1])
    FOLLOW_alter_table_stmt_in_sql_stmt_core396 = frozenset([1])
    FOLLOW_create_view_stmt_in_sql_stmt_core402 = frozenset([1])
    FOLLOW_drop_view_stmt_in_sql_stmt_core408 = frozenset([1])
    FOLLOW_create_index_stmt_in_sql_stmt_core414 = frozenset([1])
    FOLLOW_drop_index_stmt_in_sql_stmt_core420 = frozenset([1])
    FOLLOW_create_trigger_stmt_in_sql_stmt_core426 = frozenset([1])
    FOLLOW_drop_trigger_stmt_in_sql_stmt_core432 = frozenset([1])
    FOLLOW_create_virtual_table_stmt_in_schema_create_table_stmt442 = frozenset([1])
    FOLLOW_create_table_stmt_in_schema_create_table_stmt446 = frozenset([1])
    FOLLOW_id_in_qualified_table_name456 = frozenset([40])
    FOLLOW_DOT_in_qualified_table_name458 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_qualified_table_name464 = frozenset([1, 41, 43])
    FOLLOW_INDEXED_in_qualified_table_name467 = frozenset([42])
    FOLLOW_BY_in_qualified_table_name469 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_qualified_table_name473 = frozenset([1])
    FOLLOW_NOT_in_qualified_table_name477 = frozenset([41])
    FOLLOW_INDEXED_in_qualified_table_name479 = frozenset([1])
    FOLLOW_or_subexpr_in_expr488 = frozenset([1, 44])
    FOLLOW_OR_in_expr491 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_or_subexpr_in_expr494 = frozenset([1, 44])
    FOLLOW_and_subexpr_in_or_subexpr503 = frozenset([1, 45])
    FOLLOW_AND_in_or_subexpr506 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_and_subexpr_in_or_subexpr509 = frozenset([1, 45])
    FOLLOW_eq_subexpr_in_and_subexpr518 = frozenset([1, 43, 47, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_cond_expr_in_and_subexpr520 = frozenset([1])
    FOLLOW_NOT_in_cond_expr532 = frozenset([43, 60, 61, 62, 63])
    FOLLOW_match_op_in_cond_expr535 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_eq_subexpr_in_cond_expr539 = frozenset([1, 46])
    FOLLOW_ESCAPE_in_cond_expr542 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_eq_subexpr_in_cond_expr546 = frozenset([1])
    FOLLOW_NOT_in_cond_expr574 = frozenset([47])
    FOLLOW_IN_in_cond_expr577 = frozenset([48])
    FOLLOW_LPAREN_in_cond_expr579 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_cond_expr581 = frozenset([49, 50])
    FOLLOW_COMMA_in_cond_expr584 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_cond_expr586 = frozenset([49, 50])
    FOLLOW_RPAREN_in_cond_expr590 = frozenset([1])
    FOLLOW_NOT_in_cond_expr612 = frozenset([47])
    FOLLOW_IN_in_cond_expr615 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_cond_expr620 = frozenset([40])
    FOLLOW_DOT_in_cond_expr622 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_cond_expr628 = frozenset([1])
    FOLLOW_NOT_in_cond_expr656 = frozenset([47])
    FOLLOW_IN_in_cond_expr659 = frozenset([48])
    FOLLOW_LPAREN_in_cond_expr662 = frozenset([50, 121])
    FOLLOW_select_stmt_in_cond_expr665 = frozenset([50])
    FOLLOW_RPAREN_in_cond_expr668 = frozenset([1])
    FOLLOW_NOT_in_cond_expr675 = frozenset([51])
    FOLLOW_EQUALS_in_cond_expr678 = frozenset([48])
    FOLLOW_LPAREN_in_cond_expr681 = frozenset([50, 121])
    FOLLOW_select_stmt_in_cond_expr684 = frozenset([50])
    FOLLOW_RPAREN_in_cond_expr687 = frozenset([1])
    FOLLOW_ISNULL_in_cond_expr695 = frozenset([1])
    FOLLOW_NOTNULL_in_cond_expr703 = frozenset([1])
    FOLLOW_IS_in_cond_expr711 = frozenset([55])
    FOLLOW_NULL_in_cond_expr713 = frozenset([1])
    FOLLOW_NOT_in_cond_expr721 = frozenset([55])
    FOLLOW_NULL_in_cond_expr723 = frozenset([1])
    FOLLOW_IS_in_cond_expr731 = frozenset([43])
    FOLLOW_NOT_in_cond_expr733 = frozenset([55])
    FOLLOW_NULL_in_cond_expr735 = frozenset([1])
    FOLLOW_IS_in_cond_expr746 = frozenset([43])
    FOLLOW_NOT_in_cond_expr748 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_eq_subexpr_in_cond_expr751 = frozenset([1])
    FOLLOW_NOT_in_cond_expr757 = frozenset([56])
    FOLLOW_BETWEEN_in_cond_expr760 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_eq_subexpr_in_cond_expr764 = frozenset([45])
    FOLLOW_AND_in_cond_expr766 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_eq_subexpr_in_cond_expr770 = frozenset([1])
    FOLLOW_set_in_cond_expr796 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_eq_subexpr_in_cond_expr813 = frozenset([1, 51, 57, 58, 59])
    FOLLOW_set_in_match_op0 = frozenset([1])
    FOLLOW_neq_subexpr_in_eq_subexpr846 = frozenset([1, 64, 65, 66, 67])
    FOLLOW_set_in_eq_subexpr849 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_neq_subexpr_in_eq_subexpr866 = frozenset([1, 64, 65, 66, 67])
    FOLLOW_bit_subexpr_in_neq_subexpr875 = frozenset([1, 68, 69, 70, 71])
    FOLLOW_set_in_neq_subexpr878 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_bit_subexpr_in_neq_subexpr895 = frozenset([1, 68, 69, 70, 71])
    FOLLOW_add_subexpr_in_bit_subexpr904 = frozenset([1, 72, 73])
    FOLLOW_set_in_bit_subexpr907 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_add_subexpr_in_bit_subexpr916 = frozenset([1, 72, 73])
    FOLLOW_mul_subexpr_in_add_subexpr925 = frozenset([1, 74, 75, 76])
    FOLLOW_set_in_add_subexpr928 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_mul_subexpr_in_add_subexpr941 = frozenset([1, 74, 75, 76])
    FOLLOW_con_subexpr_in_mul_subexpr950 = frozenset([1, 77])
    FOLLOW_DOUBLE_PIPE_in_mul_subexpr953 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_con_subexpr_in_mul_subexpr956 = frozenset([1, 77])
    FOLLOW_unary_subexpr_in_con_subexpr965 = frozenset([1])
    FOLLOW_unary_op_in_con_subexpr969 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 48, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_unary_subexpr_in_con_subexpr971 = frozenset([1])
    FOLLOW_set_in_unary_op0 = frozenset([1])
    FOLLOW_atom_expr_in_unary_subexpr1005 = frozenset([1, 79])
    FOLLOW_COLLATE_in_unary_subexpr1008 = frozenset([80])
    FOLLOW_ID_in_unary_subexpr1013 = frozenset([1])
    FOLLOW_literal_value_in_atom_expr1025 = frozenset([1])
    FOLLOW_bind_parameter_in_atom_expr1031 = frozenset([1])
    FOLLOW_id_in_atom_expr1041 = frozenset([40])
    FOLLOW_DOT_in_atom_expr1043 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_atom_expr1049 = frozenset([40])
    FOLLOW_DOT_in_atom_expr1051 = frozenset([80])
    FOLLOW_ID_in_atom_expr1057 = frozenset([1])
    FOLLOW_ID_in_atom_expr1086 = frozenset([48])
    FOLLOW_LPAREN_in_atom_expr1088 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 50, 54, 55, 56, 72, 73, 74, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_DISTINCT_in_atom_expr1091 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_atom_expr1096 = frozenset([49, 50])
    FOLLOW_COMMA_in_atom_expr1099 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_atom_expr1103 = frozenset([49, 50])
    FOLLOW_ASTERISK_in_atom_expr1109 = frozenset([50])
    FOLLOW_RPAREN_in_atom_expr1113 = frozenset([1])
    FOLLOW_LPAREN_in_atom_expr1138 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_atom_expr1141 = frozenset([50])
    FOLLOW_RPAREN_in_atom_expr1143 = frozenset([1])
    FOLLOW_CAST_in_atom_expr1150 = frozenset([48])
    FOLLOW_LPAREN_in_atom_expr1153 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_atom_expr1156 = frozenset([83])
    FOLLOW_AS_in_atom_expr1158 = frozenset([80])
    FOLLOW_type_name_in_atom_expr1161 = frozenset([50])
    FOLLOW_RPAREN_in_atom_expr1163 = frozenset([1])
    FOLLOW_CASE_in_atom_expr1172 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_atom_expr1177 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_when_expr_in_atom_expr1181 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_ELSE_in_atom_expr1185 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_atom_expr1189 = frozenset([86])
    FOLLOW_END_in_atom_expr1193 = frozenset([1])
    FOLLOW_raise_function_in_atom_expr1216 = frozenset([1])
    FOLLOW_WHEN_in_when_expr1226 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_when_expr1230 = frozenset([88])
    FOLLOW_THEN_in_when_expr1232 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_when_expr1236 = frozenset([1])
    FOLLOW_INTEGER_in_literal_value1258 = frozenset([1])
    FOLLOW_FLOAT_in_literal_value1272 = frozenset([1])
    FOLLOW_STRING_in_literal_value1286 = frozenset([1])
    FOLLOW_BLOB_in_literal_value1300 = frozenset([1])
    FOLLOW_NULL_in_literal_value1314 = frozenset([1])
    FOLLOW_CURRENT_TIME_in_literal_value1320 = frozenset([1])
    FOLLOW_CURRENT_DATE_in_literal_value1334 = frozenset([1])
    FOLLOW_CURRENT_TIMESTAMP_in_literal_value1348 = frozenset([1])
    FOLLOW_QUESTION_in_bind_parameter1369 = frozenset([1])
    FOLLOW_QUESTION_in_bind_parameter1379 = frozenset([89])
    FOLLOW_INTEGER_in_bind_parameter1383 = frozenset([1])
    FOLLOW_COLON_in_bind_parameter1398 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_bind_parameter1402 = frozenset([1])
    FOLLOW_AT_in_bind_parameter1417 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_bind_parameter1421 = frozenset([1])
    FOLLOW_RAISE_in_raise_function1442 = frozenset([48])
    FOLLOW_LPAREN_in_raise_function1445 = frozenset([100, 101, 102, 103])
    FOLLOW_IGNORE_in_raise_function1449 = frozenset([50])
    FOLLOW_set_in_raise_function1453 = frozenset([49])
    FOLLOW_COMMA_in_raise_function1465 = frozenset([91])
    FOLLOW_STRING_in_raise_function1470 = frozenset([50])
    FOLLOW_RPAREN_in_raise_function1473 = frozenset([1])
    FOLLOW_ID_in_type_name1483 = frozenset([1, 48, 80])
    FOLLOW_LPAREN_in_type_name1487 = frozenset([72, 73, 89, 90])
    FOLLOW_signed_number_in_type_name1491 = frozenset([49, 50])
    FOLLOW_COMMA_in_type_name1494 = frozenset([72, 73, 89, 90])
    FOLLOW_signed_number_in_type_name1498 = frozenset([50])
    FOLLOW_RPAREN_in_type_name1502 = frozenset([1])
    FOLLOW_set_in_signed_number1533 = frozenset([89, 90])
    FOLLOW_set_in_signed_number1542 = frozenset([1])
    FOLLOW_PRAGMA_in_pragma_stmt1556 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_pragma_stmt1561 = frozenset([40])
    FOLLOW_DOT_in_pragma_stmt1563 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_pragma_stmt1569 = frozenset([1, 48, 51])
    FOLLOW_EQUALS_in_pragma_stmt1572 = frozenset([72, 73, 80, 89, 90, 91])
    FOLLOW_pragma_value_in_pragma_stmt1574 = frozenset([1])
    FOLLOW_LPAREN_in_pragma_stmt1578 = frozenset([72, 73, 80, 89, 90, 91])
    FOLLOW_pragma_value_in_pragma_stmt1580 = frozenset([50])
    FOLLOW_RPAREN_in_pragma_stmt1582 = frozenset([1])
    FOLLOW_signed_number_in_pragma_value1611 = frozenset([1])
    FOLLOW_ID_in_pragma_value1624 = frozenset([1])
    FOLLOW_STRING_in_pragma_value1637 = frozenset([1])
    FOLLOW_ATTACH_in_attach_stmt1655 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_DATABASE_in_attach_stmt1658 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_attach_stmt1664 = frozenset([83])
    FOLLOW_AS_in_attach_stmt1666 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_attach_stmt1670 = frozenset([1])
    FOLLOW_DETACH_in_detach_stmt1678 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_DATABASE_in_detach_stmt1681 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_detach_stmt1687 = frozenset([1])
    FOLLOW_ANALYZE_in_analyze_stmt1695 = frozenset([1, 37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_analyze_stmt1700 = frozenset([1])
    FOLLOW_id_in_analyze_stmt1706 = frozenset([40])
    FOLLOW_DOT_in_analyze_stmt1708 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_analyze_stmt1712 = frozenset([1])
    FOLLOW_REINDEX_in_reindex_stmt1722 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_reindex_stmt1727 = frozenset([40])
    FOLLOW_DOT_in_reindex_stmt1729 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_reindex_stmt1735 = frozenset([1])
    FOLLOW_VACUUM_in_vacuum_stmt1743 = frozenset([1])
    FOLLOW_OR_in_operation_conflict_clause1754 = frozenset([100, 101, 102, 103, 111])
    FOLLOW_set_in_operation_conflict_clause1756 = frozenset([1])
    FOLLOW_expr_in_ordering_term1781 = frozenset([1, 112, 113])
    FOLLOW_ASC_in_ordering_term1786 = frozenset([1])
    FOLLOW_DESC_in_ordering_term1790 = frozenset([1])
    FOLLOW_ORDER_in_operation_limited_clause1820 = frozenset([42])
    FOLLOW_BY_in_operation_limited_clause1822 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_ordering_term_in_operation_limited_clause1824 = frozenset([49, 115])
    FOLLOW_COMMA_in_operation_limited_clause1827 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_ordering_term_in_operation_limited_clause1829 = frozenset([49, 115])
    FOLLOW_LIMIT_in_operation_limited_clause1837 = frozenset([89])
    FOLLOW_INTEGER_in_operation_limited_clause1841 = frozenset([1, 49, 116])
    FOLLOW_set_in_operation_limited_clause1844 = frozenset([89])
    FOLLOW_INTEGER_in_operation_limited_clause1854 = frozenset([1])
    FOLLOW_select_list_in_select_stmt1864 = frozenset([1, 114, 115])
    FOLLOW_ORDER_in_select_stmt1869 = frozenset([42])
    FOLLOW_BY_in_select_stmt1871 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_ordering_term_in_select_stmt1873 = frozenset([1, 49, 115])
    FOLLOW_COMMA_in_select_stmt1876 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_ordering_term_in_select_stmt1878 = frozenset([1, 49, 115])
    FOLLOW_LIMIT_in_select_stmt1887 = frozenset([89])
    FOLLOW_INTEGER_in_select_stmt1891 = frozenset([1, 49, 116])
    FOLLOW_OFFSET_in_select_stmt1895 = frozenset([89])
    FOLLOW_COMMA_in_select_stmt1899 = frozenset([89])
    FOLLOW_INTEGER_in_select_stmt1904 = frozenset([1])
    FOLLOW_select_core_in_select_list1949 = frozenset([1, 117, 119, 120])
    FOLLOW_select_op_in_select_list1952 = frozenset([121])
    FOLLOW_select_core_in_select_list1955 = frozenset([1, 117, 119, 120])
    FOLLOW_UNION_in_select_op1964 = frozenset([1, 118])
    FOLLOW_ALL_in_select_op1968 = frozenset([1])
    FOLLOW_INTERSECT_in_select_op1974 = frozenset([1])
    FOLLOW_EXCEPT_in_select_op1978 = frozenset([1])
    FOLLOW_SELECT_in_select_core1987 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 74, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_ALL_in_select_core1990 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 74, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_DISTINCT_in_select_core1994 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 74, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_result_column_in_select_core1998 = frozenset([1, 49, 122, 123, 124])
    FOLLOW_COMMA_in_select_core2001 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 74, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_result_column_in_select_core2003 = frozenset([1, 49, 122, 123, 124])
    FOLLOW_FROM_in_select_core2008 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 48, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_join_source_in_select_core2010 = frozenset([1, 123, 124])
    FOLLOW_WHERE_in_select_core2015 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_select_core2019 = frozenset([1, 124])
    FOLLOW_GROUP_in_select_core2027 = frozenset([42])
    FOLLOW_BY_in_select_core2029 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_ordering_term_in_select_core2031 = frozenset([1, 49, 125])
    FOLLOW_COMMA_in_select_core2034 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_ordering_term_in_select_core2036 = frozenset([1, 49, 125])
    FOLLOW_HAVING_in_select_core2041 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_select_core2045 = frozenset([1])
    FOLLOW_ASTERISK_in_result_column2115 = frozenset([1])
    FOLLOW_id_in_result_column2123 = frozenset([40])
    FOLLOW_DOT_in_result_column2125 = frozenset([74])
    FOLLOW_ASTERISK_in_result_column2127 = frozenset([1])
    FOLLOW_expr_in_result_column2142 = frozenset([1, 37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_AS_in_result_column2146 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_result_column2152 = frozenset([1])
    FOLLOW_single_source_in_join_source2173 = frozenset([1, 49, 126, 127, 128, 129, 130, 131])
    FOLLOW_join_op_in_join_source2176 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 48, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_single_source_in_join_source2179 = frozenset([1, 49, 126, 127, 128, 129, 130, 131, 132, 133])
    FOLLOW_join_constraint_in_join_source2182 = frozenset([1, 49, 126, 127, 128, 129, 130, 131])
    FOLLOW_id_in_single_source2199 = frozenset([40])
    FOLLOW_DOT_in_single_source2201 = frozenset([80])
    FOLLOW_ID_in_single_source2207 = frozenset([1, 41, 43, 80, 83])
    FOLLOW_AS_in_single_source2211 = frozenset([80])
    FOLLOW_ID_in_single_source2217 = frozenset([1, 41, 43])
    FOLLOW_INDEXED_in_single_source2222 = frozenset([42])
    FOLLOW_BY_in_single_source2224 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_single_source2228 = frozenset([1])
    FOLLOW_NOT_in_single_source2232 = frozenset([41])
    FOLLOW_INDEXED_in_single_source2234 = frozenset([1])
    FOLLOW_LPAREN_in_single_source2275 = frozenset([121])
    FOLLOW_select_stmt_in_single_source2277 = frozenset([50])
    FOLLOW_RPAREN_in_single_source2279 = frozenset([1, 80, 83])
    FOLLOW_AS_in_single_source2283 = frozenset([80])
    FOLLOW_ID_in_single_source2289 = frozenset([1])
    FOLLOW_LPAREN_in_single_source2311 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 48, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_join_source_in_single_source2314 = frozenset([50])
    FOLLOW_RPAREN_in_single_source2316 = frozenset([1])
    FOLLOW_COMMA_in_join_op2327 = frozenset([1])
    FOLLOW_NATURAL_in_join_op2334 = frozenset([127, 128, 129, 130, 131])
    FOLLOW_LEFT_in_join_op2340 = frozenset([128, 131])
    FOLLOW_OUTER_in_join_op2345 = frozenset([131])
    FOLLOW_INNER_in_join_op2351 = frozenset([131])
    FOLLOW_CROSS_in_join_op2355 = frozenset([131])
    FOLLOW_JOIN_in_join_op2358 = frozenset([1])
    FOLLOW_ON_in_join_constraint2369 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_join_constraint2372 = frozenset([1])
    FOLLOW_USING_in_join_constraint2378 = frozenset([48])
    FOLLOW_LPAREN_in_join_constraint2380 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_join_constraint2384 = frozenset([49, 50])
    FOLLOW_COMMA_in_join_constraint2387 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_join_constraint2391 = frozenset([49, 50])
    FOLLOW_RPAREN_in_join_constraint2395 = frozenset([1])
    FOLLOW_INSERT_in_insert_stmt2414 = frozenset([44, 135])
    FOLLOW_operation_conflict_clause_in_insert_stmt2417 = frozenset([135])
    FOLLOW_REPLACE_in_insert_stmt2423 = frozenset([135])
    FOLLOW_INTO_in_insert_stmt2426 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_insert_stmt2431 = frozenset([40])
    FOLLOW_DOT_in_insert_stmt2433 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_insert_stmt2439 = frozenset([48, 121, 136, 137])
    FOLLOW_LPAREN_in_insert_stmt2446 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_insert_stmt2450 = frozenset([49, 50])
    FOLLOW_COMMA_in_insert_stmt2453 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_insert_stmt2457 = frozenset([49, 50])
    FOLLOW_RPAREN_in_insert_stmt2461 = frozenset([121, 136])
    FOLLOW_VALUES_in_insert_stmt2470 = frozenset([48])
    FOLLOW_LPAREN_in_insert_stmt2472 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_insert_stmt2476 = frozenset([49, 50])
    FOLLOW_COMMA_in_insert_stmt2479 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_insert_stmt2483 = frozenset([49, 50])
    FOLLOW_RPAREN_in_insert_stmt2487 = frozenset([1])
    FOLLOW_select_stmt_in_insert_stmt2491 = frozenset([1])
    FOLLOW_DEFAULT_in_insert_stmt2498 = frozenset([136])
    FOLLOW_VALUES_in_insert_stmt2500 = frozenset([1])
    FOLLOW_UPDATE_in_update_stmt2510 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_operation_conflict_clause_in_update_stmt2513 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_qualified_table_name_in_update_stmt2517 = frozenset([139])
    FOLLOW_SET_in_update_stmt2521 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_update_set_in_update_stmt2525 = frozenset([1, 49, 114, 115, 123])
    FOLLOW_COMMA_in_update_stmt2528 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_update_set_in_update_stmt2532 = frozenset([1, 49, 114, 115, 123])
    FOLLOW_WHERE_in_update_stmt2537 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_update_stmt2539 = frozenset([1, 114, 115])
    FOLLOW_operation_limited_clause_in_update_stmt2544 = frozenset([1])
    FOLLOW_id_in_update_set2555 = frozenset([51])
    FOLLOW_EQUALS_in_update_set2557 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_update_set2559 = frozenset([1])
    FOLLOW_DELETE_in_delete_stmt2567 = frozenset([122])
    FOLLOW_FROM_in_delete_stmt2569 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_qualified_table_name_in_delete_stmt2571 = frozenset([1, 114, 115, 123])
    FOLLOW_WHERE_in_delete_stmt2574 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_delete_stmt2576 = frozenset([1, 114, 115])
    FOLLOW_operation_limited_clause_in_delete_stmt2581 = frozenset([1])
    FOLLOW_BEGIN_in_begin_stmt2591 = frozenset([1, 142, 143, 144, 145])
    FOLLOW_set_in_begin_stmt2593 = frozenset([1, 145])
    FOLLOW_TRANSACTION_in_begin_stmt2607 = frozenset([1])
    FOLLOW_set_in_commit_stmt2617 = frozenset([1, 145])
    FOLLOW_TRANSACTION_in_commit_stmt2626 = frozenset([1])
    FOLLOW_ROLLBACK_in_rollback_stmt2636 = frozenset([1, 145, 147])
    FOLLOW_TRANSACTION_in_rollback_stmt2639 = frozenset([1, 147])
    FOLLOW_TO_in_rollback_stmt2644 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_SAVEPOINT_in_rollback_stmt2647 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_rollback_stmt2653 = frozenset([1])
    FOLLOW_SAVEPOINT_in_savepoint_stmt2663 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_savepoint_stmt2667 = frozenset([1])
    FOLLOW_RELEASE_in_release_stmt2675 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_SAVEPOINT_in_release_stmt2678 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_release_stmt2684 = frozenset([1])
    FOLLOW_ON_in_table_conflict_clause2696 = frozenset([150])
    FOLLOW_CONFLICT_in_table_conflict_clause2699 = frozenset([100, 101, 102, 103, 111])
    FOLLOW_set_in_table_conflict_clause2702 = frozenset([1])
    FOLLOW_CREATE_in_create_virtual_table_stmt2729 = frozenset([152])
    FOLLOW_VIRTUAL_in_create_virtual_table_stmt2731 = frozenset([153])
    FOLLOW_TABLE_in_create_virtual_table_stmt2733 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_virtual_table_stmt2738 = frozenset([40])
    FOLLOW_DOT_in_create_virtual_table_stmt2740 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_virtual_table_stmt2746 = frozenset([133])
    FOLLOW_USING_in_create_virtual_table_stmt2750 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_virtual_table_stmt2754 = frozenset([1, 48])
    FOLLOW_LPAREN_in_create_virtual_table_stmt2757 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 52, 53, 54, 55, 56, 60, 61, 62, 63, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_column_def_in_create_virtual_table_stmt2759 = frozenset([49, 50])
    FOLLOW_COMMA_in_create_virtual_table_stmt2762 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 52, 53, 54, 55, 56, 60, 61, 62, 63, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_column_def_in_create_virtual_table_stmt2764 = frozenset([49, 50])
    FOLLOW_RPAREN_in_create_virtual_table_stmt2768 = frozenset([1])
    FOLLOW_CREATE_in_create_table_stmt2814 = frozenset([153, 154])
    FOLLOW_TEMPORARY_in_create_table_stmt2816 = frozenset([153])
    FOLLOW_TABLE_in_create_table_stmt2819 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_IF_in_create_table_stmt2822 = frozenset([43])
    FOLLOW_NOT_in_create_table_stmt2824 = frozenset([156])
    FOLLOW_EXISTS_in_create_table_stmt2826 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_table_stmt2833 = frozenset([40])
    FOLLOW_DOT_in_create_table_stmt2835 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_table_stmt2841 = frozenset([48, 83])
    FOLLOW_LPAREN_in_create_table_stmt2847 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 52, 53, 54, 55, 56, 60, 61, 62, 63, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_column_def_in_create_table_stmt2849 = frozenset([49, 50, 157, 158, 161, 162, 163])
    FOLLOW_COMMA_in_create_table_stmt2852 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 52, 53, 54, 55, 56, 60, 61, 62, 63, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_column_def_in_create_table_stmt2854 = frozenset([49, 50, 157, 158, 161, 162, 163])
    FOLLOW_COMMA_in_create_table_stmt2859 = frozenset([49, 157, 158, 161, 162, 163])
    FOLLOW_table_constraint_in_create_table_stmt2862 = frozenset([49, 50, 157, 158, 161, 162, 163])
    FOLLOW_RPAREN_in_create_table_stmt2866 = frozenset([1])
    FOLLOW_AS_in_create_table_stmt2872 = frozenset([121])
    FOLLOW_select_stmt_in_create_table_stmt2874 = frozenset([1])
    FOLLOW_id_column_def_in_column_def2930 = frozenset([1, 43, 55, 79, 80, 137, 157, 158, 161, 162, 164])
    FOLLOW_type_name_in_column_def2932 = frozenset([1, 43, 55, 79, 137, 157, 158, 161, 162, 164])
    FOLLOW_column_constraint_in_column_def2935 = frozenset([1, 43, 55, 79, 137, 157, 158, 161, 162, 164])
    FOLLOW_CONSTRAINT_in_column_constraint2961 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_column_constraint2965 = frozenset([43, 55, 79, 137, 157, 158, 161, 162, 164])
    FOLLOW_column_constraint_pk_in_column_constraint2973 = frozenset([1])
    FOLLOW_column_constraint_not_null_in_column_constraint2979 = frozenset([1])
    FOLLOW_column_constraint_null_in_column_constraint2985 = frozenset([1])
    FOLLOW_column_constraint_unique_in_column_constraint2991 = frozenset([1])
    FOLLOW_column_constraint_check_in_column_constraint2997 = frozenset([1])
    FOLLOW_column_constraint_default_in_column_constraint3003 = frozenset([1])
    FOLLOW_column_constraint_collate_in_column_constraint3009 = frozenset([1])
    FOLLOW_fk_clause_in_column_constraint3015 = frozenset([1])
    FOLLOW_PRIMARY_in_column_constraint_pk3075 = frozenset([159])
    FOLLOW_KEY_in_column_constraint_pk3078 = frozenset([1, 112, 113, 132, 160])
    FOLLOW_set_in_column_constraint_pk3081 = frozenset([1, 132, 160])
    FOLLOW_table_conflict_clause_in_column_constraint_pk3090 = frozenset([1, 160])
    FOLLOW_AUTOINCREMENT_in_column_constraint_pk3094 = frozenset([1])
    FOLLOW_NOT_in_column_constraint_not_null3103 = frozenset([55])
    FOLLOW_NULL_in_column_constraint_not_null3105 = frozenset([1, 132])
    FOLLOW_table_conflict_clause_in_column_constraint_not_null3107 = frozenset([1])
    FOLLOW_NULL_in_column_constraint_null3124 = frozenset([1, 132])
    FOLLOW_table_conflict_clause_in_column_constraint_null3126 = frozenset([1])
    FOLLOW_UNIQUE_in_column_constraint_unique3143 = frozenset([1, 132])
    FOLLOW_table_conflict_clause_in_column_constraint_unique3146 = frozenset([1])
    FOLLOW_CHECK_in_column_constraint_check3154 = frozenset([48])
    FOLLOW_LPAREN_in_column_constraint_check3157 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_column_constraint_check3160 = frozenset([50])
    FOLLOW_RPAREN_in_column_constraint_check3162 = frozenset([1])
    FOLLOW_INTEGER_in_numeric_literal_value3173 = frozenset([1])
    FOLLOW_FLOAT_in_numeric_literal_value3187 = frozenset([1])
    FOLLOW_set_in_signed_default_number3205 = frozenset([89, 90])
    FOLLOW_numeric_literal_value_in_signed_default_number3214 = frozenset([1])
    FOLLOW_DEFAULT_in_column_constraint_default3222 = frozenset([48, 55, 72, 73, 89, 90, 91, 92, 93, 94, 95])
    FOLLOW_signed_default_number_in_column_constraint_default3226 = frozenset([1])
    FOLLOW_literal_value_in_column_constraint_default3230 = frozenset([1])
    FOLLOW_LPAREN_in_column_constraint_default3234 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_column_constraint_default3237 = frozenset([50])
    FOLLOW_RPAREN_in_column_constraint_default3239 = frozenset([1])
    FOLLOW_COLLATE_in_column_constraint_collate3248 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_column_constraint_collate3253 = frozenset([1])
    FOLLOW_CONSTRAINT_in_table_constraint3262 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_table_constraint3266 = frozenset([49, 157, 158, 161, 162, 163])
    FOLLOW_table_constraint_pk_in_table_constraint3274 = frozenset([1])
    FOLLOW_table_constraint_unique_in_table_constraint3280 = frozenset([1])
    FOLLOW_table_constraint_check_in_table_constraint3286 = frozenset([1])
    FOLLOW_table_constraint_fk_in_table_constraint3292 = frozenset([1])
    FOLLOW_PRIMARY_in_table_constraint_pk3332 = frozenset([159])
    FOLLOW_KEY_in_table_constraint_pk3334 = frozenset([48])
    FOLLOW_LPAREN_in_table_constraint_pk3338 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_table_constraint_pk3342 = frozenset([49, 50])
    FOLLOW_COMMA_in_table_constraint_pk3345 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_table_constraint_pk3349 = frozenset([49, 50])
    FOLLOW_RPAREN_in_table_constraint_pk3353 = frozenset([1, 132])
    FOLLOW_table_conflict_clause_in_table_constraint_pk3355 = frozenset([1])
    FOLLOW_UNIQUE_in_table_constraint_unique3380 = frozenset([48])
    FOLLOW_LPAREN_in_table_constraint_unique3384 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_table_constraint_unique3388 = frozenset([49, 50])
    FOLLOW_COMMA_in_table_constraint_unique3391 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_table_constraint_unique3395 = frozenset([49, 50])
    FOLLOW_RPAREN_in_table_constraint_unique3399 = frozenset([1, 132])
    FOLLOW_table_conflict_clause_in_table_constraint_unique3401 = frozenset([1])
    FOLLOW_CHECK_in_table_constraint_check3426 = frozenset([48])
    FOLLOW_LPAREN_in_table_constraint_check3429 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_table_constraint_check3432 = frozenset([50])
    FOLLOW_RPAREN_in_table_constraint_check3434 = frozenset([1])
    FOLLOW_FOREIGN_in_table_constraint_fk3442 = frozenset([159])
    FOLLOW_KEY_in_table_constraint_fk3444 = frozenset([48])
    FOLLOW_LPAREN_in_table_constraint_fk3446 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_table_constraint_fk3450 = frozenset([49, 50])
    FOLLOW_COMMA_in_table_constraint_fk3453 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_table_constraint_fk3457 = frozenset([49, 50])
    FOLLOW_RPAREN_in_table_constraint_fk3461 = frozenset([43, 55, 79, 137, 157, 158, 161, 162, 164])
    FOLLOW_fk_clause_in_table_constraint_fk3463 = frozenset([1])
    FOLLOW_REFERENCES_in_fk_clause3486 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_fk_clause3490 = frozenset([1, 43, 48, 63, 132, 167])
    FOLLOW_LPAREN_in_fk_clause3493 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_fk_clause3497 = frozenset([49, 50])
    FOLLOW_COMMA_in_fk_clause3500 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_fk_clause3504 = frozenset([49, 50])
    FOLLOW_RPAREN_in_fk_clause3508 = frozenset([1, 43, 63, 132, 167])
    FOLLOW_fk_clause_action_in_fk_clause3514 = frozenset([1, 43, 63, 132, 167])
    FOLLOW_fk_clause_deferrable_in_fk_clause3517 = frozenset([1])
    FOLLOW_ON_in_fk_clause_action3551 = frozenset([134, 138, 140])
    FOLLOW_set_in_fk_clause_action3554 = frozenset([139, 165, 166])
    FOLLOW_SET_in_fk_clause_action3567 = frozenset([55])
    FOLLOW_NULL_in_fk_clause_action3570 = frozenset([1])
    FOLLOW_SET_in_fk_clause_action3574 = frozenset([137])
    FOLLOW_DEFAULT_in_fk_clause_action3577 = frozenset([1])
    FOLLOW_CASCADE_in_fk_clause_action3581 = frozenset([1])
    FOLLOW_RESTRICT_in_fk_clause_action3585 = frozenset([1])
    FOLLOW_MATCH_in_fk_clause_action3592 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_fk_clause_action3595 = frozenset([1])
    FOLLOW_NOT_in_fk_clause_deferrable3603 = frozenset([167])
    FOLLOW_DEFERRABLE_in_fk_clause_deferrable3607 = frozenset([1, 168])
    FOLLOW_INITIALLY_in_fk_clause_deferrable3611 = frozenset([142])
    FOLLOW_DEFERRED_in_fk_clause_deferrable3614 = frozenset([1])
    FOLLOW_INITIALLY_in_fk_clause_deferrable3618 = frozenset([143])
    FOLLOW_IMMEDIATE_in_fk_clause_deferrable3621 = frozenset([1])
    FOLLOW_DROP_in_drop_table_stmt3631 = frozenset([153])
    FOLLOW_TABLE_in_drop_table_stmt3633 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_IF_in_drop_table_stmt3636 = frozenset([156])
    FOLLOW_EXISTS_in_drop_table_stmt3638 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_drop_table_stmt3645 = frozenset([40])
    FOLLOW_DOT_in_drop_table_stmt3647 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_drop_table_stmt3653 = frozenset([1])
    FOLLOW_ALTER_in_alter_table_stmt3683 = frozenset([153])
    FOLLOW_TABLE_in_alter_table_stmt3685 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_alter_table_stmt3690 = frozenset([40])
    FOLLOW_DOT_in_alter_table_stmt3692 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_alter_table_stmt3698 = frozenset([171, 172])
    FOLLOW_RENAME_in_alter_table_stmt3701 = frozenset([147])
    FOLLOW_TO_in_alter_table_stmt3703 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_alter_table_stmt3707 = frozenset([1])
    FOLLOW_ADD_in_alter_table_stmt3711 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 52, 53, 54, 55, 56, 60, 61, 62, 63, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_COLUMN_in_alter_table_stmt3714 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 52, 53, 54, 55, 56, 60, 61, 62, 63, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_column_def_in_alter_table_stmt3718 = frozenset([1])
    FOLLOW_CREATE_in_create_view_stmt3727 = frozenset([154, 174])
    FOLLOW_TEMPORARY_in_create_view_stmt3729 = frozenset([174])
    FOLLOW_VIEW_in_create_view_stmt3732 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_IF_in_create_view_stmt3735 = frozenset([43])
    FOLLOW_NOT_in_create_view_stmt3737 = frozenset([156])
    FOLLOW_EXISTS_in_create_view_stmt3739 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_view_stmt3746 = frozenset([40])
    FOLLOW_DOT_in_create_view_stmt3748 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_view_stmt3754 = frozenset([83])
    FOLLOW_AS_in_create_view_stmt3756 = frozenset([121])
    FOLLOW_select_stmt_in_create_view_stmt3760 = frozenset([1])
    FOLLOW_DROP_in_drop_view_stmt3801 = frozenset([174])
    FOLLOW_VIEW_in_drop_view_stmt3803 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_IF_in_drop_view_stmt3806 = frozenset([156])
    FOLLOW_EXISTS_in_drop_view_stmt3808 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_drop_view_stmt3815 = frozenset([40])
    FOLLOW_DOT_in_drop_view_stmt3817 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_drop_view_stmt3823 = frozenset([1])
    FOLLOW_CREATE_in_create_index_stmt3831 = frozenset([161, 175])
    FOLLOW_UNIQUE_in_create_index_stmt3834 = frozenset([175])
    FOLLOW_INDEX_in_create_index_stmt3838 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_IF_in_create_index_stmt3841 = frozenset([43])
    FOLLOW_NOT_in_create_index_stmt3843 = frozenset([156])
    FOLLOW_EXISTS_in_create_index_stmt3845 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_index_stmt3852 = frozenset([40])
    FOLLOW_DOT_in_create_index_stmt3854 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_index_stmt3860 = frozenset([132])
    FOLLOW_ON_in_create_index_stmt3864 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_index_stmt3868 = frozenset([48])
    FOLLOW_LPAREN_in_create_index_stmt3870 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_indexed_column_in_create_index_stmt3874 = frozenset([49, 50])
    FOLLOW_COMMA_in_create_index_stmt3877 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_indexed_column_in_create_index_stmt3881 = frozenset([49, 50])
    FOLLOW_RPAREN_in_create_index_stmt3885 = frozenset([1])
    FOLLOW_id_in_indexed_column3931 = frozenset([1, 79, 112, 113])
    FOLLOW_COLLATE_in_indexed_column3934 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_indexed_column3938 = frozenset([1, 112, 113])
    FOLLOW_ASC_in_indexed_column3943 = frozenset([1])
    FOLLOW_DESC_in_indexed_column3947 = frozenset([1])
    FOLLOW_DROP_in_drop_index_stmt3978 = frozenset([175])
    FOLLOW_INDEX_in_drop_index_stmt3980 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_IF_in_drop_index_stmt3983 = frozenset([156])
    FOLLOW_EXISTS_in_drop_index_stmt3985 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_drop_index_stmt3992 = frozenset([40])
    FOLLOW_DOT_in_drop_index_stmt3994 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_drop_index_stmt4000 = frozenset([1])
    FOLLOW_CREATE_in_create_trigger_stmt4030 = frozenset([154, 176])
    FOLLOW_TEMPORARY_in_create_trigger_stmt4032 = frozenset([176])
    FOLLOW_TRIGGER_in_create_trigger_stmt4035 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_IF_in_create_trigger_stmt4038 = frozenset([43])
    FOLLOW_NOT_in_create_trigger_stmt4040 = frozenset([156])
    FOLLOW_EXISTS_in_create_trigger_stmt4042 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_trigger_stmt4049 = frozenset([40])
    FOLLOW_DOT_in_create_trigger_stmt4051 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_trigger_stmt4057 = frozenset([134, 138, 140, 177, 178, 179])
    FOLLOW_BEFORE_in_create_trigger_stmt4062 = frozenset([134, 138, 140])
    FOLLOW_AFTER_in_create_trigger_stmt4066 = frozenset([134, 138, 140])
    FOLLOW_INSTEAD_in_create_trigger_stmt4070 = frozenset([180])
    FOLLOW_OF_in_create_trigger_stmt4072 = frozenset([134, 138, 140])
    FOLLOW_DELETE_in_create_trigger_stmt4077 = frozenset([132])
    FOLLOW_INSERT_in_create_trigger_stmt4081 = frozenset([132])
    FOLLOW_UPDATE_in_create_trigger_stmt4085 = frozenset([132, 180])
    FOLLOW_OF_in_create_trigger_stmt4088 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_trigger_stmt4092 = frozenset([49, 132])
    FOLLOW_COMMA_in_create_trigger_stmt4095 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_trigger_stmt4099 = frozenset([49, 132])
    FOLLOW_ON_in_create_trigger_stmt4108 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_create_trigger_stmt4112 = frozenset([87, 141, 181])
    FOLLOW_FOR_in_create_trigger_stmt4115 = frozenset([182])
    FOLLOW_EACH_in_create_trigger_stmt4117 = frozenset([183])
    FOLLOW_ROW_in_create_trigger_stmt4119 = frozenset([87, 141])
    FOLLOW_WHEN_in_create_trigger_stmt4124 = frozenset([37, 38, 39, 41, 42, 43, 44, 45, 46, 48, 54, 55, 56, 72, 73, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_expr_in_create_trigger_stmt4126 = frozenset([141])
    FOLLOW_BEGIN_in_create_trigger_stmt4132 = frozenset([111, 121, 134, 138, 140])
    FOLLOW_update_stmt_in_create_trigger_stmt4136 = frozenset([36])
    FOLLOW_insert_stmt_in_create_trigger_stmt4140 = frozenset([36])
    FOLLOW_delete_stmt_in_create_trigger_stmt4144 = frozenset([36])
    FOLLOW_select_stmt_in_create_trigger_stmt4148 = frozenset([36])
    FOLLOW_SEMI_in_create_trigger_stmt4151 = frozenset([86, 111, 121, 134, 138, 140])
    FOLLOW_END_in_create_trigger_stmt4155 = frozenset([1])
    FOLLOW_DROP_in_drop_trigger_stmt4188 = frozenset([176])
    FOLLOW_TRIGGER_in_drop_trigger_stmt4190 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_IF_in_drop_trigger_stmt4193 = frozenset([156])
    FOLLOW_EXISTS_in_drop_trigger_stmt4195 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_drop_trigger_stmt4202 = frozenset([40])
    FOLLOW_DOT_in_drop_trigger_stmt4204 = frozenset([37, 38, 39, 41, 42, 44, 45, 46, 54, 55, 56, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 91, 93, 94, 95, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183])
    FOLLOW_id_in_drop_trigger_stmt4210 = frozenset([1])
    FOLLOW_set_in_id_core4220 = frozenset([1])
    FOLLOW_id_core_in_id4239 = frozenset([1])
    FOLLOW_keyword_in_id4243 = frozenset([1])
    FOLLOW_set_in_keyword4250 = frozenset([1])
    FOLLOW_id_core_in_id_column_def4917 = frozenset([1])
    FOLLOW_keyword_column_def_in_id_column_def4921 = frozenset([1])
    FOLLOW_set_in_keyword_column_def4928 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SQLiteLexer", SQLiteParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
