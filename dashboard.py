
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Create dashboard function
def create_dashboard(product="All", region="All"):

    filtered_df = df.copy()

    if product != "All":
        filtered_df = filtered_df[filtered_df["Product"] == product]

    if region != "All":
        filtered_df = filtered_df[filtered_df["Region"] == region]

    # KPI calculations
    total_sales = filtered_df["Total_Sales"].sum()
    total_quantity = filtered_df["Quantity"].sum()
    total_transactions = len(filtered_df)
    average_sales = filtered_df["Total_Sales"].mean()

    print("=" * 50)
    print("INTERACTIVE SALES DASHBOARD")
    print("=" * 50)
    print(f"Product Filter: {product}")
    print(f"Region Filter: {region}")
    print("-" * 50)
    print(f"Total Sales: ₹{total_sales:,.2f}")
    print(f"Total Quantity: {total_quantity:,}")
    print(f"Total Transactions: {total_transactions:,}")
    print(f"Average Transaction Sales: ₹{average_sales:,.2f}")
    print("=" * 50)

    # Sales Trend
    daily_sales = (
        filtered_df.groupby("Date")["Total_Sales"]
        .sum()
        .reset_index()
    )

    fig_trend = px.line(
        daily_sales,
        x="Date",
        y="Total_Sales",
        markers=True,
        title="Daily Sales Trend"
    )

    # Product Performance
    product_sales = (
        filtered_df.groupby("Product")["Total_Sales"]
        .sum()
        .reset_index()
    )

    fig_product = px.bar(
        product_sales,
        x="Product",
        y="Total_Sales",
        title="Sales by Product"
    )

    # Regional Sales
    region_sales = (
        filtered_df.groupby("Region")["Total_Sales"]
        .sum()
        .reset_index()
    )

    fig_region = px.pie(
        region_sales,
        names="Region",
        values="Total_Sales",
        title="Regional Sales Distribution"
    )

    fig_trend.show()
    fig_product.show()
    fig_region.show()


if __name__ == "__main__":
    create_dashboard()
