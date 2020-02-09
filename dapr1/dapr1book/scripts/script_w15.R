
set.seed(1)

library(tidyverse)
library(patchwork)

nfl <- read_tsv('https://edin.ac/2TexAFA')

mu = mean(nfl$YearlySalary)
sigma = sd(nfl$YearlySalary)


# a

n = 50
x = rnorm(10000, mu, sigma / sqrt(n))

a = ggplot(tibble(x=x)) +
  geom_histogram(aes(x = x, y = stat(density)), color = 'white') +
  stat_function(fun = dnorm, args = list(mean = mu, sd = sigma / sqrt(n)), color = 'red', size = 1) +
  labs(x = expr(bar(x)), y = '', title = expr((a) ~ n == !!n)) +
  theme(plot.title = element_text(hjust = 0.5))

xlim = ggplot_build(a)$layout$panel_params[[1]]$x.range


# b

n = 500
x = rnorm(10000, mu, sigma / sqrt(n))

b = ggplot(tibble(x=x)) +
  geom_histogram(aes(x = x, y = stat(density)), color = 'white') +
  stat_function(fun = dnorm, args = list(mean = mu, sd = sigma / sqrt(n)), color = 'red', size = 1) +
  labs(x = expr(bar(x)), y = '', title = expr((b) ~ n == !!n)) +
  theme(plot.title = element_text(hjust = 0.5)) + 
  xlim(xlim[1], xlim[2])


# C

n = 20
p = 0.5

x = 0:n
y = dbinom(x, n, p)

c = ggplot(tibble(x=x, y=y)) +
  geom_segment(aes(x=x, xend=x, y=0, yend=y), size = 1) +
  stat_function(fun = dnorm, args = list(mean = n*p, sd = sqrt(n * p * (1-p))), color = 'red', size = 1) +
  labs(x = expr(hat(p)), y = '', title = expr((c) ~ n == !!n ~','~ p == !!p)) +
  theme(plot.title = element_text(hjust = 0.5)) +
  scale_x_continuous(limits = c(0, 20), labels = function(x) round(x/20, 2))


# d
n = 100
p = 0.5

x = 0:n
y = dbinom(x, n, p)

d = ggplot(tibble(x=x, y=y)) +
  geom_segment(aes(x=x, xend=x, y=0, yend=y), size = 1) +
  stat_function(fun = dnorm, args = list(mean = n*p, sd = sqrt(n * p * (1-p))), color = 'red', size = 1) +
  labs(x = expr(hat(p)), y = '', title = expr((d) ~ n == !!n ~','~ p == !!p)) +
  theme(plot.title = element_text(hjust = 0.5)) +
  scale_x_continuous(limits = c(0, 100), labels = function(x) round(x/100, 2))


(a + b) / (c + d)




###


library(tidyverse)
library(patchwork)

set.seed(1)

mu = mean(nfl$YearlySalary)
sigma = sd(nfl$YearlySalary)

n = 50
x = rnorm(10000, mu, sigma / sqrt(n))

mean(x >= 2.2 & x <= 2.3)
