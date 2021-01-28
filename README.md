# Comparing Voting Rules for Participatory Budgeting

This project is essentially a pipeline, consisting of the parts:

- Data generation: generating voters' utilities for some projects. See the folder 'utilities'.
- The voting stage: 1) convert utilities into ballots of a certain format (e.g. approval voting) and 2) aggregate these ballots to form a single ranking of all projects. See the folder 'voting'.
- The budgeting stage: convert the final ranking of projects into a selection of projects that fits into the budget.
- The evaluation stage: evaluate the selection of projects with metrics like satisfaction.

## Data generation
There are two possible methods to generate the utilities.

- Random:
- Mallows model:

## Voting stage
The methods of voting that have been implemented are:

- Approval voting
- K-approval voting
- Threshold approval voting
- Knapsack voting
- Utility voting
- Cumulative voting
- Borda-rule voting

## Budgeting stage
We only use knapsack budgeting. The projects are ordered by decreasing order of the number of votes they received, and selected one-by-one
until the budget is full.

## Evaluation stage
The 'standard' evaluation method is a comparison based on implicit utilitarian voting, meaning that
the sum of the utilities per project is evaluated. It is checked if the project that maximizes
this sum is selected.
