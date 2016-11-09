import pywikibot
import sys

player = unicode(sys.argv[1], "utf-8")
site = pywikibot.Site()
mc = pywikibot.Page(site, player)

temp = mc.text
temp1 = temp.encode('ascii','ignore')
x = temp1.split("convert|",1)[1]

print x.split("|m|",1)[0]
