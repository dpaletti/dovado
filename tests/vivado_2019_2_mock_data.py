# Everything in this file is sampled by a Vivado 2019.2

# Recap of variables in this file for convenience
parts = []


# help command stripped of everything except -directive paragraph
place_directives_paragraph = ""
route_directives_paragraph = ""
synth_directives_paragraph = ""

# full help command output
help_synth_design = ""
help_place_design = ""
help_route_design = ""

# directives contained in corresponding -directive paragraph
synth_directives = []
place_directives = []
route_directives = []

# -directive paragraph stripped of everything except "Note:" section
place_note = ""
route_note = ""

# directives contained in the "Note:" section for incremental directives
incremental_place_directives = []
incremental_route_directives = []


parts = {
    "xc7k70tfbv676-1": "kintex7",
    "xc7k70tfbv676-2": "kintex7",
    "xc7k70tfbv676-2L": "kintex7",
    "xc7k70tfbv676-3": "kintex7",
    "xc7k70tfbv484-1": "kintex7",
    "xc7k70tfbv484-2": "kintex7",
    "xc7k70tfbv484-2L": "kintex7",
    "xc7k70tfbv484-3": "kintex7",
    "xc7k70tfbg676-1": "kintex7",
    "xc7k70tfbg676-2": "kintex7",
    "xc7k70tfbg676-2L": "kintex7",
    "xc7k70tfbg676-3": "kintex7",
    "xc7k70tfbg484-1": "kintex7",
    "xc7k70tfbg484-2": "kintex7",
    "xc7k70tfbg484-2L": "kintex7",
    "xc7k70tfbg484-3": "kintex7",
    "xc7k160tfbg484-1": "kintex7",
    "xc7k160tfbg484-2": "kintex7",
    "xc7k160tfbg484-2L": "kintex7",
    "xc7k160tfbg484-3": "kintex7",
    "xc7k160tfbg676-1": "kintex7",
    "xc7k160tfbg676-2": "kintex7",
    "xc7k160tfbg676-2L": "kintex7",
    "xc7k160tfbg676-3": "kintex7",
    "xc7k160tfbv484-1": "kintex7",
    "xc7k160tfbv484-2": "kintex7",
    "xc7k160tfbv484-2L": "kintex7",
    "xc7k160tfbv484-3": "kintex7",
    "xc7k160tfbv676-1": "kintex7",
    "xc7k160tfbv676-2": "kintex7",
    "xc7k160tfbv676-2L": "kintex7",
    "xc7k160tfbv676-3": "kintex7",
    "xc7k160tffg676-1": "kintex7",
    "xc7k160tffg676-2": "kintex7",
    "xc7k160tffg676-2L": "kintex7",
    "xc7k160tffg676-3": "kintex7",
    "xc7k160tffv676-1": "kintex7",
    "xc7k160tffv676-2": "kintex7",
    "xc7k160tffv676-2L": "kintex7",
    "xc7k160tffv676-3": "kintex7",
    "xc7k160tifbv676-2L": "kintex7",
    "xc7k160tifbg484-2L": "kintex7",
    "xc7k160tifbg676-2L": "kintex7",
    "xc7k160tifbv484-2L": "kintex7",
    "xc7k160tiffv676-2L": "kintex7",
    "xc7k160tiffg676-2L": "kintex7",
    "xc7k70tlfbv676-2L": "kintex7l",
    "xc7k70tlfbv484-2L": "kintex7l",
    "xc7k70tlfbg676-2L": "kintex7l",
    "xc7k70tlfbg484-2L": "kintex7l",
    "xc7k160tlfbg484-2L": "kintex7l",
    "xc7k160tlfbg676-2L": "kintex7l",
    "xc7k160tlfbv484-2L": "kintex7l",
    "xc7k160tlfbv676-2L": "kintex7l",
    "xc7k160tlffg676-2L": "kintex7l",
    "xc7k160tlffv676-2L": "kintex7l",
    "xc7a12ticsg325-1L": "artix7",
    "xc7a12ticpg238-1L": "artix7",
    "xc7a12tcsg325-1": "artix7",
    "xc7a12tcsg325-2": "artix7",
    "xc7a12tcsg325-2L": "artix7",
    "xc7a12tcsg325-3": "artix7",
    "xc7a12tcpg238-1": "artix7",
    "xc7a12tcpg238-2": "artix7",
    "xc7a12tcpg238-2L": "artix7",
    "xc7a12tcpg238-3": "artix7",
    "xc7a25tcpg238-1": "artix7",
    "xc7a25tcpg238-2": "artix7",
    "xc7a25tcpg238-2L": "artix7",
    "xc7a25tcpg238-3": "artix7",
    "xc7a25tcsg325-1": "artix7",
    "xc7a25tcsg325-2": "artix7",
    "xc7a25tcsg325-2L": "artix7",
    "xc7a25tcsg325-3": "artix7",
    "xc7a25ticpg238-1L": "artix7",
    "xc7a25ticsg325-1L": "artix7",
    "xc7a50tcsg324-1": "artix7",
    "xc7a50tcsg324-2": "artix7",
    "xc7a50tcsg324-2L": "artix7",
    "xc7a50tcsg324-3": "artix7",
    "xc7a50tcpg236-1": "artix7",
    "xc7a50tcpg236-2": "artix7",
    "xc7a50tcpg236-2L": "artix7",
    "xc7a50tcpg236-3": "artix7",
    "xc7a50tcsg325-1": "artix7",
    "xc7a50tcsg325-2": "artix7",
    "xc7a50tcsg325-2L": "artix7",
    "xc7a50tcsg325-3": "artix7",
    "xc7a50tfgg484-1": "artix7",
    "xc7a50tfgg484-2": "artix7",
    "xc7a50tfgg484-2L": "artix7",
    "xc7a50tfgg484-3": "artix7",
    "xc7a50tftg256-1": "artix7",
    "xc7a50tftg256-2": "artix7",
    "xc7a50tftg256-2L": "artix7",
    "xc7a50tftg256-3": "artix7",
    "xc7a35tiftg256-1L": "artix7",
    "xc7a35tifgg484-1L": "artix7",
    "xc7a35ticsg325-1L": "artix7",
    "xc7a35ticsg324-1L": "artix7",
    "xc7a35ticpg236-1L": "artix7",
    "xc7a50ticpg236-1L": "artix7",
    "xc7a50tiftg256-1L": "artix7",
    "xc7a50tifgg484-1L": "artix7",
    "xc7a50ticsg325-1L": "artix7",
    "xc7a50ticsg324-1L": "artix7",
    "xc7a35tftg256-1": "artix7",
    "xc7a35tftg256-2": "artix7",
    "xc7a35tftg256-2L": "artix7",
    "xc7a35tftg256-3": "artix7",
    "xc7a35tfgg484-1": "artix7",
    "xc7a35tfgg484-2": "artix7",
    "xc7a35tfgg484-2L": "artix7",
    "xc7a35tfgg484-3": "artix7",
    "xc7a35tcsg325-1": "artix7",
    "xc7a35tcsg325-2": "artix7",
    "xc7a35tcsg325-2L": "artix7",
    "xc7a35tcsg325-3": "artix7",
    "xc7a35tcsg324-1": "artix7",
    "xc7a35tcsg324-2": "artix7",
    "xc7a35tcsg324-2L": "artix7",
    "xc7a35tcsg324-3": "artix7",
    "xc7a35tcpg236-1": "artix7",
    "xc7a35tcpg236-2": "artix7",
    "xc7a35tcpg236-2L": "artix7",
    "xc7a35tcpg236-3": "artix7",
    "xc7a15tcpg236-1": "artix7",
    "xc7a15tcpg236-2": "artix7",
    "xc7a15tcpg236-2L": "artix7",
    "xc7a15tcpg236-3": "artix7",
    "xc7a15tcsg324-1": "artix7",
    "xc7a15tcsg324-2": "artix7",
    "xc7a15tcsg324-2L": "artix7",
    "xc7a15tcsg324-3": "artix7",
    "xc7a15tcsg325-1": "artix7",
    "xc7a15tcsg325-2": "artix7",
    "xc7a15tcsg325-2L": "artix7",
    "xc7a15tcsg325-3": "artix7",
    "xc7a15tfgg484-1": "artix7",
    "xc7a15tfgg484-2": "artix7",
    "xc7a15tfgg484-2L": "artix7",
    "xc7a15tfgg484-3": "artix7",
    "xc7a15tftg256-1": "artix7",
    "xc7a15tftg256-2": "artix7",
    "xc7a15tftg256-2L": "artix7",
    "xc7a15tftg256-3": "artix7",
    "xc7a15ticpg236-1L": "artix7",
    "xc7a15ticsg324-1L": "artix7",
    "xc7a15ticsg325-1L": "artix7",
    "xc7a15tifgg484-1L": "artix7",
    "xc7a15tiftg256-1L": "artix7",
    "xc7a75tfgg484-1": "artix7",
    "xc7a75tfgg484-2": "artix7",
    "xc7a75tfgg484-2L": "artix7",
    "xc7a75tfgg484-3": "artix7",
    "xc7a75tfgg676-1": "artix7",
    "xc7a75tfgg676-2": "artix7",
    "xc7a75tfgg676-2L": "artix7",
    "xc7a75tfgg676-3": "artix7",
    "xc7a75tftg256-1": "artix7",
    "xc7a75tftg256-2": "artix7",
    "xc7a75tftg256-2L": "artix7",
    "xc7a75tftg256-3": "artix7",
    "xc7a75tcsg324-1": "artix7",
    "xc7a75tcsg324-2": "artix7",
    "xc7a75tcsg324-2L": "artix7",
    "xc7a75tcsg324-3": "artix7",
    "xc7a75ticsg324-1L": "artix7",
    "xc7a75tifgg484-1L": "artix7",
    "xc7a75tifgg676-1L": "artix7",
    "xc7a75tiftg256-1L": "artix7",
    "xc7a100tiftg256-1L": "artix7",
    "xc7a100tifgg676-1L": "artix7",
    "xc7a100tifgg484-1L": "artix7",
    "xc7a100ticsg324-1L": "artix7",
    "xc7a100tftg256-1": "artix7",
    "xc7a100tftg256-2": "artix7",
    "xc7a100tftg256-2L": "artix7",
    "xc7a100tftg256-3": "artix7",
    "xc7a100tfgg676-1": "artix7",
    "xc7a100tfgg676-2": "artix7",
    "xc7a100tfgg676-2L": "artix7",
    "xc7a100tfgg676-3": "artix7",
    "xc7a100tfgg484-1": "artix7",
    "xc7a100tfgg484-2": "artix7",
    "xc7a100tfgg484-2L": "artix7",
    "xc7a100tfgg484-3": "artix7",
    "xc7a100tcsg324-1": "artix7",
    "xc7a100tcsg324-2": "artix7",
    "xc7a100tcsg324-2L": "artix7",
    "xc7a100tcsg324-3": "artix7",
    "xc7a200tfbg484-1": "artix7",
    "xc7a200tfbg484-2": "artix7",
    "xc7a200tfbg484-2L": "artix7",
    "xc7a200tfbg484-3": "artix7",
    "xc7a200tfbg676-1": "artix7",
    "xc7a200tfbg676-2": "artix7",
    "xc7a200tfbg676-2L": "artix7",
    "xc7a200tfbg676-3": "artix7",
    "xc7a200tfbv484-1": "artix7",
    "xc7a200tfbv484-2": "artix7",
    "xc7a200tfbv484-2L": "artix7",
    "xc7a200tfbv484-3": "artix7",
    "xc7a200tfbv676-1": "artix7",
    "xc7a200tfbv676-2": "artix7",
    "xc7a200tfbv676-2L": "artix7",
    "xc7a200tfbv676-3": "artix7",
    "xc7a200tffg1156-1": "artix7",
    "xc7a200tffg1156-2": "artix7",
    "xc7a200tffg1156-2L": "artix7",
    "xc7a200tffg1156-3": "artix7",
    "xc7a200tsbv484-1": "artix7",
    "xc7a200tsbv484-2": "artix7",
    "xc7a200tsbv484-2L": "artix7",
    "xc7a200tsbv484-3": "artix7",
    "xc7a200tffv1156-1": "artix7",
    "xc7a200tffv1156-2": "artix7",
    "xc7a200tffv1156-2L": "artix7",
    "xc7a200tffv1156-3": "artix7",
    "xc7a200tsbg484-1": "artix7",
    "xc7a200tsbg484-2": "artix7",
    "xc7a200tsbg484-2L": "artix7",
    "xc7a200tsbg484-3": "artix7",
    "xc7a200tisbv484-1L": "artix7",
    "xc7a200tisbg484-1L": "artix7",
    "xc7a200tiffv1156-1L": "artix7",
    "xc7a200tiffg1156-1L": "artix7",
    "xc7a200tifbv676-1L": "artix7",
    "xc7a200tifbv484-1L": "artix7",
    "xc7a200tifbg676-1L": "artix7",
    "xc7a200tifbg484-1L": "artix7",
    "xc7a12tlcsg325-2L": "artix7l",
    "xc7a12tlcpg238-2L": "artix7l",
    "xc7a25tlcsg325-2L": "artix7l",
    "xc7a25tlcpg238-2L": "artix7l",
    "xc7a35tlcpg236-2L": "artix7l",
    "xc7a35tlcsg324-2L": "artix7l",
    "xc7a35tlcsg325-2L": "artix7l",
    "xc7a35tlfgg484-2L": "artix7l",
    "xc7a35tlftg256-2L": "artix7l",
    "xc7a15tlcpg236-2L": "artix7l",
    "xc7a15tlcsg324-2L": "artix7l",
    "xc7a15tlcsg325-2L": "artix7l",
    "xc7a15tlfgg484-2L": "artix7l",
    "xc7a15tlftg256-2L": "artix7l",
    "xc7a50tlcpg236-2L": "artix7l",
    "xc7a50tlcsg324-2L": "artix7l",
    "xc7a50tlcsg325-2L": "artix7l",
    "xc7a50tlfgg484-2L": "artix7l",
    "xc7a50tlftg256-2L": "artix7l",
    "xc7a75tlftg256-2L": "artix7l",
    "xc7a75tlfgg676-2L": "artix7l",
    "xc7a75tlfgg484-2L": "artix7l",
    "xc7a75tlcsg324-2L": "artix7l",
    "xc7a100tlcsg324-2L": "artix7l",
    "xc7a100tlfgg484-2L": "artix7l",
    "xc7a100tlfgg676-2L": "artix7l",
    "xc7a100tlftg256-2L": "artix7l",
    "xc7a200tlfbg484-2L": "artix7l",
    "xc7a200tlfbg676-2L": "artix7l",
    "xc7a200tlfbv484-2L": "artix7l",
    "xc7a200tlfbv676-2L": "artix7l",
    "xc7a200tlffg1156-2L": "artix7l",
    "xc7a200tlffv1156-2L": "artix7l",
    "xc7a200tlsbg484-2L": "artix7l",
    "xc7a200tlsbv484-2L": "artix7l",
    "xa7a35tcsg325-1I": "aartix7",
    "xa7a35tcsg325-1Q": "aartix7",
    "xa7a35tcsg325-2I": "aartix7",
    "xa7a35tcsg324-1I": "aartix7",
    "xa7a35tcsg324-1Q": "aartix7",
    "xa7a35tcsg324-2I": "aartix7",
    "xa7a35tcpg236-1I": "aartix7",
    "xa7a35tcpg236-1Q": "aartix7",
    "xa7a35tcpg236-2I": "aartix7",
    "xa7a15tcpg236-1I": "aartix7",
    "xa7a15tcpg236-1Q": "aartix7",
    "xa7a15tcpg236-2I": "aartix7",
    "xa7a15tcsg324-1I": "aartix7",
    "xa7a15tcsg324-1Q": "aartix7",
    "xa7a15tcsg324-2I": "aartix7",
    "xa7a15tcsg325-1I": "aartix7",
    "xa7a15tcsg325-1Q": "aartix7",
    "xa7a15tcsg325-2I": "aartix7",
    "xa7a50tcpg236-1I": "aartix7",
    "xa7a50tcpg236-1Q": "aartix7",
    "xa7a50tcpg236-2I": "aartix7",
    "xa7a50tcsg324-1I": "aartix7",
    "xa7a50tcsg324-1Q": "aartix7",
    "xa7a50tcsg324-2I": "aartix7",
    "xa7a50tcsg325-1I": "aartix7",
    "xa7a50tcsg325-1Q": "aartix7",
    "xa7a50tcsg325-2I": "aartix7",
    "xa7a100tfgg484-1I": "aartix7",
    "xa7a100tfgg484-1Q": "aartix7",
    "xa7a100tfgg484-2I": "aartix7",
    "xa7a100tcsg324-1I": "aartix7",
    "xa7a100tcsg324-1Q": "aartix7",
    "xa7a100tcsg324-2I": "aartix7",
    "xa7a75tcsg324-1I": "aartix7",
    "xa7a75tcsg324-1Q": "aartix7",
    "xa7a75tcsg324-2I": "aartix7",
    "xa7a75tfgg484-1I": "aartix7",
    "xa7a75tfgg484-1Q": "aartix7",
    "xa7a75tfgg484-2I": "aartix7",
    "xa7a12tcpg238-1I": "aartix7",
    "xa7a12tcpg238-1Q": "aartix7",
    "xa7a12tcpg238-2I": "aartix7",
    "xa7a12tcsg325-1I": "aartix7",
    "xa7a12tcsg325-1Q": "aartix7",
    "xa7a12tcsg325-2I": "aartix7",
    "xa7a25tcpg238-1I": "aartix7",
    "xa7a25tcpg238-1Q": "aartix7",
    "xa7a25tcpg238-2I": "aartix7",
    "xa7a25tcsg325-1I": "aartix7",
    "xa7a25tcsg325-1Q": "aartix7",
    "xa7a25tcsg325-2I": "aartix7",
    "xc7z010iclg225-1L": "zynq",
    "xc7z010iclg400-1L": "zynq",
    "xc7z010clg400-1": "zynq",
    "xc7z010clg400-2": "zynq",
    "xc7z010clg400-3": "zynq",
    "xc7z010clg225-1": "zynq",
    "xc7z010clg225-2": "zynq",
    "xc7z010clg225-3": "zynq",
    "xc7z007sclg400-1": "zynq",
    "xc7z007sclg400-2": "zynq",
    "xc7z007sclg225-1": "zynq",
    "xc7z007sclg225-2": "zynq",
    "xc7z015iclg485-1L": "zynq",
    "xc7z015clg485-1": "zynq",
    "xc7z015clg485-2": "zynq",
    "xc7z015clg485-3": "zynq",
    "xc7z012sclg485-1": "zynq",
    "xc7z012sclg485-2": "zynq",
    "xc7z020iclg484-1L": "zynq",
    "xc7z020iclg400-1L": "zynq",
    "xc7z014sclg484-1": "zynq",
    "xc7z014sclg484-2": "zynq",
    "xc7z014sclg400-1": "zynq",
    "xc7z014sclg400-2": "zynq",
    "xc7z020clg484-1": "zynq",
    "xc7z020clg484-2": "zynq",
    "xc7z020clg484-3": "zynq",
    "xc7z020clg400-1": "zynq",
    "xc7z020clg400-2": "zynq",
    "xc7z020clg400-3": "zynq",
    "xc7z030ifbg484-2L": "zynq",
    "xc7z030ifbg676-2L": "zynq",
    "xc7z030ifbv484-2L": "zynq",
    "xc7z030ifbv676-2L": "zynq",
    "xc7z030iffg676-2L": "zynq",
    "xc7z030iffv676-2L": "zynq",
    "xc7z030isbg485-2L": "zynq",
    "xc7z030isbv485-2L": "zynq",
    "xc7z030sbg485-1": "zynq",
    "xc7z030sbg485-2": "zynq",
    "xc7z030sbg485-3": "zynq",
    "xc7z030sbv485-1": "zynq",
    "xc7z030sbv485-2": "zynq",
    "xc7z030sbv485-3": "zynq",
    "xc7z030fbg484-1": "zynq",
    "xc7z030fbg484-2": "zynq",
    "xc7z030fbg484-3": "zynq",
    "xc7z030fbg676-1": "zynq",
    "xc7z030fbg676-2": "zynq",
    "xc7z030fbg676-3": "zynq",
    "xc7z030fbv484-1": "zynq",
    "xc7z030fbv484-2": "zynq",
    "xc7z030fbv484-3": "zynq",
    "xc7z030fbv676-1": "zynq",
    "xc7z030fbv676-2": "zynq",
    "xc7z030fbv676-3": "zynq",
    "xc7z030ffg676-1": "zynq",
    "xc7z030ffg676-2": "zynq",
    "xc7z030ffg676-3": "zynq",
    "xc7z030ffv676-1": "zynq",
    "xc7z030ffv676-2": "zynq",
    "xc7z030ffv676-3": "zynq",
    "xa7z010clg225-1I": "azynq",
    "xa7z010clg225-1Q": "azynq",
    "xa7z010clg400-1I": "azynq",
    "xa7z010clg400-1Q": "azynq",
    "xa7z020clg400-1I": "azynq",
    "xa7z020clg400-1Q": "azynq",
    "xa7z020clg484-1I": "azynq",
    "xa7z020clg484-1Q": "azynq",
    "xa7z030fbg484-1I": "azynq",
    "xa7z030fbg484-1Q": "azynq",
    "xa7z030fbv484-1I": "azynq",
    "xa7z030fbv484-1Q": "azynq",
    "xc7s6ftgb196-1": "spartan7",
    "xc7s6ftgb196-1IL": "spartan7",
    "xc7s6ftgb196-1Q": "spartan7",
    "xc7s6ftgb196-2": "spartan7",
    "xc7s6csga225-1": "spartan7",
    "xc7s6csga225-1IL": "spartan7",
    "xc7s6csga225-1Q": "spartan7",
    "xc7s6csga225-2": "spartan7",
    "xc7s6cpga196-1": "spartan7",
    "xc7s6cpga196-1IL": "spartan7",
    "xc7s6cpga196-1Q": "spartan7",
    "xc7s6cpga196-2": "spartan7",
    "xc7s15cpga196-1": "spartan7",
    "xc7s15cpga196-1IL": "spartan7",
    "xc7s15cpga196-1Q": "spartan7",
    "xc7s15cpga196-2": "spartan7",
    "xc7s15csga225-1": "spartan7",
    "xc7s15csga225-1IL": "spartan7",
    "xc7s15csga225-1Q": "spartan7",
    "xc7s15csga225-2": "spartan7",
    "xc7s15ftgb196-1": "spartan7",
    "xc7s15ftgb196-1IL": "spartan7",
    "xc7s15ftgb196-1Q": "spartan7",
    "xc7s15ftgb196-2": "spartan7",
    "xc7s25ftgb196-1": "spartan7",
    "xc7s25ftgb196-1IL": "spartan7",
    "xc7s25ftgb196-1Q": "spartan7",
    "xc7s25ftgb196-2": "spartan7",
    "xc7s25csga324-1": "spartan7",
    "xc7s25csga324-1IL": "spartan7",
    "xc7s25csga324-1Q": "spartan7",
    "xc7s25csga324-2": "spartan7",
    "xc7s25csga225-1": "spartan7",
    "xc7s25csga225-1IL": "spartan7",
    "xc7s25csga225-1Q": "spartan7",
    "xc7s25csga225-2": "spartan7",
    "xc7s50csga324-1": "spartan7",
    "xc7s50csga324-1IL": "spartan7",
    "xc7s50csga324-1Q": "spartan7",
    "xc7s50csga324-2": "spartan7",
    "xc7s50fgga484-1": "spartan7",
    "xc7s50fgga484-1IL": "spartan7",
    "xc7s50fgga484-1Q": "spartan7",
    "xc7s50fgga484-2": "spartan7",
    "xc7s50ftgb196-1": "spartan7",
    "xc7s50ftgb196-1IL": "spartan7",
    "xc7s50ftgb196-1Q": "spartan7",
    "xc7s50ftgb196-2": "spartan7",
    "xc7s100fgga676-1": "spartan7",
    "xc7s100fgga676-1IL": "spartan7",
    "xc7s100fgga676-1Q": "spartan7",
    "xc7s100fgga676-2": "spartan7",
    "xc7s100fgga484-1": "spartan7",
    "xc7s100fgga484-1IL": "spartan7",
    "xc7s100fgga484-1Q": "spartan7",
    "xc7s100fgga484-2": "spartan7",
    "xc7s75fgga484-1": "spartan7",
    "xc7s75fgga484-1IL": "spartan7",
    "xc7s75fgga484-1Q": "spartan7",
    "xc7s75fgga484-2": "spartan7",
    "xc7s75fgga676-1": "spartan7",
    "xc7s75fgga676-1IL": "spartan7",
    "xc7s75fgga676-1Q": "spartan7",
    "xc7s75fgga676-2": "spartan7",
    "xa7s6cpga196-1I": "aspartan7",
    "xa7s6cpga196-1Q": "aspartan7",
    "xa7s6cpga196-2I": "aspartan7",
    "xa7s6csga225-1I": "aspartan7",
    "xa7s6csga225-1Q": "aspartan7",
    "xa7s6csga225-2I": "aspartan7",
    "xa7s6ftgb196-1I": "aspartan7",
    "xa7s6ftgb196-1Q": "aspartan7",
    "xa7s6ftgb196-2I": "aspartan7",
    "xa7s15cpga196-1I": "aspartan7",
    "xa7s15cpga196-1Q": "aspartan7",
    "xa7s15cpga196-2I": "aspartan7",
    "xa7s15csga225-1I": "aspartan7",
    "xa7s15csga225-1Q": "aspartan7",
    "xa7s15csga225-2I": "aspartan7",
    "xa7s15ftgb196-1I": "aspartan7",
    "xa7s15ftgb196-1Q": "aspartan7",
    "xa7s15ftgb196-2I": "aspartan7",
    "xa7s25csga225-1I": "aspartan7",
    "xa7s25csga225-1Q": "aspartan7",
    "xa7s25csga225-2I": "aspartan7",
    "xa7s25csga324-1I": "aspartan7",
    "xa7s25csga324-1Q": "aspartan7",
    "xa7s25csga324-2I": "aspartan7",
    "xa7s25ftgb196-1I": "aspartan7",
    "xa7s25ftgb196-1Q": "aspartan7",
    "xa7s25ftgb196-2I": "aspartan7",
    "xa7s50csga324-1I": "aspartan7",
    "xa7s50csga324-1Q": "aspartan7",
    "xa7s50csga324-2I": "aspartan7",
    "xa7s50fgga484-1I": "aspartan7",
    "xa7s50fgga484-1Q": "aspartan7",
    "xa7s50fgga484-2I": "aspartan7",
    "xa7s50ftgb196-1I": "aspartan7",
    "xa7s50ftgb196-1Q": "aspartan7",
    "xa7s50ftgb196-2I": "aspartan7",
    "xa7s75fgga484-1I": "aspartan7",
    "xa7s75fgga484-1Q": "aspartan7",
    "xa7s75fgga484-2I": "aspartan7",
    "xa7s75fgga676-1I": "aspartan7",
    "xa7s75fgga676-1Q": "aspartan7",
    "xa7s75fgga676-2I": "aspartan7",
    "xa7s100fgga484-1I": "aspartan7",
    "xa7s100fgga484-1Q": "aspartan7",
    "xa7s100fgga484-2I": "aspartan7",
}


