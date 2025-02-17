###############################################
# AB Testing - Our Task for ABC Grocery
###############################################

# IMPORT REQUIRED PACKAGES

import pandas as pd
from scipy.stats import chi2_contingency, chi2



# IMPORT DATA
campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name="campaign_data")


# FILTER OUR DATA

campaign_data = campaign_data.loc[campaign_data["mailer_type"] != "Control"]


# SUMMARISE TO GET OUR OBSERVED FREQUENCIES

observed_values = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"]).values

mailer1_signup_rate = 123 / (123 + 252)
mailer2_signup_rate = 127 / (127 + 209)
print(mailer1_signup_rate, mailer2_signup_rate)



# STATE HYPOTHESIS & SET ACCEPTANCE CRITERIA

null_hypothesis = "There is no relationship between mailer type and signup rate. they are independent"
alternative_hypothesis = "There is a relationship between mailer type and signup rate. they are not independent"
acceptance_criteria = 0.05

# CALCULATE EXPECTED FREQUENCIES & CHI SQUARE STATISTIC
''' Yates correction shoud be false if degrees of freedom are equal to 1 '''

chi2_statistic, p_value, dof, expected_values = chi2_contingency(observed_values, correction=False)
print(chi2_statistic, p_value)


# FIND THE CRITICAL VALUE FOR OUR TEST
""" ppf = percentage point function """

critical_value = chi2.ppf(1 - acceptance_criteria, dof)
print(critical_value)

# PRINT THE RESULTS(CHI SQUARE STATISTIC)

if chi2_statistic >= critical_value:
    print(f"As our chi-square statistic of {chi2_statistic} is higher than our critical value of {critical_value} - we reject the null hypothesis, and conclude that: {alternative_hypothesis}")
else:
    print(f"As our chi-square statistic of {chi2_statistic} is lower than our critical value of {critical_value} - we retain the null hypothesis, and conclude that: {null_hypothesis}")


# PRINT THE RESULT (p-value)


if p_value <= acceptance_criteria:
    print(f"As our p_value of {p_value} is lower than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternative_hypothesis}")
else:
    print(f"As our p_value of {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}")















