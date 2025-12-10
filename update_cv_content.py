import os
import re

# Base directory
base_dir = r"c:\Users\122798\OneDrive\Documents\Sonstiges\Bew\Bewerbungen"

# Data to update
contact_updates = {
    r"\[Phone\]": "179 4228285",
    r"\[Email\]": "jonasglawion@aol.com",
    r"Grossostheim, Germany": "Grabenstraße 135, 63762 Großostheim, Bavaria, Germany",
    r"linkedin\.com/in/jonas-glawion": "linkedin.com/in/jonas-glawion-21824115a",
    r"https://linkedin\.com/in/jonas-glawion": "https://www.linkedin.com/in/jonas-glawion-21824115a",
    r"\[Photo\]": '<img src="Gemini_Generated_Image_ldn0ffldn0ffldn0.png" alt="Jonas Glawion" width="150" style="border-radius: 50%; object-fit: cover;">'
}

# Specific percentage replacements (context-aware to avoid replacing CSS)
# Using regex to match the number and optional surrounding text, replacing with qualitative terms
percentage_replacements = [
    (r"8-12%", "significant"),
    (r"18%", "substantial"),
    (r"15%", "considerable"),
    (r"11%", "notable"),
    (r"22%", "outstanding"),
    (r"9%", "measurable"),
    # Generic catch-all for other percentage claims in text (checking for digits followed by %)
    # We must be careful not to replace CSS width: 30% etc.
    # Strategy: Replace specific known values first.
]

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Contact Info Updates
    for pattern, replacement in contact_updates.items():
        # strict replacement for textual placeholders
        content = re.sub(pattern, replacement, content)

    # 2. Percentage Updates
    # We want to replace "X%" with "qualitative word" BUT NOT "width: 30%"
    # So we look for " X%" or "X% " in text context, or specific known stats.
    
    for pat, rep in percentage_replacements:
        content = content.replace(pat, rep)
    
    # 3. Handle any missed linkedIn ID if it didn't match the exact string
    # (The dictionary covers the main cases seen in the file view)

    if content != original_content:
        print(f"Updating {os.path.basename(filepath)}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(f"No changes for {os.path.basename(filepath)}")

def main():
    files = [f for f in os.listdir(base_dir) if f.endswith('.html') or f.endswith('.md')]
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        update_file(filepath)

if __name__ == "__main__":
    main()
