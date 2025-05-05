from nicegui import ui
import json
import os

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

# Initialize the UI
ui.add_head_html('''
    <style>
        .chat-container {
            height: calc(100vh - 200px);
            overflow-y: auto;
            padding: 1rem;
            transition: background-color 0.3s;
        }

        .message {
            margin-bottom: 1rem;
            padding: 1rem;
            border-radius: 0.5rem;
            transition: background-color 0.3s, color 0.3s;
        }

        .user-message {
            background-color: #f0f0f0;
            margin-left: auto;
            max-width: 80%;
        }

        .assistant-message {
            background-color: #e3f2fd;
            margin-right: auto;
            max-width: 80%;
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
                # Chat messages container
                with ui.column().classes('chat-container w-full'):
                    # Messages will be added here dynamically
                    pass
                
                # Input container
                with ui.column().classes('input-container'):
                    with ui.row().classes('w-full items-center gap-2'):
                        ui.textarea(placeholder='Type your message...').classes('w-full').props('outlined')
                        ui.button('Send', icon='send').classes('h-full')

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