import pywikibot
import sys

player = unicode(sys.argv[1], "utf-8")
site = pywikibot.Site()
mc = pywikibot.Page(site, player)

temp = mc.text
print temp



