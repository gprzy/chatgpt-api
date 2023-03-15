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

### Passing Input Prompts List and Output File
```bash
python3 chatgpt.py -c -f './input/prompts.json' -p -o './output/gpt_answers_context.json'
```

Where:
- `-i`: stands for interactive mode, similar to ChatGPT standar usage, but in terminal (*default* `False`);
- `-c`: stands for applying context to ChatGPT, in this case providing the prompts sequentially with the previous questions ans answers (*default* `False`);
- `-f`: stands for input file path with prompts list (*default* `None`);
- `-p`: stands for displaying information in the terminal (*default* `False`);
- `-o`: stands for outputh file path, containing the prompts and answers by ChatGPT (*default* `None`);

## Context managing

Consider the following prompts file `./input/prompts.json`:

```json
[
    "What is the speed of light?",
    "Now can you tell me the answer in miliseconds?",
    "What is the best option, the first one or the second?"
]
```

### With context
```bash
python3 chatgpt.py -c -f './input/prompts.json' -p -o './output/gpt_answers_context.json'
```

The output in `./output/gpt_answers_context.json` will be:

```json
[
    {
        "prompt": "What is the speed of light?",
        "answer": "The speed of light in a vacuum is approximately 299,792,458 meters per second (or about 186,282 miles per second). It is denoted by the symbol 'c' in scientific equations."
    },
    {
        "prompt": "Now can you tell me the answer in miliseconds?",
        "answer": "Sure! The speed of light in a vacuum is approximately 299,792,458 meters per second or 299,792,458,000 meters per millisecond (ms). Therefore, in milliseconds, the speed of light is equal to approximately 299,792.458 kilometers per millisecond."
    },
    {
        "prompt": "What is the best option, the first one or the second?",
        "answer": "I provided the same information in both responses, only with different units of measurement. The best option depends on what units you need to use in your specific situation. If you need a more precise answer, it might be better to use meters per second, but if you need a more practical measure, kilometers per millisecond might be more useful."
    }
]
```

### Without context
```bash
python3 chatgpt.py -f './input/prompts.json' -p -o './output/gpt_answers_no_context.json'
```

The output in `./output/gpt_answers_no_context.json` will be:

```json
[
    {
        "prompt": "What is the speed of light?",
        "answer": "The speed of light is approximately 299,792,458 meters per second (or about 186,282 miles per second). It is considered a fundamental constant of nature and is denoted by the symbol \"c\"."
    },
    {
        "prompt": "Now can you tell me the answer in miliseconds?",
        "answer": "One millisecond (ms) is equivalent to 1/1000th of a second. If we want to convert a larger unit of time, such as seconds or minutes, to milliseconds, we would simply multiply by 1000. For example, one second is equivalent to 1000 milliseconds (1 x 1000) and one minute is equivalent to 60,000 milliseconds (60 x 1000). So, I need to know what unit of time you want me to convert to milliseconds."
    },
    {
        "prompt": "What is the best option, the first one or the second?",
        "answer": "Without any context or information about what the options are, it is impossible for me to determine which one is the best. Can you please provide more information or details about the options you are referring to?"
    }
]
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
curl -X POST -H "Content-Type: application/json" -d '[{"role": "user", "content": "What is the speed of light?"}]' http://localhost:5000/chatgpt
```