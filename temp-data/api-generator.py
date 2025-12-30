#!/usr/bin/env python3
"""
API Generator for ComplianceCompass
Generates static JSON API endpoints from app-data.json for GitHub Pages hosting
"""

import json
import os
from datetime import datetime
from pathlib import Path
import re

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def create_api_response(data, total=None, endpoint=None):
    """Wrap data in standardized API response format"""
    return {
        "meta": {
            "version": "1.0.0",
            "generated": datetime.utcnow().isoformat() + "Z",
            "total": total if total is not None else (len(data) if isinstance(data, list) else 1),
            "endpoint": endpoint or "unknown"
        },
        "data": data
    }

def save_json(filepath, data):
    """Save data as formatted JSON file"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✓ Created {filepath}")

def generate_api_files(source_file='../app-data.json', output_dir='../../api'):
    """Generate all API endpoint files"""

    # Load source data
    print(f"Loading data from {source_file}...")
    with open(source_file, 'r', encoding='utf-8') as f:
        controls = json.load(f)

    print(f"Loaded {len(controls)} controls")

    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # 1. Generate /api/all.json - Complete dataset
    print("\n1. Generating /api/all.json...")
    save_json(
        f"{output_dir}/all.json",
        create_api_response(controls, len(controls), "/api/all.json")
    )

    # 2. Generate /api/standards/{standard}.json - Filter by standard
    print("\n2. Generating standard endpoints...")
    standards = {}
    for control in controls:
        std = control['standard'].lower()
        if std not in standards:
            standards[std] = []
        standards[std].append(control)

    for standard, std_controls in standards.items():
        save_json(
            f"{output_dir}/standards/{standard}.json",
            create_api_response(
                std_controls,
                len(std_controls),
                f"/api/standards/{standard}.json"
            )
        )

    # 3. Generate /api/categories/{category-slug}.json - Filter by category
    print("\n3. Generating category endpoints...")
    categories = {}
    for control in controls:
        cat = control['category']
        cat_slug = slugify(cat)
        if cat_slug not in categories:
            categories[cat_slug] = {
                'name': cat,
                'controls': []
            }
        categories[cat_slug]['controls'].append(control)

    for cat_slug, cat_data in categories.items():
        save_json(
            f"{output_dir}/categories/{cat_slug}.json",
            create_api_response(
                cat_data['controls'],
                len(cat_data['controls']),
                f"/api/categories/{cat_slug}.json"
            )
        )

    # 4. Generate /api/controls/{control-id}.json - Individual control details
    print("\n4. Generating individual control endpoints...")
    for control in controls:
        control_id_slug = slugify(control['id'])
        save_json(
            f"{output_dir}/controls/{control_id_slug}.json",
            create_api_response(
                control,
                endpoint=f"/api/controls/{control_id_slug}.json"
            )
        )

    # 5. Generate /api/mappings/{control-id}.json - Just mappings for a control
    print("\n5. Generating mapping endpoints...")
    for control in controls:
        control_id_slug = slugify(control['id'])
        mapping_data = {
            'id': control['id'],
            'standard': control['standard'],
            'title': control['title'],
            'mappings': control['mappings']
        }
        save_json(
            f"{output_dir}/mappings/{control_id_slug}.json",
            create_api_response(
                mapping_data,
                endpoint=f"/api/mappings/{control_id_slug}.json"
            )
        )

    # 6. Generate index file listing all endpoints
    print("\n6. Generating API index...")
    api_index = {
        "meta": {
            "version": "1.0.0",
            "generated": datetime.utcnow().isoformat() + "Z"
        },
        "endpoints": {
            "all_controls": "/api/all.json",
            "standards": {
                "owasp": "/api/standards/owasp.json",
                "iso27001": "/api/standards/iso27001.json",
                "nist": "/api/standards/nist.json"
            },
            "categories": [f"/api/categories/{slug}.json" for slug in sorted(categories.keys())],
            "individual_controls": f"/api/controls/{{control-id}}.json",
            "mappings": f"/api/mappings/{{control-id}}.json"
        },
        "usage": {
            "base_url": "https://secuardenai.github.io/compliance-compass",
            "example": "https://secuardenai.github.io/compliance-compass/api/standards/owasp.json"
        }
    }
    save_json(f"{output_dir}/index.json", api_index)

    # Generate summary
    print("\n" + "="*60)
    print("API Generation Complete!")
    print("="*60)
    print(f"Total controls: {len(controls)}")
    print(f"Standards: {len(standards)}")
    print(f"Categories: {len(categories)}")
    print(f"Individual control endpoints: {len(controls)}")
    print(f"Mapping endpoints: {len(controls)}")
    print(f"\nTotal API files created: {len(controls) * 2 + len(standards) + len(categories) + 2}")
    print("="*60)

if __name__ == "__main__":
    generate_api_files()
