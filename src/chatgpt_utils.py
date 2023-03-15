import json
import openai
from src.colors import Colors


def load_prompts(prompts_path='./input/prompts.json'):
    """
    Load prompts from .json into list
    """

    with open(prompts_path, 'r') as f:
        content = f.read()
        prompts = json.loads(content)

    return prompts


def save_to_file(prompt,
                 answer,
                 output_file='./output/gpt_answers.json'):
    try:
        with open(output_file, 'r') as f:
            content = f.read()
            content = json.loads(content)

    except FileNotFoundError:
        content = []

    with open(output_file, 'w') as f:
        insertion = {
            'prompt': prompt,
            'answer': answer
        }

        content.append(insertion)
        f.write(json.dumps(content))


def gpt_answer(messages, 
               apply_context=True,
               model='gpt-3.5-turbo'):
    chat_completion = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    answer = chat_completion.choices[0].message.content

    if apply_context:
        messages.append(
            {'role': 'assistant', 'content': answer}
        )

        return answer, messages

    else:
        return answer


def gpt_from_file(apply_context=True,
                  output_terminal=False,
                  output_file=None,
                  model='gpt-3.5-turbo'):
    prompts = load_prompts()

    print(f'{Colors.HEADER}[PROCESS STARTED]{Colors.ENDC}')

    messages = [
        {
            'role': 'system',
            'content': 'GPT assistant'
        },
    ]

    for prompt in prompts:
        message = {'role': 'user', 'content': prompt}
        messages.append(message)

        # getting answer
        answer, messages = gpt_answer(
            messages=messages,
            apply_context=apply_context,
            model=model
        )

        if output_terminal:
            print('\n' + Colors.BOLD + '-'*80 + Colors.ENDC)

            print(f'{Colors.WARNING}[Question]{Colors.ENDC}')
            print(f'{Colors.OKBLUE}>> You:{Colors.ENDC}')
            print(prompt)

            print(f'\n{Colors.WARNING}[Answer]{Colors.ENDC}')
            print(f'{Colors.OKGREEN}>> GPT:{Colors.ENDC}')
            print(answer)
        
        if output_file:
            save_to_file(
                prompt=prompt,
                answer=answer,
                output_file=output_file
            )

        # if context is not applied,
        # messages is restarted
        if not apply_context:
            messages = [
                {
                    'role': 'system',
                    'content': 'GPT assistant'
                },
            ]
        
        continue

    print(f'\n{Colors.HEADER}[PROCESS FINISHED!]{Colors.ENDC}')


def gpt_interactive(apply_context=True,
                    output_terminal=True,
                    output_file=None,
                    model='gpt-3.5-turbo'):
    print(f'{Colors.HEADER}[PROCESS STARTED]{Colors.ENDC}')

    print(
        f'Press {Colors.WARNING}<q>{Colors.ENDC} or {Colors.WARNING}<quit>{Colors.ENDC} to exit'
    )

    messages = [
        {
            'role': 'system',
            'content': 'GPT assistant'
        },
    ]

    while True:
        print('\n' + Colors.BOLD + '-'*80 + Colors.ENDC)

        print(f'{Colors.WARNING}[Question]{Colors.ENDC}')
        prompt = input(f'{Colors.OKBLUE}>> You:{Colors.ENDC}\n')

        if prompt == 'q' or prompt == 'quit':
            print(f'\n{Colors.FAIL}Exiting...{Colors.ENDC}')
            break
        else:
            messages.append(
                {
                    'role': 'user',
                    'content': prompt
                },
            )

            # getting answer
            answer, messages = gpt_answer(
                messages=messages,
                apply_context=apply_context,
                mdel=model
            )

            print(f'\n{Colors.WARNING}[Answer]{Colors.ENDC}')
            print(f'{Colors.OKGREEN}>> GPT:{Colors.ENDC}')
            print(answer)

            if output_file:
                save_to_file(
                    prompt=prompt,
                    answer=answer,
                    output_file=output_file
                )

            # if context is not applied,
            # messages is restarted
            if apply_context == False:
                messages = [
                    {
                        'role': 'system',
                        'content': 'GPT assistant'
                    },
                ]
            
            continue

    print(f'\n{Colors.HEADER}[PROCESS FINISHED!]{Colors.ENDC}')
