# Fire Crawl PY

A Python script to crawl and scrape websites using the Firecrawl API, saving the content in Markdown and HTML formats.

## Features

- Crawls websites and extracts content
- Saves data in both Markdown and HTML formats
- Organizes output in a dedicated `scraped_data` folder
- Configurable via environment variables

## Prerequisites

- Python 3.7+
- Firecrawl API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NafisRayan/Learning.git
   cd "Fire Crawl PY"
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install firecrawl-py python-dotenv
   ```

## Configuration

1. Create a `.env` file in the project root:
   ```
   FIRECRAWL_API_KEY=your_api_key_here
   ```

2. Replace `your_api_key_here` with your actual Firecrawl API key.

## Usage

1. Ensure the virtual environment is activated.

2. Run the script:
   ```bash
   python fc.py
   ```

The script will:
- Crawl the specified website (currently set to https://nafisrayan.vercel.app)
- Save Markdown and HTML files in the `scraped_data` folder
- Print progress messages to the console

## Customization

To crawl a different website, modify the `url` parameter in `fc.py`:

```python
docs = firecrawl.crawl(url="https://your-target-website.com", limit=10, scrape_options={'formats': ['markdown', 'html']})
```

You can also adjust the `limit` parameter to control the number of pages crawled.

## Output

The script creates a `scraped_data` folder containing:
- `.md` files: Markdown versions of the crawled pages
- `.html` files: HTML versions of the crawled pages

File names are generated from the URLs, with special characters replaced for filesystem compatibility.

## Project Structure

```
Fire Crawl PY/
├── fc.py                 # Main scraping script
├── .env                  # Environment variables (API key)
├── .gitignore            # Git ignore rules
├── scraped_data/         # Output folder (ignored by git)
│   ├── page1.md
│   ├── page1.html
│   └── ...
└── README.md             # This file
```

## Dependencies

- `firecrawl-py`: Python client for Firecrawl API
- `python-dotenv`: Loads environment variables from .env file

## API Key

To get a Firecrawl API key:
1. Sign up at [Firecrawl](https://firecrawl.dev)
2. Generate an API key from your dashboard
3. Add it to your `.env` file as shown above

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Nafis Rayan