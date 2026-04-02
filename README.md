# Markdown Note-Taking App

A simple web application built with FastAPI for managing markdown notes. Users can upload markdown files, check grammar, save notes, list saved notes, and render them as HTML.

## Features

- **File Upload**: Upload markdown files via REST API
- **Grammar Check**: Check grammar of notes using LanguageTool
- **Save Notes**: Save markdown text as notes
- **List Notes**: Retrieve a list of saved notes
- **Render HTML**: Convert markdown to HTML for display

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **Markdown**: Python library for parsing and rendering markdown
- **LanguageTool**: Grammar and spell checking tool
- **Uvicorn**: ASGI server for running the FastAPI app

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd markdown-note-taking-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py --port 8000
   ```

2. The API will be available at `http://localhost:8000`

## API Endpoints

- `POST /uploadfile/`: Upload a markdown file
- `POST /check-grammar/`: Check grammar of a note (text input)
- `POST /save-note/`: Save a note (markdown text)
- `GET /list-notes/`: List all saved notes
- `GET /render-note/{filename}`: Render a note as HTML

## Project Structure

```
.
├── main.py              # Entry point to run the server
├── Mark_down.py         # FastAPI application with endpoints
└── requirements.txt     # Python dependencies
```

## Contributing

Feel free to submit issues and pull requests to improve the application.

## License

This project is open source and available under the [MIT License](LICENSE).
