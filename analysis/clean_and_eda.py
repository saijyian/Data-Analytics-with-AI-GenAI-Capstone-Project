#Task 1 — Load and inspect — 2 marks
#Load the three CSVs with pd.read_csv. orders.shape must print (180, 9) before any cleaning.

import pandas as pd

# Load the three uploaded CSV files 
#Uploaded the files in Google Colab
orders = pd.read_csv("/orders.csv")
customers = pd.read_csv("/customers.csv")
products = pd.read_csv("/products.csv")

# Print the raw orders shape BEFORE any cleaning
print("Orders shape:", orders.shape)
#Output :Orders shape: (180, 9)



#Task 2 — Standardize payment_method casing — 4 marks
#Apply .str.strip().str.upper() to payment_method. Before the fix, orders['payment_method'].unique() must show 7 distinct raw values (COD, cod, Card, card, CARD, UPI, upi). After the fix, exactly 3 remain, with counts CARD: 70, UPI: 55, COD: 55.
# 1. Before cleaning: inspect raw payment method values

print("Unique payment methods BEFORE cleaning:")
print(orders["payment_method"].unique())

print(
    "Number of distinct raw values:",
    orders["payment_method"].nunique()
)

# 2. Clean payment_method: remove extra spaces and standardize capitalization
orders["payment_method"] = (
    orders["payment_method"].str.strip().str.upper()
)

# 3. After cleaning: inspect unique values and counts
print("\nUnique payment methods AFTER cleaning:")
print(orders["payment_method"].unique())

print("\nPayment method counts AFTER cleaning:")
print(orders["payment_method"].value_counts().sort_index())

#Output: 
#Unique payment methods BEFORE cleaning:
#['UPI' 'COD' 'CARD']
#Number of distinct raw values: 3

#Unique payment methods AFTER cleaning:
#['UPI' 'COD' 'CARD']

#Payment method counts AFTER cleaning:
#payment_method
#CARD    70
#COD     55
#UPI     55

#Task 3 — Remove duplicate orders — 4 marks
#Using .duplicated(subset=[...], keep='first') on the natural key customer_id, product_id, order_date, quantity, discount_pct, payment_method, rating, returned (everything except order_id, which differs on the duplicated rows by design), detect and drop duplicates. Exactly 5 rows must be flagged and dropped; orders_clean.shape must be (175, 9) afterward. Print the 5 dropped order_id values — they must be O0176, O0177, O0178, O0179, O0180.

# Columns used to identify duplicates
key = [
    'customer_id', 'product_id', 'order_date', 'quantity',
    'discount_pct', 'payment_method', 'rating', 'returned'
]

# Find and print duplicate order IDs
duplicates = orders.duplicated(subset=key, keep='first')

print("Duplicate order IDs:")
print(orders.loc[duplicates, 'order_id'].tolist())

# Remove duplicates
orders_clean = orders.drop_duplicates(subset=key, keep='first')

# Print final shape
print("Shape after removing duplicates:", orders_clean.shape)

#Output
#Duplicate order IDs:
#['O0176', 'O0177', 'O0178', 'O0179', 'O0180']
#Shape after removing duplicates: (175, 9)


#Task 4 — Impute missing values — 4 marks
#discount_pct: fill NaN with 0 (business rule: no promo code applied). 12 rows affected (count this on the deduplicated frame, i.e. after Task 3).
#rating: fill NaN with the median of the non-null ratings on the deduplicated frame. Print the median before imputing — it must be 3.0. 15 rows affected.
#After imputing, orders_clean[['discount_pct','rating']].isnull().sum() must be {'discount_pct': 0, 'rating': 0}.
# Fill missing discount_pct values with 0
print("Missing discount_pct before:", orders_clean['discount_pct'].isnull().sum())
orders_clean['discount_pct'] = orders_clean['discount_pct'].fillna(0)

# Find and print median rating before imputing
median_rating = orders_clean['rating'].median()
print("Median rating before imputation:", median_rating)

# Fill missing rating values with the median
print("Missing ratings before:", orders_clean['rating'].isnull().sum())
orders_clean['rating'] = orders_clean['rating'].fillna(median_rating)

# Check missing values after imputation
print("Missing values after imputation:")
print(orders_clean[['discount_pct', 'rating']].isnull().sum())

#Output
#Missing discount_pct before: 12
#Median rating before imputation: 3.0
#Missing ratings before: 15
#Missing values after imputation:
#discount_pct    0
#rating          0

