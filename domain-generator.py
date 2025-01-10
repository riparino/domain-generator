# Full refined script for phishing domain generation

import itertools

# Define keywords for domain generation
keywords = ["example", "test", "keyword", "company"]

# Define common TLDs
tlds = [".com", ".org", ".net", ".info", ".io", ".xyz", ".co"]

# Define common phishing modifications
modifications = [
    "", "-", ".", "secure", "auth", "login", "portal", "project", "group",
    "1", "0", "l", "o", "s", "z", "x"
]

# Define high-value keywords for filtering
high_value_keywords = ["example", "company", "secure", "login", "auth", "group", "project"]

# Define popular TLDs for filtering
popular_tlds = [".com", ".net", ".org", ".info"]

# Function to generate homograph variations of a word
def generate_homographs(word):
    homograph_map = {
        "a": ["á", "à", "â", "ã", "ä", "å", "@"],
        "e": ["é", "è", "ê", "ë"],
        "i": ["í", "ì", "î", "ï", "1", "l"],
        "o": ["ó", "ò", "ô", "õ", "ö", "0"],
        "u": ["ú", "ù", "û", "ü"],
        "c": ["ç"],
        "s": ["$", "5"],
        "l": ["1", "|"],
        "t": ["+", "7"],
        "g": ["9"],
    }
    variations = set([word])
    for i, char in enumerate(word):
        if char in homograph_map:
            for replacement in homograph_map[char]:
                variations.update(generate_homographs(word[:i] + replacement + word[i+1:]))
    return variations

# Function to generate domains with dashes properly placed
def generate_domains_with_dashes(keywords, modifications, tlds):
    domains = set()
    for i in range(2, len(keywords) + 1):  # At least 2 keywords for dashes
        for perm in itertools.permutations(keywords, i):
            base_with_dashes = "-".join(perm)
            for mod in modifications:
                modified_base = f"{base_with_dashes}-{mod}" if mod else base_with_dashes
                if not (modified_base.startswith("-") or modified_base.endswith("-")):
                    for tld in tlds:
                        domains.add(modified_base + tld)
                        domains.add(f"www.{modified_base + tld}")
    return domains

# Function to filter domains for high-probability cases
def filter_domains(domains, high_value_keywords, popular_tlds, max_domains=1000):
    filtered_domains = set()
    for domain in domains:
        contains_dash = "-" in domain
        contains_high_value_keyword = any(keyword in domain for keyword in high_value_keywords)
        ends_with_popular_tld = any(domain.endswith(tld) for tld in popular_tlds)
        if contains_high_value_keyword and ends_with_popular_tld:
            if contains_dash or len(filtered_domains) < max_domains / 2:
                filtered_domains.add(domain)
        if len(filtered_domains) >= max_domains:
            break
    return sorted(filtered_domains)

# Generate domains
generated_domains = generate_domains_with_dashes(keywords, modifications, tlds)

# Filter domains
filtered_domains = filter_domains(generated_domains, high_value_keywords, popular_tlds)

# Save to file
output_file_path = "/mnt/data/filtered_domains_output.txt"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for domain in filtered_domains:
        output_file.write(domain + "\n")

output_file_path
