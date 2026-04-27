import csv
import statistics

input_file = 'data/processed/APY_tableau_final.csv'
output_file = 'data/processed/APY_tableau_final_fixed.csv'

rows = []
coconut_yields = []

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        if row['Crop Type'] == 'Coconut':
            try:
                prod = float(row['Production (Tonnes)'])
                area = float(row['Area (Hectares)'])
                new_prod = prod * 0.00144
                row['Production (Tonnes)'] = str(new_prod)
                
                if area > 0:
                    new_yield = new_prod / area
                else:
                    new_yield = 0.0
                
                row['Yield (T/Ha)'] = str(new_yield)
                if new_yield > 0:
                    coconut_yields.append(new_yield)
            except ValueError:
                pass
        rows.append(row)

# Calculate new median yield for coconut
if coconut_yields:
    new_median = statistics.median(coconut_yields)
else:
    new_median = 0.0

# Update Coconut rows with new median and underperforming flag
for row in rows:
    if row['Crop Type'] == 'Coconut':
        row['Median_Yield'] = str(new_median)
        try:
            current_yield = float(row['Yield (T/Ha)'])
            row['Is_Underperforming'] = '1' if current_yield < new_median else '0'
        except ValueError:
            pass

# Write the fixed rows back
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
