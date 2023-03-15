import json
import openai


def load_prompts(prompts_path='./input/prompts.json'):
    """
    Load prompts from .json into list
    """

    with open(prompts_path, 'r') as f:
        content = f.read()
        loaded_prompts = json.loads(content)

    prompts = []
    for prompt in loaded_prompts:
        prompts.append(
            {
                'role': 'user',
                'content': prompt
            },
        )

    return prompts


def save_to_file(output_file='./output/gpt_answers.json'):
    with open(output_file, 'w') as f:
        pass


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
            {
                'role': 'assistant',
                'content': answer
            }
        )

        return answer, messages

    else:
        return answer


def gpt_from_file(apply_context=True,
                  output_terminal=False):
    prompts = load_prompts()

    print('[PROCESS STARTED]')

    messages = [
        {
            'role': 'system',
            'content': 'GPT assistant'
        },
    ]

    for prompt in prompts:
        # getting answer
        answer, messages = gpt_answer(
            messages=messages,
            apply_context=apply_context
        )

        if output_terminal:
            print('\n' + '-'*80)

            print(f'[Question]')
            print(f'>> You:')
            print(prompt)

            print(f'\n[Answer]')
            print(f'>> GPT:')
            print(answer)
        else:
            pass

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

    print('\n[PROCESS FINISHED!]')


def gpt_interactive(apply_context=True,
                    output_file=None):
    print('[PROCESS STARTED]')
    print('Press <q> or <quit> to exit')

    messages = [
        {
            'role': 'system',
            'content': 'GPT assistant'
        },
    ]

    while True:
        print('\n' + '-'*80)

        print(f'[Question]')
        prompt = input('>> You:\n')

        if prompt == 'q' or prompt == 'quit':
            print('\nExiting...')
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
                apply_context=apply_context
            )

            print(f'\n[Answer]')
            print(f'>> GPT:')
            print(answer)

            if output_file:
                pass

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

    print('\n[PROCESS FINISHED!]')
