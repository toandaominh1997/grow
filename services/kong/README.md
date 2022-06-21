# Kong

## Installation

```
helm install my-kong bitnami/kong 
```


if(toNumber(formatDate(prop("Date"), "DDD")) < 80, "❄️ Winter", if(toNumber(formatDate(prop("Date"), "DDD")) < 172, "🌷 Spring", if(toNumber(formatDate(prop("Date"), "DDD")) < 264, "🌞 Summer", if(toNumber(formatDate(prop("Date"), "DDD")) > 354 and toNumber(formatDate(prop("Date"), "DDD")) < 367, "❄️ Winter", "🍁 Fall"))))


formatDate(prop("Date"), "dddd")


(formatDate(prop("Date"), "d") != "7") ? (formatDate(dateSubtract(prop("Date"), -1 + toNumber(formatDate(prop("Date"), "E")), "days"), "MMM D –") + formatDate(dateSubtract(prop("Date"), -1 + toNumber(formatDate(prop("Date"), "E")) - 6, "days"), " MMM D, YYYY")) : (formatDate(prop("Date"), "MMM D –") + formatDate(dateAdd(prop("Date"), 6, "days"), " MMM D, YYYY"))


formatDate(prop("Date"), "YYYY")