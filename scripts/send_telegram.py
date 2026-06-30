"""Send Horizon daily summaries to Telegram as documents (HTML format with working TOC links)."""

import asyncio
import os
import sys
from pathlib import Path
from datetime import datetime

import httpx
import markdown
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
SUMMARIES_DIR = Path("data/summaries")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; color: #333; }}
  h1 {{ border-bottom: 2px solid #eee; padding-bottom: 10px; }}
  h2 {{ margin-top: 2em; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
  a {{ color: #0066cc; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  blockquote {{ border-left: 4px solid #ddd; margin: 0; padding: 0.5em 1em; color: #666; background: #f9f9f9; }}
  details {{ margin: 0.5em 0; padding: 0.5em; background: #f5f5f5; border-radius: 4px; }}
  summary {{ cursor: pointer; font-weight: bold; }}
  ol {{ padding-left: 1.5em; }}
  ol li {{ margin: 0.3em 0; }}
  hr {{ border: none; border-top: 1px solid #eee; margin: 2em 0; }}
</style>
</head>
<body>
{content}
</body>
</html>"""


def md_to_html(md_text: str, lang: str, title: str) -> str:
    """Convert markdown to full HTML page."""
    html_content = markdown.markdown(
        md_text,
        extensions=["extra", "toc"],
        output_format="html5",
    )
    return HTML_TEMPLATE.format(lang=lang, title=title, content=html_content)


async def send_document(client: httpx.AsyncClient, file_bytes: bytes, filename: str, caption: str) -> bool:
    """Send a file as a Telegram document."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    files = {"document": (filename, file_bytes, "text/html")}
    data = {
        "chat_id": CHAT_ID,
        "caption": caption,
    }
    resp = await client.post(url, data=data, files=files)

    if resp.status_code == 200 and resp.json().get("ok"):
        print(f"  ✅ Sent: {filename}")
        return True
    else:
        print(f"  ❌ Failed: {filename} — {resp.text}")
        return False


async def main():
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set in .env")
        sys.exit(1)

    # Determine date (use argument or today)
    if len(sys.argv) > 1:
        date_str = sys.argv[1]
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")

    lang_names = {"en": "🇬🇧 English", "zh": "🇨🇳 中文", "ja": "🇯🇵 日本語"}
    files_to_send = []

    for lang, name in lang_names.items():
        file_path = SUMMARIES_DIR / f"horizon-{date_str}-{lang}.md"
        if file_path.exists():
            md_text = file_path.read_text(encoding="utf-8")
            title = f"Horizon Daily - {date_str} ({name})"
            html_bytes = md_to_html(md_text, lang, title).encode("utf-8")
            filename = f"horizon-{date_str}-{lang}.html"
            caption = f"📡 Horizon Daily | {date_str}\n{name}"
            files_to_send.append((html_bytes, filename, caption))

    if not files_to_send:
        print(f"No summaries found for {date_str} in {SUMMARIES_DIR}")
        sys.exit(1)

    print(f"Sending {len(files_to_send)} summary file(s) to Telegram...")

    async with httpx.AsyncClient(timeout=60) as client:
        for html_bytes, filename, caption in files_to_send:
            await send_document(client, html_bytes, filename, caption)

    print("Done!")


if __name__ == "__main__":
    asyncio.run(main())
