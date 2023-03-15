# ChatGPT API Integration
💬 An API integration for ChatGPT, accepting input files with prompts and personalized configurations.

## Script Usage

### Interactive ChatGPT on Terminal
```bash
python3 chatgpt.py -i -p
```

### Passing Input Prompts List from `prompts.json`
```bash
python3 chatgpt.py -f './input/prompts.json' -p
```

### Passing Input Prompts List and Output File `gpt_answers.json`
```bash
python3 chatgpt.py -f './input/prompts.json' -p -o './output/gpt_answers.json'
```

## API Usage

### Running on Localhost
```bash
python3 app.py
```

### Health Check
```bash
curl http://localhost:5000/health
```

The response will be:
```text
{
  "status": "Alive!"
}
```

### Making a POST
```bash
curl -X POST -H "Content-Type: application/json" -d '{"role": "user", "content": "What is the speed of light?"}' http://localhost:5000/posts
```