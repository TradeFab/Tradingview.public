// www.tradingview.com/u/TradeFab/
// www.tradefab.com
// ___  __        __   __  __       __
//  |  |__)  /\  |  \ |__ |__  /\  |__)
//  |  |  \ /~~\ |__/ |__ |   /~~\ |__)
//
// TradeFab's Donchian Channel.
//
VERSION = "3.0"
// 1.0 FB 2017-01-23 draft
//
// @version=3
study("TF Donchian Channel "+VERSION, overlay=true)

// === GENERAL INPUTS ===
dcPeriod    = input(title="DC period", type=integer, defval=14)

// === LOGIC ===
dcUpper = highest(high, dcPeriod)
dcLower = lowest(low, dcPeriod)
dcBasis = avg(dcUpper, dcLower)

// === PLOTTING ===
// Donchian channel
dcUplot = plot(series=dcUpper, color=lime)
dcLplot = plot(series=dcLower, color=red)
//plot(dcBasis, color=teal, style=line, title="Mid-Line Average")
fill(dcUplot, dcLplot, color=gray, transp=90)
