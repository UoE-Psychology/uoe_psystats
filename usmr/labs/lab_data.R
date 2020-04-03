
wd <- getwd()
set.seed(1234)

id <- 1:167
lab <- factor(rep(c("Thursday", "Friday"), c(floor(length(id)*.47), ceiling(length(id)*.53))))
prog <- c("Psych", "Ling", "CogSci")
programme <- factor(c(sample(length(prog), table(lab)[2], replace = T, prob = c(.36, .34, .30)),
               sample(length(prog), table(lab)[1], replace = T, prob = c(.27, .36, .37))))
d2 <- d1 <- rep(0, length(id))
d1[programme == 2] <- 1
d2[programme == 3] <- 1

time <- round(100 + 12 * d1 - 17 * d2 +
                4.7 * (as.numeric(lab) - 1) - 3.5  + 
                (as.numeric(lab) - 1) * d1 + 6 * (as.numeric(lab) - 1) * d2 +
                rnorm(length(id), 0, 5))
tasks2 <- floor(5 + .12 * (time - min(time)) + rnorm(length(id), 0, 3))
tasks1 <- round(abs((tasks2 - 3.6 + 3.7 * d2 + rnorm(length(id), 0, 3))))
tasks1[tasks1 == 0] <- NA
tasks2[tasks2 == 0] <- NA
tasks2[tasks2 > 18] <- 18
tasks1[sample(length(tasks1), 2)] <- c(19, 21)
df <- data.frame(id, lab = as.character(lab), programme, time, tasks1, tasks2, stringsAsFactors = F)
df$lab[sample(nrow(df), 3)] <- c("Fryday", "Thrusday", "Tuesday")
df$time[is.na(tasks1) | is.na(tasks2)] <- NA
df$time[sample(nrow(df), 5)] <- c(NA, NA, 1200, -78, .120)
df <- df[sample(nrow(df)), ]
df$id <- id
names(df) <- paste0("V_", 1:ncol(df))

setwd("~/teaching/univar/week_5_chi_and_t_test")
write.csv(df, "Lab5_data.csv", row.names = F, na = "")

setwd() <- wd
