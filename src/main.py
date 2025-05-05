from nicegui import ui
import json
import os
from services import EchoService

# Load configuration
def load_config():
    config_path = 'config.json'
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return {"theme": "light"}

def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

# Initialize configuration
config = load_config()

# Initialize chat services
chat_services = {
    'echo': EchoService()
}

# Initialize the UI
ui.add_head_html('''
    <style>
        .chat-container {
            height: calc(100vh - 200px);
            overflow-y: auto;
            padding: 1rem;
            transition: background-color 0.3s;
            display: flex;
            flex-direction: column;
            gap: 1rem;
            width: 100%;
        }
        .message-row {
            display: flex;
            width: 100%;
        }
        .message {
            padding: 1rem;
            border-radius: 0.5rem;
            transition: background-color 0.3s, color 0.3s;
            max-width: 80%;
            width: fit-content;
            word-break: break-word;
        }
        .user-message {
            background-color: #f0f0f0;
            margin-left: auto;
            margin-right: 0;
        }
        .assistant-message {
            background-color: #e3f2fd;
            margin-left: 0;
            margin-right: auto;
        }
        .input-container {
            position: fixed;
            bottom: 0;
            width: 100%;
            padding: 1rem;
            border-top: 1px solid #e0e0e0;
            transition: background-color 0.3s, border-color 0.3s;
        }
        .dark .user-message {
            background-color: #2d2d2d;
        }
        .dark .assistant-message {
            background-color: #1a3a4a;
        }
        .dark .input-container {
            border-top: 1px solid #333;
        }
    </style>
''')

# Theme management
def toggle_theme(e):
    global config
    config['theme'] = 'dark' if e.value else 'light'
    save_config(config)
    ui.dark_mode(e.value)

# Set initial theme
ui.dark_mode(config['theme'] == 'dark')

# Chat management
messages = []
current_service = 'echo'

async def send_message():
    input_text = input_textarea.value
    if not input_text.strip():
        return
    # Add user message
    messages.append({'role': 'user', 'content': input_text})
    render_messages()
    input_textarea.value = ''
    # Get response from current service
    service = chat_services[current_service]
    response = await service.send_message(input_text)
    # Add assistant message
    messages.append({'role': 'assistant', 'content': response})
    render_messages()

def render_messages():
    messages_container.clear()
    for msg in messages:
        with messages_container:
            if msg['role'] == 'user':
                ui.html(f'<div class="message-row" style="justify-content: flex-end;"><div class="message user-message">{msg["content"]}</div></div>')
            else:
                ui.html(f'<div class="message-row" style="justify-content: flex-start;"><div class="message assistant-message">{msg["content"]}</div></div>')

# Create the main layout
with ui.column().classes('w-full h-screen'):
    # Create tabs
    with ui.tabs().classes('w-full') as tabs:
        chat_tab = ui.tab('Chat')
        settings_tab = ui.tab('Settings')
    
    with ui.tab_panels(tabs, value=chat_tab).classes('w-full h-full'):
        # Chat tab
        with ui.tab_panel(chat_tab):
            with ui.card().classes('w-full h-full'):
                # Service selection
                with ui.row().classes('w-full p-2 gap-2 items-center'):
                    ui.label('Service:')
                    service_select = ui.select(
                        {key: service.description for key, service in chat_services.items()},
                        value=current_service,
                        on_change=lambda e: setattr(globals(), 'current_service', e.value)
                    ).classes('w-64')
                # Chat messages container
                messages_container = ui.element('div').classes('chat-container')
                # Input container
                with ui.column().classes('input-container'):
                    with ui.row().classes('w-full items-center gap-2'):
                        input_textarea = ui.textarea(placeholder='Type your message...').classes('w-full').props('outlined')
                        ui.button('Send', icon='send', on_click=send_message).classes('h-full')
        # Settings tab
        with ui.tab_panel(settings_tab):
            with ui.card().classes('w-full h-full'):
                with ui.column().classes('gap-4 p-4'):
                    ui.label('Appearance').classes('text-lg font-bold')
                    with ui.row().classes('items-center gap-2'):
                        ui.label('Theme:')
                        theme_switch = ui.switch(value=config['theme'] == 'dark', on_change=toggle_theme).props('color=primary')
                        ui.label('Dark Mode')

# Run the application
ui.run(title='ChatGPT-like Chat', favicon='🤖') 