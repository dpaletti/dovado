# Generated from VerilogPreParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,246,317,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,
        0,5,0,94,8,0,10,0,12,0,97,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,116,8,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,
        12,1,12,5,12,155,8,12,10,12,12,12,158,9,12,1,13,1,13,1,14,1,14,1,
        14,1,14,1,14,5,14,167,8,14,10,14,12,14,170,9,14,1,14,3,14,173,8,
        14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,5,15,182,8,15,10,15,12,15,
        185,9,15,1,15,3,15,188,8,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,
        16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,
        20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,25,1,
        25,1,25,1,25,5,25,226,8,25,10,25,12,25,229,9,25,1,26,1,26,1,27,1,
        27,1,27,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,5,29,244,8,29,10,
        29,12,29,247,9,29,3,29,249,8,29,1,30,1,30,1,30,3,30,254,8,30,1,30,
        1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,33,1,33,5,33,266,8,33,10,33,
        12,33,269,9,33,1,33,1,33,1,33,1,33,1,33,3,33,276,8,33,1,34,1,34,
        1,34,1,35,1,35,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,
        1,39,1,39,1,39,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,42,
        1,42,1,42,1,42,1,43,1,43,1,44,1,44,1,44,1,44,1,45,1,45,1,45,0,0,
        46,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,
        88,90,0,0,306,0,95,1,0,0,0,2,115,1,0,0,0,4,117,1,0,0,0,6,123,1,0,
        0,0,8,126,1,0,0,0,10,130,1,0,0,0,12,132,1,0,0,0,14,136,1,0,0,0,16,
        141,1,0,0,0,18,144,1,0,0,0,20,147,1,0,0,0,22,150,1,0,0,0,24,156,
        1,0,0,0,26,159,1,0,0,0,28,161,1,0,0,0,30,176,1,0,0,0,32,191,1,0,
        0,0,34,197,1,0,0,0,36,199,1,0,0,0,38,207,1,0,0,0,40,209,1,0,0,0,
        42,211,1,0,0,0,44,213,1,0,0,0,46,215,1,0,0,0,48,217,1,0,0,0,50,227,
        1,0,0,0,52,230,1,0,0,0,54,232,1,0,0,0,56,235,1,0,0,0,58,237,1,0,
        0,0,60,253,1,0,0,0,62,257,1,0,0,0,64,259,1,0,0,0,66,275,1,0,0,0,
        68,277,1,0,0,0,70,280,1,0,0,0,72,282,1,0,0,0,74,284,1,0,0,0,76,289,
        1,0,0,0,78,292,1,0,0,0,80,295,1,0,0,0,82,298,1,0,0,0,84,304,1,0,
        0,0,86,308,1,0,0,0,88,310,1,0,0,0,90,314,1,0,0,0,92,94,3,2,1,0,93,
        92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,1,1,0,0,
        0,97,95,1,0,0,0,98,116,3,4,2,0,99,116,3,6,3,0,100,116,3,8,4,0,101,
        116,3,16,8,0,102,116,3,18,9,0,103,116,3,28,14,0,104,116,3,30,15,
        0,105,116,3,32,16,0,106,116,3,36,18,0,107,116,3,54,27,0,108,116,
        3,58,29,0,109,116,3,68,34,0,110,116,3,74,37,0,111,116,3,76,38,0,
        112,116,3,82,41,0,113,116,3,84,42,0,114,116,3,88,44,0,115,98,1,0,
        0,0,115,99,1,0,0,0,115,100,1,0,0,0,115,101,1,0,0,0,115,102,1,0,0,
        0,115,103,1,0,0,0,115,104,1,0,0,0,115,105,1,0,0,0,115,106,1,0,0,
        0,115,107,1,0,0,0,115,108,1,0,0,0,115,109,1,0,0,0,115,110,1,0,0,
        0,115,111,1,0,0,0,115,112,1,0,0,0,115,113,1,0,0,0,115,114,1,0,0,
        0,116,3,1,0,0,0,117,118,5,71,0,0,118,119,5,211,0,0,119,120,5,44,
        0,0,120,121,3,90,45,0,121,122,5,44,0,0,122,5,1,0,0,0,123,124,5,71,
        0,0,124,125,5,212,0,0,125,7,1,0,0,0,126,127,5,71,0,0,127,128,5,213,
        0,0,128,129,3,10,5,0,129,9,1,0,0,0,130,131,5,232,0,0,131,11,1,0,
        0,0,132,133,5,71,0,0,133,134,5,215,0,0,134,135,3,24,12,0,135,13,
        1,0,0,0,136,137,5,71,0,0,137,138,5,216,0,0,138,139,3,44,22,0,139,
        140,3,24,12,0,140,15,1,0,0,0,141,142,5,71,0,0,142,143,5,217,0,0,
        143,17,1,0,0,0,144,145,5,71,0,0,145,146,5,218,0,0,146,19,1,0,0,0,
        147,148,5,71,0,0,148,149,5,219,0,0,149,21,1,0,0,0,150,151,5,236,
        0,0,151,23,1,0,0,0,152,155,3,70,35,0,153,155,3,2,1,0,154,152,1,0,
        0,0,154,153,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,
        0,0,157,25,1,0,0,0,158,156,1,0,0,0,159,160,5,197,0,0,160,27,1,0,
        0,0,161,162,5,71,0,0,162,163,5,220,0,0,163,164,3,44,22,0,164,168,
        3,24,12,0,165,167,3,14,7,0,166,165,1,0,0,0,167,170,1,0,0,0,168,166,
        1,0,0,0,168,169,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,171,173,
        3,12,6,0,172,171,1,0,0,0,172,173,1,0,0,0,173,174,1,0,0,0,174,175,
        3,20,10,0,175,29,1,0,0,0,176,177,5,71,0,0,177,178,5,221,0,0,178,
        179,3,44,22,0,179,183,3,24,12,0,180,182,3,14,7,0,181,180,1,0,0,0,
        182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,187,1,0,0,0,
        185,183,1,0,0,0,186,188,3,12,6,0,187,186,1,0,0,0,187,188,1,0,0,0,
        188,189,1,0,0,0,189,190,3,20,10,0,190,31,1,0,0,0,191,192,5,71,0,
        0,192,193,5,222,0,0,193,194,5,44,0,0,194,195,3,22,11,0,195,196,5,
        44,0,0,196,33,1,0,0,0,197,198,5,200,0,0,198,35,1,0,0,0,199,200,5,
        71,0,0,200,201,5,223,0,0,201,202,3,56,28,0,202,203,5,44,0,0,203,
        204,3,22,11,0,204,205,5,44,0,0,205,206,3,34,17,0,206,37,1,0,0,0,
        207,208,5,237,0,0,208,39,1,0,0,0,209,210,5,238,0,0,210,41,1,0,0,
        0,211,212,5,239,0,0,212,43,1,0,0,0,213,214,5,246,0,0,214,45,1,0,
        0,0,215,216,5,234,0,0,216,47,1,0,0,0,217,218,5,240,0,0,218,49,1,
        0,0,0,219,226,5,241,0,0,220,226,3,38,19,0,221,226,3,40,20,0,222,
        226,3,42,21,0,223,226,3,48,24,0,224,226,3,72,36,0,225,219,1,0,0,
        0,225,220,1,0,0,0,225,221,1,0,0,0,225,222,1,0,0,0,225,223,1,0,0,
        0,225,224,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,
        0,228,51,1,0,0,0,229,227,1,0,0,0,230,231,5,230,0,0,231,53,1,0,0,
        0,232,233,5,71,0,0,233,234,5,224,0,0,234,55,1,0,0,0,235,236,5,200,
        0,0,236,57,1,0,0,0,237,238,5,71,0,0,238,239,5,225,0,0,239,248,3,
        64,32,0,240,245,3,60,30,0,241,242,5,24,0,0,242,244,3,60,30,0,243,
        241,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,
        249,1,0,0,0,247,245,1,0,0,0,248,240,1,0,0,0,248,249,1,0,0,0,249,
        59,1,0,0,0,250,251,3,62,31,0,251,252,5,61,0,0,252,254,1,0,0,0,253,
        250,1,0,0,0,253,254,1,0,0,0,254,255,1,0,0,0,255,256,3,66,33,0,256,
        61,1,0,0,0,257,258,5,197,0,0,258,63,1,0,0,0,259,260,5,197,0,0,260,
        65,1,0,0,0,261,262,5,96,0,0,262,267,3,60,30,0,263,264,5,24,0,0,264,
        266,3,60,30,0,265,263,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,
        268,1,0,0,0,268,270,1,0,0,0,269,267,1,0,0,0,270,271,5,142,0,0,271,
        276,1,0,0,0,272,276,3,56,28,0,273,276,3,72,36,0,274,276,3,26,13,
        0,275,261,1,0,0,0,275,272,1,0,0,0,275,273,1,0,0,0,275,274,1,0,0,
        0,276,67,1,0,0,0,277,278,5,71,0,0,278,279,5,226,0,0,279,69,1,0,0,
        0,280,281,5,242,0,0,281,71,1,0,0,0,282,283,5,198,0,0,283,73,1,0,
        0,0,284,285,5,71,0,0,285,286,5,214,0,0,286,287,3,46,23,0,287,288,
        3,50,25,0,288,75,1,0,0,0,289,290,5,71,0,0,290,291,3,52,26,0,291,
        77,1,0,0,0,292,293,5,244,0,0,293,294,5,243,0,0,294,79,1,0,0,0,295,
        296,5,244,0,0,296,297,5,243,0,0,297,81,1,0,0,0,298,299,5,71,0,0,
        299,300,5,227,0,0,300,301,3,80,40,0,301,302,5,151,0,0,302,303,3,
        78,39,0,303,83,1,0,0,0,304,305,5,71,0,0,305,306,5,228,0,0,306,307,
        3,86,43,0,307,85,1,0,0,0,308,309,5,245,0,0,309,87,1,0,0,0,310,311,
        5,71,0,0,311,312,5,229,0,0,312,313,3,44,22,0,313,89,1,0,0,0,314,
        315,5,231,0,0,315,91,1,0,0,0,15,95,115,154,156,168,172,183,187,225,
        227,245,248,253,267,275
    ]

