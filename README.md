# Streamlit app

## Run locally

With the project virtual environment activated, install Streamlit and start the app:

```sh
python -m pip install 'streamlit>=1.40,<2'
streamlit run app.py
```

Or install the project dependency with [uv](https://docs.astral.sh/uv/):

```sh
uv sync
uv run streamlit run app.py
```

Streamlit will print a local URL in the terminal. Edit `app.py` to build your app.
