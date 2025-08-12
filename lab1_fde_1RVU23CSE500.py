import pandas as pd

#LAB1: Data Analysis and Visualization
sales_df = pd.read_csv('sale_price.csv')
feedback_df = pd.read_json('customer_feedback.json')
print("Sales Data Sample:")
print(sales_df.head())
print("\nCustomer Feedback Sample:")
print(feedback_df.head())

required_sales_cols = ['product_id', 'sale_price', 'customer_id']
required_feedback_cols = ['customer_id', 'product_id', 'sentiment_score']

print("\nSelected Sales Columns:")
print(sales_df[required_sales_cols].head())
print("\nSelected Feedback Columns:")
print(feedback_df[required_feedback_cols].head())

# Calculate total revenue per product
sales_df['revenue'] = sales_df['sale_price']
product_revenue = sales_df.groupby('product_id')['revenue'].sum().reset_index()
top5_products = product_revenue.sort_values(by='revenue', ascending=False).head(5)
print("\nTop 5 Products by Revenue:")
print(top5_products)

# Merge with feedback to analyze sentiment for top products
top5_ids = top5_products['product_id']
top_feedback = feedback_df[feedback_df['product_id'].isin(top5_ids)]
sentiment_by_product = top_feedback.groupby('product_id')['sentiment_score'].mean().reset_index()
print("\nAverage Sentiment Score for Top 5 Products:")
print(sentiment_by_product)
