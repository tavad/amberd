import os
import yaml
from pathlib import Path

# Translation dictionary with Armenian translations
translations = {
    # Main navigation and menu items
    "About": "Մեր մասին",
    "Community": "Համայնք",
    "Research": "Հետազոտություններ",
    "Multimedia": "Մուլտիմեդիա",
    "Bulletin": "Տեղեկագիր",
    "News": "Նորություններ",
    "Releases": "Թողարկումներ",
    "Info": "Ինֆո",
    "Search Results": "Որոնման արդյունքներ",

    # About section
    "History": "Պատմություն",
    "Mission and Goals": "Առաքելություն, նպատակներ",
    "Our Team": "Մեր թիմը",
    "Staff": "Աշխատակազմ",
    "Invited Experts": "Հրավիրյալ փորձագետներ",
    "Expert Board": "Փորձագիտական խորհուրդ",
    "Partners": "Գործընկերներ",
    "Documents": "Փաստաթղթեր",
    "Charter": "Կանոնադրություն",
    "Annual Reports": "Տարեկան հաշվետվություններ",
    "Other Documents": "Այլ փաստաթղթեր",

    # Descriptions
    "Meet Our Team": "Ծանոթացեք մեր թիմին",
    "Organization Charter": "Կազմակերպության կանոնադրություն",
    "Official Documents": "Պաշտոնական փաստաթղթեր",
    "Additional Documentation": "Լրացուցիչ փաստաթղթեր",
    "Annual Reports Archive": "Տարեկան հաշվետվությունների արխիվ",
    "Our History": "Մեր պատմությունը",
    "Our Partners": "Մեր գործընկերները",
    "Our Staff Members": "Մեր աշխատակիցները",
    "Expert Board Members": "Փորձագիտական խորհրդի անդամներ",
    "Our Mission, Goals and Objectives": "Մեր առաքելությունը, նպատակները և խնդիրները",
    "Our Invited Experts": "Մեր հրավիրյալ փորձագետները",

    # Common UI elements
    "Learn More": "Իմանալ ավելին",
    "Download": "Ներբեռնել",
    "Follow us on Twitter": "Հետևեք մեզ Twitter-ում",
    "Contributions welcome": "Ողջունում ենք ներդրումները",

    # Content sections
    "Videos": "Տեսանյութեր",
    "Interviews": "Հարցազրույցներ",
    "Chronicle": "Ժամանակագրություն",
    "SWOT": "ՈՒԹՀՎ",

    # Landing page content
    "Welcome to": "Բարի գալուստ",
    "A Docsy Example Project": "Docsy օրինակելի նախագիծ",
    "This is another section": "Սա մեկ այլ բաժին է"
}

def translate_frontmatter(file_path):
    """Translate frontmatter while preserving file structure and existing translations"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find frontmatter between --- markers
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])

            # Translate title if present and not already in Armenian
            if 'title' in frontmatter and frontmatter['title'] in translations:
                if not any(ord(c) >= 0x0530 and ord(c) <= 0x058F for c in frontmatter['title']):  # Check if not already Armenian
                    frontmatter['title'] = translations[frontmatter['title']]

            # Translate description if present and not already in Armenian
            if 'description' in frontmatter and frontmatter['description'] in translations:
                if not any(ord(c) >= 0x0530 and ord(c) <= 0x058F for c in str(frontmatter['description'])):
                    frontmatter['description'] = translations[frontmatter['description']]

            # Translate linkTitle if present and not already in Armenian
            if 'linkTitle' in frontmatter and frontmatter['linkTitle'] in translations:
                if not any(ord(c) >= 0x0530 and ord(c) <= 0x058F for c in frontmatter['linkTitle']):
                    frontmatter['linkTitle'] = translations[frontmatter['linkTitle']]

            # Write back the modified file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('---\n')
                f.write(yaml.dump(frontmatter, allow_unicode=True))
                f.write('---\n')
                f.write(parts[2])

def process_directory(directory):
    """Process all markdown files in directory and subdirectories"""
    for path in Path(directory).rglob('*.md'):
        print(f"Processing {path}")
        translate_frontmatter(str(path))

if __name__ == "__main__":
    # Use absolute path
    base_dir = os.path.abspath("hy")
    print(f"Processing directory: {base_dir}")
    process_directory(base_dir)
