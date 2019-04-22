// https://www.tradingview.com/u/TradeFab/
// ___  __        __   __  __       __
//  |  |__)  /\  |  \ |__ |__  /\  |__)
//  |  |  \ /~~\ |__/ |__ |   /~~\ |__)
//
// TradeFab's Lazy River Strategy.
// The strategy uses EMA(20) and EMA(50) and looks for a constant trend
// and trades if price is bouncing back from the EMAs.
// The strategy goes ...
//
VERSION = "1.3"
// 1.3 FB 2017-01-19 order strategy draft
// 1.2 FB 2017-01-17 added lookback period
// 1.1 FB 2017-01-17 configurable MA periods; trend aligned with TF-TendIndicator-V1
// 1.0 FB 2017-01-15 basic version
//
// @version=3
strategy(
   title      = "TF Lazy River "+VERSION,
   shorttitle = "TF Lazy River "+VERSION,
   overlay    = true,
   pyramiding = 0,
   default_qty_type  = strategy.fixed,
   default_qty_value = 10000,
   currency          = "USD")

// === GENERAL INPUTS ===
maFastLen   = input(title="MA fast length", type=integer, defval=20)
maSlowLen   = input(title="MA slow length", type=integer, defval=50)
histPeriod  = input(title="Lookback period", type=integer, defval=5)

// === LOGIC ===
maFast = ema(close, maFastLen)
maSlow = ema(close, maSlowLen)

highestHigh = highest(high, histPeriod)
lowestLow   = lowest(low, histPeriod)

isUpTrend() =>
   (maFast > maSlow) and
   rising(maFast, 2) and
   rising(maSlow, 2)
isDownTrend() =>
   (maFast < maSlow) and
   falling(maFast, 2) and
   falling(maSlow, 2)

enterLong() =>
    isUpTrend()
enterShort() =>
    isDownTrend()

//if (strategy.position_size == 0)

// k = sma(stoch(close, high, low, 14), 3)
// d = sma(k, 3)
// plot(k, color=black)
// plot(d, color=red)
// h0 = hline(80)
// h1 = hline(20)
// fill(h0, h1, color=purple, transp=95)

// === PLOTTING ===
upColor = color(green, 90)
downColor = color(red, 90)
plot(maFast, color = green, linewidth=2)
plot(maSlow, color = lime,  linewidth=2)
bgcolor(isUpTrend() ? upColor : (isDownTrend() ? downColor : na))
plot(series=highestHigh, color=green)
plot(series=lowestLow, color=red)

// === POSITION EXECUTION ===
if (enterLong() and (strategy.position_size==0))
    stopLoss     = (close-lowestLow)*100000 + 50 // in ticks
    profitTarget = stopLoss
    strategy.entry("Long", strategy.long)
    strategy.exit ("L-EX1", "Long", loss=stopLoss, profit=profitTarget, qty_percent=50)
    strategy.exit ("L-EX2", "Long", loss=stopLoss, trail_points=profitTarget*2, trail_offset=stopLoss)
//    strategy.exit ("L-PT2", "Long", profit=profitTarget)
// if ((enterLong()==false) and (strategy.position_size>0))
//     strategy.close_all(true)

//strategy.exit("exit short", from_entry = "short",
//   profit       = takeProfit  > 0 ? takeProfit  : na,
//   loss         = stopLoss    > 0 ? stopLoss    : na,
//   trail_points = trailStop   > 0 ? trailStop   : na,
//   trail_offset = trailOffset > 0 ? trailOffset : na)

// === ALERTS ===

