import pandas as pd

# Merged_Sales_Merged.xlsx फाइल को लोड करना
df = pd.read_excel("Merged_Sales_Merged.xlsx")

# 'Date' कॉलम को डेटाटाइम में बदलना ताकि हम महीने का पता लगा सकें
df['Date'] = pd.to_datetime(df['Date'])

# महीने का नाम निकालना
df['Month'] = df['Date'].dt.strftime('%Y-%m')  # YYYY-MM format

# प्रत्येक महीने और उत्पाद के लिए औसत Quantity और कुल Sales निकालना
monthly_stats = df.groupby(['Month', 'Product']).agg(
    Average_Quantity=('Quantity', 'mean'),
    Total_Sales=('Total Sales', 'sum')
).reset_index()

# 'Merged_Sales_Merged.xlsx' में नए शीट में इन आंकड़ों को जोड़ना
with pd.ExcelWriter("Merged_Sales_Merged.xlsx", engine='openpyxl', mode='a') as writer:
    monthly_stats.to_excel(writer, sheet_name="Monthly_Statistics", index=False)

print("औसत मात्रा और कुल बिक्री के आंकड़े 'Monthly_Statistics' शीट में जोड़ दिए गए हैं।")
