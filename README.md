# Learning Repository

A comprehensive collection of Node.js, Python, and TypeScript learning projects demonstrating various concepts, from asynchronous programming and web development to native C++ addons, PDF manipulation, REST APIs, and more.

## 📚 Repository Overview

This repository serves as a learning hub for full-stack development, containing multiple projects that showcase different aspects of JavaScript, Node.js, Python, and TypeScript ecosystems:

1. **[Event Loop Visualizer](./Event%20Loop,%20Web%20APIs,%20(Micro)task%20Queue/)** - Interactive visualization of Node.js event loop mechanics
2. **[Express Chat App](./initial/)** - Simple real-time chat application using Express.js
3. **[Image Converter Addon](./Node.js%20C%20Addon%20(image%20convertion)/)** - High-performance image processing with native C++ addon
4. **[Excel File Generator](./Excel%20File%20Generator/)** - Excel file generation with custom formatting using ExcelJS
5. **[Fire Crawl Python R&D](./Fire%20Crawl%20Python%20R&D/)** - Python web scraping using Firecrawl API
6. **[PDF Form Fillup](./Node.js%20PDF%20Form%20Fillup/)** - Automated PDF form filling for investor registrations
7. **[PDF Form Generation](./PDF%20Form%20Generation/)** - Professional fund document generation (COUA letters, Portfolio Statements)
8. **[PDF Position Finder](./PDF%20Position%20Finder/)** - Interactive tool for finding coordinates on PDFs
9. **[REST Convention](./REST%20Convention/)** - Task tracker dashboard demonstrating REST API concepts
10. **[TinyURL RnD](./TinyURL%20RnD/)** - TypeScript URL shortener using TinyURL API

Each project includes detailed documentation, setup instructions, and comprehensive explanations of the underlying concepts.

## 🎯 Learning Objectives

This repository covers:
- **Asynchronous Programming**: Event loops, callbacks, promises, and microtasks
- **Web Development**: REST APIs, middleware, static file serving, full-stack applications
- **Native Addons**: C++ integration with Node.js using N-API, performance optimization
- **Image Processing**: Low-level pixel manipulation, format conversion, image embedding
- **PDF Manipulation**: Form filling, document generation, coordinate-based positioning
- **Data Processing**: Excel file generation, web scraping, URL shortening
- **Database Integration**: JSON files, SQLite databases
- **API Integration**: Third-party APIs (Firecrawl, TinyURL)
- **Build Systems**: node-gyp, TypeScript compilation
- **Frontend Technologies**: Vanilla JavaScript, HTML5, CSS3, Tailwind CSS, Chart.js

## 📁 Project Structure

```
Learning/
├── Event Loop, Web APIs, (Micro)task Queue/
│   ├── server.js                 # Express server for visualization
│   ├── public/
│   │   ├── index.html           # Interactive UI
│   │   └── script.js            # Event loop simulation
│   ├── test/
│   │   └── server.test.js       # Server tests
│   ├── package.json
│   └── README.md                # Detailed project docs
│
├── initial/
│   ├── app.js                   # Chat server
│   ├── messages.json            # JSON database
│   ├── public/
│   │   ├── index.html          # Chat interface
│   │   ├── style.css           # Styling
│   │   └── app.js              # Frontend logic
│   ├── package.json
│   └── README.md               # Detailed project docs
│
├── Node.js C++ Addon (image convertion)/
│   ├── index.js                 # Express server
│   ├── src/
│   │   └── addon.cc            # C++ addon source
│   ├── public/
│   │   └── index.html          # Image converter UI
│   ├── binding.gyp             # Build configuration
│   ├── TECHNICAL_DOCUMENTATION.md # In-depth technical docs
│   ├── package.json
│   └── README.md               # Detailed project docs
│
├── Excel File Generator/
│   ├── app.js                   # Excel generation script
│   ├── package.json
│   └── README.md               # Project documentation
│
├── Fire Crawl Python R&D/
│   ├── fc.py                    # Python scraping script
│   ├── scraped_data/            # Output directory
│   └── README.md               # Project documentation
│
├── Node.js PDF Form Fillup/
│   ├── index.js                 # Main application
│   ├── index-institution.js     # Institution form handler
│   ├── SASF-Individual-form.js  # Individual form service
│   ├── SASF-Institution-form.js # Institution form service
│   ├── PDF_Image_Converter.html # Image converter tool
│   ├── PDF_Paint_Editor_Tailwind.html # Paint editor
│   ├── PDF_PositionFinder.html  # Position finder tool
│   ├── package.json
│   └── README.md               # Detailed project docs
│
├── PDF Form Generation/
│   ├── index.js                 # Main generator
│   ├── index-investment-certificate.js # Certificate generator
│   ├── index-portfolio-statement.js    # Portfolio generator
│   ├── index-coua-letter.js     # COUA letter generator
│   ├── pdf-common-utils.js      # Shared utilities
│   ├── coua-letter/
│   │   ├── coua-letter-pdf-utils.js
│   │   └── coua-letter-service.js
│   ├── investment-certificate/
│   │   ├── investment-certificate-pdf-utils.js
│   │   └── investment-certificate-service.js
│   ├── portfolio-statement/
│   │   ├── portfolio-statement-pdf-utils.js
│   │   └── portfolio-statement-service.js
│   ├── templates/               # PDF templates
│   ├── package.json
│   └── README.md               # Detailed project docs
│
├── PDF Position Finder/
│   └── PDF_PositionFinder.html  # Interactive coordinate finder
│
├── REST Convention/
│   ├── server.js                # REST API server
│   ├── database.js              # SQLite database setup
│   ├── public/
│   │   ├── index.html          # Dashboard UI
│   │   └── app.js              # Frontend logic
│   ├── package.json
│   └── README.md               # Project documentation
│
└── TinyURL RnD/
    ├── src/
    │   └── index.ts            # TypeScript source
    ├── package.json
    ├── tsconfig.json           # TypeScript config
    └── README.md               # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- **Node.js** (v14+ recommended for most projects, v18+ for some)
- **npm** (comes with Node.js)
- **Python 3.7+** (for Fire Crawl project)
- **TypeScript** (for TinyURL project, install globally: `npm install -g typescript`)
- **SQLite** (for REST Convention project)
- **Python 3.11** (for C++ addon building on Windows)
- **Visual Studio Build Tools** (for C++ compilation on Windows)

### Setup All Projects

```bash
# Clone the repository
git clone https://github.com/NafisRayan/Learning.git
cd Learning

