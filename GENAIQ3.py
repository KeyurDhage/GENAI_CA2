import pandas as pd
import numpy as np


class InsuranceModel:
    def __init__(self, vehicle_id, initial_value, years_of_insurance, premium_rate):
        self.vehicle_id = vehicle_id
        self.initial_value = initial_value
        self.years_of_insurance = years_of_insurance
        self.premium_rate = premium_rate
        self.depreciation_rate = 0.07  
        self.vehicle_value_over_time = self.calculate_depreciation()

    def calculate_depreciation(self):
        values = []
        current_value = self.initial_value
        for year in range(self.years_of_insurance):
            values.append(current_value)
            current_value -= current_value * self.depreciation_rate
        return values

    def calculate_premiums(self):
        premiums = []
        for value in self.vehicle_value_over_time:
            yearly_premium = value * self.premium_rate
            quarterly_premium = yearly_premium / 4
            monthly_premium = yearly_premium / 12
            premiums.append({
                'Yearly Premium': yearly_premium,
                'Quarterly Premium': quarterly_premium,
                'Monthly Premium': monthly_premium
            })
        return premiums

    def generate_premium_chart(self):
        premiums = self.calculate_premiums()
        years = np.arange(1, self.years_of_insurance + 1)
        df = pd.DataFrame(premiums, index=years)
        df.index.name = "Year"
        return df


vehicle_id = 'V123'
initial_value = 20000  
years_of_insurance = 5  
premium_rate = 0.05  

insurance_model = InsuranceModel(vehicle_id, initial_value, years_of_insurance, premium_rate)

premium_chart = insurance_model.generate_premium_chart()

premium_chart
