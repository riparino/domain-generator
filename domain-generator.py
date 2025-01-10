# Cleaned and refined script to prevent malformed domains

import itertools

# Define keywords for domain generation
keywords = ["example", "test", "keyword", "company"]

# Define common TLDs
tlds = [".com", ".org", ".net", ".info", ".io", ".xyz", ".co"]

# Define common phishing modifications
modifications = ["", "secure", "auth", "login", "portal", "project", "group", "1", "0", "z", "x"]

# Define high-value keywords for filtering
high_value_keywords = ["example", "company", "secure", "login", "auth", "group", "project"]

# Define popular TLDs for filtering
popular_tlds = [".com", ".net", ".org", ".info"]

# Function to generate domains with dashes correctly placed
def generate_domains(keywords, modifications, tlds):
    domains = set()

    # Generate permutations of keywords
    for i in range(2, len(keywords) + 1):  # At least 2 keywords for meaningful dashes
        for perm in itertools.permutations(keywords, i):
            base_with_dashes = "-".join(perm)  # Combine keywords with dashes

            # Apply modifications, avoiding invalid placements
            for mod in modifications:
                if mod and mod not in ["-", "."]:  # Skip invalid modifiers
                    modified_base = f"{base_with_dashes}-{mod}"
                else:
                    modified_base = base_with_dashes

                # Ensure no domain starts or ends with invalid structures
                if not modified_base.startswith("-") and not modified_base.endswith("-") and ".." not in modified_base:
                    for tld in tlds:
                        domains.add(modified_base + tld)
                        domains.add(f"www.{modified_base + tld}")

    return domains

# Function to filter high-probability domains
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
generated_domains = generate_domains(keywords, modifications, tlds)

# Filter domains
filtered_domains = filter_domains(generated_domains, high_value_keywords, popular_tlds)

# Save to file
output_file_path = "output.txt"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for domain in filtered_domains:
        output_file.write(domain + "\n")

output_file_path