# Each project has its own setup - see individual READMEs
```

## 📖 Projects in Detail

### 1. Event Loop Visualizer

**Location**: [`Event Loop, Web APIs, (Micro)task Queue/`](./Event%20Loop,%20Web%20APIs,%20(Micro)task%20Queue/)

**What it teaches**:
- Node.js event loop architecture
- Task queues (macrotasks vs microtasks)
- Asynchronous execution order
- Visual debugging of async code

**Key Features**:
- Real-time event loop simulation
- Interactive task addition (sync, async, microtasks)
- Visual queue management
- Console logging with timestamps
- Educational explanations

**Tech Stack**: Node.js, Express.js, Vanilla JavaScript, Tailwind CSS

**Setup**:
```bash
cd "Event Loop, Web APIs, (Micro)task Queue"
npm install
npm start
# Visit http://localhost:3000
```

### 2. Express Chat App

**Location**: [`initial/`](./initial/)

**What it teaches**:
- RESTful API design
- Express.js middleware
- JSON file-based database
- Frontend-backend communication
- Real-time UI updates

**Key Features**:
- User messaging system
- Auto-refreshing chat interface
- JSON data persistence
- Input validation
- Responsive design

**Tech Stack**: Node.js, Express.js, Vanilla JavaScript, HTML5, CSS3

**Setup**:
```bash
cd initial
npm install
npm start
# Visit http://localhost:3000
```

### 3. Image Converter Addon

**Location**: [`Node.js C++ Addon (image convertion)/`](./Node.js%20C%20Addon%20(image%20convertion)/)

**What it teaches**:
- Native C++ addons with N-API
- Cross-language performance optimization
- Image processing algorithms
- Memory management in native code
- Build systems (node-gyp)

**Key Features**:
- Bidirectional image conversion
- High-performance C++ processing
- Drag-and-drop file upload
- JSON data export/import
- Real-time image generation

**Tech Stack**: Node.js, C++, N-API, stb_image, Express.js, Tailwind CSS

**Setup** (Windows):
```bash
cd "Node.js C++ Addon (image convertion)"
npm install
npm run build
npm start
# Visit http://localhost:3000
```

### 4. Excel File Generator

**Location**: [`Excel File Generator/`](./Excel%20File%20Generator/)

**What it teaches**:
- Excel file creation and manipulation
- XML manipulation in Excel files
- Text formatting with quotePrefix
- Working with ExcelJS library

**Key Features**:
- Generates Excel files with bank data
- Applies text formatting to prevent number conversion
- Modifies Excel XML for proper display
- Uses JSZip for archive manipulation

**Tech Stack**: Node.js, ExcelJS, JSZip, fast-xml-parser

**Setup**:
```bash
cd "Excel File Generator"
npm install
node app.js
# Output.xlsx will be generated
```

### 5. Fire Crawl Python R&D

**Location**: [`Fire Crawl Python R&D/`](./Fire%20Crawl%20Python%20R&D/)

**What it teaches**:
- Python web scraping
- API integration with Firecrawl
- Data extraction and storage
- Environment variable configuration

**Key Features**:
- Crawls websites using Firecrawl API
- Saves content in Markdown and HTML formats
- Organizes output in structured folders
- Configurable via .env files

**Tech Stack**: Python, Firecrawl API, python-dotenv

**Setup**:
```bash
cd "Fire Crawl Python R&D"
python -m venv venv
# Activate venv (Windows: .\venv\Scripts\Activate.ps1)
pip install firecrawl-py python-dotenv
# Set FIRECRAWL_API_KEY in .env
python fc.py
```

### 6. PDF Form Fillup

**Location**: [`Node.js PDF Form Fillup/`](./Node.js%20PDF%20Form%20Fillup/)

**What it teaches**:
- PDF manipulation with pdf-lib
- Coordinate-based text positioning
- Image embedding in PDFs
- Form automation for business processes

**Key Features**:
- Supports individual and institutional investor forms
- Precise text placement using coordinates
- Image embedding for photos/signatures
- Multi-page form handling

**Tech Stack**: Node.js, pdf-lib, sharp

**Setup**:
```bash
cd "Node.js PDF Form Fillup"
npm install
node index.js
# Or node index-institution.js for institutional forms
```

### 7. PDF Form Generation

**Location**: [`PDF Form Generation/`](./PDF%20Form%20Generation/)

**What it teaches**:
- Professional document generation
- Advanced PDF creation with tables and images
- Font mixing and text alignment
- Modular PDF service architecture

**Key Features**:
- Generates COUA letters and Portfolio Statements
- Company branding with logos
- Flexible table generation
- Multi-line justified text

**Tech Stack**: Node.js, pdf-lib

**Setup**:
```bash
cd "PDF Form Generation"
npm install
npm start  # For COUA letter
npm run portfolio  # For portfolio statement
```

### 8. PDF Position Finder

**Location**: [`PDF Position Finder/`](./PDF%20Position%20Finder/)

**What it teaches**:
- Interactive PDF coordinate detection
- Frontend development with Tailwind CSS
- PDF.js integration for rendering
- Mouse event handling for coordinate capture

**Key Features**:
- Interactive PDF viewer
- Real-time coordinate display
- Click-to-copy functionality
- Supports multiple PDF pages

**Tech Stack**: HTML, JavaScript, Tailwind CSS, PDF.js

**Setup**:
```bash
# Open PDF_PositionFinder.html in a web browser
```

### 9. REST Convention

**Location**: [`REST Convention/`](./REST%20Convention/)

**What it teaches**:
- RESTful API design principles
- CRUD operations implementation
- SQLite database integration
- Frontend-backend communication

**Key Features**:
- Full CRUD task management
- Interactive dashboard with charts
- Request logging and statistics
- Real-time UI updates

**Tech Stack**: Node.js, Express.js, SQLite, Chart.js, Tailwind CSS

**Setup**:
```bash
cd "REST Convention"
npm install
npm start
# Visit http://localhost:3000
```

### 10. TinyURL RnD

**Location**: [`TinyURL RnD/`](./TinyURL%20RnD/)

**What it teaches**:
- TypeScript development
- API integration with TinyURL
- Command-line interface development
- User input handling

**Key Features**:
- URL shortening via TinyURL API
- Interactive terminal interface
- Command-line argument support
- TypeScript compilation

**Tech Stack**: TypeScript, Node.js, node-fetch

**Setup**:
```bash
cd "TinyURL RnD"
npm install
npm run build
npm start
```

## 🛠️ Development Environment

### Recommended Tools

- **VS Code** with extensions:
  - JavaScript/TypeScript support
  - C/C++ extension (for addon development)
  - Node.js debugger
- **Git** for version control
- **Postman** for API testing

### Testing

Each project includes different testing approaches:
- **Event Loop**: Jest for server testing
- **Chat App**: Manual testing (could be extended)
- **Image Converter**: Manual testing with various image formats
- **Excel Generator**: Manual verification of output files
- **Fire Crawl**: Manual testing with different websites
- **PDF Projects**: Manual verification of generated PDFs
- **REST Convention**: Manual API testing with Postman
- **TinyURL**: Manual testing with various URLs

## 📚 Learning Path

Suggested order to explore the projects:

1. **Start with Express Chat App** - Learn basic Node.js web development
2. **Move to REST Convention** - Understand REST API design and database integration
3. **Explore Event Loop Visualizer** - Understand asynchronous programming deeply
4. **Try TinyURL RnD** - Learn TypeScript and API integration
5. **Advance to Excel File Generator** - Explore data processing and file manipulation
6. **Work with PDF Position Finder** - Learn PDF manipulation basics
7. **Build on PDF Form Fillup** - Advanced PDF form automation
8. **Create with PDF Form Generation** - Professional document generation
9. **Experiment with Fire Crawl Python R&D** - Python web scraping
10. **Advance to Image Converter Addon** - Explore native performance optimization

Each project builds upon the previous concepts while introducing new challenges and technologies.
