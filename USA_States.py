# Mapping of state to abbreviation
states = {
    'Alabama' : 'AL',
    'Alaska' : 'AK',
    'Arizona' : 'AZ',
    'Arkansas' : 'AR',
    'California' : 'CA',
    'Colorado' : 'CO',
    'Connecticut' : 'CT',
    'Delaware' : 'DE',
    'Florida' : 'FL',
    'Georgia' : 'GA',
    'Hawaii' : 'HI',
    'Idaho' : 'ID',
    'Illinoi' : 'IL',
    'Indiana' : 'IN',
    'Iowa' : 'IA',
    'Kansas' : 'KS',
    'Kentucky' : 'KY',
    'Louisiana' : 'LA',
    'Maine' : 'ME',
    'Maryland' : 'MD',
    'Massachusetts' : 'MA',
    'Michigan' : 'MI',
    'Minnesota' : 'MN',
    'Mississippi' : 'MS',
    'Missouri' : 'MO',
    'Montana' : 'MT',
    'Nebraska' : 'NE',
    'Nevada' : 'NV',
    'New Hampshire' : 'NH',
    'New Jersey' : 'NJ',
    'New Mexico' : 'NM',
    'New York' : 'NY',
    'North Carolina' : 'NC',
    'North Dakota' : 'ND',
    'Ohio' : 'OH',
    'Oklahoma' : 'OK',
    'Oregon' : 'OR',
    'Pennsylvania' : 'PA',
    'Rhoda Iland' : 'RI',
    'South Carolina' : 'SC',
    'South Dakota' : 'SD',
    'Tennessee' : 'TN',
    'Texas' : 'TX',
    'Utah' : 'UT',
    'Vermont' : 'VT',
    'Virginia' : 'VA',
    'Washington' : 'WA',
    'West Virginia' : 'WV',
    'Wisconsin' : 'WI',
    'Wyoming' : 'WY'
}

# Basic set of states and capital in them
cities = {
    'AL' : 'Montgomery',
    'AK' : 'Juneau',
    'AZ' : 'Phoenix',
    'AR' : 'Little Rock',
    'CA' : 'Sacramento',
    'CO' : 'Denver',
    'CT' : 'Hartford',
    'DE' : 'Dover',
    'FL' : 'Tallahassee',
    'GA' : 'Atlanta',
    'HI' : 'Honolulu',
    'ID' : 'Boise',
    'IL' : 'Springfield',
    'IN' : 'Indianapolis',
    'IA' : 'Des Moines',
    'KS' : 'Topeka',
    'KY' : 'Frankfort',
    'LA' : 'Baton Rouge',
    'ME' : 'Augusta',
    'MD' : 'Annapolis',
    'MA' : 'Boston',
    'MI' : 'Lansing',
    'MN' : 'St. Paul',
    'MS' : 'Jackson',
    'MO' : 'Jefferson City',
    'MT' : 'Helena',
    'NE' : 'Lincoln',
    'NV' : 'Carson City',
    'NH' : 'Concord',
    'NJ' : 'Trenton',
    'NM' : 'Santa Fe',
    'NY' : 'Albany',
    'NC' : 'Raleigh',
    'ND' : 'Bismarck',
    'OH' : 'Columbus',
    'OK' : 'Oklahoma City',
    'OR' : 'Salem',
    'PA' : 'Harrisburg',
    'RI' : 'Providence',
    'SC' : 'Columbia',
    'SD' : 'Pierre',
    'TN' : 'Nashville',
    'TX' : 'Austin',
    'UT' : 'Salt Lake City',
    'VT' : 'Montpelier',
    'VA' : 'Richmond',
    'WA' : 'Olympia',
    'WV' : 'Charleston',
    'WI' : 'Madison',
    'WY' : 'Cheyenne'
}

# print every state abbreviation
print('-' * 50)
print('-' * 50)
print("Here's every American States and the abbreviation:\n ")
for state, abbrev in list(states.items()):
    print(f"\t* {state} is abbreviated {abbrev}")

# print every capital in state
print('-' * 50)
print('-' * 50)
print("Here's every abbreviation with the capital:\n ")
for abbrev, city in list(cities.items()):
    print(f"\t* {abbrev} has the capital {city}")

# Now do both at the same time
print('-' * 60)
print('-' * 60)
print("Here's every American States with Abbreviation and Capital:\n ")
for state, abbrev in list(states.items()):
    print(f"\t * {state} state is abbreviated {abbrev}, and has capital {cities[abbrev]}")
