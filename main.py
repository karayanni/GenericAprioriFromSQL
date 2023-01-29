import ItemsetsSQLInfoExtractor

attributes = ['weather', 'location', 'id', 'model_type']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    frequent_outliners_item_sets = ItemsetsSQLInfoExtractor.get_frequent_sets_from_DB(
        attributes=attributes,
        min_occurrences=0.01,
        min_support=0.01,
        min_confidence=0.51,
        min_risk=1.1,
        general_db_filter_query="date < '2/1/2020' ",
        outliners_sql_filter_query="signal_1or2 = 1",
        max_length=3,
        debug_print=False
    )

    for item in frequent_outliners_item_sets:
        print(item)
