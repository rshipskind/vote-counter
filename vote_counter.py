"""Counts delegate vote totals."""

from collections import Counter
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

# select group
group = None
while group not in ['a', 'b', 'c']:
    print('Select Group\n')
    group = input('a, b, c: ')

# load file
if group == 'a':
    candidates = pd.read_csv('a.csv')
elif group == 'b':
    candidates = pd.read_csv('b.csv')
elif group == 'c':
    candidates = pd.read_csv('c.csv')

# create Counter
candidates.Votes = 0
candidates = candidates.sort_values('Number', ascending=True)
results = Counter()

# count votes
last_vote = None
print('\nEnter the vote number to increment its vote count.')
print('Enter end to save the results to disk.')
print('Enter undo to delete the last valid vote.\n')

while True:
    vote = input('Enter vote #, end or undo:')
    if vote == 'end' or vote == 'e':
        break
    elif vote == 'undo' or vote == 'u':
        try:
            results[int(last_vote)] -= 1
            print('\t\t\t\t', last_vote, ': -1')
        except TypeError as t:
            print('-------------------------------\n \tINVALID ENTRY \
            \n-------------------------------')
            continue
    else:
        try:
            if int(vote) in list(candidates.Number):
                print('\t\t\t\t', vote)
                results[int(vote)] += 1
                last_vote = vote
            else:
                print('-------------------------------\n \tINVALID VOTE \
                \n-------------------------------')
                continue
        except Exception as e:
            print('-------------------------------\n \
            INVALID VOTE \n-------------------------------')
            continue

# append votes to dataframe and sort by vote count
for i in results:
    candidates.Votes[candidates.Number == i] = results[i]

# save output to file
if group == 'a':
    candidates.to_csv('a_out.csv', index=False)
elif group == 'b':
    candidates.to_csv('b_out.csv', index=False)
elif group == 'c':
    candidates.to_csv('c_out.csv', index=False)


# display local winners
print('\n\tTop 10 vote-getters:\n')
print(candidates.sort_values('Votes', ascending=False)[0:10])
