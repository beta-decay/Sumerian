# -*- coding: utf-8 -*-

import sys

filename = sys.argv[1]

with open(filename, "r", encoding="utf8") as f:
	code = f.read()

code = "# -*- coding: utf-8 -*-\n"+code

display_cuneiform = False

if len(sys.argv) > 2:
	if sys.argv[2]:
		display_cuneiform = True

code = code.replace("𒅆𒅋𒆷","or")
code = code.replace("𒍣𒍣", "**")
code = code.replace("𒊕𒊻", "while")
code = code.replace("𒄑𒌇", "input")
code = code.replace("𒄬𒄬", "/")
code = code.replace("𒄖𒌌", ">")
code = code.replace("𒄭𒀀", "if")
code = code.replace("𒋛𒅋", "else")
code = code.replace("𒁺","print")
code = code.replace("𒈭", "+")
code = code.replace("𒊓", "=")
code = code.replace("𒆳", "!=")
code = code.replace("𒁁", "-")
code = code.replace("𒋢", "*")
code = code.replace("𒃲","%")
code = code.replace("𒄯", "<")
code = code.replace("𒌨","and")
code = code.replace("𒁇", "not")

exec(code)