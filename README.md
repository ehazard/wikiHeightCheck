# wikiHeightCheck
Look at the heights of soccer players using pywikibot and wikipedia

## Requirements
Pywikibot is the only requirement, instructions can be found [here](https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation)

## Instructions (11/9/16)

**getHeight**: sudo python pwb.py scripts/getHeight.py "Artur Boruc"

**viewGivenWiki**: sudo python pwb.py script/viewGivenWiki.py "Artur Boruc"

## What are they (11/9/16)

**getHeight**: This usually returns the numerical value for the given player's height, for Artur Boruc == "1.93" which is in this case, in meters

**viewGivenWiki**: This is for development purposes. Not all wikiTemplates look the same (feet vs. meters) so this is meant to help the developer create look at the template they're dealing with.  
