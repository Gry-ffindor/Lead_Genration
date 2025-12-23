# Lead Generation Agent

An AI-powered lead generation agent built with LangGraph that automates the process of finding, qualifying, and pitching to potential business leads. This agent uses zero-cost APIs and open-source tools to create a complete lead generation pipeline.

## Features

- **Intelligent Search**: Uses DuckDuckGo to find companies based on industry, location, and other criteria
- **Web Scraping**: Automatically scrapes company websites for detailed information
- **Lead Filtering**: AI-powered filtering to qualify leads based on your criteria
- **Email Discovery**: Finds contact emails for qualified leads
- **Automated Pitching**: Generates personalized sales pitches using LLM
- **Zero Cost**: Uses free APIs (Groq, DuckDuckGo) and open-source tools

## Architecture

The agent uses LangGraph to orchestrate a multi-step workflow:

1. **Search Node**: Constructs search queries and finds potential companies
2. **Scrape Node**: Extracts detailed information from company websites
3. **Filter Node**: Qualifies leads based on your specified criteria
4. **Email Node**: Discovers contact information
5. **Write Node**: Generates personalized sales pitches

## Installation

### Prerequisites
- Python 3.9+
- Git

### Setup Steps

1. **Clone and navigate to the project**:
   ```bash
   cd lead-generation-agent
   ```

2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -e .
   ```

4. **Install Playwright browsers**:
   ```bash
   playwright install chromium
   ```

5. **Configure API keys**:
   - Get a free API key from [Groq Console](https://console.groq.com/keys)
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

6. **Verify setup**:
   ```bash
   python test_setup.py
   ```

## Usage

### Command Line Interface

Run the main script to start the lead generation process:

```bash
python main.py
```

You'll be prompted to enter:
- Industry type (e.g., Gaming, Fintech)
- Territory/Location (e.g., India, US)
- Firm size (optional)
- Tech stack (optional)
- Pain points (optional)
- Maximum number of results

### API Interface

The agent also includes a FastAPI-based REST API for programmatic access:

```bash
python api.py
```

The API will be available at `http://localhost:8000`

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
GROQ_API_KEY=your_groq_api_key
LANGSMITH_API_KEY=your_langsmith_key  # Optional, for graph visualization
```

### Lead Criteria

The agent accepts various criteria to filter leads:
- **Industry**: Primary industry sector
- **Territory**: Geographic location
- **Firm Size**: Company size category
- **Tech Stack**: Technologies used
- **Pain Points**: Business challenges to address

## Project Structure

```
lead-generation-agent/
├── src/
│   ├── graph/
│   │   ├── state.py          # State definitions
│   │   ├── workflow.py       # LangGraph workflow
│   │   └── nodes/            # Individual workflow nodes
│   ├── tools/                # Utility tools
│   └── utils/                # Helper functions
├── config/                   # Configuration files
├── data/                     # Data storage
├── tests/                    # Test files
├── main.py                   # CLI entry point
├── api.py                    # FastAPI server
├── pyproject.toml           # Project dependencies
├── setup_guide.md           # Detailed setup instructions
└── README.md                # This file
```

## Dependencies

Key dependencies include:
- **LangGraph**: Workflow orchestration
- **LangChain**: LLM integration
- **Groq**: Free LLM API
- **DuckDuckGo Search**: Web search
- **Playwright**: Web scraping
- **BeautifulSoup4**: HTML parsing
- **FastAPI**: REST API framework

## Development

### Running Tests

```bash
pytest tests/
```

### Adding New Nodes

1. Create a new node function in `src/graph/nodes/`
2. Add the node to the workflow in `workflow.py`
3. Update the state in `state.py` if needed

### Customization

The agent can be customized by:
- Modifying search queries in `search_node.py`
- Adjusting filtering criteria in `filter_node.py`
- Customizing pitch templates in `write_node.py`

## Troubleshooting

### Common Issues

1. **Browser installation failed**: Run `playwright install chromium` again
2. **API key errors**: Verify your Groq API key in `.env`
3. **Import errors**: Ensure you're in the virtual environment and dependencies are installed

### Debug Mode

Set the `DEBUG` environment variable to get detailed logs:

```bash
DEBUG=1 python main.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for educational and legitimate business purposes only. Always respect website terms of service and privacy laws when scraping data. The authors are not responsible for misuse of this tool.