synth_directives = [
    "default",
    "runtimeoptimized",
    "AreaOptimized_high",
    "AreaOptimized_medium",
    "AlternateRoutability",
    "AreaMapLargeShiftRegToBRAM",
    "AreaMultThresholdDSP",
    "FewerCarryChains",
    "PerformanceOptimized",
]

route_directives = [
    "Explore",
    "AggressiveExplore",
    "NoTimingRelaxation",
    "MoreGlobalIterations",
    "HigherDelayCost",
    "AdvancedSkewModeling",
    "AlternateCLBRouting",
    "RuntimeOptimized",
    "Quick",
    "Default",
]

place_directives = [
    "Explore",
    "EarlyBlockPlacement",
    "WLDrivenBlockPlacement",
    "ExtraNetDelay_high",
    "ExtraNetDelay_low",
    "AltSpreadLogic_high",
    "AltSpreadLogic_medium",
    "AltSpreadLogic_low",
    "ExtraPostPlacementOpt",
    "ExtraTimingOpt",
    "SSI_SpreadLogic_high",
    "SSI_SpreadLogic_low",
    "SSI_SpreadSLLs",
    "SSI_BalanceSLLs",
    "SSI_BalanceSLRs",
    "SSI_HighUtilSLRs",
    "RuntimeOptimized",
    "Quick",
    "Default",
]

