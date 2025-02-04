import pandas as pd
import os

# 12 महीनों के नाम
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# सभी डेटा को स्टोर करने के लिए एक खाली लिस्ट
all_data = []

# सभी Excel फाइलों को पढ़कर एक लिस्ट में जोड़ना
for month in months:
    file_path = f"{month}.xlsx"  # फाइल का नाम
    
    if os.path.exists(file_path):  # चेक करें कि फाइल मौजूद है या नहीं
        df = pd.read_excel(file_path)  # फाइल को पढ़ें
        df["Month"] = month  # एक नया कॉलम जोड़ें जिससे पता चले कि डेटा किस महीने का है
        all_data.append(df)
    else:
        print(f"फाइल नहीं मिली: {file_path}")

# सभी डेटा को एक DataFrame में मर्ज करना
if all_data:
    merged_data = pd.concat(all_data, ignore_index=True)
    merged_data.to_excel("Merged_Sales.xlsx", index=False)  # नई फाइल सेव करना
    print("सभी फाइलों को मर्ज करके 'Merged_Sales.xlsx' में सेव कर दिया गया है।")
else:
    print("कोई भी डेटा मर्ज करने के लिए नहीं मिला।")
