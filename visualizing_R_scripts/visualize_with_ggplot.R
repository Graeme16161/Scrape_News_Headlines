
## for data manipulation and visualization
library(tidyverse)
library(lubridate)

## read data from csv fie
headlines <- read_csv("headlines_with_sentiment.csv", 
                                     col_types = cols(X1 = col_skip()))


## deal with date/time column

#remove extranious '-' at the end of some date/times
headlines$date <- gsub('-','',headlines$date)

# convert character dates to POSIX format, then create day feature for grouping
headlines$posix <- parse_date_time(headlines$date, "%m/%d/%Y %I:%M:%S %p",tz = "EST")
headlines$day <- format(headlines$posix, format = "%m%d")

## remove headlines with zero polarity
headlines %>%
  group_by(day)%>%
  summarise(mean_pol = mean(polarity))%>%
  ggplot(aes(day, mean_pol))+
  geom_bar(stat = 'identity')

# days with very few results
skip_days = c("0625","0626","0708")

# sources by day
headlines %>%
  filter(!day %in% skip_days)%>%
  ggplot(aes(day, fill = source))+
  geom_bar( position = "fill")+
  labs(title = "Distribution of Headline Source by Day", x = "Day", y = "Distribution of Sources")

ggsave("distribution_of_source_by_day.jpeg",plot = g,dpi = 320, width = 8, height = 4)

# Number of stories by day



g = headlines %>%
  filter(!day %in% skip_days)%>%
  group_by(day)%>%
  summarise(number = n())%>%
  ggplot(aes(day,number))+ 
  geom_bar(stat = 'identity')+ 
  annotate("rect", xmin=2.5, xmax=4.5, ymin=0, ymax=Inf, alpha=0.1, fill="red")+ 
  annotate("rect", xmin=7.5, xmax=8.5, ymin=0, ymax=Inf, alpha=0.1, fill="red")+ 
  annotate("rect", xmin=9.5, xmax=11.5, ymin=0, ymax=Inf, alpha=0.1, fill="red")+
  labs(title = "Number of News Headlines by Day", 
       subtitle = "Shaded areas are weekends and holidays",
       x = "Day", 
       y = "Number of News Headlines")+
  scale_fill_manual('Highlight this',
                    values = 'red',  
                    guide = guide_legend(override.aes = list(alpha = 1))) 

ggsave("headlines_by_day.jpeg",plot = g,dpi = 320, width = 8, height = 4)

##################################################################################################################
good_days <- c("0627","0628","0701","0702","0703","0705")

t = headlines %>%
  filter(day %in% good_days)%>%
  filter(polarity != 0)%>%
  group_by(source)%>%
  mutate(percentile = ntile(polarity,100))%>%
  group_by(day)%>%
  summarise(mean_per = mean(percentile))

g <-t %>%  ggplot(aes(day, mean_per))+
  geom_bar(stat = 'identity') + 
  coord_cartesian(
    ylim = c(45, 55))+
  labs(title = "Mean Headline Polarity Percentile by Day", x = "Day", y = "Mean Percentile")

ggsave("aspirational_plot.jpeg",plot = g,dpi = 320, width = 8, height = 4)

## Density plots of top news sources

subset_sources <- c("BNK Invest", "Zacks.com","MT Newswires", "Reuters", "Motley Fool", "InvestorPlace Media")

g <- headlines %>%
  filter(source %in% subset_sources)%>%
  ggplot(aes(polarity))+
  geom_density(bw = .05)+
  facet_wrap(~source)+
  labs(title = "Top News Sources by Polarity Distribution", x = "Polarity", y = "Density")
  
ggsave("polarity_density.jpeg",plot = g,dpi = 320, width = 8, height = 4)

g <- headlines %>%
  filter(source %in% subset_sources)%>%
  ggplot(aes(subjectivity))+
  geom_density(bw = .05)+
  facet_wrap(~source)+
  labs(title = "Top News Sources by Subjectivity Distribution", x = "Subjectivity", y = "Density")

ggsave("subjectivity_density.jpeg",plot = g,dpi = 320, width = 8, height = 4)


