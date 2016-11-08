library(ggplot2)

## ----------------------------- input --------------------------------

setwd("./practice/uspollution")
pollution <- read.csv("pollution_us_2000_2016.csv")

str(pollution)

## ---------------------------- some cleaning----------------------------

pollution$X <- NULL
pollution$Date.Local <- as.POSIXct(strptime(pollution$Date.Local, format = "%Y-%m-%d"))
pollution$NO2.Units <- NULL
pollution$O3.Units <- NULL
pollution$CO.Units <- NULL
pollution$SO2.Units <- NULL

## --------------------------------- some visualization -----------------------
# -------histograms-------

ggplot(data = pollution, aes(x = NO2.1st.Max.Hour)) + geom_histogram(
    binwidth = 1, color = "black") + scale_x_continuous(
        breaks = seq(0,24,1)) # max at midnight and 6 am

ggplot(data = pollution, aes(x = O3.1st.Max.Hour)) + geom_histogram(
    binwidth = 1, color = "black") + scale_x_continuous(
        breaks = seq(0,24,1)) # max at 10 am

ggplot(data = pollution, aes(x = SO2.1st.Max.Hour)) + geom_histogram(
    binwidth = 1, color = "black") + scale_x_continuous(
        breaks = seq(0,24,1)) # strange sudden ups and downs

ggplot(data = pollution, aes(x = CO.1st.Max.Hour)) + geom_histogram(
    binwidth = 1, color = "black") + scale_x_continuous(
        breaks = seq(0,24,1)) # strange at midnight, max at 6-7 am

# -------- scatterplots --------

ggplot(data = pollution, aes(x = NO2.Mean , y = O3.Mean )) + geom_point(alpha = 0.1)
