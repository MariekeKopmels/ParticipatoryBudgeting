from data.generate_costs import generate_costs
from data.generate_utilities import *
from voting.approval_voting import approval_voting
from voting.threshold_approval_voting import threshold_approval_voting

if __name__ == '__main__':
    # generate utilities, costs
    generate_utilities()
    generate_costs()

    # perform all voting types
    rankings = []
    rankings.append(approval_voting())
    rankings.append(threshold_approval_voting())

    print(rankings)
