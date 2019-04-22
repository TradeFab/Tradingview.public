// www.tradingview.com/u/TradeFab/
// www.tradefab.com
// ___  __        __   __  __       __
//  |  |__)  /\  |  \ |__ |__  /\  |__)
//  |  |  \ /~~\ |__/ |__ |   /~~\ |__)
//
// TradeFab's Aroon Indicator.
//
VERSION = "1.0"
// 1.0 FB 2018-02-27 basic version
//
// @version=3
study("TF Aroon Indicator "+VERSION, overlay=false)

// === INPUTS ===
length  = input(title="Length", defval=14, minval=1)

// === LOGIC ===
upIndex     = highestbars(high, length)
dnIndex     = lowestbars(low, length)
aroonUp     = fixnan(((length - upIndex)/length)*100 )
aroonDn     = fixnan(((length - dnIndex)/length)*100 )

// === PLOTTING ===
plot(aroonUp*-1, color=blue, title="Aroon Up", style=line, linewidth=2)
plot(aroonDn*-1, color=red,  title="Aroon Up", style=line, linewidth=2)

hline(-150)
hline(-120)
hline(-180)