read_checkpoint_directives = [
    "RuntimeOptimized",
    "TimingClosure",
    "Quick",
]

incremental_place_directives = [
    "Explore",
    "Quick",
    "Default",
]

incremental_route_directives = [
    "Explore",
    "Quick",
    "Default",
]

read_checkpoint_directives_paragraph = """
  -directive [ RuntimeOptimized | TimingClosure | Quick ] - (Optional)
  Specifies a directive, or mode of operation for the -incremental process.

   *  RuntimeOptimized: The target WNS is the referenced from the incremental
      DCP. Trade-off timing for faster runtime.

   *  TimingClosure: The target WNS is 0. This mode attempts to meet timing
      at the expense of runtime.

   *  Quick: Specifies a low effort, non-timing-driven incremental
      implementation mode with the fastest runtime.
"""

place_directives_paragraph = """
  -directive <arg> - (Optional) Direct placement to achieve specific design
  objectives. Only one directive can be specified for a single place_design
  command, and values are case-sensitive. Supported values include:

   *  Explore - Increased placer effort in detail placement and
      post-placement optimization .

   *  EarlyBlockPlacement - Timing-driven placement of RAM and DSP blocks.
      The RAM and DSP block locations are finalized early in the placement
      process and are used as anchors to place the remaining logic.

   *  WLDrivenBlockPlacement - Wire length-driven placement of RAM and DSP
      blocks. Override timing-driven placement by directing the Vivado placer
      to minimize the distance of connections to and from blocks.

   *  ExtraNetDelay_high - Increases estimated delay of high fanout and
      long-distance nets. Three levels of pessimism are supported: high,
      medium, and low. ExtraNetDelay_high applies the highest level of
      pessimism.

   *  ExtraNetDelay_low - Increases estimated delay of high fanout and
      long-distance nets. Three levels of pessimism are supported: high,
      medium, and low. ExtraNetDelay_low applies the lowest level of
      pessimism.

   *  AltSpreadLogic_high - Spreads logic throughout the device to avoid
      creating congested regions. Three levels are supported: high, medium,
      and low. AltSpreadLogic_high achieves the highest level of spreading.

   *  AltSpreadLogic_medium - Spreads logic throughout the device to avoid
      creating congested regions. Three levels are supported: high, medium,
      and low. AltSpreadLogic_medium achieves a medium level of spreading
      compared to low and high.

   *  AltSpreadLogic_low - Spreads logic throughout the device to avoid
      creating congested regions. Three levels are supported: high, medium,
      and low. AltSpreadLogic_low achieves the lowest level of spreading.

   *  ExtraPostPlacementOpt - Increased placer effort in post-placement
      optimization.

   *  ExtraTimingOpt - Use an alternate algorithm for timing-driven placement
      with greater effort for timing.

   *  SSI_SpreadLogic_high - Distribute logic across SLRs.
      SSI_SpreadLogic_high achieves the highest level of distribution.

   *  SSI_SpreadLogic_low - Distribute logic across SLRs. SSI_SpreadLogic_low
      achieves a minimum level of logic distribution, while reducing
      placement runtime.

   *  SSI_SpreadSLLs - Partition across SLRs and allocate extra area for
      regions of higher connectivity.

   *  SSI_BalanceSLLs - Partition across SLRs while attempting to balance
      SLLs between SLRs.

   *  SSI_BalanceSLRs - Partition across SLRs to balance number of cells
      between SLRs.

   *  SSI_HighUtilSLRs - Direct the placer to attempt to place logic closer
      together in each SLR.

   *  RuntimeOptimized - Run fewest iterations, trade higher design
      performance for faster runtime.

   *  Quick - Absolute, fastest runtime, non-timing-driven, performs the
      minimum required placement for a legal design.

   *  Default - Run place_design with default settings.

  Note: The -directive option controls the overall placement strategy, and is
  not compatible with some place_design options. It can be used with
  -no_psip, -no_bufg_opt, -quiet and -verbose. Only the Explore, Quick, and
  Default directives are compatible with high reuse designs and the
  incremental implementation flow as defined by read_checkpoint -incremental.
  Refer to the Vivado Design Suite User Guide: Implementation (UG904) for
  more information on placement strategies and the use of the -directive
  option.
"""

