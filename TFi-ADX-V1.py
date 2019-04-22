// www.tradingview.com/u/TradeFab/
// www.tradefab.com
// ___  __        __   __  __       __
//  |  |__)  /\  |  \ |__ |__  /\  |__)
//  |  |  \ /~~\ |__/ |__ |   /~~\ |__)
//
// DISCLAIMER: Futures, stocks and options trading involves substantial risk of loss 
// and is not suitable for every investor. You are responsible for all the risks and 
// financial resources you use and for the chosen trading system.
// Past performance is not indicative for future results. In making an investment decision,
// traders must rely on their own examination of the entity making the trading decisions!
//
// TradeFab's ADX Indicator.
//
VERSION = "1.0"
// 1.0 FB 2018-05-12 basic version
//
// @version=3
study("TF ADX Indicator "+VERSION, overlay=false)

// === INPUTS ===
adxPeriod = input(title="ADX Period", type=integer,   defval=3, minval=1)

// === LOGIC ===
dirmov(len) =>
	up = change(high)
	down = -change(low)
	truerange = rma(tr, len)
	plus = fixnan(100 * rma(up > down and up > 0 ? up : 0, len) / truerange)
	minus = fixnan(100 * rma(down > up and down > 0 ? down : 0, len) / truerange)
	[plus, minus]

adx(len) => 
	[plus, minus] = dirmov(len)
	sum = plus + minus
	100 * rma(abs(plus - minus) / (sum == 0 ? 1 : sum), len)

adxFast = adx(adxPeriod)

// === PLOTTING ===
plot(adxFast, color=blue, title="ADX", style=line, linewidth=2)
hline(25)
hline(75)
