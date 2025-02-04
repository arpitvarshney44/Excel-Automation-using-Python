import pandas as pd
import random
from datetime import datetime, timedelta

# 12 महीनों के नाम
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# संभावित उत्पादों की सूची
products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch", "Keyboard", "Mouse", "Monitor", "Printer", "Speaker"]

# 12 महीनों के लिए डेटा जनरेट करना
for month_index, month in enumerate(months):
    file_path = f"{month}.xlsx"  # फाइल नाम
    
    # प्रत्येक महीने की शुरुआत की तारीख निकालना
    start_date = datetime(2024, month_index + 1, 1)
    days_in_month = (datetime(2024, month_index + 2, 1) - timedelta(days=1)).day if month_index != 11 else 31
    
    # 100 बिक्री रिकॉर्ड बनाना
    sales_data = []
    for _ in range(100):
        date = start_date + timedelta(days=random.randint(0, days_in_month - 1))
        product = random.choice(products)
        quantity = random.randint(1, 10)
        price = random.randint(500, 50000)  # प्रति यूनिट कीमत
        total_sales = quantity * price
        
        sales_data.append([date.strftime("%Y-%m-%d"), product, quantity, price, total_sales])
    
    # डेटा फ्रेम बनाना
    df_sales = pd.DataFrame(sales_data, columns=["Date", "Product", "Quantity", "Price", "Total Sales"])
    
    # एक्सेल फाइल में सेव करना
    df_sales.to_excel(file_path, index=False)

print("सभी 12 महीनों की Excel फाइलों में डेटा जोड़ दिया गया है।")
