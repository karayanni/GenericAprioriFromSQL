# GenericAprioriFromSQL

This is an implementation of the apriori algorithm for frequent itemset mining.
The implementation samples the item sets from a SQL DB using simple groupt by and conditions querys.

To use:

1. cange the DB connector and table,schema names in ItemsetsSQLInfoExtractor.py
2. call the ItemsetsSQLInfoExtractor.get_frequent_sets_from_DB with the desired values, see example in main.py
