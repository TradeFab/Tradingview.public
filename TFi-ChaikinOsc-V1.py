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
// TradeFab's Chaikin Oscillator Indicator.
//
VERSION = "1.0"
// 1.0 FB 2018-05-26 basic version
//
// @version=3
study("TF Chaikin Oscillator Indicator "+VERSION, overlay=false)


// === INPUTS ===
chaiEmaFast = input(title="Chaikin EMA Fast Period", type=integer, defval=3, minval=1)
chaiEmaSlow = input(title="Chaikin EMA Slow Period", type=integer, defval=10, minval=1)


// === LOGIC ===
chaiOsc = ema(accdist, chaiEmaFast) - ema(accdist, chaiEmaSlow)


// === PLOTTING ===
plot(series=chaiOsc, color=color(#FF8080, 0))
hline(0, color=gray, linestyle=dashed)
