import os
import re

# Base directory
base_dir = r"c:\Users\122798\OneDrive\Documents\Sonstiges\Bew\Bewerbungen"

# The incorrect string we introduced was likely:
# "MAAG Group | Grabenstraße 135, 63762 Großostheim, Bavaria, Germany"
# or similar, where "Grossostheim, Germany" was replaced by the full address.

# We want to revert "Grabenstraße 135, 63762 Großostheim, Bavaria, Germany" 
# to "Großostheim, Germany" ONLY where it appears next to MAAG Group.
# Actually, since the user's address IS Grabenstraße, we should only change it if it's associated with MAAG.
# In the CVs, it looks like: <div class="exp-company">MAAG Group | Grabenstraße 135, 63762 Großostheim, Bavaria, Germany</div>

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Regex to find MAAG Group followed by the wrong address
    # We'll look for "MAAG Group" + any separator + "Grabenstraße 135, 63762 Großostheim, Bavaria, Germany"
    
    # Target pattern: MAAG Group | Grabenstraße 135, 63762 Großostheim, Bavaria, Germany
    # Replacement: MAAG Group | Großostheim, Germany
    
    pattern = r"(MAAG Group\s*\|\s*)Grabenstraße 135, 63762 Großostheim, Bavaria, Germany"
    replacement = r"\1Großostheim, Germany"
    
    content = re.sub(pattern, replacement, content)

    # Also handle the MD file case if it's different
    # In MD it might be: **MAAG Group** | Grabenstraße 135...
    pattern_md = r"(\*\*MAAG Group\*\*\s*\|\s*)Grabenstraße 135, 63762 Großostheim, Bavaria, Germany"
    replacement_md = r"\1Großostheim, Germany"
    
    content = re.sub(pattern_md, replacement_md, content)

    if content != original_content:
        print(f"Fixing address in {os.path.basename(filepath)}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        # print(f"No changes for {os.path.basename(filepath)}")
        pass

def main():
    files = [f for f in os.listdir(base_dir) if f.endswith('.html') or f.endswith('.md')]
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        update_file(filepath)

if __name__ == "__main__":
    main()
