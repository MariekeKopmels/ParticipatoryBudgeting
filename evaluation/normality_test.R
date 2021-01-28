library(ggpubr)
library(ggplot2)

# import data
library(readxl)
combined_results_sum <- read_excel("C:/Users/lonne/Google Drive/Bachelor AI/2020-2021/Bachelorproject AI/GitHub/ParticipatoryBudgeting/results/voters=50_projects=25_true-rankings=2_runs=100_costs-dist=betavariate/satisfaction/combined_results.xlsx", 
                                   sheet = "sum", range = "B1:Q101")
combined_results_min <- read_excel("C:/Users/lonne/Google Drive/Bachelor AI/2020-2021/Bachelorproject AI/GitHub/ParticipatoryBudgeting/results/voters=50_projects=25_true-rankings=2_runs=100_costs-dist=betavariate/satisfaction/combined_results.xlsx",
                                   sheet = "min", range = "B1:Q101")
combined_results_max <- read_excel("C:/Users/lonne/Google Drive/Bachelor AI/2020-2021/Bachelorproject AI/GitHub/ParticipatoryBudgeting/results/voters=50_projects=25_true-rankings=2_runs=100_costs-dist=betavariate/satisfaction/combined_results.xlsx",
                                   sheet = "max", range = "B1:Q101")

# Generate qqplot of one voting rule
ggqqplot(combined_results_sum$'knapsack')
shapiro.test(combined_results_sum$'knapsack')
