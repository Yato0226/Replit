import pandas as pd

Product Data

products = { "Designer Evening Dress": (4500, 35), "Premium Business Suit": (8500, 28), "Luxury Casual Blazer": (6200, 20), "High-End Silk Shirt": (3800, 40), "Formal Leather Shoes": (7000, 25) }

Markup Percentage

markup = 1.8

Calculate Selling Prices and Base Daily Revenue

base_daily_revenue = 0 for product, (cost_price, daily_demand) in products.items(): selling_price = cost_price * markup daily_revenue = selling_price * daily_demand base_daily_revenue += daily_revenue

Base Monthly Revenue

base_monthly_revenue = base_daily_revenue * 30

Seasonal Adjustments

seasonal_adjustments = { "January": 0.00, "February": 0.10, "March": 0.10, "April": 0.10, "May": 0.10, "June": 0.15, "July": -0.06, "August": -0.06, "September": -0.13, "October": -0.13, "November": 0.18, "December": 0.25 }

Calculate adjusted revenues

forecast_data = [] total_revenue = 0 for month, adjustment in seasonal_adjustments.items(): adjusted_revenue = base_monthly_revenue * (1 + adjustment) total_revenue += adjusted_revenue forecast_data.append([month, f"{adjustment*100:+.0f}%", f"₱{adjusted_revenue:,.2f}"])

Add total row

forecast_data.append(["Total", "", f"₱{total_revenue:,.2f}"])

Create DataFrame

df = pd.DataFrame(forecast_data, columns=["Month", "Adjustment", "Forecasted Revenue"])

Save to Excel

excel_filename = "Adjusted_Monthly_Revenue_Forecast.xlsx" df.to_excel(excel_filename, index=False)

print(f"Excel file '{excel_filename}' has been created successfully.")

