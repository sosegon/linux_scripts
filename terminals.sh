#!/bin/bash

# This config is for a 17" screen with a top and bottom panels in lubuntu

xterm -hold -geometry 95x25+0+0 -fa 'Monospace' -fs 12 & # top-letf
xterm -hold -geometry 96x25+955+26 -fa 'Monospace' -fs 12  & # top-right
xterm -hold -geometry 95x26+0+533 -fa 'Monospace' -fs 12  & # bottom-left
xterm -hold -geometry 96x26+955+533 -fa 'Monospace' -fs 12 # bottom-right