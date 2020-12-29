# Participatory Budgeting Project


# import data
# Update number of runs!
library(readxl)
combined_results_sum <- read_excel("C:/Users/lonne/Google Drive/Bachelor AI/2020-2021/Bachelorproject AI/GitHub/ParticipatoryBudgeting/results/util-algo=mallows_costs-dist=betavariate_voters=50_projects=25_true-rankings=2/satisfaction/combined_results.xlsx", 
                                   sheet = "sum", range = "B1:Q51")
combined_results_min <- read_excel("C:/Users/lonne/Google Drive/Bachelor AI/2020-2021/Bachelorproject AI/GitHub/ParticipatoryBudgeting/results/util-algo=mallows_costs-dist=betavariate_voters=50_projects=25_true-rankings=2/satisfaction/combined_results.xlsx",
                                   sheet = "min", range = "B1:Q51")
combined_results_max <- read_excel("C:/Users/lonne/Google Drive/Bachelor AI/2020-2021/Bachelorproject AI/GitHub/ParticipatoryBudgeting/results/util-algo=mallows_costs-dist=betavariate_voters=50_projects=25_true-rankings=2/satisfaction/combined_results.xlsx",
                                   sheet = "max", range = "B1:Q51")

# Create a boxplot of the satisfactions
png(filename='MAX_200voters_25projects_50runs.png', width=1500, height=1200)
boxplot(combined_results_max, main="Maximum satisfaction", ylab="Satisfaction", las=2)
dev.off()

png(filename='MIN_200voters_25projects_50runs.png', width=1500, height=1200)
boxplot(combined_results_min, main="Minimum satisfaction", ylab="Satisfaction", las=2)
dev.off()

png(filename='SUM_200voters_25projects_50runs.png', width=1500, height=1200)
boxplot(combined_results_sum, main="Sum of satisfaction", ylab="Satisfaction", las=2)
dev.off()

