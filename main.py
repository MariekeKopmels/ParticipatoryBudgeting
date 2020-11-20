from data.generate_costs import generate_costs
from data.generate_utilities import *
from voting.approval_voting import approval_voting
from voting.threshold_approval_voting import threshold_approval_voting
from voting.utility_voting import utility_voting
from voting.cumulative_voting import cumulative_voting

if __name__ == '__main__':
    # generate utilities, costs
    generate_utilities()
    generate_costs()

    # perform all voting types
    rankings = [approval_voting(),
                threshold_approval_voting(),
                utility_voting(),
                cumulative_voting()]

    print(rankings)