class VerilogPreParser ( Parser ):

    grammarFileName = "VerilogPreParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'always'", "'&'", "'&&'", "'&&&'", "'and'", 
                     "'*'", "'**'", "'*>'", "'assign'", "'@'", "'automatic'", 
                     "'begin'", "'buf'", "'bufif1'", "'bufif0'", "'^'", 
                     "'case'", "'casex'", "'casez'", "'^~'", "'cell'", "':'", 
                     "'cmos'", "','", "'config'", "'deassign'", "'default'", 
                     "'defparam'", "'design'", "'disable'", "'$'", "'$fullskew'", 
                     "'$hold'", "'$nochange'", "'$period'", "'$recovery'", 
                     "'$recrem'", "'$removal'", "'$setup'", "'$setuphold'", 
                     "'$skew'", "'$timeskew'", "'$width'", "'\"'", "'.'", 
                     "'edge'", "'else'", "'!'", "'!='", "'!=='", "'end'", 
                     "'endcase'", "'endconfig'", "'endfunction'", "'endgenerate'", 
                     "'endmodule'", "'endprimitive'", "'endspecify'", "'endtable'", 
                     "'endtask'", "'='", "'=='", "'==='", "'=>'", "'event'", 
                     "'for'", "'force'", "'forever'", "'fork'", "'function'", 
                     "<INVALID>", "'generate'", "'genvar'", "'>'", "'>='", 
                     "'>>'", "'>>>'", "'#'", "'highz1'", "'highz0'", "'if'", 
                     "'ifnone'", "'include'", "'initial'", "'inout'", "'input'", 
                     "'instance'", "'integer'", "'join'", "'large'", "'['", 
                     "'{'", "'liblist'", "'library'", "'localparam'", "'('", 
                     "'<'", "'<='", "'<<'", "'<<<'", "'macromodule'", "'medium'", 
                     "'-'", "'-:'", "'->'", "'-incdir'", "'%'", "'module'", 
                     "'nand'", "'negedge'", "'nmos'", "'nor'", "'noshowcancelled'", 
                     "'not'", "'notif1'", "'notif0'", "'or'", "'output'", 
                     "'parameter'", "'PATHPULSE$'", "'+'", "'+:'", "'pmos'", 
                     "'posedge'", "'primitive'", "'pulldown'", "'pull1'", 
                     "'pullup'", "'pull0'", "'pulsestyle_ondetect'", "'pulsestyle_onevent'", 
                     "'?'", "']'", "'}'", "'rcmos'", "'real'", "'realtime'", 
                     "'reg'", "'release'", "'repeat'", "'rnmos'", "')'", 
                     "'rpmos'", "'rtran'", "'rtranif1'", "'rtranif0'", "';'", 
                     "'scalared'", "'showcancelled'", "'signed'", "'/'", 
                     "'small'", "'specify'", "'specparam'", "'strong1'", 
                     "'strong0'", "'supply1'", "'supply0'", "'table'", "'task'", 
                     "'~'", "'~&'", "'~^'", "'time'", "'~|'", "'tran'", 
                     "'tranif1'", "'tranif0'", "'tri'", "'triand'", "'tri1'", 
                     "'trior'", "'trireg'", "'tri0'", "'use'", "'uwire'", 
                     "'vectored'", "'|'", "'||'", "'wait'", "'wand'", "'weak1'", 
                     "'weak0'", "'while'", "'wire'", "'wor'", "'xnor'", 
                     "'xor'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'celldefine'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'end_keywords'", "'endcelldefine'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'nounconnected_drive'", 
                     "<INVALID>", "'resetall'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'``'", "<INVALID>", "'`\\`\"'", "'`\"'" ]

    symbolicNames = [ "<INVALID>", "ALWAYS", "AM", "AMAM", "AMAMAM", "AND", 
                      "AS", "ASAS", "ASGT", "ASSIGN", "AT", "AUTOMATIC", 
                      "BEGIN", "BUF", "BUFIFONE", "BUFIFZERO", "CA", "CASE", 
                      "CASEX", "CASEZ", "CATI", "CELL", "CL", "CMOS", "CO", 
                      "CONFIG", "DEASSIGN", "DEFAULT", "DEFPARAM", "DESIGN", 
                      "DISABLE", "DL", "DLFULLSKEW", "DLHOLD", "DLNOCHANGE", 
                      "DLPERIOD", "DLRECOVERY", "DLRECREM", "DLREMOVAL", 
                      "DLSETUP", "DLSETUPHOLD", "DLSKEW", "DLTIMESKEW", 
                      "DLWIDTH", "DQ", "DT", "EDGE", "ELSE", "EM", "EMEQ", 
                      "EMEQEQ", "END", "ENDCASE", "ENDCONFIG", "ENDFUNCTION", 
                      "ENDGENERATE", "ENDMODULE", "ENDPRIMITIVE", "ENDSPECIFY", 
                      "ENDTABLE", "ENDTASK", "EQ", "EQEQ", "EQEQEQ", "EQGT", 
                      "EVENT", "FOR", "FORCE", "FOREVER", "FORK", "FUNCTION", 
                      "GA", "GENERATE", "GENVAR", "GT", "GTEQ", "GTGT", 
                      "GTGTGT", "HA", "HIGHZONE", "HIGHZZERO", "IF", "IFNONE", 
                      "INCLUDE", "INITIAL", "INOUT", "INPUT", "INSTANCE", 
                      "INTEGER", "JOIN", "LARGE", "LB", "LC", "LIBLIST", 
                      "LIBRARY", "LOCALPARAM", "LP", "LT", "LTEQ", "LTLT", 
                      "LTLTLT", "MACROMODULE", "MEDIUM", "MI", "MICL", "MIGT", 
                      "MIINCDIR", "MO", "MODULE", "NAND", "NEGEDGE", "NMOS", 
                      "NOR", "NOSHOWCANCELLED", "NOT", "NOTIFONE", "NOTIFZERO", 
                      "OR", "OUTPUT", "PARAMETER", "PATHPULSEDL", "PL", 
                      "PLCL", "PMOS", "POSEDGE", "PRIMITIVE", "PULLDOWN", 
                      "PULLONE", "PULLUP", "PULLZERO", "PULSESTYLE_ONDETECT", 
                      "PULSESTYLE_ONEVENT", "QM", "RB", "RC", "RCMOS", "REAL", 
                      "REALTIME", "REG", "RELEASE", "REPEAT", "RNMOS", "RP", 
                      "RPMOS", "RTRAN", "RTRANIFONE", "RTRANIFZERO", "SC", 
                      "SCALARED", "SHOWCANCELLED", "SIGNED", "SL", "SMALL", 
                      "SPECIFY", "SPECPARAM", "STRONGONE", "STRONGZERO", 
                      "SUPPLYONE", "SUPPLYZERO", "TABLE", "TASK", "TI", 
                      "TIAM", "TICA", "TIME", "TIVL", "TRAN", "TRANIFONE", 
                      "TRANIFZERO", "TRI", "TRIAND", "TRIONE", "TRIOR", 
                      "TRIREG", "TRIZERO", "USE", "UWIRE", "VECTORED", "VL", 
                      "VLVL", "WAIT", "WAND", "WEAKONE", "WEAKZERO", "WHILE", 
                      "WIRE", "WOR", "XNOR", "XOR", "BINARY_BASE", "COMMENT", 
                      "DECIMAL_BASE", "ESCAPED_IDENTIFIER", "EXPONENTIAL_NUMBER", 
                      "FIXED_POINT_NUMBER", "HEX_BASE", "OCTAL_BASE", "SIMPLE_IDENTIFIER", 
                      "STRING", "SYSTEM_TF_IDENTIFIER", "UNSIGNED_NUMBER", 
                      "WHITE_SPACE", "BINARY_VALUE", "X_OR_Z_UNDERSCORE", 
                      "EDGE_DESCRIPTOR", "HEX_VALUE", "FILE_PATH_SPEC", 
                      "OCTAL_VALUE", "EDGE_SYMBOL", "LEVEL_ONLY_SYMBOL", 
                      "OUTPUT_OR_LEVEL_SYMBOL", "BEGIN_KEYWORDS_DIRECTIVE", 
                      "CELLDEFINE_DIRECTIVE", "DEFAULT_NETTYPE_DIRECTIVE", 
                      "DEFINE_DIRECTIVE", "ELSE_DIRECTIVE", "ELSIF_DIRECTIVE", 
                      "END_KEYWORDS_DIRECTIVE", "ENDCELLDEFINE_DIRECTIVE", 
                      "ENDIF_DIRECTIVE", "IFDEF_DIRECTIVE", "IFNDEF_DIRECTIVE", 
                      "INCLUDE_DIRECTIVE", "LINE_DIRECTIVE", "NOUNCONNECTED_DRIVE_DIRECTIVE", 
                      "PRAGMA_DIRECTIVE", "RESETALL_DIRECTIVE", "TIMESCALE_DIRECTIVE", 
                      "UNCONNECTED_DRIVE_DIRECTIVE", "UNDEF_DIRECTIVE", 
                      "MACRO_USAGE", "VERSION_SPECIFIER", "DEFAULT_NETTYPE_VALUE", 
                      "COMMENT_5", "MACRO_NAME", "WHITE_SPACE_7", "FILENAME", 
                      "MACRO_DELIMITER", "MACRO_ESC_NEWLINE", "MACRO_ESC_QUOTE", 
                      "MACRO_QUOTE", "MACRO_TEXT", "SOURCE_TEXT", "TIME_UNIT", 
                      "TIME_VALUE", "UNCONNECTED_DRIVE_VALUE", "MACRO_IDENTIFIER" ]

    RULE_source_text = 0
    RULE_compiler_directive = 1
    RULE_begin_keywords_directive = 2
    RULE_celldefine_directive = 3
    RULE_default_nettype_directive = 4
    RULE_default_nettype_value = 5
    RULE_else_directive = 6
    RULE_elsif_directive = 7
    RULE_end_keywords_directive = 8
    RULE_endcelldefine_directive = 9
    RULE_endif_directive = 10
    RULE_filename = 11
    RULE_group_of_lines = 12
    RULE_identifier = 13
    RULE_ifdef_directive = 14
    RULE_ifndef_directive = 15
    RULE_include_directive = 16
    RULE_level = 17
    RULE_line_directive = 18
    RULE_macro_delimiter = 19
    RULE_macro_esc_newline = 20
    RULE_macro_esc_quote = 21
    RULE_macro_identifier = 22
    RULE_macro_name = 23
    RULE_macro_quote = 24
    RULE_macro_text = 25
    RULE_macro_usage = 26
    RULE_nounconnected_drive_directive = 27
    RULE_number = 28
    RULE_pragma_directive = 29
    RULE_pragma_expression = 30
    RULE_pragma_keyword = 31
    RULE_pragma_name = 32
    RULE_pragma_value = 33
    RULE_resetall_directive = 34
    RULE_source_text_ = 35
    RULE_string_ = 36
    RULE_text_macro_definition = 37
    RULE_text_macro_usage = 38
    RULE_time_precision = 39
    RULE_time_unit = 40
    RULE_timescale_directive = 41
    RULE_unconnected_drive_directive = 42
    RULE_unconnected_drive_value = 43
    RULE_undef_directive = 44
    RULE_version_specifier = 45

    ruleNames =  [ "source_text", "compiler_directive", "begin_keywords_directive", 
                   "celldefine_directive", "default_nettype_directive", 
                   "default_nettype_value", "else_directive", "elsif_directive", 
                   "end_keywords_directive", "endcelldefine_directive", 
                   "endif_directive", "filename", "group_of_lines", "identifier", 
                   "ifdef_directive", "ifndef_directive", "include_directive", 
                   "level", "line_directive", "macro_delimiter", "macro_esc_newline", 
                   "macro_esc_quote", "macro_identifier", "macro_name", 
                   "macro_quote", "macro_text", "macro_usage", "nounconnected_drive_directive", 
                   "number", "pragma_directive", "pragma_expression", "pragma_keyword", 
                   "pragma_name", "pragma_value", "resetall_directive", 
                   "source_text_", "string_", "text_macro_definition", "text_macro_usage", 
                   "time_precision", "time_unit", "timescale_directive", 
                   "unconnected_drive_directive", "unconnected_drive_value", 
                   "undef_directive", "version_specifier" ]

    EOF = Token.EOF
    ALWAYS=1
    AM=2
    AMAM=3
    AMAMAM=4
    AND=5
    AS=6
    ASAS=7
    ASGT=8
    ASSIGN=9
    AT=10
    AUTOMATIC=11
    BEGIN=12
    BUF=13
    BUFIFONE=14
    BUFIFZERO=15
    CA=16
    CASE=17
    CASEX=18
    CASEZ=19
    CATI=20
    CELL=21
    CL=22
    CMOS=23
    CO=24
    CONFIG=25
    DEASSIGN=26
    DEFAULT=27
    DEFPARAM=28
    DESIGN=29
    DISABLE=30
    DL=31
    DLFULLSKEW=32
    DLHOLD=33
    DLNOCHANGE=34
    DLPERIOD=35
    DLRECOVERY=36
    DLRECREM=37
    DLREMOVAL=38
    DLSETUP=39
    DLSETUPHOLD=40
    DLSKEW=41
    DLTIMESKEW=42
    DLWIDTH=43
    DQ=44
    DT=45
    EDGE=46
    ELSE=47
    EM=48
    EMEQ=49
    EMEQEQ=50
    END=51
    ENDCASE=52
    ENDCONFIG=53
    ENDFUNCTION=54
    ENDGENERATE=55
    ENDMODULE=56
    ENDPRIMITIVE=57
    ENDSPECIFY=58
    ENDTABLE=59
    ENDTASK=60
    EQ=61
    EQEQ=62
    EQEQEQ=63
    EQGT=64
    EVENT=65
    FOR=66
    FORCE=67
    FOREVER=68
    FORK=69
    FUNCTION=70
    GA=71
    GENERATE=72
    GENVAR=73
    GT=74
    GTEQ=75
    GTGT=76
    GTGTGT=77
    HA=78
    HIGHZONE=79
    HIGHZZERO=80
    IF=81
    IFNONE=82
    INCLUDE=83
    INITIAL=84
    INOUT=85
    INPUT=86
    INSTANCE=87
    INTEGER=88
    JOIN=89
    LARGE=90
    LB=91
    LC=92
    LIBLIST=93
    LIBRARY=94
    LOCALPARAM=95
    LP=96
    LT=97
    LTEQ=98
    LTLT=99
    LTLTLT=100
    MACROMODULE=101
    MEDIUM=102
    MI=103
    MICL=104
    MIGT=105
    MIINCDIR=106
    MO=107
    MODULE=108
    NAND=109
    NEGEDGE=110
    NMOS=111
    NOR=112
    NOSHOWCANCELLED=113
    NOT=114
    NOTIFONE=115
    NOTIFZERO=116
    OR=117
    OUTPUT=118
    PARAMETER=119
    PATHPULSEDL=120
    PL=121
    PLCL=122
    PMOS=123
    POSEDGE=124
    PRIMITIVE=125
    PULLDOWN=126
    PULLONE=127
    PULLUP=128
    PULLZERO=129
    PULSESTYLE_ONDETECT=130
    PULSESTYLE_ONEVENT=131
    QM=132
    RB=133
    RC=134
    RCMOS=135
    REAL=136
    REALTIME=137
    REG=138
    RELEASE=139
    REPEAT=140
    RNMOS=141
    RP=142
    RPMOS=143
    RTRAN=144
    RTRANIFONE=145
    RTRANIFZERO=146
    SC=147
    SCALARED=148
    SHOWCANCELLED=149
    SIGNED=150
    SL=151
    SMALL=152
    SPECIFY=153
    SPECPARAM=154
    STRONGONE=155
    STRONGZERO=156
    SUPPLYONE=157
    SUPPLYZERO=158
    TABLE=159
    TASK=160
    TI=161
    TIAM=162
    TICA=163
    TIME=164
    TIVL=165
    TRAN=166
    TRANIFONE=167
    TRANIFZERO=168
    TRI=169
    TRIAND=170
    TRIONE=171
    TRIOR=172
    TRIREG=173
    TRIZERO=174
    USE=175
    UWIRE=176
    VECTORED=177
    VL=178
    VLVL=179
    WAIT=180
    WAND=181
    WEAKONE=182
    WEAKZERO=183
    WHILE=184
    WIRE=185
    WOR=186
    XNOR=187
    XOR=188
    BINARY_BASE=189
    COMMENT=190
    DECIMAL_BASE=191
    ESCAPED_IDENTIFIER=192
    EXPONENTIAL_NUMBER=193
    FIXED_POINT_NUMBER=194
    HEX_BASE=195
    OCTAL_BASE=196
    SIMPLE_IDENTIFIER=197
    STRING=198
    SYSTEM_TF_IDENTIFIER=199
    UNSIGNED_NUMBER=200
    WHITE_SPACE=201
    BINARY_VALUE=202
    X_OR_Z_UNDERSCORE=203
    EDGE_DESCRIPTOR=204
    HEX_VALUE=205
    FILE_PATH_SPEC=206
    OCTAL_VALUE=207
    EDGE_SYMBOL=208
    LEVEL_ONLY_SYMBOL=209
    OUTPUT_OR_LEVEL_SYMBOL=210
    BEGIN_KEYWORDS_DIRECTIVE=211
    CELLDEFINE_DIRECTIVE=212
    DEFAULT_NETTYPE_DIRECTIVE=213
    DEFINE_DIRECTIVE=214
    ELSE_DIRECTIVE=215
    ELSIF_DIRECTIVE=216
    END_KEYWORDS_DIRECTIVE=217
    ENDCELLDEFINE_DIRECTIVE=218
    ENDIF_DIRECTIVE=219
    IFDEF_DIRECTIVE=220
    IFNDEF_DIRECTIVE=221
    INCLUDE_DIRECTIVE=222
    LINE_DIRECTIVE=223
    NOUNCONNECTED_DRIVE_DIRECTIVE=224
    PRAGMA_DIRECTIVE=225
    RESETALL_DIRECTIVE=226
    TIMESCALE_DIRECTIVE=227
    UNCONNECTED_DRIVE_DIRECTIVE=228
    UNDEF_DIRECTIVE=229
    MACRO_USAGE=230
    VERSION_SPECIFIER=231
    DEFAULT_NETTYPE_VALUE=232
    COMMENT_5=233
    MACRO_NAME=234
    WHITE_SPACE_7=235
    FILENAME=236
    MACRO_DELIMITER=237
    MACRO_ESC_NEWLINE=238
    MACRO_ESC_QUOTE=239
    MACRO_QUOTE=240
    MACRO_TEXT=241
    SOURCE_TEXT=242
    TIME_UNIT=243
    TIME_VALUE=244
    UNCONNECTED_DRIVE_VALUE=245
    MACRO_IDENTIFIER=246

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Source_textContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compiler_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.Compiler_directiveContext)
            else:
                return self.getTypedRuleContext(VerilogPreParser.Compiler_directiveContext,i)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_source_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSource_text" ):
                listener.enterSource_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSource_text" ):
                listener.exitSource_text(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSource_text" ):
                return visitor.visitSource_text(self)
            else:
                return visitor.visitChildren(self)




    def source_text(self):

        localctx = VerilogPreParser.Source_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_source_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==71:
                self.state = 92
                self.compiler_directive()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compiler_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def begin_keywords_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Begin_keywords_directiveContext,0)


        def celldefine_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Celldefine_directiveContext,0)


        def default_nettype_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Default_nettype_directiveContext,0)


        def end_keywords_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.End_keywords_directiveContext,0)


        def endcelldefine_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Endcelldefine_directiveContext,0)


        def ifdef_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Ifdef_directiveContext,0)


        def ifndef_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Ifndef_directiveContext,0)


        def include_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Include_directiveContext,0)


        def line_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Line_directiveContext,0)


        def nounconnected_drive_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Nounconnected_drive_directiveContext,0)


        def pragma_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Pragma_directiveContext,0)


        def resetall_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Resetall_directiveContext,0)


        def text_macro_definition(self):
            return self.getTypedRuleContext(VerilogPreParser.Text_macro_definitionContext,0)


        def text_macro_usage(self):
            return self.getTypedRuleContext(VerilogPreParser.Text_macro_usageContext,0)


        def timescale_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Timescale_directiveContext,0)


        def unconnected_drive_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Unconnected_drive_directiveContext,0)


        def undef_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Undef_directiveContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_compiler_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompiler_directive" ):
                listener.enterCompiler_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompiler_directive" ):
                listener.exitCompiler_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompiler_directive" ):
                return visitor.visitCompiler_directive(self)
            else:
                return visitor.visitChildren(self)




    def compiler_directive(self):

        localctx = VerilogPreParser.Compiler_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_compiler_directive)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.begin_keywords_directive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.celldefine_directive()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.default_nettype_directive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.end_keywords_directive()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.endcelldefine_directive()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 103
                self.ifdef_directive()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 104
                self.ifndef_directive()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 105
                self.include_directive()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 106
                self.line_directive()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 107
                self.nounconnected_drive_directive()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 108
                self.pragma_directive()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 109
                self.resetall_directive()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 110
                self.text_macro_definition()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 111
                self.text_macro_usage()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 112
                self.timescale_directive()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 113
                self.unconnected_drive_directive()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 114
                self.undef_directive()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Begin_keywords_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def BEGIN_KEYWORDS_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.BEGIN_KEYWORDS_DIRECTIVE, 0)

        def DQ(self, i:int=None):
            if i is None:
                return self.getTokens(VerilogPreParser.DQ)
            else:
                return self.getToken(VerilogPreParser.DQ, i)

        def version_specifier(self):
            return self.getTypedRuleContext(VerilogPreParser.Version_specifierContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_begin_keywords_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBegin_keywords_directive" ):
                listener.enterBegin_keywords_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBegin_keywords_directive" ):
                listener.exitBegin_keywords_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBegin_keywords_directive" ):
                return visitor.visitBegin_keywords_directive(self)
            else:
                return visitor.visitChildren(self)




    def begin_keywords_directive(self):

        localctx = VerilogPreParser.Begin_keywords_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_begin_keywords_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(VerilogPreParser.GA)
            self.state = 118
            self.match(VerilogPreParser.BEGIN_KEYWORDS_DIRECTIVE)
            self.state = 119
            self.match(VerilogPreParser.DQ)
            self.state = 120
            self.version_specifier()
            self.state = 121
            self.match(VerilogPreParser.DQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Celldefine_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def CELLDEFINE_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.CELLDEFINE_DIRECTIVE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_celldefine_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCelldefine_directive" ):
                listener.enterCelldefine_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCelldefine_directive" ):
                listener.exitCelldefine_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCelldefine_directive" ):
                return visitor.visitCelldefine_directive(self)
            else:
                return visitor.visitChildren(self)




    def celldefine_directive(self):

        localctx = VerilogPreParser.Celldefine_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_celldefine_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(VerilogPreParser.GA)
            self.state = 124
            self.match(VerilogPreParser.CELLDEFINE_DIRECTIVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Default_nettype_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def DEFAULT_NETTYPE_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.DEFAULT_NETTYPE_DIRECTIVE, 0)

        def default_nettype_value(self):
            return self.getTypedRuleContext(VerilogPreParser.Default_nettype_valueContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_default_nettype_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefault_nettype_directive" ):
                listener.enterDefault_nettype_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefault_nettype_directive" ):
                listener.exitDefault_nettype_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefault_nettype_directive" ):
                return visitor.visitDefault_nettype_directive(self)
            else:
                return visitor.visitChildren(self)




    def default_nettype_directive(self):

        localctx = VerilogPreParser.Default_nettype_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_default_nettype_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(VerilogPreParser.GA)
            self.state = 127
            self.match(VerilogPreParser.DEFAULT_NETTYPE_DIRECTIVE)
            self.state = 128
            self.default_nettype_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Default_nettype_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT_NETTYPE_VALUE(self):
            return self.getToken(VerilogPreParser.DEFAULT_NETTYPE_VALUE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_default_nettype_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefault_nettype_value" ):
                listener.enterDefault_nettype_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefault_nettype_value" ):
                listener.exitDefault_nettype_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefault_nettype_value" ):
                return visitor.visitDefault_nettype_value(self)
            else:
                return visitor.visitChildren(self)




    def default_nettype_value(self):

        localctx = VerilogPreParser.Default_nettype_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_default_nettype_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(VerilogPreParser.DEFAULT_NETTYPE_VALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def ELSE_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.ELSE_DIRECTIVE, 0)

        def group_of_lines(self):
            return self.getTypedRuleContext(VerilogPreParser.Group_of_linesContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_else_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_directive" ):
                listener.enterElse_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_directive" ):
                listener.exitElse_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_directive" ):
                return visitor.visitElse_directive(self)
            else:
                return visitor.visitChildren(self)




    def else_directive(self):

        localctx = VerilogPreParser.Else_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_else_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(VerilogPreParser.GA)
            self.state = 133
            self.match(VerilogPreParser.ELSE_DIRECTIVE)
            self.state = 134
            self.group_of_lines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elsif_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def ELSIF_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.ELSIF_DIRECTIVE, 0)

        def macro_identifier(self):
            return self.getTypedRuleContext(VerilogPreParser.Macro_identifierContext,0)


        def group_of_lines(self):
            return self.getTypedRuleContext(VerilogPreParser.Group_of_linesContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_elsif_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElsif_directive" ):
                listener.enterElsif_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElsif_directive" ):
                listener.exitElsif_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsif_directive" ):
                return visitor.visitElsif_directive(self)
            else:
                return visitor.visitChildren(self)




    def elsif_directive(self):

        localctx = VerilogPreParser.Elsif_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elsif_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(VerilogPreParser.GA)
            self.state = 137
            self.match(VerilogPreParser.ELSIF_DIRECTIVE)
            self.state = 138
            self.macro_identifier()
            self.state = 139
            self.group_of_lines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_keywords_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def END_KEYWORDS_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.END_KEYWORDS_DIRECTIVE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_end_keywords_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd_keywords_directive" ):
                listener.enterEnd_keywords_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd_keywords_directive" ):
                listener.exitEnd_keywords_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_keywords_directive" ):
                return visitor.visitEnd_keywords_directive(self)
            else:
                return visitor.visitChildren(self)




    def end_keywords_directive(self):

        localctx = VerilogPreParser.End_keywords_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_end_keywords_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(VerilogPreParser.GA)
            self.state = 142
            self.match(VerilogPreParser.END_KEYWORDS_DIRECTIVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Endcelldefine_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def ENDCELLDEFINE_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.ENDCELLDEFINE_DIRECTIVE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_endcelldefine_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndcelldefine_directive" ):
                listener.enterEndcelldefine_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndcelldefine_directive" ):
                listener.exitEndcelldefine_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndcelldefine_directive" ):
                return visitor.visitEndcelldefine_directive(self)
            else:
                return visitor.visitChildren(self)




    def endcelldefine_directive(self):

        localctx = VerilogPreParser.Endcelldefine_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_endcelldefine_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(VerilogPreParser.GA)
            self.state = 145
            self.match(VerilogPreParser.ENDCELLDEFINE_DIRECTIVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Endif_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def ENDIF_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.ENDIF_DIRECTIVE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_endif_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndif_directive" ):
                listener.enterEndif_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndif_directive" ):
                listener.exitEndif_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndif_directive" ):
                return visitor.visitEndif_directive(self)
            else:
                return visitor.visitChildren(self)




    def endif_directive(self):

        localctx = VerilogPreParser.Endif_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_endif_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(VerilogPreParser.GA)
            self.state = 148
            self.match(VerilogPreParser.ENDIF_DIRECTIVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilenameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILENAME(self):
            return self.getToken(VerilogPreParser.FILENAME, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_filename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilename" ):
                listener.enterFilename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilename" ):
                listener.exitFilename(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilename" ):
                return visitor.visitFilename(self)
            else:
                return visitor.visitChildren(self)




    def filename(self):

        localctx = VerilogPreParser.FilenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_filename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(VerilogPreParser.FILENAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Group_of_linesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def source_text_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.Source_text_Context)
            else:
                return self.getTypedRuleContext(VerilogPreParser.Source_text_Context,i)


        def compiler_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.Compiler_directiveContext)
            else:
                return self.getTypedRuleContext(VerilogPreParser.Compiler_directiveContext,i)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_group_of_lines

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_of_lines" ):
                listener.enterGroup_of_lines(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_of_lines" ):
                listener.exitGroup_of_lines(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup_of_lines" ):
                return visitor.visitGroup_of_lines(self)
            else:
                return visitor.visitChildren(self)




    def group_of_lines(self):

        localctx = VerilogPreParser.Group_of_linesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_group_of_lines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 154
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [242]:
                        self.state = 152
                        self.source_text_()
                        pass
                    elif token in [71]:
                        self.state = 153
                        self.compiler_directive()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIMPLE_IDENTIFIER(self):
            return self.getToken(VerilogPreParser.SIMPLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = VerilogPreParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(VerilogPreParser.SIMPLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifdef_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def IFDEF_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.IFDEF_DIRECTIVE, 0)

        def macro_identifier(self):
            return self.getTypedRuleContext(VerilogPreParser.Macro_identifierContext,0)


        def group_of_lines(self):
            return self.getTypedRuleContext(VerilogPreParser.Group_of_linesContext,0)


        def endif_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Endif_directiveContext,0)


        def elsif_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.Elsif_directiveContext)
            else:
                return self.getTypedRuleContext(VerilogPreParser.Elsif_directiveContext,i)


        def else_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Else_directiveContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_ifdef_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfdef_directive" ):
                listener.enterIfdef_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfdef_directive" ):
                listener.exitIfdef_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfdef_directive" ):
                return visitor.visitIfdef_directive(self)
            else:
                return visitor.visitChildren(self)




    def ifdef_directive(self):

        localctx = VerilogPreParser.Ifdef_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifdef_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(VerilogPreParser.GA)
            self.state = 162
            self.match(VerilogPreParser.IFDEF_DIRECTIVE)
            self.state = 163
            self.macro_identifier()
            self.state = 164
            self.group_of_lines()
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 165
                    self.elsif_directive() 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 171
                self.else_directive()


            self.state = 174
            self.endif_directive()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifndef_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def IFNDEF_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.IFNDEF_DIRECTIVE, 0)

        def macro_identifier(self):
            return self.getTypedRuleContext(VerilogPreParser.Macro_identifierContext,0)


        def group_of_lines(self):
            return self.getTypedRuleContext(VerilogPreParser.Group_of_linesContext,0)


        def endif_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Endif_directiveContext,0)


        def elsif_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.Elsif_directiveContext)
            else:
                return self.getTypedRuleContext(VerilogPreParser.Elsif_directiveContext,i)


        def else_directive(self):
            return self.getTypedRuleContext(VerilogPreParser.Else_directiveContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_ifndef_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfndef_directive" ):
                listener.enterIfndef_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfndef_directive" ):
                listener.exitIfndef_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfndef_directive" ):
                return visitor.visitIfndef_directive(self)
            else:
                return visitor.visitChildren(self)




    def ifndef_directive(self):

        localctx = VerilogPreParser.Ifndef_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifndef_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(VerilogPreParser.GA)
            self.state = 177
            self.match(VerilogPreParser.IFNDEF_DIRECTIVE)
            self.state = 178
            self.macro_identifier()
            self.state = 179
            self.group_of_lines()
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 180
                    self.elsif_directive() 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 186
                self.else_directive()


            self.state = 189
            self.endif_directive()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def INCLUDE_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.INCLUDE_DIRECTIVE, 0)

        def DQ(self, i:int=None):
            if i is None:
                return self.getTokens(VerilogPreParser.DQ)
            else:
                return self.getToken(VerilogPreParser.DQ, i)

        def filename(self):
            return self.getTypedRuleContext(VerilogPreParser.FilenameContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_include_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclude_directive" ):
                listener.enterInclude_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclude_directive" ):
                listener.exitInclude_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_directive" ):
                return visitor.visitInclude_directive(self)
            else:
                return visitor.visitChildren(self)




    def include_directive(self):

        localctx = VerilogPreParser.Include_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_include_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(VerilogPreParser.GA)
            self.state = 192
            self.match(VerilogPreParser.INCLUDE_DIRECTIVE)
            self.state = 193
            self.match(VerilogPreParser.DQ)
            self.state = 194
            self.filename()
            self.state = 195
            self.match(VerilogPreParser.DQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LevelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNSIGNED_NUMBER(self):
            return self.getToken(VerilogPreParser.UNSIGNED_NUMBER, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_level

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLevel" ):
                listener.enterLevel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLevel" ):
                listener.exitLevel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLevel" ):
                return visitor.visitLevel(self)
            else:
                return visitor.visitChildren(self)




    def level(self):

        localctx = VerilogPreParser.LevelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_level)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(VerilogPreParser.UNSIGNED_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def LINE_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.LINE_DIRECTIVE, 0)

        def number(self):
            return self.getTypedRuleContext(VerilogPreParser.NumberContext,0)


        def DQ(self, i:int=None):
            if i is None:
                return self.getTokens(VerilogPreParser.DQ)
            else:
                return self.getToken(VerilogPreParser.DQ, i)

        def filename(self):
            return self.getTypedRuleContext(VerilogPreParser.FilenameContext,0)


        def level(self):
            return self.getTypedRuleContext(VerilogPreParser.LevelContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_line_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_directive" ):
                listener.enterLine_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_directive" ):
                listener.exitLine_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_directive" ):
                return visitor.visitLine_directive(self)
            else:
                return visitor.visitChildren(self)




    def line_directive(self):

        localctx = VerilogPreParser.Line_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_line_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(VerilogPreParser.GA)
            self.state = 200
            self.match(VerilogPreParser.LINE_DIRECTIVE)
            self.state = 201
            self.number()
            self.state = 202
            self.match(VerilogPreParser.DQ)
            self.state = 203
            self.filename()
            self.state = 204
            self.match(VerilogPreParser.DQ)
            self.state = 205
            self.level()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_delimiterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_DELIMITER(self):
            return self.getToken(VerilogPreParser.MACRO_DELIMITER, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_macro_delimiter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_delimiter" ):
                listener.enterMacro_delimiter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_delimiter" ):
                listener.exitMacro_delimiter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_delimiter" ):
                return visitor.visitMacro_delimiter(self)
            else:
                return visitor.visitChildren(self)




    def macro_delimiter(self):

        localctx = VerilogPreParser.Macro_delimiterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_macro_delimiter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(VerilogPreParser.MACRO_DELIMITER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_esc_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_ESC_NEWLINE(self):
            return self.getToken(VerilogPreParser.MACRO_ESC_NEWLINE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_macro_esc_newline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_esc_newline" ):
                listener.enterMacro_esc_newline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_esc_newline" ):
                listener.exitMacro_esc_newline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_esc_newline" ):
                return visitor.visitMacro_esc_newline(self)
            else:
                return visitor.visitChildren(self)




    def macro_esc_newline(self):

        localctx = VerilogPreParser.Macro_esc_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_macro_esc_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(VerilogPreParser.MACRO_ESC_NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_esc_quoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_ESC_QUOTE(self):
            return self.getToken(VerilogPreParser.MACRO_ESC_QUOTE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_macro_esc_quote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_esc_quote" ):
                listener.enterMacro_esc_quote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_esc_quote" ):
                listener.exitMacro_esc_quote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_esc_quote" ):
                return visitor.visitMacro_esc_quote(self)
            else:
                return visitor.visitChildren(self)




    def macro_esc_quote(self):

        localctx = VerilogPreParser.Macro_esc_quoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_macro_esc_quote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(VerilogPreParser.MACRO_ESC_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_identifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_IDENTIFIER(self):
            return self.getToken(VerilogPreParser.MACRO_IDENTIFIER, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_macro_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_identifier" ):
                listener.enterMacro_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_identifier" ):
                listener.exitMacro_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_identifier" ):
                return visitor.visitMacro_identifier(self)
            else:
                return visitor.visitChildren(self)




    def macro_identifier(self):

        localctx = VerilogPreParser.Macro_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_macro_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(VerilogPreParser.MACRO_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_NAME(self):
            return self.getToken(VerilogPreParser.MACRO_NAME, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_macro_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_name" ):
                listener.enterMacro_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_name" ):
                listener.exitMacro_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_name" ):
                return visitor.visitMacro_name(self)
            else:
                return visitor.visitChildren(self)




    def macro_name(self):

        localctx = VerilogPreParser.Macro_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_macro_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(VerilogPreParser.MACRO_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_quoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_QUOTE(self):
            return self.getToken(VerilogPreParser.MACRO_QUOTE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_macro_quote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_quote" ):
                listener.enterMacro_quote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_quote" ):
                listener.exitMacro_quote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_quote" ):
                return visitor.visitMacro_quote(self)
            else:
                return visitor.visitChildren(self)




    def macro_quote(self):

        localctx = VerilogPreParser.Macro_quoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_macro_quote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(VerilogPreParser.MACRO_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_textContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(VerilogPreParser.MACRO_TEXT)
            else:
                return self.getToken(VerilogPreParser.MACRO_TEXT, i)

        def macro_delimiter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.Macro_delimiterContext)
            else:
                return self.getTypedRuleContext(VerilogPreParser.Macro_delimiterContext,i)


        def macro_esc_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.Macro_esc_newlineContext)
            else:
                return self.getTypedRuleContext(VerilogPreParser.Macro_esc_newlineContext,i)


        def macro_esc_quote(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.Macro_esc_quoteContext)
            else:
                return self.getTypedRuleContext(VerilogPreParser.Macro_esc_quoteContext,i)


        def macro_quote(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.Macro_quoteContext)
            else:
                return self.getTypedRuleContext(VerilogPreParser.Macro_quoteContext,i)


        def string_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.String_Context)
            else:
                return self.getTypedRuleContext(VerilogPreParser.String_Context,i)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_macro_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_text" ):
                listener.enterMacro_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_text" ):
                listener.exitMacro_text(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_text" ):
                return visitor.visitMacro_text(self)
            else:
                return visitor.visitChildren(self)




    def macro_text(self):

        localctx = VerilogPreParser.Macro_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_macro_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la - 198)) & ~0x3f) == 0 and ((1 << (_la - 198)) & 17042430230529) != 0:
                self.state = 225
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [241]:
                    self.state = 219
                    self.match(VerilogPreParser.MACRO_TEXT)
                    pass
                elif token in [237]:
                    self.state = 220
                    self.macro_delimiter()
                    pass
                elif token in [238]:
                    self.state = 221
                    self.macro_esc_newline()
                    pass
                elif token in [239]:
                    self.state = 222
                    self.macro_esc_quote()
                    pass
                elif token in [240]:
                    self.state = 223
                    self.macro_quote()
                    pass
                elif token in [198]:
                    self.state = 224
                    self.string_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_usageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_USAGE(self):
            return self.getToken(VerilogPreParser.MACRO_USAGE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_macro_usage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_usage" ):
                listener.enterMacro_usage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_usage" ):
                listener.exitMacro_usage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_usage" ):
                return visitor.visitMacro_usage(self)
            else:
                return visitor.visitChildren(self)




    def macro_usage(self):

        localctx = VerilogPreParser.Macro_usageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_macro_usage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(VerilogPreParser.MACRO_USAGE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nounconnected_drive_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def NOUNCONNECTED_DRIVE_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.NOUNCONNECTED_DRIVE_DIRECTIVE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_nounconnected_drive_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNounconnected_drive_directive" ):
                listener.enterNounconnected_drive_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNounconnected_drive_directive" ):
                listener.exitNounconnected_drive_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNounconnected_drive_directive" ):
                return visitor.visitNounconnected_drive_directive(self)
            else:
                return visitor.visitChildren(self)




    def nounconnected_drive_directive(self):

        localctx = VerilogPreParser.Nounconnected_drive_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_nounconnected_drive_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(VerilogPreParser.GA)
            self.state = 233
            self.match(VerilogPreParser.NOUNCONNECTED_DRIVE_DIRECTIVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNSIGNED_NUMBER(self):
            return self.getToken(VerilogPreParser.UNSIGNED_NUMBER, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = VerilogPreParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(VerilogPreParser.UNSIGNED_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def PRAGMA_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.PRAGMA_DIRECTIVE, 0)

        def pragma_name(self):
            return self.getTypedRuleContext(VerilogPreParser.Pragma_nameContext,0)


        def pragma_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.Pragma_expressionContext)
            else:
                return self.getTypedRuleContext(VerilogPreParser.Pragma_expressionContext,i)


        def CO(self, i:int=None):
            if i is None:
                return self.getTokens(VerilogPreParser.CO)
            else:
                return self.getToken(VerilogPreParser.CO, i)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_pragma_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma_directive" ):
                listener.enterPragma_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma_directive" ):
                listener.exitPragma_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragma_directive" ):
                return visitor.visitPragma_directive(self)
            else:
                return visitor.visitChildren(self)




    def pragma_directive(self):

        localctx = VerilogPreParser.Pragma_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_pragma_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(VerilogPreParser.GA)
            self.state = 238
            self.match(VerilogPreParser.PRAGMA_DIRECTIVE)
            self.state = 239
            self.pragma_name()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==96 or (((_la - 197)) & ~0x3f) == 0 and ((1 << (_la - 197)) & 11) != 0:
                self.state = 240
                self.pragma_expression()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 241
                    self.match(VerilogPreParser.CO)
                    self.state = 242
                    self.pragma_expression()
                    self.state = 247
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pragma_value(self):
            return self.getTypedRuleContext(VerilogPreParser.Pragma_valueContext,0)


        def pragma_keyword(self):
            return self.getTypedRuleContext(VerilogPreParser.Pragma_keywordContext,0)


        def EQ(self):
            return self.getToken(VerilogPreParser.EQ, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_pragma_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma_expression" ):
                listener.enterPragma_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma_expression" ):
                listener.exitPragma_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragma_expression" ):
                return visitor.visitPragma_expression(self)
            else:
                return visitor.visitChildren(self)




    def pragma_expression(self):

        localctx = VerilogPreParser.Pragma_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_pragma_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 250
                self.pragma_keyword()
                self.state = 251
                self.match(VerilogPreParser.EQ)


            self.state = 255
            self.pragma_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_keywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIMPLE_IDENTIFIER(self):
            return self.getToken(VerilogPreParser.SIMPLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_pragma_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma_keyword" ):
                listener.enterPragma_keyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma_keyword" ):
                listener.exitPragma_keyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragma_keyword" ):
                return visitor.visitPragma_keyword(self)
            else:
                return visitor.visitChildren(self)




    def pragma_keyword(self):

        localctx = VerilogPreParser.Pragma_keywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_pragma_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(VerilogPreParser.SIMPLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIMPLE_IDENTIFIER(self):
            return self.getToken(VerilogPreParser.SIMPLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_pragma_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma_name" ):
                listener.enterPragma_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma_name" ):
                listener.exitPragma_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragma_name" ):
                return visitor.visitPragma_name(self)
            else:
                return visitor.visitChildren(self)




    def pragma_name(self):

        localctx = VerilogPreParser.Pragma_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_pragma_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(VerilogPreParser.SIMPLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(VerilogPreParser.LP, 0)

        def pragma_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerilogPreParser.Pragma_expressionContext)
            else:
                return self.getTypedRuleContext(VerilogPreParser.Pragma_expressionContext,i)


        def RP(self):
            return self.getToken(VerilogPreParser.RP, 0)

        def CO(self, i:int=None):
            if i is None:
                return self.getTokens(VerilogPreParser.CO)
            else:
                return self.getToken(VerilogPreParser.CO, i)

        def number(self):
            return self.getTypedRuleContext(VerilogPreParser.NumberContext,0)


        def string_(self):
            return self.getTypedRuleContext(VerilogPreParser.String_Context,0)


        def identifier(self):
            return self.getTypedRuleContext(VerilogPreParser.IdentifierContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_pragma_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma_value" ):
                listener.enterPragma_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma_value" ):
                listener.exitPragma_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragma_value" ):
                return visitor.visitPragma_value(self)
            else:
                return visitor.visitChildren(self)




    def pragma_value(self):

        localctx = VerilogPreParser.Pragma_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_pragma_value)
        self._la = 0 # Token type
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [96]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(VerilogPreParser.LP)
                self.state = 262
                self.pragma_expression()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 263
                    self.match(VerilogPreParser.CO)
                    self.state = 264
                    self.pragma_expression()
                    self.state = 269
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 270
                self.match(VerilogPreParser.RP)
                pass
            elif token in [200]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.number()
                pass
            elif token in [198]:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.string_()
                pass
            elif token in [197]:
                self.enterOuterAlt(localctx, 4)
                self.state = 274
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Resetall_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def RESETALL_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.RESETALL_DIRECTIVE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_resetall_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResetall_directive" ):
                listener.enterResetall_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResetall_directive" ):
                listener.exitResetall_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResetall_directive" ):
                return visitor.visitResetall_directive(self)
            else:
                return visitor.visitChildren(self)




    def resetall_directive(self):

        localctx = VerilogPreParser.Resetall_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_resetall_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(VerilogPreParser.GA)
            self.state = 278
            self.match(VerilogPreParser.RESETALL_DIRECTIVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Source_text_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SOURCE_TEXT(self):
            return self.getToken(VerilogPreParser.SOURCE_TEXT, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_source_text_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSource_text_" ):
                listener.enterSource_text_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSource_text_" ):
                listener.exitSource_text_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSource_text_" ):
                return visitor.visitSource_text_(self)
            else:
                return visitor.visitChildren(self)




    def source_text_(self):

        localctx = VerilogPreParser.Source_text_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_source_text_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(VerilogPreParser.SOURCE_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(VerilogPreParser.STRING, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_string_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_" ):
                listener.enterString_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_" ):
                listener.exitString_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_" ):
                return visitor.visitString_(self)
            else:
                return visitor.visitChildren(self)




    def string_(self):

        localctx = VerilogPreParser.String_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_string_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(VerilogPreParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Text_macro_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def DEFINE_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.DEFINE_DIRECTIVE, 0)

        def macro_name(self):
            return self.getTypedRuleContext(VerilogPreParser.Macro_nameContext,0)


        def macro_text(self):
            return self.getTypedRuleContext(VerilogPreParser.Macro_textContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_text_macro_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText_macro_definition" ):
                listener.enterText_macro_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText_macro_definition" ):
                listener.exitText_macro_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText_macro_definition" ):
                return visitor.visitText_macro_definition(self)
            else:
                return visitor.visitChildren(self)




    def text_macro_definition(self):

        localctx = VerilogPreParser.Text_macro_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_text_macro_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(VerilogPreParser.GA)
            self.state = 285
            self.match(VerilogPreParser.DEFINE_DIRECTIVE)
            self.state = 286
            self.macro_name()
            self.state = 287
            self.macro_text()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Text_macro_usageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def macro_usage(self):
            return self.getTypedRuleContext(VerilogPreParser.Macro_usageContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_text_macro_usage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText_macro_usage" ):
                listener.enterText_macro_usage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText_macro_usage" ):
                listener.exitText_macro_usage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText_macro_usage" ):
                return visitor.visitText_macro_usage(self)
            else:
                return visitor.visitChildren(self)




    def text_macro_usage(self):

        localctx = VerilogPreParser.Text_macro_usageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_text_macro_usage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(VerilogPreParser.GA)
            self.state = 290
            self.macro_usage()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Time_precisionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIME_VALUE(self):
            return self.getToken(VerilogPreParser.TIME_VALUE, 0)

        def TIME_UNIT(self):
            return self.getToken(VerilogPreParser.TIME_UNIT, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_time_precision

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_precision" ):
                listener.enterTime_precision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_precision" ):
                listener.exitTime_precision(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTime_precision" ):
                return visitor.visitTime_precision(self)
            else:
                return visitor.visitChildren(self)




    def time_precision(self):

        localctx = VerilogPreParser.Time_precisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_time_precision)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(VerilogPreParser.TIME_VALUE)
            self.state = 293
            self.match(VerilogPreParser.TIME_UNIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Time_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIME_VALUE(self):
            return self.getToken(VerilogPreParser.TIME_VALUE, 0)

        def TIME_UNIT(self):
            return self.getToken(VerilogPreParser.TIME_UNIT, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_time_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_unit" ):
                listener.enterTime_unit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_unit" ):
                listener.exitTime_unit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTime_unit" ):
                return visitor.visitTime_unit(self)
            else:
                return visitor.visitChildren(self)




    def time_unit(self):

        localctx = VerilogPreParser.Time_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_time_unit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(VerilogPreParser.TIME_VALUE)
            self.state = 296
            self.match(VerilogPreParser.TIME_UNIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Timescale_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def TIMESCALE_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.TIMESCALE_DIRECTIVE, 0)

        def time_unit(self):
            return self.getTypedRuleContext(VerilogPreParser.Time_unitContext,0)


        def SL(self):
            return self.getToken(VerilogPreParser.SL, 0)

        def time_precision(self):
            return self.getTypedRuleContext(VerilogPreParser.Time_precisionContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_timescale_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimescale_directive" ):
                listener.enterTimescale_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimescale_directive" ):
                listener.exitTimescale_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimescale_directive" ):
                return visitor.visitTimescale_directive(self)
            else:
                return visitor.visitChildren(self)




    def timescale_directive(self):

        localctx = VerilogPreParser.Timescale_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_timescale_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(VerilogPreParser.GA)
            self.state = 299
            self.match(VerilogPreParser.TIMESCALE_DIRECTIVE)
            self.state = 300
            self.time_unit()
            self.state = 301
            self.match(VerilogPreParser.SL)
            self.state = 302
            self.time_precision()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unconnected_drive_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def UNCONNECTED_DRIVE_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.UNCONNECTED_DRIVE_DIRECTIVE, 0)

        def unconnected_drive_value(self):
            return self.getTypedRuleContext(VerilogPreParser.Unconnected_drive_valueContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_unconnected_drive_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnconnected_drive_directive" ):
                listener.enterUnconnected_drive_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnconnected_drive_directive" ):
                listener.exitUnconnected_drive_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnconnected_drive_directive" ):
                return visitor.visitUnconnected_drive_directive(self)
            else:
                return visitor.visitChildren(self)




    def unconnected_drive_directive(self):

        localctx = VerilogPreParser.Unconnected_drive_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_unconnected_drive_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(VerilogPreParser.GA)
            self.state = 305
            self.match(VerilogPreParser.UNCONNECTED_DRIVE_DIRECTIVE)
            self.state = 306
            self.unconnected_drive_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unconnected_drive_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNCONNECTED_DRIVE_VALUE(self):
            return self.getToken(VerilogPreParser.UNCONNECTED_DRIVE_VALUE, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_unconnected_drive_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnconnected_drive_value" ):
                listener.enterUnconnected_drive_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnconnected_drive_value" ):
                listener.exitUnconnected_drive_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnconnected_drive_value" ):
                return visitor.visitUnconnected_drive_value(self)
            else:
                return visitor.visitChildren(self)




    def unconnected_drive_value(self):

        localctx = VerilogPreParser.Unconnected_drive_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_unconnected_drive_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(VerilogPreParser.UNCONNECTED_DRIVE_VALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Undef_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GA(self):
            return self.getToken(VerilogPreParser.GA, 0)

        def UNDEF_DIRECTIVE(self):
            return self.getToken(VerilogPreParser.UNDEF_DIRECTIVE, 0)

        def macro_identifier(self):
            return self.getTypedRuleContext(VerilogPreParser.Macro_identifierContext,0)


        def getRuleIndex(self):
            return VerilogPreParser.RULE_undef_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUndef_directive" ):
                listener.enterUndef_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUndef_directive" ):
                listener.exitUndef_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUndef_directive" ):
                return visitor.visitUndef_directive(self)
            else:
                return visitor.visitChildren(self)




    def undef_directive(self):

        localctx = VerilogPreParser.Undef_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_undef_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(VerilogPreParser.GA)
            self.state = 311
            self.match(VerilogPreParser.UNDEF_DIRECTIVE)
            self.state = 312
            self.macro_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Version_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERSION_SPECIFIER(self):
            return self.getToken(VerilogPreParser.VERSION_SPECIFIER, 0)

        def getRuleIndex(self):
            return VerilogPreParser.RULE_version_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersion_specifier" ):
                listener.enterVersion_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersion_specifier" ):
                listener.exitVersion_specifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersion_specifier" ):
                return visitor.visitVersion_specifier(self)
            else:
                return visitor.visitChildren(self)




    def version_specifier(self):

        localctx = VerilogPreParser.Version_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_version_specifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(VerilogPreParser.VERSION_SPECIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





