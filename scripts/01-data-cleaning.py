import pandas as pd

## load data
df = pd.read_csv('./data/FUBC_1_to_9_data.csv')

## filter for the FUBC_report_number == 9
wave_9 = df[df['FUBC_report_number'] == 9]
wave_9.describe()

## show list of countries in wave 9
print(wave_9['Country'].unique())
print(wave_9['Country'].nunique())
print(wave_9["Crop"].unique())
print(wave_9["Crop"].nunique())

# 64 countries are represented in wave 9

## show descriptives for Nan values in wave 9
print(wave_9.isna().sum())

print(wave_9)

# drop columns with nan values
wave_9 = wave_9.dropna(axis=1)

# make all column names lowercase
wave_9.columns = wave_9.columns.str.lower()

# drop columns "original_country_name_in_fubc_report", "fubc_report_number", "year_fubc_publication", "p2o5_k_t", "k2o_k_t", "n_p2o5_k2o_k_t", "aver_p2o5_rate_kg_ha",'aver_k2o_rate_kg_ha', 'aver_n_p2o5_k2o_rate_kg_ha'
wave_9 = wave_9.drop(["original_country_name_in_fubc_report", "fubc_report_number", "year_fubc_publication", "p2o5_k_t", "k2o_k_t", "n_p2o5_k2o_k_t", "aver_p2o5_rate_kg_ha",'aver_k2o_rate_kg_ha', 'aver_n_p2o5_k2o_rate_kg_ha'], axis=1)

# create columns "fertilizer emission id", "ghg_type_id", "reliability_score", "academic_citation", "created at" and fill them with nan values
wave_9["fertilizer_emission_id"] = "NaN"
wave_9["ghg_type_id"] = "NaN"
wave_9["reliability_score"] = "NaN"
wave_9["academic_citation"] = "Ludemann, C.I., Gruere, A., Heffer, P. et al. Global data on fertilizer use by crop and by country. Sci Data 9, 501 (2022). https://doi.org/10.1038/s41597-022-01592-z"
wave_9["created_at"] = "NaN"


print(wave_9.columns)

# save wave 9 as csv file
wave_9.to_csv('data-clean/N_use_crop_country.csv', index=False)