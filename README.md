# CrewAI_RAG

## Overview
This project sets up an AI-driven workflow using CrewAI, which orchestrates multiple AI agents to process PDF documents and generate summaries. The project utilizes OpenAI's GPT models to perform different tasks.

## Features
- **PDF Analysis**: Extracts information from a specified PDF file.
- **Summary Generation**: Writes a concise summary based on the extracted information.
- **Multiple AI Agents**: Uses different GPT models to handle specific tasks.
- **CrewAI Framework**: Defines AI agents and tasks in a structured workflow.

## Installation
### Prerequisites
- Python 3.8+
- Required dependencies installed via pip

### Setup
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables (Optional):
   ```sh
   export OPENAI_API_KEY="your_openai_api_key"
   ```

## Project Structure
```
├── custom_agents.py    # Defines AI agents
├── tasks.py            # Defines tasks for agents
├── main.py             # Entry point for running the crew
├── requirements.txt    # Required dependencies
└── README.md           # Documentation
```

## How It Works
1. **Agent Setup**
   - `pdf_agent`: Extracts information from the PDF file.
   - `writer_agent`: Summarizes the extracted information.
2. **Task Execution**
   - `pdf_task`: Uses `pdf_agent` to analyze a PDF.
   - `writer_task`: Uses `writer_agent` to generate a summary.
3. **Crew Execution**
   - The `CustomCrew` class orchestrates the execution of agents and tasks.
   - The result is printed after execution.

## Running the Project
To start the AI crew, run:
```sh
python main.py
```
You will be prompted to enter a variable for processing.

## Troubleshooting
- Ensure the API key is valid and set correctly.
- Check that all dependencies are installed.
- Verify the PDF file exists in the expected path.

## Future Enhancements
- Add more agents for different document types.
- Improve summarization techniques.
- Integrate with a database for storing results.