place_note = """
  Note: The -directive option controls the overall placement strategy, and is
  not compatible with some place_design options. It can be used with
  -no_psip, -no_bufg_opt, -quiet and -verbose. Only the Explore, Quick, and
  Default directives are compatible with high reuse designs and the
  incremental implementation flow as defined by read_checkpoint -incremental.
  Refer to the Vivado Design Suite User Guide: Implementation (UG904) for
  more information on placement strategies and the use of the -directive
  option.
"""

route_directives_paragraph = """
  -directive <arg> - (Optional) Direct routing to achieve specific design
  objectives. Only one directive can be specified for a single route_design
  command, and values are case-sensitive. Supported values are:

   *  Explore - Causes the Vivado router to explore different critical path
      routes based on timing, after an initial route.

   *  AggressiveExplore - Directs the router to further expand its
      exploration of critical path routes while maintaining original timing
      budgets. The router runtime might be significantly higher compared to
      the Explore directive as the router uses more aggressive optimization
      thresholds to attempt to meet timing constraints.

   *  NoTimingRelaxation - Prevents the router from relaxing timing to
      complete routing. If the router has difficulty meeting timing, it will
      run longer to try to meet the original timing constraints.

   *  MoreGlobalIterations - Uses detailed timing analysis throughout all
      stages instead of just the final stages, and will run more global
      iterations even when timing improves only slightly.

   *  HigherDelayCost - Adjusts the router`s internal cost functions to
      emphasize delay over iterations, allowing a trade-off of runtime for
      better performance.

   *  AdvancedSkewModeling - Uses more accurate skew modeling throughout all
      routing stages which may improve design performance on higher-skew
      clock networks.

   *  AlternateCLBRouting - (UltraScale only) Chooses alternate routing
      algorithms that require extra runtime but may help resolve routing
      congestion.

   *  RuntimeOptimized - Run fewest iterations, trade higher design
      performance for faster runtime.

   *  Quick - Absolute fastest runtime, non-timing-driven, performs the
      minimum required routing for a legal design.

   *  Default - Run route_design with default settings.

  Note: The -directive option controls the overall routing strategy, and is
  not compatible with any specific route_design options, except -preserve and
  -tns_cleanup. It can also be used with -quiet and -verbose. Only the
  Explore, Quick, and Default directives are compatible with high reuse
  designs and the incremental implementation flow as defined by
  read_checkpoint -incremental. Refer to the Vivado Design Suite User Guide:
  Implementation (UG904) for more information on the use of the -directive
  option.
"""
route_note = """
  Note: The -directive option controls the overall routing strategy, and is
  not compatible with any specific route_design options, except -preserve and
  -tns_cleanup. It can also be used with -quiet and -verbose. Only the
  Explore, Quick, and Default directives are compatible with high reuse
  designs and the incremental implementation flow as defined by
  read_checkpoint -incremental. Refer to the Vivado Design Suite User Guide:
  Implementation (UG904) for more information on the use of the -directive
  option.
"""
synth_directives_paragraph = """
  -directive <arg> - (Optional) Direct synthesis to achieve specific design
  objectives. Only one directive can be specified for a single synth_design
  command, and values are case-sensitive. Valid values are:

   *  default - Run the default synthesis process.

   *  runtimeoptimized - Perform fewer timing optimizations and eliminate
      some RTL optimizations to reduce synthesis run time.

   *  AreaOptimized_high - Perform general area optimizations including
      AreaMapLargeShiftRegToBRAM, AreaThresholdUseDSP directives.

   *  AreaOptimized_medium - Perform general area optimizations including
      forcing ternary adder implementation, applying new thresholds for use
      of carry chain in comparators, and implementing area optimized
      multiplexers.

   *  AlternateRoutability - Algorithms to improve routability with reduced
      use of MUXFs and CARRYs.

   *  AreaMapLargeShiftRegToBRAM - Detects large shift registers and
      implements them using dedicated blocks of RAM.

   *  AreaMultThresholdDSP - Lower threshold for dedicated DSP block
      inference for packing multipliers.

   *  FewerCarryChains - Higher operand size threshold to use LUTs instead of
      the carry chain.

   *  PerformanceOptimized - Perform general timing optimizations including
      logic level reduction at the expense of area.
"""
help_synth_design = """
help synth_design
synth_design

Description:
Synthesize a design using Vivado Synthesis and open that design

Syntax:
synth_design  [-name <arg>] [-part <arg>] [-constrset <arg>] [-top <arg>]
              [-include_dirs <args>] [-generic <args>] [-verilog_define <args>]
              [-flatten_hierarchy <arg>] [-gated_clock_conversion <arg>]
              [-directive <arg>] [-rtl] [-bufg <arg>] [-no_lc]
              [-fanout_limit <arg>] [-shreg_min_size <arg>] [-mode <arg>]
              [-fsm_extraction <arg>] [-rtl_skip_ip] [-rtl_skip_constraints]
              [-keep_equivalent_registers] [-resource_sharing <arg>]
              [-cascade_dsp <arg>] [-control_set_opt_threshold <arg>]
              [-incremental <arg>] [-max_bram <arg>] [-max_uram <arg>]
              [-max_dsp <arg>] [-max_bram_cascade_height <arg>]
              [-max_uram_cascade_height <arg>] [-retiming] [-no_srlextract]
              [-assert] [-no_timing_driven] [-sfcu] [-quiet] [-verbose]

Returns:
design object

Usage:
  Name                          Description
  -----------------------------------------
  [-name]                       Design name
  [-part]                       Target part
  [-constrset]                  Constraint fileset to use
  [-top]                        Specify the top module name
  [-include_dirs]               Specify verilog search directories
  [-generic]                    Specify generic parameters. Syntax: -generic
                                <name>=<value> -generic <name>=<value> ...
  [-verilog_define]             Specify verilog defines. Syntax:
                                -verilog_define <macro_name>[=<macro_text>]
                                -verilog_define <macro_name>[=<macro_text>]
                                ...
  [-flatten_hierarchy]          Flatten hierarchy during LUT mapping. Values:
                                full, none, rebuilt
                                Default: rebuilt
  [-gated_clock_conversion]     Convert clock gating logic to flop enable.
                                Values: off, on, auto
                                Default: off
  [-directive]                  Synthesis directive. Values: default,
                                RuntimeOptimized, AreaOptimized_high,
                                AreaOptimized_medium,AlternateRoutability,
                                AreaMapLargeShiftRegToBRAM,
                                AreaMultThresholdDSP, FewerCarryChains,Perfor
                                manceOptimized
                                Default: default
  [-rtl]                        Elaborate and open an rtl design
  [-bufg]                       Max number of global clock buffers used by
                                synthesis
                                Default: 12
  [-no_lc]                      Disable LUT combining. Do not allow combining
                                LUT pairs into single dual output LUTs.
  [-fanout_limit]               Fanout limit. This switch does not impact
                                control signals (such as set,reset, clock
                                enable) use MAX_FANOUT to replicate these
                                signals if needed.
                                Default: 10000
  [-shreg_min_size]             Minimum length for chain of registers to be
                                mapped onto SRL
                                Default: 3
  [-mode]                       The design mode. Values: default,
                                out_of_context
                                Default: default
  [-fsm_extraction]             FSM Extraction Encoding. Values: off,
                                one_hot, sequential, johnson, gray,
                                user_encoding, auto
                                Default: auto
  [-rtl_skip_ip]                Exclude subdesign checkpoints in the RTL
                                elaboration of the design; requires -rtl
                                option.
  [-rtl_skip_constraints]       Do not load and validate constraints against
                                elaborated design; requires -rtl option.
  [-keep_equivalent_registers]  Prevents registers sourced by the same logic
                                from being merged. (Note that the merging can
                                otherwise be prevented using the synthesis
                                KEEP attribute)
  [-resource_sharing]           Sharing arithmetic operators. Value: auto,
                                on, off
                                Default: auto
  [-cascade_dsp]                Controls how adders summing DSP block outputs
                                will be implemented. Value: auto, tree, force
                                Default: auto
  [-control_set_opt_threshold]  Threshold for synchronous control set
                                optimization to lower number of control sets.
                                Valid values are 'auto' and non-negative
                                integers. The higher the number, the more
                                control set optimization will be performed
                                and fewer control sets will result. To
                                disable control set optimization completely,
                                set to 0.
                                Default: auto
  [-incremental]                dcp file for incremental flowvalue of this is
                                the file name
  [-max_bram]                   Maximum number of block RAM allowed in
                                design. (Note -1 means that the tool will
                                choose the max number allowed for the part in
                                question)
                                Default: -1
  [-max_uram]                   Maximum number of Ultra RAM blocks allowed in
                                design. (Note -1 means that the tool will
                                choose the max number allowed for the part in
                                question)
                                Default: -1
  [-max_dsp]                    Maximum number of block DSP allowed in
                                design. (Note -1 means that the tool will
                                choose the max number allowed for the part in
                                question)
                                Default: -1
  [-max_bram_cascade_height]    Controls the maximum number of BRAM that can
                                be cascaded by the tool. (Note -1 means that
                                the tool will choose the max number allowed
                                for the part in question)
                                Default: -1
  [-max_uram_cascade_height]    Controls the maximum number of URAM that can
                                be cascaded by the tool. (Note -1 means that
                                the tool will choose the max number allowed
                                for the part in question)
                                Default: -1
  [-retiming]                   Seeks to improve circuit performance for
                                intra-clock sequential paths by automatically
                                moving registers (register balancing) across
                                combinatorial gates or LUTs.  It maintains
                                the original behavior and latency of the
                                circuit and does not require changes to the
                                RTL sources.
  [-no_srlextract]              Prevents the extraction of shift registers so
                                that they get implemented as simple registers
  [-assert]                     Enable VHDL assert statements to be
                                evaluated. A severity level of failure will
                                stop the synthesis flow and produce an error.
  [-no_timing_driven]           Do not run in timing driven mode
  [-sfcu]                       Run in single-file compilation unit mode
  [-quiet]                      Ignore command errors
  [-verbose]                    Suspend message limits during command
                                execution

Categories:
Tools

Description:

  Directly launches the Vivado synthesis engine to compile and synthesize a
  design in either Project Mode or Non-Project Mode in the Vivado Design
  Suite. Refer to the Vivado Design Suite User Guide: Design Flows Overview
  (UG892) for a complete description of Project Mode and Non-Project Mode.

  Vivado synthesis can be launched directly with the synth_design command in
  the Non-Project Mode of the Vivado Design Suite.

  Note: The synth_design can be multi-threaded to speed the process. Refer to
  the set_param command for more information on setting the
  general.maxThreads parameter.

  In Project Mode, synthesis should be launched from an existing synthesis
  run created with the create_run command. The run is launched using the
  launch_runs command, and this in turn calls synth_design for Vivado
  synthesis.

  You can also use the synth_design command to elaborate RTL source files,
  and open an elaborated design:

    synth_design -rtl -name rtl_1


  This command returns a transcript of the synthesis process, or returns an
  error if it fails.

Arguments:

  -name <arg> - (Optional) This is the name assigned to the synthesized
  design when it is opened by the Vivado tool after synthesis has completed.
  This name is for reference purposes, and has nothing to do with the
  top-level of the design or any logic contained within.

  -part <arg> - (Optional) The target Xilinx device to use for the design. If
  the part is not specified the default part assigned to the project will be
  used.

  -constrset <arg> - (Optional) The name of the XDC constraints to use when
  synthesizing the design. Vivado synthesis requires the use of XDC, and does
  not support UCF. The -constrset argument must refer to a constraint fileset
  that exists. It cannot be used to create a new fileset. Use the
  create_fileset command for that purpose.

  -top <arg> - (Optional) The top module of the design hierarchy.

  Note: If you use the find_top command to define the -top option, be sure to
  specify only one top if find_top returns multiple prospects. See the
  examples below.

  -include_dirs <args> - (Optional) The directories to search for Verilog
  `include files. You can specify multiple directories by creating a list to
  contain them:

    -include_dirs {C:/data/include1 C:/data/include2}


  -generic <name>=<value> - (Optional) The value of a VHDL generic entity, or
  of a Verilog parameter. The -generic option can be used to override the
  assigned values of parameters in the RTL design sources. However it can
  only override parameters at the top level of the design. The parameters of
  lower-level modules can only be overridden at the time of instantiation and
  not by the -generic option. The syntax for the -generic argument is
  <name>=<value>, specifying the name of the generic or parameter, and the
  value to be assigned. Repeat the -generic option multiple times in the
  synth_design command for each generic or parameter value to be defined:

    synth_design -generic width=32 -generic depth=512 ...


  Note: When specifying binary values for boolean or std_logic VHDL generic
  types, you must specify the value using the Verilog bit format, rather than
  standard VHDL format:

    0 = 1`b0
    01010000 = 8`b01010000


  -verilog_define <name>=<text> - (Optional) Set values for Verilog `define,
  and `ifdef, statements. The syntax for the -verilog_define argument is
  <name>=<text>, specifying the name of the define directive, and the value
  to be assigned. The argument can be reused multiple times in a single
  synth_design command.

    synth_design -verilog_define <name>=<value> -verilog_define <name>=<value> ...


  -flatten_hierarchy <arg> - (Optional) Flatten the hierarchy of the design
  during LUT mapping. The valid values are:

   *  rebuilt - This will attempt to rebuild the original hierarchy of the
      RTL design after synthesis has completed. This is the default setting.

   *  full - Flatten the hierarchy of the design.

   *  none - Do not flatten the hierarchy of the design. This will preserve
      the hierarchy of the design, but will also limit the design
      optimization that can be performed by the synthesis tool.

  -gated_clock_conversion <arg> - (Optional) Convert clock gating logic to
  use the flop enable pins when available. This optimization can eliminate
  logic and simplify the netlist. Refer to the GATED_CLOCK property in the
  Vivado Design Suite User Guide: Synthesis (UG901) for more information.
  Valid values for this option are:

   *  off - Disables the conversion of clock gating logic during synthesis,
      regardless of the use of the GATED_CLOCK property in the RTL design.

   *  on - Converts clock gating logic based on the use of the GATED_CLOCK
      property in the RTL design.

   *  auto - lets Vivado synthesis perform gated clock conversion if either
      the GATED_CLOCK property is present in the RTL, or if the Vivado tool
      detects a gate with a valid clock constraint.

  -directive <arg> - (Optional) Direct synthesis to achieve specific design
  objectives. Only one directive can be specified for a single synth_design
  command, and values are case-sensitive. Valid values are:

   *  default - Run the default synthesis process.

   *  runtimeoptimized - Perform fewer timing optimizations and eliminate
      some RTL optimizations to reduce synthesis run time.

   *  AreaOptimized_high - Perform general area optimizations including
      AreaMapLargeShiftRegToBRAM, AreaThresholdUseDSP directives.

   *  AreaOptimized_medium - Perform general area optimizations including
      forcing ternary adder implementation, applying new thresholds for use
      of carry chain in comparators, and implementing area optimized
      multiplexers.

   *  AlternateRoutability - Algorithms to improve routability with reduced
      use of MUXFs and CARRYs.

   *  AreaMapLargeShiftRegToBRAM - Detects large shift registers and
      implements them using dedicated blocks of RAM.

   *  AreaMultThresholdDSP - Lower threshold for dedicated DSP block
      inference for packing multipliers.

   *  FewerCarryChains - Higher operand size threshold to use LUTs instead of
      the carry chain.

   *  PerformanceOptimized - Perform general timing optimizations including
      logic level reduction at the expense of area.

  -rtl - (Optional) Elaborate the HDL source files and open the RTL design.
  In designs that use out-of-context (OOC) modules, such as IP from the
  Xilinx IP catalog, the Vivado Design Suite will import synthesized design
  checkpoints (DCP) for the OOC modules in the design, and import associated
  constraint files (XDC) into the elaborated design. However, you can disable
  the default behavior using the -rtl_skip_ip and -rtl_skip_constraints
  options.

  -rtl_skip_ip - (Optional) This option requires the use of the -rtl option.
  When elaborating the RTL design, this option causes the Vivado Design Suite
  to skip loading the DCP files for OOC modules in the design, and instead
  load a stub file to treat the OOC modules as black boxes. This can
  significantly speed elaboration of the design.

  Note: An OOC synthesis run will be needed in either case to generate the
  DCP file that is loaded during elaboration, or to generate the stub file
  needed for the black box.

  -rtl_skip_constraints - (Optional) This option requires the use of the -rtl
  option. When elaborating the RTL design, this option causes the Vivado
  Design Suite to skip loading any design constraints (XDC) into the
  elaborated design. This can significantly speed elaboration of the design.

  -bufg <arg> - (Optional) Specify the maximum number of global clock buffers
  to be used on clock nets during synthesis. Specified as a value >= 1, which
  should not exceed the BUFG count on the target device. The default value is
  12.

  Note: Vivado synthesis infers up to the number of BUFGs specified,
  including those instantiated in the RTL source. For example, with the
  default setting of -bufg 12, if there are three BUFGs instantiated in the
  RTL, the tool infers up to nine more for a total of 12.

  -no_lc - (Optional) Disable the default LUT combining feature of Vivado
  synthesis.

  -fanout_limit <arg> - (Optional) Specify a target limit for the maximum net
  fanout applied during synthesis. The default value is 10,000. This option
  is applied by Vivado synthesis when the number of loads exceeds an internal
  limit, and is only a guideline for the tool, not a strict requirement. When
  strict fanout control is required for specific signals, use the MAX_FANOUT
  property instead.

  Note: -fanout_limit does not affect control signals (such as set, reset,
  clock enable). Use the MAX_FANOUT property to replicate these signals as
  needed.

  -shreg_min_size <arg> - (Optional) Specified as an integer, this is the
  minimum length for a chain of registers to be mapped onto SRL. The default
  is three.

  -mode [ default | out_of_context ] - (Optional) Out of Context mode
  specifies the synthesis of an IP module, or block module, for use in an
  out-of-context design flow. This mode turns off I/O buffer insertion for
  the module, and marks the module as OOC, to facilitate its use in the tool
  flow. The block can also be implemented for analysis purposes. Refer to the
  Vivado Design Suite User Guide: Designing with IP (UG896) or the Vivado
  Design Suite User Guide: Hierarchical Design (UG905) for more information.

  -fsm_extraction <arg> - (Optional) Finite state machine (FSM) encoding is
  automatic (auto) in Vivado synthesis by default. This option enables state
  machine identification and specifies the type of encoding that should be
  applied. Valid values are: off, one_hot, sequential, johnson, gray, auto.
  Automatic encoding (auto) allows the tool to choose the best encoding for
  each state machine identified. In this case, the tool may use different
  encoding styles for different FSMs in the same design.

  Note: Use -fsm_extraction off to disable finite state machine extraction in
  Vivado synthesis. This will override the FSM_ENCODING property when
  specified.

  -keep_equivalent_registers - (Optional) Works like the KEEP property to
  prevent the merging of registers during optimization.

  -resource_sharing <arg> - (Optional) Share arithmetic operators like adders
  or subtractors between different signals, rather than creating new
  operators. This can result in better area usage when it is turned on. Valid
  values are: auto, on, off. The default is auto.

  -cascade_dsp [ auto | tree | force ] - (Optional) Specifies how to
  implement adders that add DSP block outputs. Valid values include auto,
  tree, force. The default setting is auto.

  -control_set_opt_threshold <arg> - (Optional) Threshold for synchronous
  control set optimization to decrease the number of control sets. Specifies
  how large the fanout of a control set should be before it starts using it
  as a control set. For example, if -control_set_opt_threshold is set to 10,
  a synchronous reset that only fans out to 5 registers would be moved to the
  D input logic, rather than using the reset line of a register. However, if
  -control_set_opt_threshold is set to 4, then the reset line is used. This
  option can be specified as "auto", or as an integer from 0 to 16. The
  default setting is "auto", and the actual threshold used under "auto" can
  vary depending on the selected device architecture.

  -incremental - (Optional) Specify a DCP file for the incremental
  compilation flow. In the incremental synthesis flow, the netlist from the
  incremental DCP is applied to the design objects in the current design to
  reuse existing synthesis results when possible.

  -max_bram <arg> - (Optional) Specify the maximum number of Block RAM to add
  to the design during synthesis. Specify a value >= 1, which should not
  exceed the available BRAM count on the target device. If a value of -1 is
  used, the Vivado synthesis tool will not exceed the available Block RAM
  limit of the device. The default value is -1.

  Note: A value of 0 directs Vivado synthesis to not infer BRAMs in the
  design, but is not a recommended value.

  -max_uram <arg> - (Optional) Specify the maximum number of Ultra RAM blocks
  (URAM) to add to the design during synthesis. Specify a value >= 1, which
  should not exceed the available URAM count on the target device. If a value
  of -1 is used, the Vivado synthesis tool will not exceed the available URAM
  block limit of the device. The default value is -1.

  Note: A value of 0 directs Vivado synthesis to not infer URAM in the
  design, but is not a recommended value.

  -max_dsp <arg> - (Optional) Specify the maximum number of DSPs to add to
  the design during synthesis. Specify a value >= 1, which should not exceed
  the available DSP count on the target device. If a value of -1 is used, the
  Vivado synthesis tool will not exceed the available limit of the device.
  The default value is -1.

  Note: A value of 0 directs Vivado synthesis to not infer DSPs in the
  design, but is not a recommended value.

  -max_bram_cascade_height <arg> - (Optional) Controls the maximum number of
  BRAM that can be cascaded by the tool. A value of -1 lets Vivado synthesis
  choose up to the maximum number allowed for the target part. The default
  value is -1.

  -max_uram_cascade_height <arg> - (Optional) Controls the maximum number of
  URAM that can be cascaded by the tool. A value of -1 lets Vivado synthesis
  choose up to the maximum number allowed for the target part. The default
  value is -1.

  -retiming - (Optional) Seeks to improve circuit performance for intra-clock
  sequential paths by automatically moving registers (register balancing)
  across combinatorial gates or LUTs. It maintains the original behavior and
  latency of the circuit and does not require changes to the RTL sources.

  -no_srlextract - (Optional) Prevents the extraction of shift registers so
  that they get implemented as simple registers.

  -assert - (Optional) Enable VHDL assert statements to be evaluated. A
  severity level of failure will stop the synthesis flow and produce an
  error.

  -no_timing_driven - (Optional) Disables the default timing driven synthesis
  algorithm. This results in a reduced synthesis runtime, but ignores the
  effect of timing on synthesis.

  -quiet - (Optional) Execute the command quietly, returning no messages from
  the command. The command also returns TCL_OK regardless of any errors
  encountered during execution.

  Note: Any errors encountered on the command-line, while launching the
  command, will be returned. Only errors occurring inside the command will be
  trapped.

  -verbose - (Optional) Temporarily override any message limits and return
  all messages from this command.

  Note: Message limits can be defined with the set_msg_config command.

Examples:

  The following example uses the set_property command to define the target
  part for the active project, then elaborates the source files and opens an
  RTL design:

    set_property part xc7vx485tffg1158-1 [current_project]
    synth_design -rtl -name rtl_1


  Note: The default source set, constraint set, and part will be used in this
  example.

  The following example uses the find_top command to define the top of the
  current design for synthesis:


    synth_design -top [lindex [find_top] 0]


  Note: Since find_top returns multiple possible candidates, choosing index 0
  chooses the best top candidate for synthesis.

  The following example runs synthesis on the current design, defining the
  top module and the target part, and specifying no flattening of the
  hierarchy. The results of the synthesis run are then opened in a netlist
  design:

    synth_design -top top -part xc7k70tfbg676-2 -flatten_hierarchy none
    open_run synth_1 -name netlist_1


See Also:

   *  create_ip_run
   *  create_run
   *  current_design
   *  current_project
   *  find_top
   *  open_run
   *  opt_design
   *  report_seu
   *  set_property
"""
help_place_design = """
help place_design
place_design

Description: 
Automatically place ports and leaf-level instances

Syntax:
place_design  [-directive <arg>] [-no_timing_driven] [-timing_summary]
              [-unplace] [-post_place_opt] [-no_psip] [-no_bufg_opt] [-quiet]
              [-verbose]

Usage:
  Name                 Description
  --------------------------------
  [-directive]         Mode of behavior (directive) for this command. Please
                       refer to Arguments section of this help for values for
                       this option.
                       Default: Default
  [-no_timing_driven]  Do not run in timing driven mode
  [-timing_summary]    Enable accurate post-placement timing summary.
  [-unplace]           Unplace all the instances which are not locked by
                       Constraints.
  [-post_place_opt]    Run only the post commit optimizer
  [-no_psip]           Disable PSIP (Physical Synthesis In Placer)
                       optimization during placement.
  [-no_bufg_opt]       Disable global buffer insertion during placement
  [-quiet]             Ignore command errors
  [-verbose]           Suspend message limits during command execution

Categories:
Tools

Description:

  Place the specified ports and logic cells in the current design, or all
  ports and logic cells, onto device resources on the target part. The tool
  optimizes placement to minimize negative timing slack and reduce overall
  wire length, while also attempting to spread out placement to reduce
  routing congestion.

  Placement is one step of the complete design implementation process, which
  can be run automatically through the use of the launch_runs command when
  running the Vivado tools in Project Mode.

  In Non-Project Mode, the implementation process must be run manually with
  the individual commands: opt_design, place_design, phys_opt_design,
  power_opt_design, and route_design. Refer to the Vivado Design Suite User
  Guide: Design Flows Overview (UG892) for a complete description of Project
  Mode and Non-Project Mode.

  Both placement and routing can be completed incrementally, based on prior
  results stored in a Design Checkpoint file (DCP), using the incremental
  implementation flow. Refer to the read_checkpoint command, or to Vivado
  Design Suite User Guide: Implementation (UG904) for more information on
  incremental place and route.

  Note: The place_design can be multi-threaded to speed the process. Refer to
  the set_param command for more information on setting the
  general.maxThreads parameter.

  You can also manually place some elements of the design using place_ports,
  or by setting LOC properties on the cell, and then automatically place the
  remainder of the design using place_design.

  This command requires an open synthesized design, and it is recommended
  that you run the opt_design command prior to running place_design to avoid
  placing a suboptimal netlist.

Arguments:

  -directive <arg> - (Optional) Direct placement to achieve specific design
  objectives. Only one directive can be specified for a single place_design
  command, and values are case-sensitive. Supported values include:

   *  Explore - Increased placer effort in detail placement and
      post-placement optimization .

   *  EarlyBlockPlacement - Timing-driven placement of RAM and DSP blocks.
      The RAM and DSP block locations are finalized early in the placement
      process and are used as anchors to place the remaining logic.

   *  WLDrivenBlockPlacement - Wire length-driven placement of RAM and DSP
      blocks. Override timing-driven placement by directing the Vivado placer
      to minimize the distance of connections to and from blocks.

   *  ExtraNetDelay_high - Increases estimated delay of high fanout and
      long-distance nets. Three levels of pessimism are supported: high,
      medium, and low. ExtraNetDelay_high applies the highest level of
      pessimism.

   *  ExtraNetDelay_low - Increases estimated delay of high fanout and
      long-distance nets. Three levels of pessimism are supported: high,
      medium, and low. ExtraNetDelay_low applies the lowest level of
      pessimism.

   *  AltSpreadLogic_high - Spreads logic throughout the device to avoid
      creating congested regions. Three levels are supported: high, medium,
      and low. AltSpreadLogic_high achieves the highest level of spreading.

   *  AltSpreadLogic_medium - Spreads logic throughout the device to avoid
      creating congested regions. Three levels are supported: high, medium,
      and low. AltSpreadLogic_medium achieves a medium level of spreading
      compared to low and high.

   *  AltSpreadLogic_low - Spreads logic throughout the device to avoid
      creating congested regions. Three levels are supported: high, medium,
      and low. AltSpreadLogic_low achieves the lowest level of spreading.

   *  ExtraPostPlacementOpt - Increased placer effort in post-placement
      optimization.

   *  ExtraTimingOpt - Use an alternate algorithm for timing-driven placement
      with greater effort for timing.

   *  SSI_SpreadLogic_high - Distribute logic across SLRs.
      SSI_SpreadLogic_high achieves the highest level of distribution.

   *  SSI_SpreadLogic_low - Distribute logic across SLRs. SSI_SpreadLogic_low
      achieves a minimum level of logic distribution, while reducing
      placement runtime.

   *  SSI_SpreadSLLs - Partition across SLRs and allocate extra area for
      regions of higher connectivity.

   *  SSI_BalanceSLLs - Partition across SLRs while attempting to balance
      SLLs between SLRs.

   *  SSI_BalanceSLRs - Partition across SLRs to balance number of cells
      between SLRs.

   *  SSI_HighUtilSLRs - Direct the placer to attempt to place logic closer
      together in each SLR.

   *  RuntimeOptimized - Run fewest iterations, trade higher design
      performance for faster runtime.

   *  Quick - Absolute, fastest runtime, non-timing-driven, performs the
      minimum required placement for a legal design.

   *  Default - Run place_design with default settings.

  Note: The -directive option controls the overall placement strategy, and is
  not compatible with some place_design options. It can be used with
  -no_psip, -no_bufg_opt, -quiet and -verbose. Only the Explore, Quick, and
  Default directives are compatible with high reuse designs and the
  incremental implementation flow as defined by read_checkpoint -incremental.
  Refer to the Vivado Design Suite User Guide: Implementation (UG904) for
  more information on placement strategies and the use of the -directive
  option.

  -no_timing_driven - (Optional) Disables the default timing driven placement
  algorithm. This results in a faster placement based on wire lengths, but
  ignores any timing constraints during the placement process.

  -timing_summary - (Optional) Report the post-placement worst negative slack
  (WNS) using results from static timing analysis. The WNS value is identical
  to that of report_timing_summary when run on the post-placement design. By
  default the placer reports an estimated WNS based on incremental placement
  updates during the design implementation. The -timing_summary option incurs
  additional runtime to run a full timing analysis.

  -unplace - (Optional) Unplace all the instances which are not locked by
  constraints. Cells with fixed placement (IS_LOC_FIXED set to TRUE), are not
  affected.

  Note: Use the set_property to change IS_LOC_FIXED to FALSE prior to
  unplacing fixed cells.

  -post_place_opt - (Optional) Run optimization after placement to improve
  critical path timing at the expense of additional placement and routing
  runtime. This optimization can be run at any stage after placement. The
  optimization examines the worst case timing paths and tries to improve
  placement to reduce delay.

  Note: Any placement changes will result in unrouted connections, so
  route_design will need to be run after -post_place_opt.

  -no_psip - (Optional) Disable PSIP (Physical Synthesis In Placer)
  optimization during placement. By default, to improve delay the Vivado
  placer performs optimizations such as replicating drivers of high-fanout
  nets and drivers of loads that are far-apart. This option disables those
  optimizations.

  -no_bufg_opt - (Optional) By default, global buffers are inserted during
  placement to drive high-fanout nets. This option disables global buffer
  insertion to reduce the number of routing resources consumed by high fanout
  nets that are not timing-critical.

  -quiet - (Optional) Execute the command quietly, returning no messages from
  the command. The command also returns TCL_OK regardless of any errors
  encountered during execution.

  Note: Any errors encountered on the command-line, while launching the
  command, will be returned. Only errors occurring inside the command will be
  trapped.

  -verbose - (Optional) Temporarily override any message limits and return
  all messages from this command.

  Note: Message limits can be defined with the set_msg_config command.

Examples:

  The following example places the current design, runs optimization, routes
  the design, runs post placement optimization, and then reroutes the design
  to cleanup any unconnected nets as a result of post placement optimization:

    place_design
    phys_opt_design
    route_design
    place_design -post_place_opt
    phys_opt_design
    route_design


  The following example directs the Vivado placer to try different placement
  algorithms to achieve a better placement result:

    place_design -directive Explore


  This example unplaces the current design:

    place_design -unplace


See Also:

   *  launch_runs
   *  opt_design
   *  place_ports
   *  phys_opt_design
   *  power_opt_design
   *  read_checkpoint
   *  route_design
   *  set_property
"""
help_route_design = """
help route_design
route_design

Description:
Route the current design

Syntax:
route_design  [-unroute] [-release_memory] [-nets <args>] [-physical_nets]
              [-pins <arg>] [-directive <arg>] [-tns_cleanup]
              [-no_timing_driven] [-preserve] [-delay] [-auto_delay]
              -max_delay <arg> -min_delay <arg> [-timing_summary] [-finalize]
              [-ultrathreads] [-quiet] [-verbose]

Usage:
  Name                 Description
  --------------------------------
  [-unroute]           Unroute whole design or the given nets/pins if used
                       with -nets or -pins.
  [-release_memory]    Release Router memory. Not compatible with any other
                       options.
  [-nets]              Operate on the given nets.
  [-physical_nets]     Operate on all physical nets.
  [-pins]              Operate on the given pins.
  [-directive]         Mode of behavior (directive) for this command. Please
                       refer to Arguments section of this help for values for
                       this option.
                       Default: Default
  [-tns_cleanup]       Do optional TNS clean up.
  [-no_timing_driven]  Do not run in timing driven mode.
  [-preserve]          Preserve existing routing.
  [-delay]             Use with -nets or -pins option to route in delay
                       driven mode.
  [-auto_delay]        Use with -nets or -pins option to route in constraint
                       driven mode.
  -max_delay           Use with -pins option to specify the max_delay
                       constraint on the pins.When specified -delay is
                       implicit.
  -min_delay           Use with -pins option to specify the max_delay
                       constraint on the pins.When specified -delay is
                       implicit.
  [-timing_summary]    Enable post-router signoff timing summary.
  [-finalize]          finalize route_design in interactive mode.
  [-ultrathreads]      Enable Turbo mode routing.
  [-quiet]             Ignore command errors
  [-verbose]           Suspend message limits during command execution

Categories:
Tools

Description:

  Route the nets in the current design to complete logic connections on the
  target part.

  Predefined routing strategies can be quickly selected using the
  route_design -directive command, or specific route options can be
  configured to define your own routing strategy.

  Routing can be completed automatically with route_design, or can be
  completed iteratively using the various options of the route_design command
  to achieve route completion and timing closure. Iterative routing provides
  you some control over the routing process to route critical nets first and
  then route less critical nets, and to control the level of effort and the
  timing algorithms for these various route passes.

  Routing is one step of the complete design implementation process, which
  can be run automatically through the use of the launch_runs command when
  running the Vivado tools in Project Mode.

  In Non-Project Mode, the implementation process must be run manually with
  the individual commands: opt_design, place_design, phys_opt_design,
  power_opt_design, and route_design. Refer to the Vivado Design Suite User
  Guide: Design Flows Overview (UG892) for a complete description of Project
  Mode and Non-Project Mode.

  Note: The route_design can be multi-threaded to speed the process. Refer to
  the set_param command for more information on setting the
  general.maxThreads parameter.

  Both placement and routing can be completed incrementally, based on prior
  results stored in a Design Checkpoint file (DCP), using the incremental
  implementation flow. Refer to the read_checkpoint command, or to Vivado
  Design Suite User Guide: Implementation (UG904) for more information on
  incremental place and route.

  This command requires a placed design, and it is recommended that you have
  optimized the design with opt_design prior to placement.

Arguments:

  -unroute <arg> - (Optional) Unroute nets in the design. If no arguments are
  specified, all nets in the design are unrouted. The route_design command
  will not route any nets when the -unroute option is specified.

   *  Combine with the -nets option to limit unrouting to a list of nets.

   *  Combine with the -pins option to unroute from a specified pin to the
      nearest branch of the net.

   *  Combine with the -physical_nets option to unroute all logic 1 and logic
      0 nets.

  -release_memory - (Optional) Free router memory resources for subsequent
  route passes. This option does not run route passes, but only releases
  memory held by the router to reduce router initialization. The router will
  need to reload design data for subsequent route passes.

  -nets <args> - (Optional) Route or unroute only the specified net objects.
  Net objects must be specified using the get_nets command.

  Note: The router uses a quick route approach to find a routing solution for
  the specified nets, ignoring timing delays, when routing with -nets,
  -physical_nets, or -pins specified. Use -delay to find a route with the
  shortest delay.

  -physical_nets - (Optional) Route or unroute only logic zero and logic one
  nets.

  -pins <args> - (Optional) Route or unroute to the specified pins, which
  must be input pins. If a specified pin is driven by a multiple fanout net,
  only the route segment between the net and pin is affected.

  -directive <arg> - (Optional) Direct routing to achieve specific design
  objectives. Only one directive can be specified for a single route_design
  command, and values are case-sensitive. Supported values are:

   *  Explore - Causes the Vivado router to explore different critical path
      routes based on timing, after an initial route.

   *  AggressiveExplore - Directs the router to further expand its
      exploration of critical path routes while maintaining original timing
      budgets. The router runtime might be significantly higher compared to
      the Explore directive as the router uses more aggressive optimization
      thresholds to attempt to meet timing constraints.

   *  NoTimingRelaxation - Prevents the router from relaxing timing to
      complete routing. If the router has difficulty meeting timing, it will
      run longer to try to meet the original timing constraints.

   *  MoreGlobalIterations - Uses detailed timing analysis throughout all
      stages instead of just the final stages, and will run more global
      iterations even when timing improves only slightly.

   *  HigherDelayCost - Adjusts the router`s internal cost functions to
      emphasize delay over iterations, allowing a trade-off of runtime for
      better performance.

   *  AdvancedSkewModeling - Uses more accurate skew modeling throughout all
      routing stages which may improve design performance on higher-skew
      clock networks.

   *  AlternateCLBRouting - (UltraScale only) Chooses alternate routing
      algorithms that require extra runtime but may help resolve routing
      congestion.

   *  RuntimeOptimized - Run fewest iterations, trade higher design
      performance for faster runtime.

   *  Quick - Absolute fastest runtime, non-timing-driven, performs the
      minimum required routing for a legal design.

   *  Default - Run route_design with default settings.

  Note: The -directive option controls the overall routing strategy, and is
  not compatible with any specific route_design options, except -preserve and
  -tns_cleanup. It can also be used with -quiet and -verbose. Only the
  Explore, Quick, and Default directives are compatible with high reuse
  designs and the incremental implementation flow as defined by
  read_checkpoint -incremental. Refer to the Vivado Design Suite User Guide:
  Implementation (UG904) for more information on the use of the -directive
  option.

  -tns_cleanup - (Optional) By default, to reduce runtime, the router focuses
  on optimizing the Worst Negative Slack (WNS) path as opposed to Total
  Negative Slack (TNS) paths. This option invokes an optional phase at the
  end of routing where the router attempts to fix the TNS paths, those
  failing paths other than the WNS path. This option may reduce TNS at the
  cost of added runtime, but will not affect WNS. The -tns_cleanup option is
  recommended when using post-route phys_opt_design to ensure that
  optimization focuses on the WNS path and does not waste effort on TNS paths
  that can be fixed by the router. This option can be used in combination
  with -directive.

  -no_timing_driven - (Optional) Disables the default timing driven routing
  algorithm. This results in faster routing results, but ignores any timing
  constraints during the routing process.

  -preserve - (Optional) Existing completed routes will be preserved and not
  subject to the rip-up and reroute phase. This does not apply to routing
  that is fixed using the IS_ROUTE_FIXED or FIXED_ROUTE properties, which is
  not subject to being rerouted. Routing is preserved only for the current
  route_design command.

  Note: Partially routed nets are subject to rerouting to complete the
  connection. If you want to preserve the routing of a partially routed net,
  you should apply the FIXED_ROUTE property to the portion of the route you
  want to preserve.

  -delay - (Optional) Can only be used in combination with the -nets or -pins
  options. By default nets are routed to achieve the fastest routing runtime,
  ignoring timing constraints, when using -nets and -pins options. The -delay
  option directs the router to try to achieve the shortest routed
  interconnect delay, but still ignores timing constraints.

  Note: You can specify multiple nets to route at the same time using the
  -delay option, but this can result in conflicts for routing resources. The
  Vivado router may create node overlap errors if the nets are in close
  proximity to each other because the -delay option will reuse routing
  resources to achieve the shortest routes for all specified nets. Therefore
  it is recommended to route nets and pins individually using the -delay
  option, beginning with the most critical.

  -auto_delay - (Optional) Can only be used in combination with the -nets or
  -pins options. It is recommended to use the -auto_delay option on a placed
  design, and limit the specified number of nets or pins to less than 100.
  The -auto_delay option directs the router to prioritize setup and hold
  critical paths using the defined timing constraints.

  -max_delay <arg> - (Optional) Can only be used with -pins. Directs the
  router to try to achieve an interconnect delay less than or equal to the
  specified delay given in picoseconds. When this options is specified, the
  -delay option is implied.

  Note: The -max_delay and -min_delay options specify the delay limits for
  the interconnect only, not the logic or intra-site delay. The router
  attempts to satisfy the delay restrictions on the interconnect.

  -min_delay <arg> - (Optional) Can only be used with -pins. Directs the
  router to try to achieve an interconnect delay greater than or equal to the
  specified delay given in picoseconds. When this option is specified, the
  -delay option is implied.

  -timing_summary - (Optional) By default, the router outputs a final timing
  summary to the log, based on Vivado router internal estimated timing which
  might differ slightly from the actual routed timing due to pessimism in the
  delay estimates. The -timing_summary option forces the router to launch the
  Vivado static timing analyzer to report the timing summary based on actual
  routed delays, but incurs additional run time for the static timing
  analysis. The timing summary consists of the Worst Negative Slack (WNS),
  Total Negative Slack (TNS), Worst Hold Slack (WHS), and Total Hold Slack
  (THS). The values are identical to that of report_timing_summary when run
  on the post-route design.

  Note: The Vivado static timing analyzer is also launched by the -directive
  Explore option.

  -finalize - (Optional) When routing interactively you can specify
  route_design -finalize to complete any partially routed connections.

  -ultrathreads - (Optional) Reduces router runtime at the expense of
  repeatability. This option enables the router to run faster, but there will
  be some variation in routing results between otherwise identical runs.

  -quiet - (Optional) Execute the command quietly, returning no messages from
  the command. The command also returns TCL_OK regardless of any errors
  encountered during execution.

  Note: Any errors encountered on the command-line, while launching the
  command, will be returned. Only errors occurring inside the command will be
  trapped.

  -verbose - (Optional) Temporarily override any message limits and return
  all messages from this command.

  Note: Message limits can be defined with the set_msg_config command.

Examples:

  Route the entire design, and direct the router to try multiple algorithms
  for improving critical path delay:

    route_design -directive Explore


  The following example routes the set of timing critical nets,
  $criticalNets, to the shortest interconnect delay, marks the nets as fixed
  using the IS_ROUTE_FIXED property, and then routes the rest of the design
  using a low effort directive for fast results:

    route_design -delay -nets $criticalNets
    set_property IS_ROUTE_FIXED 1 $criticalNets
    route_design -directive RuntimeOptimized


  Route the specified nets using the fastest runtime:

    route_design -nets [get_nets ctrl0/ctr*]


  Route the specified nets to get the shortest interconnect delays:

    route_design -nets [get_nets ctrl0/ctr*] -delay


  Route to the specified pins:

    route_design -pins [get_pins ctrl0/reset_reg/D ctrl0/ram0/ADDRARDADDR]


  Route to a particular pin, try to achieve less than 500 ps delay:

    route_design -pins [get_pins ctrl0/reset_reg/D] -max_delay 500


  Route to a particular pin, try to achieve more than 200 ps delay:

    route_design -pins [get_pins ctrl0/ram0/ADDRARDADDR] -min_delay 200


See Also:

   *  get_nets
   *  get_pins
   *  launch_runs
   *  opt_design
   *  phys_opt_design
   *  place_design
   *  power_opt_design
   *  read_checkpoint
   *  set_property
   *  write_checkpoint
"""
help_read_checkpoint = """
help read_checkpoint
read_checkpoint

Description:
Read a design checkpoint

Syntax:
read_checkpoint  [-cell <arg>] [-incremental] [-directive <arg>]
                 [-reuse_objects <args>] [-fix_objects <args>]
                 [-dcp_cell_list <args>] [-quiet] [-verbose] [<file>]

Usage:
  Name              Description
  -----------------------------
  [-cell]           Replace this cell with the checkpoint. The cell must be a
                    black box.
  [-incremental]    Input design checkpoint file to be used for re-using
                    implementation.
  [-directive]      Mode of behavior (directive) for this command. Please
                    refer to Arguments section of this help for values for
                    this option.
                    Default: RuntimeOptimized
  [-reuse_objects]  Reuse only given list of cells, clock regions, SLRs and
                    Designs
  [-fix_objects]    Fix only given list of cells, clock regions, SLRs or
                    Design
  [-dcp_cell_list]  A list of cell/dcp pairs, e.g. {<cell1> <dcp1> <cell2>
                    <dcp2>}. The option value should be in curly braces.
  [-quiet]          Ignore command errors
  [-verbose]        Suspend message limits during command execution
  [<file>]          Design checkpoint file

Categories:
FileIO

Description:

  Reads a design checkpoint file (DCP) that contains the netlist,
  constraints, and may optionally have the placement and routing information
  of an implemented design. You can save design checkpoints at any stage in
  the design using the write_checkpoint command.

  The read_checkpoint command simply reads the associated checkpoint file,
  without opening a design or project in-memory. To create a project from the
  imported checkpoint, use the open_checkpoint command instead of
  read_checkpoint, or use the link_design command after read_checkpoint to
  open the in-memory design from the checkpoint or checkpoint files currently
  read.

  Note: When multiple design checkpoints are open in the Vivado tool, you
  must use the current_project command to switch between the open designs.
  You can use current_design to check which checkpoint is the active design.

Arguments:

  -cell <arg> - (Optional) Specifies a black box cell in the current design
  to populate with the netlist data from the checkpoint file being read. This
  option cannot be used with -incremental, or any of its related options.

  -incremental - (Optional) Load a checkpoint file into an already open
  design to enable the incremental implementation design flow, where <file>
  specifies the path and filename of the incremental design checkpoint (DCP)
  file. In the incremental implementation flow, the placement and routing
  from the incremental DCP is applied to matching netlist objects in the
  current design to reuse existing placement and routing. Refer to the Vivado
  Design Suite User Guide: Implementation (UG904) for more information on
  incremental implementation.

  Note: The -incremental switch is not intended to merge two DCP files into a
  single design. It applies the placement and routing of the incremental
  checkpoint to the netlist objects in the current design.

  After loading an incremental design checkpoint, you can use the
  report_incremental_reuse command to determine the percentage of physical
  data reused from the incremental checkpoint, in the current design. The
  place_design and route_design commands will run incremental place and
  route, preserving reused placement and routing information and
  incorporating it into the design solution.

  Reading a design checkpoint with -incremental, loads the physical data into
  the current in-memory design. To clear out the incremental design data, you
  must either reload the current design, using open_run to open the synthesis
  run for instance, or read a new incremental checkpoint to overwrite the one
  previously loaded.

  -directive [ RuntimeOptimized | TimingClosure | Quick ] - (Optional)
  Specifies a directive, or mode of operation for the -incremental process.

   *  RuntimeOptimized: The target WNS is the referenced from the incremental
      DCP. Trade-off timing for faster runtime.

   *  TimingClosure: The target WNS is 0. This mode attempts to meet timing
      at the expense of runtime.

   *  Quick: Specifies a low effort, non-timing-driven incremental
      implementation mode with the fastest runtime.

  -reuse_objects <args> - (Optional) For use with the -incremental option, to
  read and reuse only a portion of the checkpoint file, this option specifies
  to reuse only the placement and routing data of the specified list of
  cells, clock regions, and SLRs from the incremental checkpoint.

  Note: When this option is not specified, the whole design will be reused.
  The -reuse_objects options can be used multiple times to reuse different
  object types. See examples below.

  -fix_objects - (Optional) When -incremental is specified, mark the
  placement location of specifed cells as fixed (IS_LOC_FIXED) to prevent
  changes by the place_design command. This option will fix the placement of
  the specified list of cells, clock regions, SLRs or the current_design.

  -dcp_cell_list <arg> - (Optional) Lets you specify a list of cell/dcp
  pairs. This lets you read in multiple DCP files for specified cells in a
  single run of the read_checkpoint command. The format is specified as a
  list of cell/DCP pairs enclosed in curly braces: {<cell1> <dcp1> <cell2>
  <dcp2>}.

  -quiet - (Optional) Execute the command quietly, returning no messages from
  the command. The command also returns TCL_OK regardless of any errors
  encountered during execution.

  Note: Any errors encountered on the command-line, while launching the
  command, will be returned. Only errors occurring inside the command will be
  trapped.

  -verbose - (Optional) Temporarily override any message limits and return
  all messages from this command.

  Note: Message limits can be defined with the set_msg_config command.

  <file> - (Required) The path and filename of the checkpoint file to read.

  Note: If the path is not specified as part of the file name, the tool will
  search for the specified file in the current working directory and then in
  the directory from which the tool was launched.

Examples:

  The following example imports the specified checkpoint file into the tool,
  and then links the various design elements to create an in-memory design of
  the specified name:

    read_checkpoint C:/Data/checkpoint.dcp
    link_design -name Test1


  This example reads a design checkpoint on top of the current design for
  incremental place and route of the design:

    read_checkpoint -incremental C:/Data/routed.dcp


  Reuse and fix the placement and routing associated with the DSPs and Block
  RAMs:

    read_checkpoint -incremental C:/Data/routed.dcp \
    -reuse_objects [all_rams] -reuse_objects [all_dsps] -fix_objects [current_design]


  Note: The -reuse_objects option could also be written as:

    -reuse_objects [get_cells -hier -filter {PRIMITIVE_TYPE =~ BMEM.*.* || PRIMITIVE_TYPE =~ MULT.dsp.* }]


  The following example reuses the placement and routing of the cells inside
  the hierarchical cpuEngine cell, and fixes the placement of the DSP cells:

    read_checkpoint -incremental C:/Data/routed.dcp -reuse_objects [get_cells cpuEngine] -fix_objects [all_dsps]



See Also:

   *  all_dsps
   *  config_implementation
   *  current_design
   *  current_project
   *  get_cells
   *  link_design
   *  open_checkpoint
   *  report_config_implementation
   *  write_checkpoint
"""
utilization_metrics = {
    "Slice Logic": [
        "Slice LUTs*",
        "LUT as Logic",
        "LUT as Memory",
        "LUT as Distributed RAM",
        "LUT as Shift Register",
        "Slice Registers",
        "Register as Flip Flop",
        "Register as Latch",
        "F7 Muxes",
        "F8 Muxes",
    ],
    "Memory": ["Block RAM Tile", "RAMB36/FIFO*", "RAMB18"],
    "DSP": ["DSPs"],
    "IO and GT Specific": [
        "Bonded IOB",
        "Bonded IPADs",
        "Bonded IOPADs",
        "PHY_CONTROL",
        "PHASER_REF",
        "OUT_FIFO",
        "IN_FIFO",
        "IDELAYCTRL",
        "IBUFDS",
        "PHASER_OUT/PHASER_OUT_PHY",
        "PHASER_IN/PHASER_IN_PHY",
        "IDELAYE2/IDELAYE2_FINEDELAY",
        "ILOGIC",
        "OLOGIC",
    ],
    "Clocking": [
        "BUFGCTRL",
        "BUFIO",
        "MMCME2_ADV",
        "PLLE2_ADV",
        "BUFMRCE",
        "BUFHCE",
        "BUFR",
    ],
    "Specific Feature": [
        "BSCANE2",
        "CAPTUREE2",
        "DNA_PORT",
        "EFUSE_USR",
        "FRAME_ECCE2",
        "ICAPE2",
        "STARTUPE2",
        "XADC",
    ],
}
