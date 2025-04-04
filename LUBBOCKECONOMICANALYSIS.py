import pandas as pd

fp ="C:/Users/mattv/Downloads/"
report_csv = 'report.csv'

earn_data = "C:/Users/mattv/Downloads/SMU48311800500000003.csv"
hours_data = "C:/Users/mattv/Downloads/SMU48311800500000002.csv"
unemployment_data = "C:/Users/mattv/Downloads/UnemploymentIncome.csv"

dfearn = pd.read_csv(earn_data, delimiter=',') 
dfhours = pd.read_csv(hours_data, delimiter=',') 
dfunemployment = pd.read_csv(unemployment_data, delimiter=',') 


final_df = pd.merge(dfearn, dfhours, on='DATE', how='outer')

final_df = pd.merge(final_df, dfunemployment, on='DATE', how='outer')


final_df['Average Hours Worked a Week'] *= 4

new_column_name = 'Average Hours Worked a Month'  
final_df.rename(columns={'Average Hours Worked a Week': new_column_name}, inplace=True)

final_df['Average Monthly Income'] = final_df['Average Wage Per Hour'] * final_df['Average Hours Worked a Month']



sum_of_avg_monthly_22 = final_df['Average Monthly Income'].iloc[0:11].sum()

final_df['2022 Yearly Income'] = " "  
final_df.at[0, '2022 Yearly Income'] = sum_of_avg_monthly_22

sum_of_avg_monthly_23 = final_df['Average Monthly Income'].iloc[12:23].sum()

final_df['2023 Yearly Income'] = " "  
final_df.at[0, '2023 Yearly Income'] = sum_of_avg_monthly_23




specific_column_index = final_df.columns.get_loc('Unemployment Average Income Monthly')

column_to_move = final_df.pop('Unemployment Average Income Monthly')

final_df.insert(specific_column_index + 1, 'Unemployment Average Income Monthly', column_to_move)


output_csv = fp + 'final_report.csv'

final_df.to_csv(output_csv, index=False)
