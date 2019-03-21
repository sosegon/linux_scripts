#!/bin/bash

# This config is for a 17" screen with a top and bottom panels in lubuntu
if [ $1 -eq 1 ]
then
	xterm -hold -geometry 95x25+0+0 -fa 'Monospace' -fs 12 & # top-letf
elif [ $1 -eq 2 ]
then
	xterm -hold -geometry 96x25+955+26 -fa 'Monospace' -fs 12  & # top-right
elif [ $1 -eq 3 ]
then
	xterm -hold -geometry 95x26+0+533 -fa 'Monospace' -fs 12  & # bottom-left
elif [ $1 -eq 4 ]
then
	xterm -hold -geometry 96x26+955+533 -fa 'Monospace' -fs 12 # bottom-right
else
	xterm -hold -geometry 95x25+0+0 -fa 'Monospace' -fs 12 & # top-letf
	sleep .1
	xterm -hold -geometry 96x25+955+26 -fa 'Monospace' -fs 12  & # top-right
	sleep .1
	xterm -hold -geometry 95x26+0+533 -fa 'Monospace' -fs 12  & # bottom-left
	sleep .1
	xterm -hold -geometry 96x26+955+533 -fa 'Monospace' -fs 12 # bottom-right
fi