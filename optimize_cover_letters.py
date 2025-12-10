import os

base_dir = r"c:\Users\122798\OneDrive\Documents\Sonstiges\Bew\Bewerbungen"

print_css = """
        @media print {
            @page {
                size: A4;
                margin: 0;
            }
            body {
                margin: 0;
                padding: 0;
                background-color: white;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
                width: 210mm;
                height: 297mm;
            }
            .container {
                width: 100%;
                max-width: none;
                box-shadow: none;
                margin: 0;
                padding: 20mm;
                min-height: 100vh;
            }
            header {
                margin-bottom: 20px;
            }
        }
"""

def update_cover_letter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already added it (simple check)
    if "@page { size: A4;" in content:
        # print(f"Skipping {os.path.basename(filepath)}, already optimized.")
        return

    # Insert before </style>
    if "</style>" in content:
        new_content = content.replace("</style>", print_css + "\n    </style>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")
    else:
        print(f"Could not find </style> in {os.path.basename(filepath)}")

def main():
    files = [f for f in os.listdir(base_dir) if f.startswith("Cover_Letter_") and f.endswith(".html")]
    for filename in files:
        update_cover_letter(os.path.join(base_dir, filename))

if __name__ == "__main__":
    main()
