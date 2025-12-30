import csv
import json

def convert_csv_to_json(csv_file, standard_name):
    """Convert CSV compliance data to JSON format"""
    data = []

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Generate unique ID based on control code and number
            control_code = row.get('cntrl_code', '').strip()
            control_number = row.get('cntrl_number', '').strip()
            item_id = f"{control_code}-{control_number}" if control_number else control_code

            item = {
                'id': item_id,
                'standard': standard_name,
                'category': row.get('addressed_control', '').strip(),
                'title': row.get('recommendations', '').strip(),
                'description': row.get('Description', '').strip() if row.get('Description') else '',
                'mappings': {
                    'owasp': [],
                    'iso27001': [],
                    'nist': []
                },
                'recommendation': row.get('action_items', '').strip()
            }

            # Parse mappings from mapping_id column
            # Format: ISO27001:2013:A.14.1.1;NIST-SSDF-PO-1-1;OPSC-C3;
            mapping_id = row.get('mapping_id', '').strip()
            if mapping_id:
                # Split by semicolon and filter out empty strings
                mappings = [m.strip() for m in mapping_id.split(';') if m.strip()]

                for mapping in mappings:
                    # OWASP mappings: OPSC-C1, OPSC-C1-1
                    if mapping.startswith('OPSC-'):
                        item['mappings']['owasp'].append(mapping)
                    # ISO27001 mappings: ISO27001:2013:A.14.1.1 or A.14.1.1
                    elif 'ISO27001' in mapping or mapping.startswith('A.'):
                        # Extract just the control ID (A.14.1.1)
                        if ':' in mapping:
                            control_id = mapping.split(':')[-1]
                        else:
                            control_id = mapping
                        item['mappings']['iso27001'].append(control_id)
                    # NIST mappings: NIST-SSDF-PO-1-1, NIST:NIST-SSDF:PO.2, PO.1.1
                    elif 'NIST' in mapping or mapping.startswith('PO.') or mapping.startswith('PS.') or mapping.startswith('PW.') or mapping.startswith('RV.'):
                        # Extract the practice ID (PO.1.1, PO.2, etc.)
                        if ':' in mapping:
                            parts = mapping.split(':')
                            control_id = parts[-1]
                        elif mapping.startswith('NIST-SSDF-'):
                            # Convert NIST-SSDF-PO-1-1 to PO.1.1
                            control_id = mapping.replace('NIST-SSDF-', '').replace('-', '.')
                        else:
                            control_id = mapping
                        item['mappings']['nist'].append(control_id)

            data.append(item)

    return data

# Convert each standard
owasp_data = convert_csv_to_json('owasp_controls.csv', 'OWASP')
iso_data = convert_csv_to_json('iso27001_controls.csv', 'ISO27001')
nist_data = convert_csv_to_json('nist_ssdf.csv', 'NIST')

# Combine all data
all_data = owasp_data + iso_data + nist_data

# Save to JSON
with open('../app-data.json', 'w') as f:
    json.dump(all_data, f, indent=2)

print(f"Converted {len(all_data)} controls to JSON")