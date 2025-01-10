# Phishing Domain Generator

This Python script generates and filters potential phishing domains based on a set of keywords, modifications, and common TLDs. The tool is designed to identify domains that mimic legitimate ones and prioritize high-probability phishing scenarios for proactive monitoring and defense.

## Features

- **Keyword-Based Permutations**: Generates realistic domain permutations using provided keywords.
- **Dash Placement**: Ensures dashes (`-`) are only used in meaningful positions (e.g., between keywords).
- **TLD Support**: Includes popular TLDs (e.g., `.com`, `.net`, `.org`) for phishing scenarios.
- **High-Probability Filtering**: Focuses on domains containing high-value keywords and popular TLDs.
- **Avoids Malformed Domains**: Prevents invalid structures such as `-` at the start or end, or consecutive special characters like `..`.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/phishing-domain-generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd phishing-domain-generator
   ```

3. Install any required dependencies (if applicable):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Edit the script to include your own keywords, modifications, and TLDs:

   ```python
   keywords = ["example", "test", "keyword", "company"]
   modifications = ["", "secure", "auth", "login", "portal"]
   tlds = [".com", ".net", ".org", ".info"]
   ```

2. Run the script:

   ```bash
   python generate_domains.py
   ```

3. The script generates a file named `cleaned_validated_filtered_domains.txt` containing filtered domains.

## Output

The output file will contain a sorted list of potential phishing domains, such as:

```
example-test-login.com
www.example-keyword-secure.net
company-test-portal.org
```

## Customization

- **Keywords**: Update the `keywords` list with terms relevant to your organization or project.
- **TLDs**: Modify the `tlds` list to include additional or region-specific TLDs.
- **Modifications**: Add or remove phishing-specific keywords from the `modifications` list.
- **Max Domains**: Adjust the `max_domains` value in the filtering function to limit the number of results.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your fork.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer

This tool is intended for ethical and defensive purposes only. Use it responsibly and in compliance with applicable laws and regulations.

## Acknowledgment

This README was generated with the assistance of GPT, an AI language model by OpenAI.

