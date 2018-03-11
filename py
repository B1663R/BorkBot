import time
import sys, getOpt
import datetime
from poloniex import poloniex

def main(argv):
  period = 10
  pair = "BTC_XML"
  
  try:
      opts, args = getopt.getopt(argv,"hp:c:", ["period=","currency="])
  except getopt.GetoptError:
      print 'bork-bot.py -p <period> -c <currency pair>'
      sys.exit(2)
  
  for opt, arg in opts:
      if opt == '-h':
          print 'bork-bot.py -p <period> -c <currency pair>'
          sys.exit()
      elif opt in ("-p", "--period"):
          if (int(arg) in [300,900,1800,7200,14400,86400]):
              period = arg
          else:
               print 'Poloniex requires periods in 300, 900, 1800, 7200, 14400, or 86400 second increments'
               sys.exit(2)
      elif opt in ("-c", "--currency"):
          pair = arg
          
  conn = poloniex('','')
  
  while = True:
      currentValues = conn.api_query("returnTicker")
      
      lastPairPrice = currentValues[pair]["last"]
      
      print "{:%Y-%m-%d %H:%M%S}".format(datetime.datetime.now()) + " Period: %ss %s: %s" % (period, pair, lastPair)
      time.sleep(int(period))

if __name__ == "__main__":
  main(sys.argv[1:])
