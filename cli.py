#!/usr/bin/env python3
import os
import subprocess
import json
import datetime
import click
import yaml
import openai

@click.group()
def cli():
    pass

# --- twoje istniejące komendy (nowy-projekt, podsumuj-etap, itd.) ---
# tu wklej cały kod dotychczasowych komend
# …

# ==== nasz nowy blok AI ====
@cli.command()
@click.argument('prompt')
def ai(prompt):
    """Wygeneruj kod z ChatGPT na podstawie prompta."""
    openai.api_key = os.getenv('OPENAI_API_KEY')
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content": prompt}]
    )
    click.echo(resp.choices[0].message.content)

if __name__ == "__main__":
    cli()
