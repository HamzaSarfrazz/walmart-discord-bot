import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import config
import time

# Define Discord Intents
intents = discord.Intents.default()
intents.message_content = True

# Set up the bot
bot = commands.Bot(command_prefix='/', intents=intents)

# Walmart search function using Selenium
def search_walmart_inventory(upc, zip_code):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    url = f"https://www.walmart.com/search?q={upc}&zip={zip_code}"
    
    try:
        driver.get(url)
        time.sleep(3)  # wait for JS to load; adjust as needed
        product_elements = driver.find_elements(By.CLASS_NAME, "absolute")

        results = []
        for el in product_elements:
            text = el.text.strip()
            if text and len(results) < 5:  # Limit to 5 results
                results.append(text)

        return results if results else ["No visible product titles found."]
    except Exception as e:
        print(f"Error: {e}")
        return ["Error occurred while scraping."]
    finally:
        driver.quit()

# Discord command to trigger Walmart search
@bot.command()
async def walmart(ctx, upc, zip_code):
    await ctx.send(f"🔍 Searching Walmart for UPC `{upc}` near ZIP `{zip_code}`...")
    results = search_walmart_inventory(upc, zip_code)
    
    await ctx.send("📦 Search Results:")
    for i, result in enumerate(results, 1):
        await ctx.send(f"{i}. {result}")

# Run the bot
bot.run(config.TOKEN)