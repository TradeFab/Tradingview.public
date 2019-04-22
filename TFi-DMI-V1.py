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
// TradeFab's DMI Indicator.
//
VERSION = "1.0"
// 1.0 FB 2018-05-21 basic version
//
// @version=3
study("TF DMI Indicator "+VERSION, overlay=false)

// === INPUTS ===
dmiPeriod = input(title="DMI Period", type=integer, defval=14, minval=1)

// === LOGIC ===
atrInd  = atr(dmiPeriod)
upMove  = high - nz(high[1])
dnMove  = nz(low[1]) - low
plusDM  = ((upMove > dnMove) and (upMove > 0)) ? upMove : 0
minusDM = ((dnMove > upMove) and (dnMove > 0)) ? dnMove : 0

// +DI,-DI and ADX
plusDI  = 100 * (rma(plusDM, dmiPeriod)/atrInd)
minusDI = 100 * (rma(minusDM, dmiPeriod)/atrInd)
absDX   = 100 * abs((plusDI - minusDI) / (plusDI + minusDI))
adxInd  = rma(absDX, dmiPeriod)

// === PLOTTING ===
plot(plusDI, color= navy, linewidth= 1, title= "+DI", transp=0)
plot(minusDI, color= red, linewidth= 1, title= "-DI", transp=0)
plot(adxInd, color= green, linewidth= 2, title= "ADX", transp=0)
hline(20, color= black, linestyle=dashed, linewidth= 1, title= "Trend Strength")