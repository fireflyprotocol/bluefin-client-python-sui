Networks = {
  "SUI_STAGING":{
      "url":"https://fullnode.testnet.sui.io:443",
      "chainId":1234,
      "apiGateway":"https://dapi.api.sui-staging.bluefin.io",
      "socketURL":"wss://dapi.api.sui-staging.bluefin.io",
      "dmsURL":"https://dapi.api.sui-staging.bluefin.io",
      "webSocketURL":"wss://notifications.api.sui-staging.bluefin.io",
      "onboardingUrl": "https://testnet.bluefin.io",

  },
  "SUI_PROD":{
      "url":"https://fullnode.testnet.sui.io:443",
      "chainId":1234,
      "apiGateway":"https://dapi.api.sui-prod.bluefin.io",
      "socketURL":"wss://dapi.api.sui-prod.bluefin.io",
      "dmsURL":"https://dapi.api.sui-prod.bluefin.io",
      "webSocketURL":"wss://notifications.api.sui-prod.bluefin.io",
      "onboardingUrl": "https://trade.bluefin.io",
  }
}

EIP712_DOMAIN_NAME = "IsolatedTrader"


EIP712_DOMAIN_STRING = "EIP712Domain(string name,string version,uint128 chainId,address verifyingContract)"


EIP712_ORDER_STRUCT_STRING = \
    "Order(" +  \
    "bytes8 flags," + \
    "uint128 quantity," + \
    "uint128 price," + \
    "uint128 triggerPrice," + \
    "uint128 leverage," + \
    "address maker," + \
    "uint128 expiration" + \
    ")"

ORDER_FLAGS = {
    "IS_BUY":1,
    "IS_DECREASE_ONLY": 2
}

TIME = {
  "SECONDS_IN_A_MINUTE": 60,
  "SECONDS_IN_A_DAY": 86400,
  "SECONDS_IN_A_MONTH": 2592000
}

ADDRESSES = {
  "ZERO": "0x0000000000000000000000000000000000000000",
}

SERVICE_URLS = {
  "MARKET": {
    "ORDER_BOOK": "/orderbook",
    "RECENT_TRADE": "/recentTrades",
    "CANDLE_STICK_DATA": "/candlestickData",
    "EXCHANGE_INFO": "/exchangeInfo",
    "MARKET_DATA": "/marketData",
    "META": "/meta",
    "STATUS": "/status",
    "SYMBOLS": "/marketData/symbols",
    "CONTRACT_ADDRESSES": "/marketData/contractAddresses",
    "TICKER": "/ticker",
    "MASTER_INFO": "/masterInfo",
    "FUNDING_RATE":"/fundingRate"
  },
  "USER": {
    "USER_POSITIONS": "/userPosition",
    "USER_TRADES": "/userTrades",
    "ORDERS": "/orders",
    "GENERATE_READONLY_TOKEN": "/generateReadOnlyToken",
    "ACCOUNT": "/account",
    "USER_TRANSACTION_HISTORY": "/userTransactionHistory",
    "AUTHORIZE": "/authorize",
    "ADJUST_LEVERAGE": "/account/adjustLeverage",
    "FUND_GAS": "/account/fundGas",
    "TRANSFER_HISTORY": "/userTransferHistory",
    "FUNDING_HISTORY": "/userFundingHistory",
    "CANCEL_ON_DISCONNECT": "/dms-countdown"
  },
  "ORDERS": {
    "ORDERS": "/orders",
    "ORDERS_HASH": "/orders/hash",
  },
}

EIP712_CANCEL_ORDER_STRUCT_STRING ="CancelLimitOrder(string action,bytes32[] orderHashes)"

EIP712_ONBOARDING_ACTION_STRUCT_STRING = \
    'firefly(' + \
    'string action,' + \
    'string onlySignOn' + \
    ')'

EIP712_DOMAIN_STRING_NO_CONTRACT = \
    "EIP712Domain(" + \
    "string name," + \
    "string version," + \
    "uint128 chainId" + \
    ")"



SUI_BASE_NUM=1000000000
DAPI_BASE_NUM=1000000000000000000