import pandas as pd

# Define model information for User and IpoInfo
models_info = {
    'User': {
        'username': {'type': 'String', 'size': 150},
        'email': {'type': 'String', 'size': 255},
        'password': {'type': 'String', 'size': 128},
        'created_at': {'type': 'DateTime', 'size': None},
    },
    'IpoInfo': {
        'ipo_id': {'type': 'Integer', 'size': None},
        'company_name': {'type': 'String', 'size': 255},
        'offering_price': {'type': 'Float', 'size': None},
        'shares_offered': {'type': 'Integer', 'size': None},
        'created_at': {'type': 'DateTime', 'size': None},
    }
}

# Convert the model information to a DataFrame
data = []
for model_name, fields in models_info.items():
    for field_name, details in fields.items():
        data.append({
            'Model': model_name,
            'Field': field_name,
            'Type': details['type'],
            'Size': details['size']
        })

df = pd.DataFrame(data)

# Generate an Excel file
excel_file_path = 'database_models.xlsx'
df.to_excel(excel_file_path, index=False)

print(f'Successfully generated {excel_file_path}')