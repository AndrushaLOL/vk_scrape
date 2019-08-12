# Getting started
- ```pip install -r requirements.txt```
- Create .env file with:
    - LOGIN
    - PASSWORD
    - CLIENT_ID
    - APP_ID
    - CLIENT_SECRET
    - GRANT_TYPE
- ```python main.py```
<br>
**Messages will be saved in messages.json**
<br>
<br>
Example:
```python
[
    'username': [
        {
            'date': 1341920680,
            'from_id': 177311979,
            'id': 231,
            'out': 0,
            'peer_id': 177311979,
            'text': 'ну что как?',
            'conversation_message_id': 1,
            'fwd_messages': [],
            'important': False,
            'random_id': 0,
            'attachments': [],
            'is_hidden': False},
        },
        ...
    ],
    ...
]
```
