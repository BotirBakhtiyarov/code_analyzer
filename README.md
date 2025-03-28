# CodeAnalyzer 🔍

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AI-powered GitHub repository vulnerability scanner with DeepSeek integration.

## Features ✨

- Automated GitHub repository analysis
- Security vulnerability detection using AI
- Streaming summary generation
- Support for 15+ programming languages
- CLI interface with progress tracking

## Installation 📦

```bash
pip install code-analyzer
```

## Usage 🚀

1. First-time setup:
```bash
codeanalyzer setup
# Edit .env file with your DeepSeek API key
```

2. Analyze a repository:
```bash
codeanalyzer analyze https://github.com/username/repository
```

## Example Output 📄

```text
🔍 Starting analysis of https://github.com/example/repo
📁 Found 42 files to analyze
Analyzing Files: [████████████████████] 100% (42/42) [00:35]

📝 Final Summary:
Critical vulnerabilities found in 3 files:
- SQL injection risk in api_handler.py
- Hardcoded credentials in config_loader.py
- XSS vulnerability in template_engine.js

🔍 Detailed Findings:
File: src/api_handler.py
------------------------------------------------------------
Potential SQL injection vulnerability found in line 42...
```

## Configuration ⚙️

Create `.env` file:
```ini
DEEPSEEK_API_KEY=your_api_key_here
```

## Testing 🧪

```bash
pip install pytest
pytest tests/ -v
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a PR

## License 📄

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.
