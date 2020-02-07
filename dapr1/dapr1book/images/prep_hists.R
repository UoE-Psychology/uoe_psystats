
library(tidyverse)
library(moderndive)

set.seed(33)

nfl <- read_tsv('https://edin.ac/2TexAFA')

nfl_sample_means_n_50 <- nfl %>%
    rep_sample_n(size = 50, reps = 2000) %>%
    group_by(replicate) %>%
    summarise(avg = mean(YearlySalary))

nfl_sample_means_n_100 <- nfl %>%
    rep_sample_n(size = 100, reps = 2000) %>%
    group_by(replicate) %>%
    summarise(avg = mean(YearlySalary))

nfl_sample_means_n_500 <- nfl %>%
    rep_sample_n(size = 500, reps = 2000) %>%
    group_by(replicate) %>%
    summarise(avg = mean(YearlySalary))

nfl_sample_means_vary_n <- bind_rows(
    nfl_sample_means_n_50 %>% mutate(n = 50),
    nfl_sample_means_n_100 %>% mutate(n = 100),
    nfl_sample_means_n_500 %>% mutate(n = 500)
)

ggplot(nfl_sample_means_vary_n, aes(x = avg)) +
    geom_histogram(color = "white") +
    facet_grid(cols = vars(n), labeller = label_both) +
    labs(x = expr(bar(x)), title = "Distribution of the sample mean for samples of size 50, 100, 500")


dim(nfl_sample_means_n_50)

sum(nfl_sample_means_n_50$avg >= 2.2 & nfl_sample_means_n_50$avg <= 2.3)

mean(nfl_sample_means_n_50$avg >= 2.2 & nfl_sample_means_n_50$avg <= 2.3)


