import pandas as pd 

# read in the data and emission factors
crop_country = pd.read_csv('data-clean\\N_use_crop_country.csv')
emission_factors = pd.read_csv('data\\emission-factors.csv', encoding = 'latin-1')
# make all column names lower case for emissino factors
emission_factors.columns = emission_factors.columns.str.lower()

print(crop_country.head())
print(emission_factors.head())


# create a dictionary with the country names and iso codes from the crop_country data
country_dict = dict(zip(crop_country['country'], crop_country['iso3_code']))

print(country_dict)

# show row for China in emission factors
print(emission_factors[emission_factors['country'] == 'China'])

# import the iso3 codes from the csv file
iso3_codes = pd.read_csv('data-clean\\country_iso3.csv', header=None, index_col=0).to_dict()

#combine the iso3_codes and country_dict
iso3_codes = {**iso3_codes[1], **country_dict}
print(iso3_codes)

# show data structure of iso3_codes
print(len(iso3_codes))

# fill the missing values in the iso3_code column in emission factors with the iso3 codes from the iso3_codes dictionary
emission_factors['iso3_code'] = emission_factors['country'].map(iso3_codes)

# print all country names that have a missing value in the iso3_code column in emission factors 
print(emission_factors[emission_factors['iso3_code'].isna()]['country'].unique())

