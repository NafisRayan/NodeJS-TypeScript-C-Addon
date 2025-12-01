# pip install firecrawl-py

import os
from dotenv import load_dotenv
from firecrawl import Firecrawl

load_dotenv()

firecrawl = Firecrawl(api_key=os.getenv('FIRECRAWL_API_KEY'))

docs = firecrawl.crawl(url="https://nafisrayan.vercel.app", limit=10, scrape_options={'formats': ['markdown', 'html']})

for doc in docs.data:
    # Create filename from URL
    filename_base = doc.metadata.url.replace('https://', '').replace('http://', '').replace('/', '_').replace(':', '').replace('.', '_')
    
    # Save markdown
    if doc.markdown:
        with open(f"{filename_base}.md", 'w', encoding='utf-8') as f:
            f.write(doc.markdown)
        print(f"Saved markdown to {filename_base}.md")
    
    # Save html
    if doc.html:
        with open(f"{filename_base}.html", 'w', encoding='utf-8') as f:
            f.write(doc.html)
        print(f"Saved html to {filename_base}.html")