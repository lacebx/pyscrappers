# pyscrappers — Python Web Scraping Templates

Built this because I got tired of rewriting the same Selenium boilerplate every time I needed to pull data off a website. `pyscrappers` is a growing collection of reusable Python scraping templates — drop in your URL and CSS selectors, and walk away with a CSV.

The idea is simple: scraping the web follows the same pattern almost every time. You load a page, wait for elements to appear, loop through them, extract what you need, and dump it somewhere useful. This repo captures that pattern so you don't have to reinvent it.

> *Birarenze* — the best tools are the ones you built yourself.

---

## What's Inside

### `text_scrapper.py`
A Selenium-powered text scraper that:
- Launches Chrome via WebDriver
- Navigates to a target URL
- Waits for dynamic content to load using `WebDriverWait`
- Scrolls elements into view before extracting
- Collects text content via CSS selectors
- Exports everything to a `.csv` file

It's intentionally generic. Swap in your site URL and selectors and it just works.

---

## Setup

```bash
pip install selenium
```

You'll also need:
- [ChromeDriver](https://chromedriver.chromium.org/) matching your Chrome version
- Add `chromedriver` to your system PATH

---

## Usage

Open `text_scrapper.py` and replace the placeholder values:

```python
driver.get('siteURL')                  # ← Your target URL
'.container of what you want to scrape' # ← CSS selector for your element container
'actual text/thing you want to scrape'  # ← CSS selector for the text element
```

Then run:
```bash
python text_scrapper.py
```

Output: `yourthings.csv` in the same directory.

---

## Tech Stack

- **Language:** Python 3
- **Automation:** Selenium WebDriver
- **Export:** Python `csv` module
- **Browser:** Chrome (headless-compatible)

---

## What's Coming

This is meant to be a library of templates. Future additions:
- `image_scrapper.py` — download images from a page
- `table_scrapper.py` — extract HTML tables to CSV/JSON
- `pagination_scrapper.py` — handle multi-page sites
- `auth_scrapper.py` — scrape behind login walls

Pull requests welcome if you've got a pattern worth adding.
