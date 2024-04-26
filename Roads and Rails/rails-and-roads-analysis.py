from dbfread import DBF
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def percentage (full, part):
    return (part/full)*100.0

def pie_chart(labels, sizes):

    sizes = sorted(sizes, reverse=True)
    patches, texts = plt.pie(sizes, startangle=90, radius=1.2)
    # Format labels based on size
    labels_new = []
    for i, j in zip(labels, sizes):
        if j < 1:
            labels_new.append('{0} - {1:.2f}%'.format(i, j))  # Two decimal points if size is less than 1
        else:
            labels_new.append('{0} - {1:d}%'.format(i, round(j)))  # Integer percentage if size is 1 or greater

    plt.legend(patches, labels_new, loc='best', bbox_to_anchor=(-0.1, 1.), fontsize=15)


filename = 'C:/Users/lejla/OneDrive/Desktop/Atlantbh praksa/2 mjesec/North America Supplement/roads.dbf'
# Open the DBF file
roads_table = DBF(filename)
# Convert DBF to DataFrame
roads_df = pd.DataFrame(iter(roads_table))
print(roads_df)

no_rows_roads = len(roads_df)

unique_class = roads_df['class'].unique()
print(unique_class)

unique_type = roads_df['type'].unique()
print(unique_type)


interstate_roads = roads_df[roads_df['class']=='Interstate']
federal_roads = roads_df[roads_df['class']=='Federal']
state_roads = roads_df[roads_df['class']=='State']
other_roads = roads_df[roads_df['class']=='Other']

# =============================================================================
# CHECKING INTERSTATE ROADS PREFIX
# =============================================================================

interstate_number_invalid = []
interstate_roads_prefixes = interstate_roads['prefix'].value_counts()
print("Length of interstate roads: ", len(interstate_roads))
print("Prefix for interstate roads:\n", interstate_roads_prefixes)

for index, row in interstate_roads.iterrows():
    if not str(row['number']).isdigit():
        interstate_number_invalid.append(row)

print("Length of invalid interstate numbers: ", len(interstate_number_invalid))
print("ID's of roads with invalid interstate numbers: ")
for i in range (len(interstate_number_invalid)):
    print(interstate_number_invalid[i]['uident'])


# =============================================================================
# CHECKING FEDERAL ROADS PREFIX
# =============================================================================
federal_number_invalid = []
federal_roads_prefixes = federal_roads['prefix'].value_counts()
print("Length of federal roads: ", len(federal_roads))
print("Prefix for federal roads:\n", federal_roads_prefixes)


for index, row in federal_roads.iterrows():
    if not str(row['number']).isdigit():
        federal_number_invalid.append(row)

print("Length of invalid federal numbers: ", len(federal_number_invalid))
print("ID's of roads with invalid federal numbers: ")
for i in range (len(federal_number_invalid)):
    print(federal_number_invalid[i]['uident'])


# =============================================================================
# CHECKING STATE ROADS PREFIX
# =============================================================================
state_number_invalid = []
state_roads_prefixes = state_roads['prefix'].value_counts()
print("Length of state roads: ", len(state_roads))
print("Prefix for state roads:\n", state_roads_prefixes)

for index, row in state_roads.iterrows():
    if not str(row['number']).isdigit():
        state_number_invalid.append(row)

print("Length of invalid state numbers: ", len(state_number_invalid))
print("ID's of roads with invalid state numbers: ")
for i in range (len(state_number_invalid)):
    print(state_number_invalid[i]['uident'])

# =============================================================================
# CHECKING OTHER ROADS PREFIX
# =============================================================================
other_number_invalid = []
other_roads_prefixes = other_roads['prefix'].value_counts()
print("Length of other roads: ", len(other_roads))
print("Prefix for other roads:\n", other_roads_prefixes)


for index, row in other_roads.iterrows():
    if not str(row['number']).isdigit():
        other_number_invalid.append(row)

print("Length of invalid other numbers: ", len(other_number_invalid))
print("ID's of roads with invalid other numbers: ")
for i in range (len(other_number_invalid)):
    print(other_number_invalid[i]['uident'])


# =============================================================================
# PIE CHART OF ATTRIBUTE "CLASS"
# =============================================================================

interstate_percentage = percentage(no_rows_roads, len(interstate_roads))
federal_percentage = percentage(no_rows_roads, len(federal_roads))
state_percentage = percentage(no_rows_roads, len(state_roads))
other_percentage = percentage(no_rows_roads, len(other_roads))


print("Interstate prcentage: ", interstate_percentage)
print("Federal percentage: ", federal_percentage)
print("State percentage: ", state_percentage)
print("Other percentage: ", other_percentage)


percentages = [round(interstate_percentage), round(federal_percentage), round(state_percentage),round(other_percentage)]
labels = ['Interstate', 'Federal', 'State', 'Other' ]
pie_chart(labels, percentages)
plt.title('Frequency of class attribute');


# =============================================================================
# PIE CHART OF ATTRIBUTE "TYPE"
# =============================================================================
# Calculate the frequency of each road type
road_type_counts = roads_df['type'].value_counts() # Series type which has type & count column
type_percentage_values = (road_type_counts/no_rows_roads)*100.0
print(type_percentage_values)

type_percentage_values_help = [53, 28, 12, 6, 0.84, 0.08]
labels_type_percentage_values = type_percentage_values.index.tolist()
pie_chart(labels_type_percentage_values , type_percentage_values_help )
plt.title('Frequency of type attribute');



# =============================================================================
# PIE CHART OF ATTRIBUTE "DIVIDED"
# =============================================================================
# Calculate the frequency of each divided road type
divided_road_counts = roads_df['divided'].value_counts(dropna=False)
divided_percentage_values = (divided_road_counts/no_rows_roads)*100.0
print(divided_percentage_values)

divided_roads_percentage = [53, 30, 17]
labels_divided_roads = ['Value is blank', 'Undivided', 'Divided']
pie_chart(labels_divided_roads, divided_roads_percentage)
plt.title('Frequency of divided attribute');


# =============================================================================
# MIN AND MAX VALUES FOR ATTRIBUTE "LENGTH"
# =============================================================================
max_length_index = roads_df['length'].idxmax()
row_with_max_length = roads_df.loc[max_length_index]['uident']
print("ID with maximum length: ", row_with_max_length, ", Length: ", roads_df.loc[max_length_index]['length'])
min_length_index = roads_df['length'].idxmin()
row_with_min_length = roads_df.loc[min_length_index]['uident']
print("ID with minimum length: ", row_with_min_length, ", Length: ", roads_df.loc[min_length_index]['length'])



# =============================================================================
# CHECKING ID UNIQUENESS
# =============================================================================

# Count the appearance of each unique 'id'
id_counts = roads_df['uident'].value_counts()
print("Unique IDs and their appearance counts:")
print(id_counts)

# =============================================================================
# PRINTING NOT-UNIQUE ID'S AND THEIR COUNT
# =============================================================================
for index, count in id_counts.items():
    if count > 1:
        print(index, " ", count)
