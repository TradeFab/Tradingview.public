// www.tradingview.com/u/TradeFab/
// www.tradefab.com
// ___  __        __   __  __       __
//  |  |__)  /\  |  \ |__ |__  /\  |__)
//  |  |  \ /~~\ |__/ |__ |   /~~\ |__)
//
// TradeFab's Bollinger Band Indicator.
//
VERSION = "1.1"
// 1.1 FB 2017-05-26 renamed variables
// 1.0 FB 2017-02-26 basic version
//
// @version=3
study("TF Bollinger Band Indicator "+VERSION, overlay=true)

// === INPUTS ===
bbPeriod    = input(title="Bollinger Period", defval=20, minval=1)
bbStdDev    = input(title="Bollinger StdDev", defval=2.0, minval=0.001, maxval=50.0)

// === LOGIC ===
bbBasis   = sma(close, bbPeriod)
bbDev     = bbStdDev * stdev(close, bbPeriod)
bbUpper   = bbBasis + bbDev
bbLower   = bbBasis - bbDev

// === PLOTTING ===
plot(bbBasis, color=red)
p1 = plot(bbUpper, color=blue)
p2 = plot(bbLower, color=blue)
fill(p1, p2)
