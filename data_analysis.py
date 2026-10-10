import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("data/retail_sales_dataset copy.csv")


# Check the number of rows and columns
print(df.shape)

# Check column names and data types
print(df.info())

# Get basic statistical information
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Check duplicate rows
print(df.duplicated().sum())

#convert the date column to datetime format
df['Date']=pd.to_datetime(df['Date'])

#check the date after conversion
print(df.info())

#check the date range of the dataset
print('first transaction date:',df['Date'].min())
print('last transaction date:',df['Date'].max())

#check unique product catagory
print('unique product category:', df['Product Category'].unique())

#check unique gender
print('unique gender:',df['Gender'].unique())

# Verify the total amount calculation
print('incorrect amount records:',(df['Total Amount'] != df['Quantity'] * df['Price per Unit']).sum())


#FIND TOTAL REVENUE 
print('total revenue:', df['Total Amount'].sum())
print('total transactions:', df['Transaction ID'].nunique())
print('average transaction value:', df['Total Amount'].mean())'''

#analyze the sales data by product category
category_sales = df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)
print(category_sales)

'''plt.figure(figsize=(8,5))
plt.bar(category_sales.index, category_sales.values)
plt.title('Total sales by product category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()'''

#analyze the sales data by gender
gender_sales = df.groupby('Gender')['Total Amount'].sum().sort_values(ascending=False)
print(gender_sales)
'''
plt.figure(figsize=(7,5))
plt.bar(gender_sales.index, gender_sales.values)
plt.title('Total sales by gender')
plt.xlabel('Gender')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

#no of transacrtions per category
category_transaction=df.groupby('Product Category')['Transaction ID'].sum().sort_values(ascending=False)
print(category_transaction)

#which age group has the highest sales

df["Age Group"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65"]
)

age_sales = df.groupby("Age Group", observed=False)["Total Amount"].sum()

print(age_sales.sort_values(ascending=False))

#which gender spends more on average
average_spending = df.groupby('Gender')['Total Amount'].mean()
print(average_spending)


# Monthly Sales Trend

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Total Amount"].sum()

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))

sns.boxplot(
    data=df,
    x="Product Category",
    y="Total Amount"
)

plt.title("Sales Distribution by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Transaction Amount")

plt.tight_layout()
plt.show()

# Select numerical columns
numeric_df = df[
    ["Age", "Quantity", "Price per Unit", "Total Amount"]
]

# Calculate correlation matrix
correlation = numeric_df.corr()

# Create heatmap
plt.figure(figsize=(8, 5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap of Retail Sales")
plt.tight_layout()
plt.show()'''

'''# 1. Top-selling product category
print("Top Product Category:")
print(category_sales.idxmax())

# 2. Lowest-selling product category
print("Lowest Product Category:")
print(category_sales.idxmin())

# 3. Month with the highest sales
print("Best Sales Month:")
print(monthly_sales.idxmax())

# 4. Month with the lowest sales
print("Lowest Sales Month:")
print(monthly_sales.idxmin())

# 5. Highest average spending by gender
print("Average Spending by Gender:")
print(average_spending.sort_values(ascending=False))

df.to_csv("data/retail_sales_cleaned.csv", index=False)

print("Cleaned dataset exported successfully!")

print("\n===== RETAIL SALES BUSINESS INSIGHTS =====")

# Overall performance
print("Total Revenue:", df["Total Amount"].sum())
print("Total Transactions:", df["Transaction ID"].nunique())
print("Average Transaction Value:", round(df["Total Amount"].mean(), 2))

# Best-performing category
print("\nTop Product Category:")
print(category_sales.idxmax(), "-", category_sales.max())

# Gender contributing the most revenue
print("\nHighest Revenue by Gender:")
print(gender_sales.idxmax(), "-", gender_sales.max())

# Best-performing month
print("\nBest Sales Month:")
print(monthly_sales.idxmax(), "-", monthly_sales.max())

# Highest average spending by gender
print("\nHighest Average Spending by Gender:")
print(average_spending.idxmax(), "-", round(average_spending.max(), 2))
