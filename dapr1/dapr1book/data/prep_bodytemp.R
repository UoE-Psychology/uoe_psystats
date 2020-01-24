# Process BodyTemp data

rm(list = ls())

library(tidyverse)

bodytemp = read_tsv('http://www.lock5stat.com/datasets/BodyTemp50.txt')
bodytemp

dim(bodytemp)

bodytemp = bodytemp %>%
    select(BodyTemp, Pulse) %>%
    mutate(BodyTemp = (BodyTemp - 32) * 5/9)
bodytemp

write_tsv(bodytemp, 'data/BodyTemp.txt')
