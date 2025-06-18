def birthdayCakeCandles(candles):
    output = 0
    biggest = 0
    for candle in candles:
        if candle > biggest:
            biggest = candle
            output = 0
        if candle == biggest:
            output += 1
    print(output)


birthdayCakeCandles([4,4,1,3])
#output = 2
# The tallest candles are 4. There are 2 candles with this height, so the function should return 2.
birthdayCakeCandles([1, 1, 1, 1])
#output = 4
# All candles are the same height, so all are the tallest.
birthdayCakeCandles([])
#output = 0