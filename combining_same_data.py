import pandas as pd

# Merged_Sales.xlsx फाइल को लोड करना
df = pd.read_excel("Merged_Sales.xlsx")

# समान तारीख और उत्पाद के लिए डेटा को मर्ज करना
df_merged = df.groupby(['Date', 'Product'], as_index=False).agg({
    'Quantity': 'sum',        # Quantity को जोड़ना
    'Price': 'first',         # Price (क्योंकि Price समान होता है)
    'Total Sales': 'sum'      # Total Sales को जोड़ना
})

# मर्ज किए गए डेटा को नई Excel फाइल में सेव करना
df_merged.to_excel("Merged_Sales_Merged.xlsx", index=False)

print("समान उत्पाद और तारीख के लिए एंट्रीज़ मर्ज कर दी गई हैं और नई फाइल 'Merged_Sales_Merged.xlsx' में सेव कर दी गई है।")
